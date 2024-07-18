import  numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import editdistance

def get_entity_names(ent_id_path, thres_hold=3000):
    """
    :param ent_id_path:
    :param thres_hold:
    :return:
    """
    entity_list = []
    counter = 0
    with open(ent_id_path) as f:
        for line in f.readlines():
            if counter == thres_hold: break
            line = line.split("\t")
            entity = line[1].split('/')[-1].strip()
            entity_list.append(entity)
            counter += 1

    return entity_list

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
def compute_csls(X_src, X_tgt, k=10):
    """
    Compute Cross-domain Similarity Local Scaling (CSLS).

    Parameters:
    X_src : np.array
        Source domain embeddings (n_samples_src, n_features)
    X_tgt : np.array
        Target domain embeddings (n_samples_tgt, n_features)
    k : int
        Number of nearest neighbors for local scaling

    Returns:
    csls_matrix : np.array
        CSLS similarity scores matrix (n_samples_src, n_samples_tgt)
    """
    # Compute cosine similarity matrix
    cosine_sim = np.dot(X_src, X_tgt.T)

    # Normalize vectors to have unit norm
    X_src_norm = np.linalg.norm(X_src, axis=1, keepdims=True)
    X_tgt_norm = np.linalg.norm(X_tgt, axis=1, keepdims=True)
    cosine_sim /= (X_src_norm @ X_tgt_norm.T)

    # Compute nearest neighbor similarity for source and target domains
    src_nn_sim = np.zeros(X_src.shape[0])
    tgt_nn_sim = np.zeros(X_tgt.shape[0])

    for i in range(X_src.shape[0]):
        src_nn_sim[i] = np.mean(np.sort(cosine_sim[i, :])[-k:])

    for j in range(X_tgt.shape[0]):
        tgt_nn_sim[j] = np.mean(np.sort(cosine_sim[:, j])[-k:])

    # Compute CSLS similarity scores
    csls_matrix = np.zeros(cosine_sim.shape)
    for i in range(X_src.shape[0]):
        for j in range(X_tgt.shape[0]):
            csls_matrix[i, j] = 2 * cosine_sim[i, j] - src_nn_sim[i] - tgt_nn_sim[j]

    return csls_matrix

def get_candidates(Lvec, Rvec, entity_text_left, entity_text_right, n_cand=100, method='all'):
    """
    According to bert embeddings to get entity candidates
    :param Lvec: all the embeddings for the left entity
    :param Rvec: all the embeddings for the right entity
    :param entity_text_left: all the entity name for the left entity
    :param entity_text_right: all the entity name for the right entity
    :param n_cand:
    :return:
    """
    if method == 'cosine':

        sim = 1 - np.array(cosine_similarity(Lvec, Rvec))


    elif method == 'ed':

        sim = np.zeros((len(entity_text_left), len(entity_text_right)))
        for i in range(len(entity_text_left)):
            for j in range(len(entity_text_right)):
                # sim_edit_dis[i][j] = edit_distance(entity_text_left[i],entity_text_right[j],len(entity_text_left[i]),len(entity_text_right[j]))
                sim[i][j] = editdistance.eval(entity_text_left[i], entity_text_right[j])

    elif method == 'csls':

        sim = 1 - compute_csls(np.array(Lvec), np.array(Rvec))

    elif method == 'all':

        sim = 1 - np.array(cosine_similarity(Lvec, Rvec))

        sim_edit_dis = np.zeros((len(entity_text_left), len(entity_text_right)))

        for i in range(len(entity_text_left)):
            for j in range(len(entity_text_right)):
                # sim_edit_dis[i][j] = edit_distance(entity_text_left[i],entity_text_right[j],len(entity_text_left[i]),len(entity_text_right[j]))
                sim_edit_dis[i][j] = editdistance.eval(entity_text_left[i], entity_text_right[j])
        sim_csls = 1 - compute_csls(np.array(Lvec), np.array(Rvec))

        candidates = [0] * len(Lvec)
        ent_left = [0] * len(Lvec)
        ent_right = [0] * len(Lvec)
        for i in range(len(Lvec)):
            rank1 = sim[i, :].argsort()
            rank2 = sim_edit_dis[i, :].argsort()
            rank3 = sim_csls[i, :].argsort()

            candidates[i] = list(set(rank1[0:n_cand]).union(set(rank2[0:n_cand])).union(set(rank3[0:n_cand])))
            # # 用文本格式转存
            # candidates[i] = [entity_text_right[idx] for idx in candidates[i]]

            ent_left[i] = entity_text_left[i]
            ent_right[i] = entity_text_right[i]

        return candidates, ent_left, ent_right

    elif method == 'all add':

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
        for i in range(len(Lvec)):
            rank = sim[i, :].argsort()
            candidates[i] = rank[0:n_cand]
            # # 用文本格式转存
            # candidates[i] = [entity_text_right[idx] for idx in candidates[i]]

            ent_left[i] = entity_text_left[i]
            ent_right[i] = entity_text_right[i]

        return candidates, ent_left, ent_right

    elif method == 'cosine+csls':

        sim = 1 - np.array(cosine_similarity(Lvec, Rvec))

        sim_csls = 1 - compute_csls(np.array(Lvec), np.array(Rvec))

        candidates = [0] * len(Lvec)
        ent_left = [0] * len(Lvec)
        ent_right = [0] * len(Lvec)
        for i in range(len(Lvec)):
            rank1 = sim[i, :].argsort()
            rank2 = sim_csls[i, :].argsort()

            candidates[i] = list(set(rank1[0:n_cand]).union(set(rank2[0:n_cand])))

            ent_left[i] = entity_text_left[i]
            ent_right[i] = entity_text_right[i]

        return candidates, ent_left, ent_right

    candidates = [0] * len(Lvec)
    ent_left = [0] * len(Lvec)
    ent_right = [0] * len(Lvec)
    for i in range(len(Lvec)):
        rank = sim[i, :].argsort()

        candidates[i] = rank[0:n_cand]

        ent_left[i] = entity_text_left[i]
        ent_right[i] = entity_text_right[i]

    return candidates, ent_left, ent_right

