import json

import numpy as np

from run.utils import coverage_eval, get_candidates, get_entity_names,coverage_eval_segment
# from Test import get_hits


def get_performance_of_semantic_embedding_similarity(
        semantic_embedding_matrix_left,
        semantic_embedding_matrix_right,
        candidates_save_path,
        thres_hold
):
    """
    获取语义向量和结构化向量embedding的结果
    :param semantic_embedding_matrix:
    :param subgraph_motif_embeddig_matrix:
    :param semantic_embedding_matrix_right:
    :param subgraph_motif_embeddig_matrix_right
    :param candidates_save_path
    :param thres_hold:
    :return:
    """

    assert len(semantic_embedding_matrix_left) == len(semantic_embedding_matrix_right), '向量维度需要相等'


    matrix1 = semantic_embedding_matrix_left
    matrix2 = semantic_embedding_matrix_right

    # matrix1 = subgraph_motif_embeddig_matrix_left
    # matrix2 = subgraph_motif_embeddig_matrix_right

    # get_hits(matrix1, matrix2)
    # exit()

    with open(entity_left_path) as f:
        entity_left = json.load(f)

    with open(entity_right_path) as f:
        entity_right = json.load(f)

    # entity_left = get_entity_names(entity_ids_1_path, thres_hold)
    # entity_right = get_entity_names(entity_ids_2_path, thres_hold)


    n_cand = 1
    method = 'all add'
    candidates_idx_list, ent_left, ent_right = get_candidates(matrix1,
                                                              matrix2,
                                                              entity_left,
                                                              entity_right,
                                                              n_cand=n_cand,
                                                              method=method)

    candidates_save_path = candidates_save_path + 'candiadtes_{}_{}_{}_{}.txt'.format('semantic_embed', n_cand, thres_hold, method)

    # if method != 'all':
    #     np.savetxt(candidates_save_path, candidates_idx_list, delimiter=',', fmt='%d')
    # else:
    #     with open(candidates_save_path, 'w') as f:
    #         for cand_list in candidates_idx_list:
    #             cand_list = [str(cand) for cand in cand_list]
    #             if len(cand_list) != 1:
    #                 f.write(','.join(cand_list)+'\n')
    #             else:
    #                 f.write(cand_list[0] + '\n')


    out_file = candidates_save_path.split('.')[0] + '_put_correct_ans_last.txt'
    print(out_file)
    print("语义向量的覆盖率为：\n", coverage_eval(candidates_idx_list,
                                                 ent_left,
                                                 ent_right,
                                                 ent_right,
                                                 out_file
                                                 ))

    # cut_indices = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200]
    # for cut_indice in cut_indices:
    #     coverage = coverage_eval_segment(candidates_idx_list, ent_left, ent_right, ent_right, cut_indice)
    #     print("{} candidates, Coverage is:".format(cut_indice), coverage)

if __name__ == '__main__':
    dataset = 'icews_yago'
    threshold = 5647
    mid_reuslts = '/mid_results_rs_0.3_zeroembed_icews_yago/'

    llm_resp_save_dir = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_.json'

    # entity_ids_1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_{}/new_ent_ids_1'.format(type)
    # entity_ids_2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_{}/new_ent_ids_2'.format(type)
    entity_left_path = llm_resp_save_dir.replace("/llm_response/", mid_reuslts).replace("gpt4_turbo_", "entity_text_left_")
    entity_right_path = llm_resp_save_dir.replace("/llm_response/", mid_reuslts).replace("gpt4_turbo_", "entity_text_right_")

    semantic_embedding_matrix_left = np.loadtxt(llm_resp_save_dir.replace("/llm_response/", mid_reuslts).replace("gpt4_turbo_", "entity_embed_left_"), delimiter=',')
    semantic_embedding_matrix_right = np.loadtxt(llm_resp_save_dir.replace("/llm_response/", mid_reuslts).replace("gpt4_turbo_", "entity_embed_right_"), delimiter=',')

    print(len(semantic_embedding_matrix_left))
    print(len(semantic_embedding_matrix_right))
    candidates_save_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/'.format(dataset)

    get_performance_of_semantic_embedding_similarity(
        semantic_embedding_matrix_left,
        semantic_embedding_matrix_right,
        candidates_save_path,
        thres_hold=threshold
    )
