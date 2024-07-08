import numpy as np 
import sys
import pickle
import os
import string
from zhon.hanzi import punctuation
from transformers import BertModel, BertTokenizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import tqdm
import time
import subprocess
import editdistance
from utils import compute_csls, coverage_eval


def edit_distance(s1, s2, m, n):
    """
    :param s1:
    :param s2:
    :param m:
    :param n:
    :return:
    """
    if m == 0:
        return n
    if n == 0:
        return m

    if s1[m-1] == s2[n-1]:
        return edit_distance(s1, s2, m-1, n-1)

    return 1 + min(edit_distance(s1, s2, m, n-1),
                  edit_distance(s1, s2, m-1, n),
                  edit_distance(s1, s2, m-1, n-1))

def refine_one(ent_i, candidates_list, entity_text_right):
    prompt = """
    As a good encyclopedia, your task is entity alignment where given an entity, find the equivalent entity from given candidates and also sort the candidates by relevance. For example:

    ------------- Example starts: -------------
    Given entity: 'Tony Stark'
    Candidates: ['Captain America', 'the 17th president of USA', 'Iron Man', 'Black Widow', 'Bat Man']
    Equivalent Entity: <ANSWER>'Iron Man'</ANSWER>
    Sorted Candidates: <SORT>'Iron Man','Captain America','Black Widow','Bat Man','the 17th president of USA'</SORT>
    ------------- Example ends -------------

    According to the example above, please complete the entity alignment task below. You have to strictly follow the example format and requirements. 

    ============= Task starts: =============
    Given entity: '{entity}'
    Candidates: [{candidates_txt}]
    Equivalent Entity: <ANSWER>"""
    
    candidates_txt = ""
    for idx in candidates_list:
        cand_txt = entity_text_right[idx]
        candidates_txt = candidates_txt + "'" + cand_txt + "', "


    candidates_txt = candidates_txt[:-2]
    input_msg = prompt.format(entity=ent_i, candidates_txt=candidates_txt)
    messages_input = [
                {
                    "role": "user",
                    "content": input_msg,
                },
            ]

    response = get_gpt_4_turbo(messages_input)
    
    return response


def refine_all(ent_left, candidates, entity_text_right, save_dir):
    """
    refine all entities, convert candidates into entity pair
    :param ent_left: left entity list to be aligned with
    :param candidates: candidates idx list for each left entity
    :param entity_text_right: candidates entity texts for each left entity
    :param save_dir:
    :return:
    """
    llm_response_dict = {}
    count_save = 0
    count_all = 0
   
    try:
        with open(save_dir, 'r', encoding='utf8') as f:
            llm_response_dict = json.load(f)
    except:
        pass

    for idx in range(len(ent_left)):
        ent_i = ent_left[idx]
        cand_list = candidates[idx]

        if ent_i in llm_response_dict and llm_response_dict[ent_i] != "Failed!":
            continue

        count_all += 1
        count_save += 1

        response_i = refine_one(ent_i, cand_list, entity_text_right)
        llm_response_dict[ent_i] = response_i

        if count_save % 2 == 0:
            with open(save_dir, "w", encoding='utf8') as f_out:
                json.dump(llm_response_dict, f_out, indent = 4)

    with open(save_dir, 'w', encoding='utf8') as f:
        json.dump(llm_response_dict, f, indent=4)


