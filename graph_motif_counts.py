import os, sys
import networkx as nx
import matplotlib.pyplot as plt
import csv, json, pickle
import editdistance
import subprocess
import networkx as nx
import numpy as np
from scipy.spatial.distance import cosine
from sklearn.metrics.pairwise import cosine_similarity
from run.utils import coverage_eval, get_candidates, get_entity_names

def save_graph(G, save_path):
    """
    :param G:
    :param save_path:
    :return:
    """
    with open(save_path, 'w') as f:
        # f.write(str(len(G.nodes))+' '+str(len(G.edges))+'\n')
        for edge in G.edges():
            f.write(str(edge[0])+' '+str(edge[1])+'\n')

def read_graph(save_path):
    """
    :param save_path:
    :return:
    """
    edges = []
    with open(save_path, 'r') as f:
        # next(f)
        for line in f.readlines():
            line = line.split(' ')
            edges.append((int(line[0]), int(line[1].strip())))
    return edges

def get_graph_without_relation(kg_path, newkg_path):
    """
    获取无向图
    :param kg_path:
    :param newkg_path:
    :return:
    """
    ## 以图的格式保存triples文件，暂时未用到
    # Graph = nx.Graph()
    # with open(kg_path, 'r') as f:
    #         for line in f.readlines():
    #             line = line.split('\t')
    #             hentity = line[0]
    #             tentity = line[2].strip()
    #             Graph.add_node(hentity)
    #             Graph.add_node(tentity)
    #             Graph.add_edges_from([(hentity, tentity)])
    #
    # with open(newkg_path, 'w') as out:
    #     out.write(str(len(Graph.nodes)) + ' ' + str(len(Graph.edges)) + '\n')
    #     for line in Graph.edges:
    #         out.write(line[0] + ' ' + line[1] + '\n')
    new_graph = []
    with open(newkg_path, 'w') as out:
        with open(kg_path, 'r') as f:
                for line in f.readlines():
                    line = line.split('\t')
                    hentity = line[0]
                    tentity = line[2].strip()
                    new_graph.append((hentity, tentity))
                    out.write(hentity+' '+tentity+'\n')

    return new_graph

# 定义一个函数来获取每个节点的三阶及以内邻居形成的子图
def get_subgraph_within_k_per_node(G, node, k):
    """
    单个节点下获取大图的K阶邻居子图（K=3）
    :param G:
    :param node:
    :param k:
    :return:
    """
    subgraph = nx.Graph()
    frontier = set([node])
    for _ in range(k):
        next_frontier = set()
        for n in frontier:
            neighbors = set(G.neighbors(n))
            subgraph.add_node(n)
            subgraph.add_edges_from((n, nbr) for nbr in neighbors)
            next_frontier.update(neighbors)
        frontier = next_frontier

    return subgraph

def get_subgraph_with_k_all_nodes(graph_edges, nodes=[], subgraph_savepath=''):
    """
    获取给定节点的K阶子图 (k=3)
    :param graph_edges:
    :param nodes:
    :return:
    """
    # 创建一个示例图
    G = nx.Graph()
    G.add_edges_from(graph_edges)

    nodes = nodes

    # 获取每个节点的三阶及以内邻居形成的子图
    node_subgraphs = {}
    for node in nodes:
        print(node)
        try:
            subgraph = get_subgraph_within_k_per_node(G, node, 2)
            save_graph(subgraph, subgraph_savepath.format(node))
            node_subgraphs[node] = subgraph
        except:
            pass

    # # 打印每个节点的子图节点和边信息
    # for node, subgraph in node_subgraphs.items():
    #     print(f"Node {node} subgraph: {subgraph}")
    #     print(f"Node {node} subgraph nodes: {subgraph.nodes()}")
    #     print(f"Node {node} subgraph edges: {subgraph.edges()}")

    return node_subgraphs

# 定义一个函数来计算 Motif count
def count_motifs(G):
    motifs = {
        '003': 0,  # 无三角形
        '012': 0,  # 一种三角形
        '102': 0,  # 另一种三角形
        '021C': 0,  # 一种三角形和一条边
        '021D': 0,  # 两种三角形
        '111D': 0,  # 三种三角形
        '030T': 0,  # 三角形中有一个三角形
        '030C': 0,  # 三角形中有一条边
        '201': 0,  # 两个三角形
        '120D': 0,  # 三个三角形
        '120U': 0,  # 三个三角形
        '210': 0,  # 三个三角形
    }
    for u, v in G.edges():
        neighbors_u = set(G.neighbors(u))
        neighbors_v = set(G.neighbors(v))
        common_neighbors = neighbors_u & neighbors_v
        for w in common_neighbors:
            if G.has_edge(u, w) and G.has_edge(v, w):
                motifs['021D'] += 1
        if len(common_neighbors) == 1:
            motifs['012'] += 1
        elif len(common_neighbors) == 2:
            motifs['102'] += 1
        elif len(common_neighbors) == 0:
            motifs['003'] += 1
        elif len(common_neighbors) == 3:
            motifs['021C'] += 1
    return motifs

