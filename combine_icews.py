import numpy as np

from run.utils import coverage_eval, get_candidates, get_entity_names
from Test import get_hits
def get_performance_of_semantic_and_subgraph_motif_embedding_similarity(
        semantic_embedding_matrix_left,
        subgraph_motif_embeddig_matrix_left,
        semantic_embedding_matrix_right,
        subgraph_motif_embeddig_matrix_right,
        candidates_save_path,
        thres_hold=3000
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
    print(len(subgraph_motif_embeddig_matrix_left),
          len(subgraph_motif_embeddig_matrix_right))

    assert len(semantic_embedding_matrix_left) == thres_hold and len(subgraph_motif_embeddig_matrix_left)==thres_hold and\
            len(semantic_embedding_matrix_right) == thres_hold and len(subgraph_motif_embeddig_matrix_right)==thres_hold,\
            '语义向量或结构向量长度必须等于threshold'

    matrix1 = np.concatenate((semantic_embedding_matrix_left, subgraph_motif_embeddig_matrix_left), axis=1)
    matrix2 = np.concatenate((semantic_embedding_matrix_right, subgraph_motif_embeddig_matrix_right), axis=1)

    matrix1 = semantic_embedding_matrix_left
    matrix2 = semantic_embedding_matrix_right

    # matrix1 = subgraph_motif_embeddig_matrix_left
    # matrix2 = subgraph_motif_embeddig_matrix_right

    # get_hits(matrix1, matrix2)
    # exit()

    entity_left = get_entity_names(entity_ids_1_path)
    entity_right = get_entity_names(entity_ids_2_path)

    n_cand = 100
    method = 'all'
    candidates_idx_list, ent_left, ent_right = get_candidates(matrix1,
                                                              matrix2,
                                                              entity_left,
                                                              entity_right,
                                                              n_cand=n_cand,
                                                              method=method)

    candidates_save_path = candidates_save_path + 'candiadtes_{}_{}_{}_{}.txt'.format('semantic_embed', n_cand, thres_hold, method)

    if method != 'all':
        np.savetxt(candidates_save_path, delimiter=',', fmt='%d')
    else:
        with open(candidates_save_path, 'w') as f:
            for cand_list in candidates_idx_list:
                cand_list = [str(cand) for cand in cand_list]
                if len(cand_list) != 1:
                    f.write(','.join(cand_list)+'\n')
                else:
                    f.write(cand_list[0] + '\n')


    print("合并语义向量和结构化向量覆盖率为：\n", coverage_eval(ent_left, candidates_idx_list, ent_right, ent_right))

if __name__ == '__main__':
    lang = 'zh_en'
    threshold = 3000
    llm_resp_save_dir = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_{}.json'.format(lang)

    entity_ids_1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/{}/ent_ids_1'.format(lang)
    entity_ids_2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/{}/ent_ids_2'.format(lang)

    semantic_embedding_matrix_left = np.loadtxt(llm_resp_save_dir.replace("/llm_response/", "/mid_results_{}_zeroembed_cos_ed_csls_union_{}/".format(str(threshold), lang)).replace("gpt4_turbo_", "entity_embed_left_"), delimiter=',')
    semantic_embedding_matrix_right = np.loadtxt(llm_resp_save_dir.replace("/llm_response/", "/mid_results_{}_zeroembed_cos_ed_csls_union_{}/".format(str(threshold), lang)).replace("gpt4_turbo_", "entity_embed_right_"), delimiter=',')


    subgraph1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/{}/1_neighbor_subgraph_1'.format(lang)
    subgraph2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/{}/1_neighbor_subgraph_2'.format(lang)

    subgraph1_motif_matrix_savepath = '/'.join(subgraph1_path.split('/')[:-1]) + '/1_neighbor_subgraph1_motif_matrix_{}.npy'.format(str(threshold))
    subgraph2_motif_matrix_savepath = '/'.join(subgraph1_path.split('/')[:-1]) + '/1_neighbor_subgraph2_motif_matrix_{}.npy'.format(str(threshold))
    subgraph_motif_embeddig_matrix_left = np.loadtxt(subgraph1_motif_matrix_savepath, delimiter=',')
    subgraph_motif_embeddig_matrix_right = np.loadtxt(subgraph2_motif_matrix_savepath, delimiter=',')

    candidates_save_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/{}/'.format(lang)
    get_performance_of_semantic_and_subgraph_motif_embedding_similarity(
        semantic_embedding_matrix_left,
        subgraph_motif_embeddig_matrix_left,
        semantic_embedding_matrix_right,
        subgraph_motif_embeddig_matrix_right,
        candidates_save_path,
        thres_hold=threshold
    )
