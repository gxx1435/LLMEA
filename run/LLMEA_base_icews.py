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

    candidates_txt = ", ".join([f"'{entity_text_right[idx]}'" for idx in candidates_list])
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

    for idx, ent_i in enumerate(ent_left):
        if ent_i in llm_response_dict and llm_response_dict[ent_i] != "Failed!":
            continue

        count_all += 1
        count_save += 1

        response_i = refine_one(ent_i, candidates[idx], entity_text_right)
        llm_response_dict[ent_i] = response_i

        if count_save % 2 == 0:
            with open(save_dir, "w", encoding='utf8') as f_out:
                json.dump(llm_response_dict, f_out, indent=4)

    with open(save_dir, 'w', encoding='utf8') as f:
        json.dump(llm_response_dict, f, indent=4)


def get_candidates(Lvec, Rvec, entity_text_left, entity_text_right, n_cand=100):
    sim = 1 - np.array(cosine_similarity(Lvec, Rvec))

    sim_edit_dis = np.zeros((len(entity_text_left), len(entity_text_right)))
    for i, text_left in enumerate(entity_text_left):
        for j, text_right in enumerate(entity_text_right):
            sim_edit_dis[i][j] = editdistance.eval(text_left, text_right)

    sim_csls = 1 - compute_csls(np.array(Lvec), np.array(Rvec))

    candidates = []
    for i in range(len(Lvec)):
        rank1 = sim[i, :].argsort()
        rank2 = sim_edit_dis[i, :].argsort()
        rank3 = sim_csls[i, :].argsort()

        candidates.append(list(set(rank1[:n_cand]).union(set(rank2[:n_cand])).union(set(rank3[:n_cand]))))

    return candidates, entity_text_left, entity_text_right


def get_target_embed(filename, tokenizer, model, type=1):
    with open(filename, "r") as input_f:
        entity_text_all = []
        entity_embed_all = []
        counter = 0

        for line in input_f:
            counter += 1
            if type == 1:
                entity_text = line.split('\t')[1].strip()
            elif type == 2:
                entity_text = line.split('\t')[1].split('/')[-1].strip()

            # entity_text = entity_text.translate(str.maketrans('', '', string.punctuation + punctuation))

            # punctuation_eng = string.punctuation
            # punctuation_zh = punctuation
            # for i in punctuation_eng:
            #     entity_text = entity_text.replace(i, '')
            #
            # for j in punctuation_zh:
            #     entity_text = entity_text.replace(j, '')
            entity_text = entity_text.replace('_', ' ')
            print(entity_text)

            entity_text_all.append(entity_text)

            input_txt_ent = "[MASK] is identical with " + entity_text + '. '

            tokens_ent = tokenizer(
                input_txt_ent,
                return_token_type_ids=False,
                return_attention_mask=True,
                return_tensors='pt')

            tokenized_ent_text = tokenizer.convert_ids_to_tokens(tokens_ent["input_ids"][0])

            encoded_layers_ent = model(input_ids=tokens_ent["input_ids"],
                                       attention_mask=tokens_ent["attention_mask"])['last_hidden_state']

            mask_idx = tokenized_ent_text.index("[MASK]")
            entity_embed = encoded_layers_ent[0][mask_idx]

            entity_embed_all.append(entity_embed.detach().numpy())

            if counter == thresh_num:
                break


    return entity_text_all, entity_embed_all

def data_preprocess():
    """
    使ent1和ent2对齐
    :return:
    """
    data_dir = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago'
    ref_ent_ids = data_dir + '/ref_ent_ids'
    ref_ent_ids_list = []
    with open(ref_ent_ids, 'r') as f:
        for line in f.readlines():
            ref_ent_ids_list.append((line.split('\t')[0], line.split('\t')[1].strip()))
    ref_ent_ids_list = sorted(ref_ent_ids_list, key=lambda x: int(x[0]))

    # new_ref_ent_ids = data_dir + '/new_ref_ent_ids'
    # with open(new_ref_ent_ids, 'w') as f:
    #     for line in ref_ent_ids_list:
    #         f.write(line[0]+'\t'+line[1]+'\n')

    ent_ids_1 = data_dir + '/ent_ids_1'
    ent_ids_1_dict = {}
    ent_ids_1_keys = []
    ent_ids_1_values = []
    with open(ent_ids_1) as f:
        for line in f.readlines():
            ent_ids_1_keys.append(line.split('\t')[0])
            ent_ids_1_values.append(line.split('\t')[1].strip())
    ent_ids_1_dict = dict(zip(ent_ids_1_keys, ent_ids_1_values))

    ent_ids_2 = data_dir + '/ent_ids_2'
    ent_ids_2_dict = {}
    ent_ids_2_keys = []
    ent_ids_2_values = []
    with open(ent_ids_2) as f:
        for line in f.readlines():
            ent_ids_2_keys.append(line.split('\t')[0])
            ent_ids_2_values.append(line.split('\t')[1].split('/')[-1].strip())
    ent_ids_2_dict = dict(zip(ent_ids_2_keys, ent_ids_2_values))

    new_ent_ids_1 = data_dir + '/new_ent_ids_1'
    new_ent_ids_2 = data_dir + '/new_ent_ids_2'
    with open(new_ent_ids_1, 'w') as f:
        for line in ref_ent_ids_list:
            print(line)
            f.write(line[0] + '\t' + ent_ids_1_dict[line[0]] + '\n')

    with open(new_ent_ids_2, 'w') as f:
        for line in ref_ent_ids_list:
            f.write(line[1] + '\t' + ent_ids_2_dict[line[1]] + '\n')