# 定义一个函数来计算 Motif count 相似度
def motif_count_similarity(G1, G2):
    """
    获取两个图的motif similarity,每次都要调用motif counts函数
    :param G1:
    :param G2:
    :return:
    """
    motifs_G1 = count_motifs(G1)
    motifs_G2 = count_motifs(G2)

    # 将 Motif count 转换为向量形式
    vector_G1 = [motifs_G1[m] for m in sorted(motifs_G1)]
    vector_G2 = [motifs_G2[m] for m in sorted(motifs_G2)]

    # 计算余弦相似度
    similarity = 1 - cosine(vector_G1, vector_G2)
    return similarity

def get_subgraph_from_graph(newgraph_path, subgraph_node_path, entity_ids_path, threhold=3000):
    """
    从大图里获取node节点为 [] 的子图
    1. 先读取大图
    2. 确定需要获取子图的节点
    3. 从大图中获取node节点为i的子图
    :param newgraph_path:
    :param subgraph_node_path:
    :param entity_ids_path:
    :param threhold:
    :return:
    """
    ## 读取大图
    nodes = []
    cnt = 0
    with open(entity_ids_path) as f:
       for line in f.readlines():
            if cnt == threhold: break
            idx = int(line.split('\t')[0])
            nodes.append(idx)
            cnt += 1

    graph_edges_kg = read_graph(newgraph_path)
    subgraph_node_path = subgraph_node_path + '/{}.graph'

    get_subgraph_with_k_all_nodes(graph_edges_kg, nodes, subgraph_node_path)

def get_subgraph_edges(subgraph_path):
    """
    调用escape包，获取每个子图escape标准输入edges文件,原文件为未经处理的图的边文件
    :param subgraph_path
    :return:
    """
    import subprocess
    python_f = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/escape/python/sanitize.py'
    subgraph_files = [f for f in os.listdir(subgraph_path) if 'graph' in f]

    for i, subgraph_file in enumerate(subgraph_files):
        print(subgraph_file)
        subprocess.run(['python3', python_f, subgraph_path, subgraph_file])


def get_subgraph_motif_vectors(subgraph_edges_path):
    """
    调用escape获取子图的motif counts vectors
    :param subgraph_edges_path: escape标准输入文件edges
    :return:
    """
    # 指定目标目录
    target_directory = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/escape/wrappers'

    # 切换到目标目录
    os.chdir(target_directory)

    python_f = 'subgraph_counts.py'
    subgraph_edges_files = [os.path.join(subgraph_edges_path, f) for f in os.listdir(subgraph_edges_path) if 'edges' in f]

    for i, subgraph_edges_file in enumerate(subgraph_edges_files):
        out_file = subgraph_edges_file.replace('edges', 'out')
        print(subgraph_edges_file)
        subprocess.run(['python3', python_f, subgraph_edges_file, '4', '-i', out_file])

def get_subgraph_motif_statics(subgraph_out_path):
    """
    获取所有子图motif文件的向量长度，以便于初始化motif counts矩阵
    :param subgraph_out_path:
    :return:
    """
    subgraph_out_files = [os.path.join(subgraph_out_path, f) for f in os.listdir(subgraph_out_path) if 'out' in f]
    length = []
    for file in subgraph_out_files:
        file_len = len(open(file).readlines())
        if file_len != 17: print(file)
        length.append(file_len)
    print(len(length))
    print('Motif count file has lines: ', set(length))

def get_subgraph_motif_matrix(subgraph_path, subgraph_motif_matrix_savepath, thres_hold=3000):
    """
    初始化motif counts矩阵，并以array格式保存
    :param subgraph_path:
    :return:
    """
    if os.path.exists(subgraph_motif_matrix_savepath):

        subgraph_motif_matrix = np.loadtxt(subgraph_motif_matrix_savepath, delimiter=',')

    else:

        subgraph_out_files = [f for f in os.listdir(subgraph_path) if 'out' in f]
        # 获取threshold个数的 out 文件生成motif matrix
        subgraph_out_files = sorted(subgraph_out_files, key=lambda x: int(x.split('.')[0]))[:thres_hold]
        subgraph_out_files = [os.path.join(subgraph_path, f) for f in subgraph_out_files]

        motif_type_counts = 15
        subgraph_motif_matrix = np.zeros((thres_hold, motif_type_counts))
        for i in range(thres_hold):
            vecs = [int(float(x.strip())) for x in open(subgraph_out_files[i]).readlines()[2:]]
            print(vecs)
            subgraph_motif_matrix[i] = vecs

        print('归一化前 matrix：\n', subgraph_motif_matrix)

        # L2范数归一化
        row_norm = np.linalg.norm(subgraph_motif_matrix, axis=1, keepdims=True)
        subgraph_motif_matrix = subgraph_motif_matrix / row_norm
        print('归一化后的矩阵:\n', subgraph_motif_matrix)

        # 处理特殊值
        # 替换 NaN 为 0
        subgraph_motif_matrix = np.nan_to_num(subgraph_motif_matrix, nan=0.0)
        # 替换 Infinity 为一个较大的数（例如 np.finfo(np.float64).max）
        subgraph_motif_matrix = np.nan_to_num(subgraph_motif_matrix,
                                              posinf=np.finfo(np.float64).max,
                                              neginf=np.finfo(np.float64).min)

        np.savetxt(subgraph_motif_matrix_savepath, subgraph_motif_matrix, delimiter=',', fmt='%f')

    return subgraph_motif_matrix

