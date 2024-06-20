import pickle
import json

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

    with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/mid_results_Xiao/entity_candidates.txt', 'w') as f:
        for idx in range(len(ent_left)):
            ent_i = ent_left[idx]
            cand_list = candidates[idx]

            if ent_i in llm_response_dict and llm_response_dict[ent_i] != "Failed!":
                continue

            count_all += 1
            count_save += 1

            candidates_txt = ""
            for i in cand_list:
                cand_txt = entity_text_right[i]
                candidates_txt = candidates_txt + "'" + cand_txt + "', "

            candidates_txt = candidates_txt[:-2]

            print(ent_i, candidates_txt,'\n')
            f.write(ent_i+'\t'+candidates_txt+'\n')


if __name__ == '__main__':
    llm_resp_save_dir = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_zh_en.json'

    with open(llm_resp_save_dir.replace("/llm_response/", "/mid_results_xiao/").replace("gpt4_turbo_", "candidates_").replace(
                    ".json", ".pkl"), "rb") as fp:
        candidates_idx_list = pickle.load(fp)

    with open(llm_resp_save_dir.replace("/llm_response/", "/mid_results_Xiao/").replace("gpt4_turbo_", "target_entity_"),
              'r', encoding='utf8') as f:
        ent_left = json.load(f)

    with open(llm_resp_save_dir.replace("/llm_response/", "/mid_results_Xiao/").replace("gpt4_turbo_", "aligned_entity_"),
              'r', encoding='utf8') as f:
        ent_right = json.load(f)

    with open(llm_resp_save_dir.replace("/llm_response/", "/mid_results_Xiao/").replace("gpt4_turbo_", "entity_text_left_"),
              'r', encoding='utf8') as f:
        entity_text_left = json.load(f)

    with open(llm_resp_save_dir.replace("/llm_response/", "/mid_results_Xiao/").replace("gpt4_turbo_", "entity_text_right_"),
              'r', encoding='utf8') as f:
        entity_text_right = json.load(f)

    # cnt = 0
    # for i in range(len(ent_left)):
    #     if ent_right[i] == ent_left[i]:
    #         cnt +=1
    #     print(ent_left[i], ' | ', ent_right[i])
    # print(cnt/len(ent_left))

    # refine_all(ent_left, candidates_idx_list, entity_text_right, llm_resp_save_dir)

    print(coverage_eval(ent_left, candidates_idx_list, ent_right, entity_text_right))