def get_ent_id_dict(ent_id_path):
    """
    :param ent_id_path
    :return:
    """
    entity_id_dict = {}
    with open(ent_id_path, 'r') as f:
        for line in f.readlines():
            idx = line.split('\t')[0]
            entity = line.split('\t')[1].split('/')[-1].strip()
            entity_id_dict.update({entity: idx})
    return entity_id_dict

def get_id_entity_dict(ent_id_path):
    """
    :param ent_id_path
    :return:
    """
    id_entity_dict = {}
    with open(ent_id_path, 'r') as f:
        for line in f.readlines():
            idx = line.split('\t')[0]
            entity = line.split('\t')[1].split('/')[-1].strip()
            id_entity_dict.update({idx: entity})
    return id_entity_dict

def coverage_eval_segment(candidates_idx_list, ent_left, ent_right, entity_text_right, cut_indice):
    """

    :param candidate_idx_list:
    :param ent_left:
    :param ent_right:
    :return:
    """
    cnt = 0
    for i in range(len(ent_left)):
        cand_list = candidates_idx_list[i][:cut_indice]
        candidates = []
        for idx in cand_list:
                cand_txt = entity_text_right[idx]
                candidates.append(cand_txt)

        if ent_right[i] in candidates:
                cnt += 1

    return cnt / len(ent_left)



def coverage_eval(candidates_idx_list, ent_left, ent_right, entity_text_right, out_file=''):
    """
    :param ent_left: source entity
    :param candidates_idx_list: candidates idx list
    :param ent_right: target entity
    :param entity_text_right:
    :param out_file:
    :return:
    """
    cnt = 0
    # ent_id_1_dict = get_ent_id_dict('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/ent_ids_1')
    # id_ent_1_cn_dict = get_id_entity_dict('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/ent_ids_1_cn')
    candidates_list = []
    for i in range(len(ent_left)):
        cand_list = candidates_idx_list[i]
        candidates = []
        for j in cand_list:

            cand_txt = entity_text_right[j]
            candidates.append(cand_txt)

        # print(ent_left[i], candidates, ent_right[i])

        if ent_right[i] in candidates:
           cnt += 1
        elif ent_right[i] not in candidates:
            candidates.append(ent_right[i])

        candidates_list.append(candidates)
        print(ent_right[i], candidates, '\n')

    with open(out_file, 'w') as f:
        for i in range(len(ent_left)):
            f.write(ent_left[i] + '\t' + ','.join(candidates_list[i]) + '\n')


    return float(cnt / len(ent_left))