def get_subgraph_motif_similarity_matrix(subgraph1_motif_matrix,
                                         subgraph2_motif_matrix,
                                         subgraph_motif_similairty_savepath):
    """
    获取两个motif counts matrix的cosine similarity matrix
    :param subgraph1_motif_matrix:
    :param subgraph2_motif_matrix:
    :param subgraph_motif_similairty_savepath:
    :return:
    """
    if os.path.exists(subgraph_motif_similairty_savepath):
        sim = np.loadtxt(subgraph_motif_similairty_savepath, delimiter=',')
    else:
        sim = np.array(cosine_similarity(subgraph1_motif_matrix, subgraph2_motif_matrix))
        np.savetxt(subgraph_motif_similairty_savepath, sim, delimiter=',',  fmt='%f')

def check_not_generated_files(ent_ids_path, subgraph_path, threshold=3000):
    """
    丢失文件全部为out类型，重新生成
    :param ent_ids_path:
    :param subgraph_path:
    :param threshold:
    :return:
    """
    missing_files = []

    nodes = []
    cnt = 0
    with open(ent_ids_path) as f:
        for line in f.readlines():
            if cnt == threshold: break
            idx = line.split('\t')[0]
            nodes.append(idx)
            cnt += 1

    ## check out file缺失文件
    for key in ['out', 'graph', 'edges']:
        for node in nodes:
            f_path = os.path.join(subgraph_path, node+'.{}'.format(key))
            if not os.path.exists(f_path):
                print('Not exisites path, please check:', f_path)
                missing_files.append(f_path)

    return missing_files

def regenerate_missing_files(missing_files):
    """
    :return:
    """
    # 指定目标目录
    target_directory = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/escape/wrappers'

    # 切换到目标目录
    os.chdir(target_directory)

    python_f = 'subgraph_counts.py'
    missing_files_edges = [f.replace('out', 'edges') for f in missing_files]

    for i, subgraph_edges_file in enumerate(missing_files_edges):
        out_file = subgraph_edges_file.replace('edges', 'out')
        print(subgraph_edges_file)
        subprocess.run(['python3', python_f, subgraph_edges_file, '4', '-i', out_file])



# def main():
#     """
#     暂时没有用到
#     :return:
#     """
#     subgraph1_left = [os.path.join(subgraph1_path, f) for f in os.listdir(subgraph1_path)]
#     subgraph2_right = [os.path.join(subgraph2_path, f) for f in os.listdir(subgraph2_path)]
#
#     subgraph_motif_similairty = np.zeros((len(subgraph1_left), len(subgraph2_right)))
#     for i in range(len(subgraph1_left)):
#         for j in range(len(subgraph2_right)):
#             graph1_edges = read_graph(subgraph1_left[i])
#             graph2_edges = read_graph(subgraph2_right[j])
#             graph1 = nx.Graph()
#             graph1.add_edges_from(graph1_edges)
#             graph2 = nx.Graph()
#             graph2.add_edges_from(graph2_edges)
#             motif_similarity = motif_count_similarity(graph1, graph2)
#             print(motif_similarity)
#             subgraph_motif_similairty[i][j] = motif_similarity
#
#     np.save(subgraph_motif_similairty_path, subgraph_motif_similairty)


