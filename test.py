import numpy as np

def eval(ent_left, candidates, gold_label):
    cnt = 0
    for i in range(len(ent_left)):
        if gold_label in candidates[i]:
           cnt += 1
    return float(cnt / len(ent_left))

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


# Example usage
# X_src = np.random.rand(100, 50)  # 100 samples, 50 features in source domain
# X_tgt = np.random.rand(100, 50)  # 100 samples, 50 features in target domain
#
# csls_matrix = compute_csls(X_src, X_tgt, k=10)
# print(csls_matrix.shape)
x = np.array([1,4,3,-1,6,9])
x.argsort()
print(np.argsort(x))
# x = [3, 0, 2, 1, 4, 5]
# y = [0, 2, 5, 3, 4, 1]
# rank = [(x[i], y[i]) for i in range(len(x))]
# rank.sort(key=lambda x: (x[0], x[1]))
# print(rank)