def get_candidates(Lvec, Rvec, entity_text_left, entity_text_right, n_cand=100):
    """
    According to bert embeddings to get entity candidates
    :param Lvec: all the embeddings for the left entity
    :param Rvec: all the embeddings for the right entity
    :param entity_text_left: all the entity name for the left entity
    :param entity_text_right: all the entity name for the right entity
    :param n_cand:
    :return:
    """
    sim = 1 - np.array(cosine_similarity(Lvec, Rvec))

    sim_edit_dis = np.zeros((len(entity_text_left), len(entity_text_right)))
    for i in range(len(entity_text_left)):
        for j in range(len(entity_text_right)):
            # sim_edit_dis[i][j] = edit_distance(entity_text_left[i],entity_text_right[j],len(entity_text_left[i]),len(entity_text_right[j]))
            sim_edit_dis[i][j] = editdistance.eval(entity_text_left[i], entity_text_right[j])

    sim_csls = 1 - compute_csls(np.array(Lvec), np.array(Rvec))

    # sim1_2 = np.array([[sim[i][j]+sim_edit_dis[i][j] for j in range(len(entity_text_right))]
    #           for i in range(len(entity_text_left))])
    # sim1_3 = np.array([[sim[i][j]+sim_csls[i][j] for j in range(len(entity_text_right))]
    #           for i in range(len(entity_text_left))])
    # sim2_3 = np.array([[sim_edit_dis[i][j] + sim_csls[i][j] for j in range(len(entity_text_right))]
    #           for i in range(len(entity_text_left))])
    # sim1_2_3 = np.array([[sim[i][j] + sim_edit_dis[i][j] + sim_csls[i][j] for j in range(len(entity_text_right))]
    #           for i in range(len(entity_text_left))])

    candidates = [0] * len(Lvec)
    ent_left = [0] * len(Lvec)
    ent_right = [0] * len(Lvec)
    for i in range(len(Lvec)):
        rank1 = sim[i, :].argsort()
        rank2 = sim_edit_dis[i, :].argsort()
        rank3 = sim_csls[i, :].argsort()
        # rank = sim1_2[i, :].argsort()
        # rank = sim1_3[i, :].argsort()
        # rank = sim2_3[i, :].argsort()
        # rank = sim1_2_3[i, :].argsort()

        # candidates[i] = rank[0:n_cand]

        candidates[i] = list(set(rank1[0:n_cand]).union(set(rank2[0:n_cand])).union(set(rank3[0:n_cand])))

        ent_left[i] = entity_text_left[i]
        ent_right[i] = entity_text_right[i]
    
    return candidates, ent_left, ent_right


def get_target_embed(filename, tokenizer, model):
    """
    Get target embeddings for the entities
    :param filename:
    :param tokenizer:
    :param model:
    :return:
    """
    with open(filename, "r") as input_f:
        entity_text_all = []
        entity_embed_all = []
        counter = 0

        # counter_list no use
        counter_list = []

        for line in input_f:
            tmp = line.strip().replace("...", "")
            real_label = tmp.replace("\n", '')
            
            # Adding word_embed, get entity name
            entity_text = real_label.split(":")[0].strip()
            entity_text = entity_text.split('(')[0].strip()
            entity_text = entity_text.split('（')[0].strip()
            
            # remove punctuation from entity text
            punctuation_eng = string.punctuation
            punctuation_zh = punctuation
            for i in punctuation_eng:
                entity_text = entity_text.replace(i, '')
                
            for j in punctuation_zh:
                entity_text = entity_text.replace(j, '')
                
            # get input_txt_all and input_txt_ent
            # Note: input_txt_all is not used
            sep_idx = real_label.index(":")
            real_label = entity_text + real_label[sep_idx:]
            input_txt_list = real_label.split(":")
            input_txt_all = entity_text + ": " + "[MASK] is identical with " + entity_text +'. '
            for i in input_txt_list[1:]:
                input_txt_all = input_txt_all + i
                
            entity_text_all.append(entity_text)
            
            input_txt_ent = "[MASK] is identical with " + entity_text +'. '

            tokens_ent = tokenizer(
                input_txt_ent,               
                return_token_type_ids=False,   
                return_attention_mask=True,     
                return_tensors='pt')        
            
            tokenized_ent_text = tokenizer.convert_ids_to_tokens(tokens_ent["input_ids"][0])

            encoded_layers_ent = model(input_ids=tokens_ent["input_ids"],
                                       attention_mask=tokens_ent["attention_mask"])['last_hidden_state']

            last_hidden_state_ent = encoded_layers_ent[0]
            mask_idx = tokenized_ent_text.index("[MASK]")
            entity_embed = last_hidden_state_ent[mask_idx]

            entity_embed_all.append(entity_embed.detach().numpy())


            if counter > thresh_num:
                break
            counter += 1

    return counter_list, entity_text_all, entity_embed_all