if __name__ == '__main__':

    lang = sys.argv[1]
    thres_hold = 3765
    dataset = 'icews_yago'

    kg1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/triples_1'.format(dataset)
    kg2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/triples_2'.format(dataset)

    newgraph1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/newgraph_1'.format(dataset)
    newgraph2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/newgraph_2'.format(dataset)

    entity_ids_1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1'.format(dataset)
    entity_ids_2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_2'.format(dataset)

    subgraph1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/2_neighbor_subgraph_1'.format(dataset)
    subgraph2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/2_neighbor_subgraph_2'.format(dataset)


    ## 根据triples 获取大图的边list文件
    try:
        with open(newgraph1_path, 'r') as f:
            newgraph1 = f.readlines()

        with open(newgraph2_path, 'r') as f:
            newgraph2 = f.readlines()

    except:
        get_graph_without_relation(kg1_path, newgraph1_path)
        get_graph_without_relation(kg2_path, newgraph2_path)

    ##判断子图文件夹是否存在，不存在就创建一个
    if not os.path.exists(subgraph1_path):
        os.mkdir(subgraph1_path)
    if not os.path.exists(subgraph2_path):
        os.mkdir(subgraph2_path)

    ## 从大图中获得k阶邻居子图

    get_subgraph_from_graph(newgraph1_path, subgraph1_path, entity_ids_1_path, threhold=thres_hold)
    get_subgraph_from_graph(newgraph2_path, subgraph2_path, entity_ids_2_path, threhold=thres_hold)
    exit()
    #
    # ## 根据大图和给定节点获取3阶邻居子图的边list文件
    # get_subgraph_edges(subgraph1_path)
    # get_subgraph_edges(subgraph2_path)
    #
    # ## 调用escape包获取子图motif counts
    # get_subgraph_motif_vectors(subgraph_edges_path=subgraph1_path)
    # get_subgraph_motif_vectors(subgraph_edges_path=subgraph2_path)
    #
    # # 检查motif counts的statics信息
    # get_subgraph_motif_statics(subgraph1_path)
    # get_subgraph_motif_statics(subgraph2_path)
    #
    # # 生成missing的out文件
    # subgraph1_missing_files = check_not_generated_files(entity_ids_1_path, subgraph1_path, threshold=thres_hold)
    # subgraph2_missing_files = check_not_generated_files(entity_ids_2_path, subgraph2_path, threshold=thres_hold)
    #
    # regenerate_missing_files(subgraph1_missing_files)
    # regenerate_missing_files(subgraph2_missing_files)
    #

    ## 获取子图motif counts 归一化矩阵
    subgraph1_motif_matrix_savepath = '/'.join(subgraph1_path.split('/')[:-1]) + '/1_neighbor_subgraph1_motif_matrix_{}.npy'.format(str(thres_hold))
    subgraph2_motif_matrix_savepath = '/'.join(subgraph1_path.split('/')[:-1]) + '/1_neighbor_subgraph2_motif_matrix_{}.npy'.format(str(thres_hold))

    subgraph1_motif_matrix = get_subgraph_motif_matrix(subgraph1_path,
                                                       subgraph1_motif_matrix_savepath,
                                                       thres_hold=thres_hold)
    subgraph2_motif_matrix = get_subgraph_motif_matrix(subgraph2_path,
                                                       subgraph2_motif_matrix_savepath,
                                                       thres_hold=thres_hold)


    try:
        with open('/'.join(
            subgraph1_path.split('/')[:-1]) + '/subgraph_motif_similarity_candidates_{}.pkl'.format(lang), "rb") as fp:
            candidates_idx_list = pickle.load(fp)

        with open('/'.join(
            subgraph1_path.split('/')[:-1]) + '/aligned_entity_{}.json'.format(lang), 'r', encoding='utf8') as f:
            ent_right = json.load(f)

        with open('/'.join(
            subgraph1_path.split('/')[:-1]) + '/target_entity_{}.json'.format(lang), 'r', encoding='utf8') as f:
            ent_left = json.load(f)
    except:

        entity_left = get_entity_names(entity_ids_1_path)
        entity_right = get_entity_names(entity_ids_2_path)

        print(len(entity_left), len(entity_right))
        candidates_idx_list, ent_left, ent_right = get_candidates(subgraph1_motif_matrix,
                                                                  subgraph2_motif_matrix,
                                                                  entity_left,
                                                                  entity_right,
                                                                  n_cand=50,
                                                                  method='csls')
        print(len(ent_left), len(ent_right))
        save_dir = '/'.join(
        subgraph1_path.split('/')[:-1]) + '/subgraph_motif_similarity_candidates_{}.pkl'.format(lang)
        with open(save_dir, 'w', encoding='utf8') as f:
            pickle.dump(candidates_idx_list, open(save_dir, "wb"))

        save_dir = '/'.join(
        subgraph1_path.split('/')[:-1]) + '/aligned_entity_{}.json'.format(lang)
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(ent_right, f)

        save_dir = '/'.join(
        subgraph1_path.split('/')[:-1]) + '/target_entity_{}.json'.format(lang)
        with open(save_dir, 'w', encoding='utf8') as f:
            json.dump(ent_left, f)


    # print(coverage_eval(ent_left, candidates_idx_list, ent_right, ent_right))


