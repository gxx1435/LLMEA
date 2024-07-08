import numpy as np

from run.utils import coverage_eval, get_candidates, get_entity_names
def get_performance_of_semantic_and_subgraph_motif_embedding_similarity(
        semantic_embedding_matrix_left,
        subgraph_motif_embeddig_matrix_left,
        semantic_embedding_matrix_right,
        subgraph_motif_embeddig_matrix_right,
        thres_hold=3000
):
    """
    获取语义向量和结构化向量embedding的结果
    :param semantic_embedding_matrix:
    :param subgraph_motif_embeddig_matrix:
    :param semantic_embedding_matrix_right:
    :param subgraph_motif_embeddig_matrix_right
    :param thres_hold:
    :return:
    """
    print(len(subgraph_motif_embeddig_matrix_left),
          len(subgraph_motif_embeddig_matrix_right))
    assert len(semantic_embedding_matrix_left) == thres_hold and len(subgraph_motif_embeddig_matrix_left)==thres_hold and\
            len(semantic_embedding_matrix_right) == thres_hold and len(subgraph_motif_embeddig_matrix_right)==thres_hold,\
            '语义向量或结构向量长度必须等于threshold'

    matrix1 = np.concatenate((semantic_embedding_matrix_left, subgraph_motif_embeddig_matrix_left), axis=1)
    matrix2 = np.concatenate((semantic_embedding_matrix_left, subgraph_motif_embeddig_matrix_left), axis=1)

    entity_left = get_entity_names(entity_ids_1_path)
    entity_right = get_entity_names(entity_ids_2_path)

    candidates_idx_list, ent_left, ent_right = get_candidates(matrix1,
                                                              matrix2,
                                                              entity_left,
                                                              entity_right,
                                                              method='all')
    print("合并语义向量和结构化向量覆盖率为：\n", coverage_eval(ent_left, candidates_idx_list, ent_right, ent_right))

if __name__ == '__main__':

    llm_resp_save_dir = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_zh_en.json'

    entity_ids_1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/ent_ids_1'
    entity_ids_2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/ent_ids_2'

    semantic_embedding_matrix_left = np.loadtxt(llm_resp_save_dir.replace("/llm_response/", "/mid_results_3000_zeroembed_cos_ed_csls_union/").replace("gpt4_turbo_", "entity_embed_left_"), delimiter=',')
    semantic_embedding_matrix_right = np.loadtxt(llm_resp_save_dir.replace("/llm_response/", "/mid_results_3000_zeroembed_cos_ed_csls_union/").replace("gpt4_turbo_", "entity_embed_right_"), delimiter=',')


    subgraph1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/subgraph_1'
    subgraph2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/subgraph_2'

    subgraph1_motif_matrix_savepath = '/'.join(subgraph1_path.split('/')[:-1]) + '/subgraph1_motif_matrix.npy'
    subgraph2_motif_matrix_savepath = '/'.join(subgraph1_path.split('/')[:-1]) + '/subgraph2_motif_matrix.npy'
    subgraph_motif_embeddig_matrix_left = np.loadtxt(subgraph1_motif_matrix_savepath, delimiter=',')
    subgraph_motif_embeddig_matrix_right = np.loadtxt(subgraph2_motif_matrix_savepath, delimiter=',')

    get_performance_of_semantic_and_subgraph_motif_embedding_similarity(
        semantic_embedding_matrix_left,
        subgraph_motif_embeddig_matrix_left,
        semantic_embedding_matrix_right,
        subgraph_motif_embeddig_matrix_right,
        thres_hold=3000
    )
