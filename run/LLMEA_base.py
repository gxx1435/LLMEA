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


# def compute_csls(X_src, X_tgt, k=10):
#     """
#     Compute Cross-domain Similarity Local Scaling (CSLS).
#
#     Parameters:
#     X_src : np.array
#         Source domain embeddings (n_samples_src, n_features)
#     X_tgt : np.array
#         Target domain embeddings (n_samples_tgt, n_features)
#     k : int
#         Number of nearest neighbors for local scaling
#
#     Returns:
#     csls_matrix : np.array
#         CSLS similarity scores matrix (n_samples_src, n_samples_tgt)
#     """
#     # Compute cosine similarity matrix
#     cosine_sim = np.dot(X_src, X_tgt.T)
#
#     # Normalize vectors to have unit norm
#     X_src_norm = np.linalg.norm(X_src, axis=1, keepdims=True)
#     X_tgt_norm = np.linalg.norm(X_tgt, axis=1, keepdims=True)
#     cosine_sim /= (X_src_norm @ X_tgt_norm.T)
#
#     # Compute nearest neighbor similarity for source and target domains
#     src_nn_sim = np.zeros(X_src.shape[0])
#     tgt_nn_sim = np.zeros(X_tgt.shape[0])
#
#     for i in range(X_src.shape[0]):
#         src_nn_sim[i] = np.mean(np.sort(cosine_sim[i, :])[-k:])
#
#     for j in range(X_tgt.shape[0]):
#         tgt_nn_sim[j] = np.mean(np.sort(cosine_sim[:, j])[-k:])
#
#     # Compute CSLS similarity scores
#     csls_matrix = np.zeros(cosine_sim.shape)
#     for i in range(X_src.shape[0]):
#         for j in range(X_tgt.shape[0]):
#             csls_matrix[i, j] = 2 * cosine_sim[i, j] - src_nn_sim[i] - tgt_nn_sim[j]
#
#     return csls_matrix

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


def coverage_eval(ent_left, candidates_idx_list, ent_right, entity_text_right):
    """
    :param ent_left: source entity
    :param candidates_idx_list: candidates idx list
    :param ent_right: target entity
    :param entity_text_right:
    :return:
    """
    cnt = 0
    for i in range(len(ent_left)):
        cand_list = candidates_idx_list[i]
        candidates = []
        for j in cand_list:
            cand_txt = entity_text_right[j]
            candidates.append(cand_txt)

        if ent_right[i] in candidates:
           cnt += 1

    return float(cnt / len(ent_left))

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
            sim_edit_dis[i][j] = edit_distance(entity_text_left[i],entity_text_right[j],len(entity_text_left[i]),len(entity_text_right[j]))

    print(sim.shape, sim_edit_dis.shape)
    candidates = [0] * len(Lvec)
    ent_left = [0] * len(Lvec)
    ent_right = [0] * len(Lvec)
    for i in range(len(Lvec)):
        rank = sim[i, :].argsort()
        rank_edit_dis = sim_edit_dis[i, :].argsort()
        rank_all = np.array([rank[i]+rank_edit_dis[i] for i in range(len(rank))])
        rank_all = rank_all.argsort()

        candidates[i] = rank_all[0:n_cand]
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
            print('input_txt_all: ', input_txt_all)
            print('input_txt_ent: ', input_txt_ent)

            tokens_ent = tokenizer(
                input_txt_ent,               
                return_token_type_ids=False,   
                return_attention_mask=True,     
                return_tensors='pt')        
            
            tokenized_ent_text = tokenizer.convert_ids_to_tokens(tokens_ent["input_ids"][0])
            print('tokenized_ent_text:', tokenized_ent_text)

            encoded_layers_ent = model(input_ids=tokens_ent["input_ids"],
                                       attention_mask=tokens_ent["attention_mask"])['last_hidden_state']

            last_hidden_state_ent = encoded_layers_ent[0]
            mask_idx = tokenized_ent_text.index("[MASK]")
            entity_embed = last_hidden_state_ent[mask_idx]

            print('encoded_layers_ent:', encoded_layers_ent)
            print('last_hidden_state_ent:', last_hidden_state_ent)
            print('mask_idx:', mask_idx)
            print('entity_embed:', entity_embed)

            entity_embed_all.append(entity_embed.detach().numpy())
            
            if counter > thresh_num:
                break
            counter += 1
            
    return counter_list, entity_text_all, entity_embed_all


if __name__ == '__main__':
    input_prompt_dir_1 = sys.argv[1]   
    input_prompt_dir_2 = sys.argv[2] 
    llm_resp_save_dir = sys.argv[3] 
    thresh_num = 1000
    bert_model = 'bert-base-uncased'  #"bert-base-multilingual-cased"
    try:
        with open(llm_resp_save_dir.replace("/llm_response/", "/mid_results/").replace("gpt4_turbo_", "candidates_").replace(".json", ".pkl"), "rb") as fp:
            candidates_idx_list = pickle.load(fp)

        with open(llm_resp_save_dir.replace("/llm_response/", "/mid_results/").replace("gpt4_turbo_", "aligned_entity_"), 'r', encoding='utf8') as f:
            ent_right = json.load(f)

        with open(llm_resp_save_dir.replace("/llm_response/", "/mid_results/").replace("gpt4_turbo_", "target_entity_"), 'r', encoding='utf8') as f:
            ent_left = json.load(f)

        with open(llm_resp_save_dir.replace("/llm_response/", "/mid_results/").replace("gpt4_turbo_", "entity_text_left_"), 'r', encoding='utf8') as f:
            entity_text_left = json.load(f)

        with open(llm_resp_save_dir.replace("/llm_response/", "/mid_results/").replace("gpt4_turbo_", "entity_text_right_"), 'r', encoding='utf8') as f:
            entity_text_right = json.load(f)
    except:
        tokenizer = BertTokenizer.from_pretrained(bert_model)
        model = BertModel.from_pretrained(bert_model, output_hidden_states=True)
        model.eval()  

        c_list_1, entity_text_left, entity_embed_left = get_target_embed(input_prompt_dir_1, tokenizer, model)
        c_list_2, entity_text_right, entity_embed_right = get_target_embed(input_prompt_dir_2, tokenizer, model)
        print('entity_text_left:', entity_text_left)
        print('entity_embed_left:', entity_embed_left)

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
        print('candiadate_idx_list:\n', candidates_idx_list)
        print('candidates_idx_list len', len(candidates_idx_list))
        print('ent_left:\n', ent_left)
        print('ent_left len', len(ent_left))
        print('ent_right:\n', ent_right)

        save_dir = llm_resp_save_dir.replace("/llm_response/", "/mid_results/").replace("gpt4_turbo_", "aligned_entity_")
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(ent_right, f)

        save_dir = llm_resp_save_dir.replace("/llm_response/", "/mid_results/").replace("gpt4_turbo_", "target_entity_")
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(ent_left, f)

        save_dir = llm_resp_save_dir.replace("/llm_response/", "/mid_results/").replace("gpt4_turbo_", "candidates_").replace(".json", ".pkl")
        pickle.dump(candidates_idx_list, open(save_dir, "wb"))

        save_dir = llm_resp_save_dir.replace("/llm_response/", "/mid_results/").replace("gpt4_turbo_", "entity_text_left_")
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(entity_text_left, f)

        save_dir = llm_resp_save_dir.replace("/llm_response/", "/mid_results/").replace("gpt4_turbo_", "entity_text_right_")
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(entity_text_right, f)

    refine_all(ent_left, candidates_idx_list, entity_text_right, llm_resp_save_dir)


