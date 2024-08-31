import numpy as np 
import sys
import pickle
import os
import string
from zhon.hanzi import punctuation
from transformers import BertModel, BertTokenizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import torch
import tqdm
import time
import subprocess
from utils import compute_csls
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import editdistance
except ImportError:
    install('editdistance')
    import editdistance

import editdistance

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


def coverage_eval(ent_left, candidates_idx_list, ent_right, entity_text_right):
    """
    :param ent_left: aligned entity
    :param candidates_idx_list: candidates idx list
    :param ent_right: target entity
    :param entity_text_right: right entity text
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

def get_candidates(Lvec, Rvec, entity_text_left, entity_text_right, n_cand=100):
    sim_cosine = 1 - np.array(cosine_similarity(Lvec, Rvec))

    sim_edit_dis = np.zeros((len(entity_text_left), len(entity_text_right)))

    for i in range(len(entity_text_left)):
        for j in range(len(entity_text_right)):
            sim_edit_dis[i][j] = editdistance.eval(entity_text_left[i], entity_text_right[j])

    sim_csls = 1 - compute_csls(np.array(Lvec), np.array(Rvec))

    sim = sim_cosine + sim_edit_dis + sim_csls


    candidates = [0] * len(Lvec)
    ent_left = [0] * len(Lvec)
    ent_right = [0] * len(Lvec)
    ranks = [0] * len(Lvec)

    for i in range(len(Lvec)):
        rank = sim[i, :].argsort()
        ranks[i] = rank
        candidates[i] = rank[0:n_cand]

        ent_left[i] = entity_text_left[i]
        ent_right[i] = entity_text_right[i]
    
    return ranks, candidates, ent_left, ent_right


def get_embed(summed_last_4_layers, tokenized_text):
    sep_idx = tokenized_text.index(".")
    cls_idx = tokenized_text.index("[CLS]")
    summed_embed = summed_last_4_layers[cls_idx]
    for i in range(cls_idx+1, sep_idx): 
        summed_embed = summed_embed + summed_last_4_layers[i]

    return summed_embed


def get_target_embed(filename, tokenizer, model):
    """
    :param filename:
    :param tokenizer:
    :param model:
    :param embed_save_dir:
    :return:
    """
    with open(filename, "r") as input_f:
        entity_text_all = []
        target_embed = []
        entity_embed_all = []
        counter = 0
        counter_list = []
        for line in input_f:
            counter += 1
            tmp = line.strip().replace("...", "")
            real_label = tmp.replace("\n", '')

            ### Adding word_embed
            entity_text = real_label.split(":")[0].strip()
            original_entity_text = entity_text
            entity_text = entity_text.split('(')[0].strip()
            entity_text = entity_text.split('（')[0].strip()

            # remove punctuation
            punctuation_eng = string.punctuation
            punctuation_zh = punctuation
            for i in punctuation_eng:
                entity_text = entity_text.replace(i, '')

            for j in punctuation_zh:
                entity_text = entity_text.replace(j, '')
            #
            entity_text = entity_text.replace('_', ' ')
            print(original_entity_text, '\t', entity_text)

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
            encoded_layers_ent = model(input_ids=tokens_ent["input_ids"], attention_mask=tokens_ent["attention_mask"])['last_hidden_state']
            last_hidden_state_ent = encoded_layers_ent[0]
            mask_idx = tokenized_ent_text.index("[MASK]")
            entity_embed = last_hidden_state_ent[mask_idx]
            entity_embed_all.append(entity_embed.detach().numpy())

            tokens = tokenizer(
                input_txt_all,
                return_token_type_ids=False,
                return_attention_mask=True,
                return_tensors='pt')

            tokenized_text = tokenizer.convert_ids_to_tokens(tokens["input_ids"][0])

            with torch.no_grad():
                try:
                    encoded_layers = model(input_ids=tokens["input_ids"], attention_mask=tokens["attention_mask"])['last_hidden_state']
                    last_hidden_state = encoded_layers[0]
                    tokens = get_embed(last_hidden_state, tokenized_text)
                    target_embed.append(tokens.numpy())
                except:
                    counter_list.append(counter)
                    target_embed.append(len(entity_embed)*[0])

            # print('counter:', counter,
            #       'target_embed:', len(target_embed),
            #       'entity_embed_all:', len(entity_embed_all))

            if counter == thresh_num:
                print('\n\n')
                break

    # return counter_list, entity_text_all, target_embed
    return counter_list, entity_text_all, np.array(target_embed)+np.array(entity_embed_all)


# def get_target_embed(filename, tokenizer, model):
#     with open(filename, "r") as input_f:
#         entity_text_all = []
#         target_embed = []
#         entity_embed_all = []
#         counter = 0
#         counter_list = []
#         for line in input_f:
#             tmp = line.strip().replace("...", "")
#             real_label = tmp.replace("\n", '')
#
#             ### Adding wrod_embed
#             entity_text = real_label.split(":")[0].strip()
#             entity_text = entity_text.split('(')[0].strip()
#             entity_text = entity_text.split('（')[0].strip()
#
#             # remove punctuation
#             punctuation_eng = string.punctuation
#             punctuation_zh = punctuation
#             for i in punctuation_eng:
#                 entity_text = entity_text.replace(i, '')
#
#             for j in punctuation_zh:
#                 entity_text = entity_text.replace(j, '')
#
#             sep_idx = real_label.index(":")
#             real_label = entity_text + real_label[sep_idx:]
#             input_txt_list = real_label.split(":")
#             input_txt_all = entity_text + ": " + "[MASK] is identical with " + entity_text + '. '
#             for i in input_txt_list[1:]:
#                 input_txt_all = input_txt_all + i
#
#             entity_text_all.append(entity_text)
#
#             input_txt_ent = "[MASK] is identical with " + entity_text + '. '
#             tokens_ent = tokenizer(
#                 input_txt_ent,
#                 return_token_type_ids=False,
#                 return_attention_mask=True,
#                 return_tensors='pt')
#
#             tokenized_ent_text = tokenizer.convert_ids_to_tokens(tokens_ent["input_ids"][0])
#             encoded_layers_ent = model(input_ids=tokens_ent["input_ids"], attention_mask=tokens_ent["attention_mask"])[
#                 'last_hidden_state']
#             last_hidden_state_ent = encoded_layers_ent[0]
#             mask_idx = tokenized_ent_text.index("[MASK]")
#             entity_embed = last_hidden_state_ent[mask_idx]
#             entity_embed_all.append(entity_embed.detach().numpy())
#
#             tokens = tokenizer(
#                 input_txt_all,
#                 return_token_type_ids=False,
#                 return_attention_mask=True,
#                 return_tensors='pt')
#
#             tokenized_text = tokenizer.convert_ids_to_tokens(tokens["input_ids"][0])
#
#             with torch.no_grad():
#                 try:
#                     encoded_layers = model(input_ids=tokens["input_ids"], attention_mask=tokens["attention_mask"])[
#                         'last_hidden_state']
#                     last_hidden_state = encoded_layers[0]
#                     tokens = get_embed(last_hidden_state, tokenized_text)
#                     target_embed.append(tokens.numpy())
#                 except:
#                     counter_list.append(counter)
#                     target_embed.append(len(entity_embed) * [0])
#
#             print('counter:', counter,
#                               'target_embed:', len(target_embed),
#                               'entity_embed_all:', len(entity_embed_all))
#
#             if counter > thresh_num:
#                 break
#             counter += 1
#
#     # return counter_list, entity_text_all, target_embed
#     return counter_list, entity_text_all, np.array(target_embed) + np.array(entity_embed_all)


if __name__ == '__main__':
    input_prompt_dir_1 = sys.argv[1]   
    input_prompt_dir_2 = sys.argv[2] 
    llm_resp_save_dir = sys.argv[3]
    mid_results_dir = sys.argv[4]
    thresh_num = int(sys.argv[5])


    if not os.path.exists(os.getcwd()+mid_results_dir[:-1]):
        os.mkdir(os.getcwd()+mid_results_dir[:-1])

    bert_model = 'bert-base-uncased'  #"bert-base-multilingual-cased"
    try:
        with open(llm_resp_save_dir.replace("/llm_response/", mid_results_dir).replace("gpt4_turbo_", "ranks_").replace(".json", ".pkl"), "rb") as fp:
            ranks = pickle.load(fp)

        with open(llm_resp_save_dir.replace("/llm_response/", mid_results_dir).replace("gpt4_turbo_", "candidates_").replace(".json", ".pkl"), "rb") as fp:
            candidates_idx_list = pickle.load(fp)

        with open(llm_resp_save_dir.replace("/llm_response/", mid_results_dir).replace("gpt4_turbo_", "aligned_entity_"), 'r', encoding='utf8') as f:
            ent_right = json.load(f)

        with open(llm_resp_save_dir.replace("/llm_response/", mid_results_dir).replace("gpt4_turbo_", "target_entity_"), 'r', encoding='utf8') as f:
            ent_left = json.load(f)

        with open(llm_resp_save_dir.replace("/llm_response/", mid_results_dir).replace("gpt4_turbo_", "entity_text_left_"), 'r', encoding='utf8') as f:
            entity_text_left = json.load(f)

        with open(llm_resp_save_dir.replace("/llm_response/", mid_results_dir).replace("gpt4_turbo_", "entity_text_right_"), 'r', encoding='utf8') as f:
            entity_text_right = json.load(f)

        entity_embed_left = np.loadtxt(llm_resp_save_dir.replace("/llm_response/", mid_results_dir).replace("gpt4_turbo_", "entity_embed_left_"), delimiter=',')

        entity_embed_right = np.loadtxt(llm_resp_save_dir.replace("/llm_response/", mid_results_dir).replace("gpt4_turbo_", "entity_embed_right_"), delimiter=',')

    except:

        print("LLMEA_zero_embed_base start!")
        tokenizer = BertTokenizer.from_pretrained(bert_model)
        model = BertModel.from_pretrained(bert_model, output_hidden_states=True)
        model.eval()  

        # c_list_1, entity_text_left, entity_embed_left = get_target_embed(input_prompt_dir_1, tokenizer, model)
        # c_list_2, entity_text_right, entity_embed_right = get_target_embed(input_prompt_dir_2, tokenizer, model)

        c_list_1, entity_text_left, entity_embed_left = get_target_embed(input_prompt_dir_1,
                                                                         tokenizer,
                                                                         model)
        c_list_2, entity_text_right, entity_embed_right = get_target_embed(input_prompt_dir_2,
                                                                           tokenizer,
                                                                           model)

        entity_embed_left_save_dir = llm_resp_save_dir.replace("/llm_response/", mid_results_dir).replace("gpt4_turbo_", "entity_embed_left_")
        entity_embed_right_save_dir = llm_resp_save_dir.replace("/llm_response/", mid_results_dir).replace("gpt4_turbo_", "entity_embed_right_")

        np.savetxt(entity_embed_left_save_dir, np.array(entity_embed_left), delimiter=',', fmt='%f')
        np.savetxt(entity_embed_right_save_dir, np.array(entity_embed_right), delimiter=',', fmt='%f')


        tmp_list = list(set(c_list_1 + c_list_2))
        c_list_all = sorted(tmp_list, reverse=True)


        ranks, candidates_idx_list, ent_left, ent_right = get_candidates(entity_embed_left, entity_embed_right, entity_text_left, entity_text_right)
        
        save_dir = llm_resp_save_dir.replace("/llm_response/", mid_results_dir).replace("gpt4_turbo_", "aligned_entity_")
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(ent_right, f, indent=4)

        save_dir = llm_resp_save_dir.replace("/llm_response/", mid_results_dir).replace("gpt4_turbo_", "target_entity_")
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(ent_left, f,  indent=4)

        # save_dir = llm_resp_save_dir.replace("/llm_response/", mid_results_dir).replace("gpt4_turbo_", "ranks_").replace(".json", ".pkl")
        # pickle.dump(ranks, open(save_dir, "wb"))
        #
        # save_dir = llm_resp_save_dir.replace("/llm_response/", mid_results_dir).replace("gpt4_turbo_", "candidates_").replace(".json", ".pkl")
        # pickle.dump(candidates_idx_list, open(save_dir, "wb"))

        save_dir = llm_resp_save_dir.replace("/llm_response/", mid_results_dir).replace("gpt4_turbo_", "entity_text_left_")
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(entity_text_left, f, indent=4)

        save_dir = llm_resp_save_dir.replace("/llm_response/", mid_results_dir).replace("gpt4_turbo_", "entity_text_right_")
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(entity_text_right, f, indent=4)

    refine_all(ent_left, candidates_idx_list, entity_text_right, llm_resp_save_dir)