if __name__ == '__main__':
    input_prompt_dir_1 = sys.argv[1]   
    input_prompt_dir_2 = sys.argv[2] 
    llm_resp_save_dir = sys.argv[3] 
    thresh_num = 3000
    bert_model = 'bert-base-uncased'  #"bert-base-multilingual-cased"
    try:
        with open(llm_resp_save_dir.replace("/llm_response/", "/mid_results_3000_cos_ed_csls_union/").replace("gpt4_turbo_", "candidates_").replace(".json", ".pkl"), "rb") as fp:
            candidates_idx_list = pickle.load(fp)

        with open(llm_resp_save_dir.replace("/llm_response/", "/mid_results_3000_cos_ed_csls_union/").replace("gpt4_turbo_", "aligned_entity_"), 'r', encoding='utf8') as f:
            ent_right = json.load(f)

        with open(llm_resp_save_dir.replace("/llm_response/", "/mid_results_3000_cos_ed_csls_union/").replace("gpt4_turbo_", "target_entity_"), 'r', encoding='utf8') as f:
            ent_left = json.load(f)

        with open(llm_resp_save_dir.replace("/llm_response/", "/mid_results_3000_cos_ed_csls_union/").replace("gpt4_turbo_", "entity_text_left_"), 'r', encoding='utf8') as f:
            entity_text_left = json.load(f)

        with open(llm_resp_save_dir.replace("/llm_response/", "/mid_results_3000_cos_ed_csls_union/").replace("gpt4_turbo_", "entity_text_right_"), 'r', encoding='utf8') as f:
            entity_text_right = json.load(f)

        entity_embed_left = np.loadtxt(llm_resp_save_dir.replace("/llm_response/", "/mid_results_3000_cos_ed_csls_union/").replace("gpt4_turbo_", "entity_embed_left_"), delimiter=',')

        entity_embed_right = np.loadtxt(llm_resp_save_dir.replace("/llm_response/", "/mid_results_3000_cos_ed_csls_union/").replace("gpt4_turbo_", "entity_embed_right_"), delimiter=',')

    except:
        tokenizer = BertTokenizer.from_pretrained(bert_model)
        model = BertModel.from_pretrained(bert_model, output_hidden_states=True)
        model.eval()  

        entity_embed_left_save_dir = llm_resp_save_dir.replace("/llm_response/", "/mid_results_3000_cos_ed_csls_union/").replace("gpt4_turbo_", "entity_embed_left_")
        entity_embed_right_save_dir = llm_resp_save_dir.replace("/llm_response/", "/mid_results_3000_cos_ed_csls_union/").replace("gpt4_turbo_", "entity_embed_right_")
        c_list_1, entity_text_left, entity_embed_left = get_target_embed(input_prompt_dir_1,
                                                                         tokenizer,
                                                                         model)
        c_list_2, entity_text_right, entity_embed_right = get_target_embed(input_prompt_dir_2,
                                                                           tokenizer,
                                                                           model)
        ## 把向量保存下来
        np.savetxt(entity_embed_left_save_dir, np.array(entity_embed_left), delimiter=',', fmt='%f')
        np.savetxt(entity_embed_right_save_dir, np.array(entity_embed_right), delimiter=',', fmt='%f')


        tmp_list = list(set(c_list_1 + c_list_2))
        c_list_all = sorted(tmp_list, reverse=True)

        ### No need to know this part, Start:
        if c_list_all:
            for j in c_list_all:
                del entity_text_left[j]
                del entity_text_right[j]
                del entity_embed_left[j]
                del entity_embed_right[j]
        ### End

        candidates_idx_list, ent_left, ent_right = get_candidates(entity_embed_left, entity_embed_right, entity_text_left, entity_text_right)

        save_dir = llm_resp_save_dir.replace("/llm_response/", "/mid_results_3000_cos_ed_csls_union/").replace("gpt4_turbo_", "aligned_entity_")
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(ent_right, f)

        save_dir = llm_resp_save_dir.replace("/llm_response/", "/mid_results_3000_cos_ed_csls_union/").replace("gpt4_turbo_", "target_entity_")
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(ent_left, f)

        save_dir = llm_resp_save_dir.replace("/llm_response/", "/mid_results_3000_cos_ed_csls_union/").replace("gpt4_turbo_", "candidates_").replace(".json", ".pkl")
        pickle.dump(candidates_idx_list, open(save_dir, "wb"))

        save_dir = llm_resp_save_dir.replace("/llm_response/", "/mid_results_3000_cos_ed_csls_union/").replace("gpt4_turbo_", "entity_text_left_")
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(entity_text_left, f)

        save_dir = llm_resp_save_dir.replace("/llm_response/", "/mid_results_3000_cos_ed_csls_union/").replace("gpt4_turbo_", "entity_text_right_")
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(entity_text_right, f)

    refine_all(ent_left, candidates_idx_list, entity_text_right, llm_resp_save_dir)