if __name__ == '__main__':
    input_ent_dir_1 = sys.argv[1]
    input_ent_dir_2 = sys.argv[2]
    llm_resp_save_dir = sys.argv[3]
    mid_results_dir = sys.argv[4]
    thresh_num = 3000
    bert_model = 'bert-base-uncased'



    try:
        with open(llm_resp_save_dir.replace("/llm_response/", sys.argv[4]).replace(
                "gpt4_turbo_", "candidates_").replace(".json", ".pkl"), "rb") as fp:
            candidates_idx_list = pickle.load(fp)

        with open(llm_resp_save_dir.replace("/llm_response/", sys.argv[4]).replace(
                "gpt4_turbo_", "aligned_entity_"), 'r', encoding='utf8') as f:
            ent_right = json.load(f)

        with open(llm_resp_save_dir.replace("/llm_response/", sys.argv[4]).replace(
                "gpt4_turbo_", "target_entity_"), 'r', encoding='utf8') as f:
            ent_left = json.load(f)

        with open(llm_resp_save_dir.replace("/llm_response/", sys.argv[4]).replace(
                "gpt4_turbo_", "entity_text_left_"), 'r', encoding='utf8') as f:
            entity_text_left = json.load(f)

        with open(llm_resp_save_dir.replace("/llm_response/", sys.argv[4]).replace(
                "gpt4_turbo_", "entity_text_right_"), 'r', encoding='utf8') as f:
            entity_text_right = json.load(f)

        entity_embed_left = np.loadtxt(
            llm_resp_save_dir.replace("/llm_response/", sys.argv[4]).replace("gpt4_turbo_",
                                                                                                        "entity_embed_left_"),
            delimiter=',')

        entity_embed_right = np.loadtxt(
            llm_resp_save_dir.replace("/llm_response/", sys.argv[4]).replace("gpt4_turbo_",
                                                                                                        "entity_embed_right_"),
            delimiter=',')

    except:
        tokenizer = BertTokenizer.from_pretrained(bert_model)
        model = BertModel.from_pretrained(bert_model, output_hidden_states=True)
        model.eval()

        entity_embed_left_save_dir = llm_resp_save_dir.replace("/llm_response/",
                                                               sys.argv[4]).replace(
            "gpt4_turbo_", "entity_embed_left_")
        entity_embed_right_save_dir = llm_resp_save_dir.replace("/llm_response/",
                                                                sys.argv[4]).replace(
            "gpt4_turbo_", "entity_embed_right_")

        entity_text_left, entity_embed_left = get_target_embed(input_ent_dir_1, tokenizer, model, 1)
        entity_text_right, entity_embed_right = get_target_embed(input_ent_dir_2, tokenizer, model, 1)

        np.savetxt(entity_embed_left_save_dir, np.array(entity_embed_left), delimiter=',', fmt='%f')
        np.savetxt(entity_embed_right_save_dir, np.array(entity_embed_right), delimiter=',', fmt='%f')

        candidates_idx_list, ent_left, ent_right = get_candidates(entity_embed_left, entity_embed_right,
                                                                  entity_text_left, entity_text_right)

        save_dir = llm_resp_save_dir.replace("/llm_response/", sys.argv[4]).replace(
            "gpt4_turbo_", "aligned_entity_")
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(ent_right, f)

        save_dir = llm_resp_save_dir.replace("/llm_response/", sys.argv[4]).replace(
            "gpt4_turbo_", "target_entity_")
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(ent_left, f)

        save_dir = llm_resp_save_dir.replace("/llm_response/", sys.argv[4]).replace(
            "gpt4_turbo_", "candidates_").replace(".json", ".pkl")
        with open(save_dir, "wb") as fp:
            pickle.dump(candidates_idx_list, fp)

        save_dir = llm_resp_save_dir.replace("/llm_response/", sys.argv[4]).replace(
            "gpt4_turbo_", "entity_text_left_")
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(entity_text_left, f)

        save_dir = llm_resp_save_dir.replace("/llm_response/", sys.argv[4]).replace(
            "gpt4_turbo_", "entity_text_right_")
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(entity_text_right, f)

    refine_all(ent_left, candidates_idx_list, entity_text_right, llm_resp_save_dir)
