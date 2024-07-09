import os.path
import networkx as nx
from itertools import combinations
from heapq import nlargest
import numpy as np
from collections import Counter, defaultdict


from run.utils import get_id_entity_dict, get_ent_id_dict

tmp = """
import connected_with, Express_intent_to_provide_economic_aid, Express_intent_to_meet_or_negotiate
import Impose_blockade_restrict_movement, Demonstrate_or_rally, fight_with_artillery_and_tanks
import Accuse, Express_intent_to_engage_in_diplomatic_cooperation

def National_Drug_Law_Enforcement_Agency_connected_with_triangle_motif(self):
    National_Drug_Law_Enforcement_Agency = connected_with(European_Union)
    European_Union = connected_with(Olusegun_Mimiko)
    Olusegun_Mimiko = connected_with(National_Drug_Law_Enforcement_Agency)

    return National_Drug_Law_Enforcement_Agency, European_Union, Olusegun_Mimiko

def Nigeria_Express_intent_to_provide_economic_aid_triangle_motif(self):
    Nigeria = Express_intent_to_provide_economic_aid(National_Drug_Law_Enforcement_Agency)
    National_Drug_Law_Enforcement_Agency = connected_with(Olusegun_Mimiko)
    Olusegun_Mimiko = Express_intent_to_meet_or_negotiate(Nigeria)

    return Nigeria, National_Drug_Law_Enforcement_Agency, Olusegun_Mimiko

def Goodluck_Jonathan_fight_with_artillery_and_tanks_triangle_motif(self):
    Goodluck_Jonathan = connected_with(National_Drug_Law_Enforcement_Agency)
    National_Drug_Law_Enforcement_Agency = connected_with(Olusegun_Mimiko)
    Olusegun_Mimiko = fight_with_artillery_and_tanks(Goodluck_Jonathan)

    return Goodluck_Jonathan, National_Drug_Law_Enforcement_Agency, Olusegun_Mimiko

def National_Drug_Law_Enforcement_Agency_Demonstrate_or_rally_triangle_motif(self):
    National_Drug_Law_Enforcement_Agency = connected_with(Olusegun_Mimiko)
    Olusegun_Mimiko = Demonstrate_or_rally(Peter_Obi)
    Peter_Obi = Demonstrate_or_rally(National_Drug_Law_Enforcement_Agency)

    return National_Drug_Law_Enforcement_Agency, Olusegun_Mimiko, Peter_Obi

def National_Drug_Law_Enforcement_Agency_fight_with_artillery_and_tanks_triangle_motif(self):
    National_Drug_Law_Enforcement_Agency = connected_with(Olusegun_Mimiko)
    Olusegun_Mimiko = fight_with_artillery_and_tanks(Muhammadu_Buhari)
    Muhammadu_Buhari = Express_intent_to_meet_or_negotiate(National_Drug_Law_Enforcement_Agency)

    return National_Drug_Law_Enforcement_Agency, Olusegun_Mimiko, Muhammadu_Buhari

def Olusegun_Mimiko_Express_intent_to_meet_or_negotiate_triangle_motif(self):
    Olusegun_Mimiko = Express_intent_to_meet_or_negotiate(Muhammadu_Buhari)
    Muhammadu_Buhari = connected_with(National_Drug_Law_Enforcement_Agency)
    National_Drug_Law_Enforcement_Agency = connected_with(Olusegun_Mimiko)

    return Olusegun_Mimiko, Muhammadu_Buhari, National_Drug_Law_Enforcement_Agency
"""

def find_triangle_or_star_motifs(graph, node, top_n=5):
    """
    :param graph:
    :param node:
    :param top_n:
    :return:
    """
    # 获取目标节点的邻居
    neighbors = set(graph.neighbors(node))

    # 字典来记录每个邻居节点与目标节点共享的三角形列表
    shared_triangles = {neighbor: [] for neighbor in neighbors}

    # 遍历每个邻居节点，找出共享三角形
    for neighbor in neighbors:
        # 获取邻居节点的邻居
        neighbors_of_neighbor = set(graph.neighbors(neighbor))

        # 找出共同邻居（即三角形中的第三个节点）
        common_neighbors = neighbors & neighbors_of_neighbor

        # 记录共享三角形
        for common_neighbor in common_neighbors:
            triangle = tuple(sorted((node, neighbor, common_neighbor)))
            shared_triangles[neighbor].append(triangle)

    # 将所有共享三角形收集到一个列表中
    all_shared_triangles = []
    for triangles in shared_triangles.values():
        all_shared_triangles.extend(triangles)

    # 找出前 top_n 个共享次数最多的三角形
    top_shared_triangles = nlargest(top_n, set(all_shared_triangles), key=lambda t: all_shared_triangles.count(t))

    # 构建包含这些三角形motif的子图
    motif_graphs = []
    for triangle in top_shared_triangles:
        motif_graph = nx.Graph()
        motif_graph.add_edges_from(
            [(triangle[0], triangle[1]),
             (triangle[1], triangle[2]),
             (triangle[2], triangle[0])]
        )
        motif_graphs.append(motif_graph)

    ## if the triangle is empty list, then give its star information
    if len(motif_graphs) == 0:
        motif_graphs = find_top_star_motif(graph, node, top_n)

    return motif_graphs

def find_top_star_motif(G, node, top_n):
    def build_star_motif(graph, center_node, top_n):
        # 获取节点的出边和入边
        out_edges = list(graph.out_edges(center_node))
        in_edges = list(graph.in_edges(center_node))

        # 对出边和入边分别按度数排序，并保留最多五条边
        top_out_edges = sorted(out_edges, key=lambda edge: graph.degree(edge[1]), reverse=True)[:top_n]
        top_in_edges = sorted(in_edges, key=lambda edge: graph.degree(edge[0]), reverse=True)[:top_n]

        # 构建星型motif子图
        star_motif = nx.DiGraph()
        for edge in top_out_edges:
            star_motif.add_edge(*edge)
        for edge in top_in_edges:
            star_motif.add_edge(*edge)

        return star_motif

    # 指定要查找star型motif的节点
    star_motif = build_star_motif(G, node, top_n)

    return [star_motif]

# def find_triangle_motifs(graph, node, top_n=5):
#     """
#     Find all triangle motifs in the graph and return them as subgraphs.
#
#     :param graph: A NetworkX graph
#     :return: A list of subgraphs, each representing a triangle motif
#     """
#     # triangles = [clique for clique in nx.enumerate_all_cliques(graph) if len(clique) == 3]
#     # subgraphs = []
#     #
#     # for triangle in triangles:
#     #     print(triangle)
#     #     subgraph = graph.subgraph(triangle).copy()
#     #     subgraphs.append(subgraph)
#     #
#     # return subgraphs
#
#     # subgraphs = []
#     #
#     # # 使用 NetworkX 提供的函数查找所有三角形
#     # # for node in graph.nodes():
#     # neighbors = list(graph.neighbors(node))
#     # print(len(neighbors))
#     #
#     # neighbors = neighbors[:50]
#     # for i in range(len(neighbors)):
#     #     for j in range(i + 1, len(neighbors)):
#     #         if graph.has_edge(neighbors[i], neighbors[j]):
#     #             triangle = tuple(sorted([node, neighbors[i], neighbors[j]]))
#     #             subgraph = graph.subgraph(triangle).copy()
#     #             subgraphs.append(subgraph)
#     #
#     # return subgraphs
#
#     # 获取目标节点的邻居
#     neighbors = set(graph.neighbors(node))
#
#     # 字典来记录每个邻居节点与目标节点共享的三角形列表
#     shared_triangles = {neighbor: [] for neighbor in neighbors}
#
#     # 遍历每个邻居节点，找出共享三角形
#     for neighbor in neighbors:
#         # 获取邻居节点的邻居
#         neighbors_of_neighbor = set(graph.neighbors(neighbor))
#
#         # 找出共同邻居（即三角形中的第三个节点）
#         common_neighbors = neighbors & neighbors_of_neighbor
#
#         # 记录共享三角形
#         for common_neighbor in common_neighbors:
#             triangle = tuple(sorted((node, neighbor, common_neighbor)))
#             shared_triangles[neighbor].append(triangle)
#
#         # 将所有共享三角形收集到一个列表中
#         all_shared_triangles = []
#         for triangles in shared_triangles.values():
#                 all_shared_triangles.extend(triangles)
#
#         # 找出前 top_n 个共享次数最多的三角形
#         top_shared_triangles = nlargest(top_n, set(all_shared_triangles), key=lambda t: all_shared_triangles.count(t))
#
#         # 构建包含这些三角形motif的子图
#         motif_graphs = []
#         for triangle in top_shared_triangles:
#                 motif_graph = nx.Graph()
#                 motif_graph.add_edges_from(
#                 [(triangle[0], triangle[1]), (triangle[1], triangle[2]), (triangle[2], triangle[0])])
#
#                 if node in motif_graph.nodes():
#                     motif_graphs.append(motif_graph)
#
#         return motif_graphs

    # def find_top_triangle_subgraphs(G, top_count=5):
    #     triangles = [clique for clique in nx.enumerate_all_cliques(graph) if len(clique) == 3]
    #
    #     triangle_counts = Counter(triangles)
    #     top_triangles = triangle_counts.most_common(top_count)
    #
    #     top_triangle_subgraphs = defaultdict(lambda: {'subgraph': None, 'count': 0})
    #
    #     for triangle, count in top_triangles:
    #         u, v, w = triangle
    #         subgraph_nodes = tuple(sorted([u, v, w]))
    #         if top_triangle_subgraphs[subgraph_nodes]['subgraph'] is None:
    #             subgraph = G.subgraph([u, v, w])
    #             top_triangle_subgraphs[subgraph_nodes] = {'subgraph': subgraph, 'count': count}
    #         else:
    #             top_triangle_subgraphs[subgraph_nodes]['count'] += count
    #
    #     return top_triangle_subgraphs
    #
    # # 示例用法：
    # # 假设 G 是你的图对象
    # top_triangle_subgraphs = find_top_triangle_subgraphs(graph)
    #
    # motif_graphs = []
    # # 打印每个三角形子图的节点和边，以及计数
    # for subgraph_nodes, data in top_triangle_subgraphs.items():
    #     print(f"Triangle Nodes: {subgraph_nodes}, Count: {data['count']}")
    #     subgraph = data['subgraph']
    #     motif_graphs.append(subgraph)
    #
    #
    # return motif_graphs

def find_four_cycles(G):
    """
    Find all 4 cycle motifs in the graph and return them as subgraphs.

    :param graph: A NetworkX graph
    :return: A list of subgraphs, each representing a 4 cycle motif
    :return:
    """
    four_cycles = []
    nodes = list(G.nodes())
    for combo in combinations(nodes, 4):
        subgraph = G.subgraph(combo)
        if len(subgraph.edges()) == 4:
            four_cycles.append(combo)

    subgraphs = [G.subgraph(cycle).copy() for cycle in four_cycles]

    return subgraphs


import networkx as nx


def create_star_motif_with_8_edges(graph, center_node, num_edges=5):
    """
    Create a star motif centered around the specified node in the graph, retaining up to num_edges edges.

    Parameters:
    graph (networkx.DiGraph): The input directed graph.
    center_node (str/int): The node to be the center of the star motif.
    num_edges (int): The maximum number of edges to retain in the star motif.

    Returns:
    networkx.DiGraph: A subgraph containing the star motif.
    """
    # Create a new directed graph for the star motif
    star_motif = nx.DiGraph()

    # Add the center node
    star_motif.add_node(center_node)

    # Get the outgoing and incoming edges of the center node
    out_edges = list(graph.out_edges(center_node))
    in_edges = list(graph.in_edges(center_node))

    # Combine the edges and sort them to keep the order consistent
    combined_edges = out_edges + in_edges
    combined_edges = sorted(combined_edges, key=lambda edge: (edge[0], edge[1]))

    # Keep only up to num_edges edges
    combined_edges = combined_edges[:num_edges]

    # Add the edges to the star motif
    star_motif.add_edges_from(combined_edges)

    return star_motif


def find_star_motifs(graph, node):
    """
    Find all star motifs in the graph and return them as subgraphs.

    :param graph: A NetworkX graph
    :return: A list of subgraphs, each representing a star motif
    """
    stars = []

    # Iterate over nodes to find stars

    neighbors = list(graph.neighbors(node))
    if len(neighbors) > 1:  # Node has more than one neighbor
            star_nodes = [node] + neighbors
            star = graph.subgraph(star_nodes).copy()

            star = create_star_motif_with_8_edges(star, node, 8)

            stars.append(star)

    return stars


def find_chain_motifs(graph, length):
    """
    Find all chain motifs of the specified length in the graph and return them as subgraphs.

    :param graph: A NetworkX graph
    :param length: The length of the chain motif
    :return: A list of subgraphs, each representing a chain motif of the specified length
    """
    chains = []

    # Iterate over nodes to find chains
    for node in graph.nodes():
        paths = nx.single_source_shortest_path(graph, node, cutoff=length - 1)
        for path in paths.values():
            if len(path) == length:
                chain = graph.subgraph(path).copy()
                chains.append(chain)

    return chains

def find_tree_motifs(graph, root, size):
    """
    Find all tree motifs in the graph of a given size that include the specified root node and return them as subgraphs.

    :param graph: A NetworkX graph
    :param root: The root node to find tree motifs around
    :param size: The number of nodes in the tree motif
    :return: A list of subgraphs, each representing a tree motif of the specified size that includes the root node
    """

    def is_tree(subgraph):
        return nx.is_tree(subgraph)

    motifs = []
    nodes = list(graph.nodes())

    for combination in combinations(nodes, size):
        if root in combination:
            subgraph = graph.subgraph(combination)
            if is_tree(subgraph):
                motifs.append(subgraph)
    return motifs

def find_star_triangle_motifs(graph):
    """
    Find all star-triangle motifs in the graph and return them as subgraphs.

    :param graph: A NetworkX graph
    :return: A list of subgraphs, each representing a star-triangle motif
    """
    motifs = []

    for node in graph.nodes():
        neighbors = list(graph.neighbors(node))
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                neighbor1 = neighbors[i]
                neighbor2 = neighbors[j]
                if graph.has_edge(neighbor1, neighbor2):
                    # Add the third node to complete the triangle
                    for k in range(j + 1, len(neighbors)):
                        neighbor3 = neighbors[k]
                        if graph.has_edge(neighbor1, neighbor3) and graph.has_edge(neighbor2, neighbor3):
                            motif_nodes = {node, neighbor1, neighbor2, neighbor3}
                            subgraph = graph.subgraph(motif_nodes).copy()
                            motifs.append(subgraph)

    return motifs
def test_find_motifs():
    # 创建图
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 4), (2, 4), (4, 5), (5, 6), (6, 4)])

    # 获取所有三角形motif子图
    triangle_motifs = find_triangle_or_star_motifs(G)

    # 打印每个三角形motif子图的节点和边
    for i, subgraph in enumerate(triangle_motifs):
        print(f"Triangle {i + 1}:")
        print("Nodes:", subgraph.nodes())
        print("Edges:", subgraph.edges())

def test_find_different_motifs_from_subgraphs():
    id_ent_dict = get_id_entity_dict('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/ent_ids_1_cn')
    # print(id_ent_dict)

    subgraph_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/2_neighbor_subgraph_1'
    subgraph_files = sorted([f for f in os.listdir(subgraph_path) if 'graph' in f],
                            key=lambda x: int(x.split('.')[0]))
    subgraph_files = [os.path.join(subgraph_path, f) for f in subgraph_files]

    for file in subgraph_files:
        edges = []
        with open(file, 'r') as f:
            for line in f.readlines():
                edges.append((line.split(' ')[0], line.split(' ')[1].strip()))
        G = nx.Graph()
        G.add_edges_from(edges)

        node = file.split('/')[-1].split('.')[0]
        if node == '184': break
        motifs = find_triangle_or_star_motifs(G)
        # motifs = find_four_cycles(G)
        # motifs = find_star_motifs(G)

        # motifs = find_tree_motifs(G, node, 4)
        # motifs = find_chain_motifs(G, 3)
        # motifs = find_star_triangle_motifs(G)


        # for i, subgraph in enumerate(triangle_motifs):
        for i, subgraph in enumerate(motifs):
            if node in subgraph.nodes:

                print(node, id_ent_dict[node], '\t', f"{i + 1}:")

                nodes = [id_ent_dict[idx] for idx in subgraph.nodes()]
                edges = [(id_ent_dict[i], id_ent_dict[j]) for i, j in subgraph.edges()]

                print("Nodes:", nodes)
                print("Edges:", edges)

def test_get_relation():
    #         ent_ids.append((ent_id_1, rel_id, ent_id_2))
    # ent_ids = set(ent_ids)
    # ent_ids = sorted(ent_ids, key=lambda x: (int(x[0]), int(x[2])))
    # with open(new_triples2, 'w') as f:
    #     for line in ent_ids:
    #         f.write(line[0]+'\t'+line[1]+'\t'+line[2]+'\n')

    # triple1_dict = {}
    # with open(new_triples1) as f:
    #     for line in f.readlines():
    #         try:
    #             ent_id_1 = line.split('\t')[0].strip()
    #             rel_id = line.split('\t')[1].strip()
    #             ent_id_2 = line.split('\t')[2].strip()
    #             triple1_dict.update({ent_id_1: {ent_id_2: triple1_dict[ent_id_1][ent_id_2].append(rel_id)}})
    #         except:
    #             triple1_dict.update({ent_id_1: {ent_id_2: []}})

    # triple2_dict = {}
    # with open(new_triples2) as f:
    #     for line in f.readlines():
    #         try:
    #             ent_id_1 = line.split('\t')[0].strip()
    #             rel_id = line.split('\t')[1].strip()
    #             ent_id_2 = line.split('\t')[2].strip()
    #             triple2_dict.update({ent_id_1: {ent_id_2: triple2_dict[ent_id_1][ent_id_2].append(rel_id)}})
    #         except:
    #             triple2_dict.update({ent_id_1: {ent_id_2: []}})
    exit()

dataset = 'icews_yago'

id_ent_dict1 = get_id_entity_dict(
    '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/ent_ids_1'.format(dataset))
id_ent_dict2 = get_id_entity_dict(
    '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/ent_ids_2'.format(dataset))
# ent_id_dict1 = get_ent_id_dict(
#     '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/ent_ids_1'.format(dataset))


ent_id_1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1'.format(dataset)
ent_id_2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_2_aligned'.format(dataset)

sematic_embedding_candidates_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_10_3765_all_corrected.txt'.format(dataset)
entity_keys = [line.split('\t')[0].strip() for line in open(sematic_embedding_candidates_path).readlines()]
cand_list_values = [line.split('\t')[1].strip().split(',') for line in open(sematic_embedding_candidates_path).readlines()]
candidates = dict(zip(entity_keys, cand_list_values))

##  获取relation of two nodes
triple1 = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/triples_1'.format(dataset)
triple2 = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/triples_2'.format(dataset)
new_triples1 = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_triples_1'.format(dataset)
new_triples2 = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_triples_2'.format(dataset)
G1 = nx.MultiDiGraph()
with open(new_triples1) as f:
    for line in f.readlines():
        ent_id_1 = line.split('\t')[0].strip()
        rel_id = line.split('\t')[1].strip()
        ent_id_2 = line.split('\t')[2].strip()
        G1.add_edge(ent_id_1, ent_id_2, relation=rel_id)


G2 = nx.MultiDiGraph()
# ent_ids = []
with open(new_triples2) as f:
    for line in f.readlines():
        ent_id_1 = line.split('\t')[0].strip()
        rel_id = line.split('\t')[1].strip()
        ent_id_2 = line.split('\t')[2].strip()
        G2.add_edge(ent_id_1, ent_id_2, relation=rel_id)

rel_1_dict = dict()
rel_ids_1 = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_wiki/rel_ids_1'
with open(rel_ids_1) as f:
    for line in f.readlines():
        rel_1_dict.update({line.split('\t')[0]: line.split('\t')[1].strip()})

rel_2_dict = dict()
rel_ids_2 = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_wiki/rel_ids_2'
with open(rel_ids_2)as f:
    for line in f.readlines():
        rel_2_dict.update({line.split('\t')[0]: line.split('\t')[1].strip()})

_2_neighbor_subgraph1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/2_neighbor_subgraph_1'.format(dataset)
_1_neighbor_subgraph1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/1_neighbor_subgraph_1'.format(dataset)
_2_neighbor_subgraph2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/2_neighbor_subgraph_2'.format(dataset)
_1_neighbor_subgraph2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/1_neighbor_subgraph_2'.format(dataset)

class Entity:

    def __init__(self, entity_name, entity_id, entity_type):
        self.entity_name = entity_name
        self.entity_id = entity_id
        self.entity_type = entity_type

    def get_relation(self, G, ent_id_1, ent_id_2):
        """
        :return:
        """
        rel = ' connected with '

        if G.has_edge(ent_id_1, ent_id_2):

            relations = []

            for key in G[ent_id_1][ent_id_2]:
                edge_data = G[ent_id_1][ent_id_2][key]
                if isinstance(edge_data, dict) and 'relation' in edge_data:
                    relations.append(edge_data['relation'])

            if self.entity_type == 'target':
                relations = [rel_1_dict[idx] for idx in relations]
            elif self.entity_type == 'candidate':
                relations = [rel_2_dict[idx] for idx in relations]

            relation_counter = Counter(relations)
            top_5_relations = relation_counter.most_common(5)
            top_5_relations = [relation for relation, _ in top_5_relations]

            return ' ' + ','.join(top_5_relations) + ' '

        # relations = []
        # try:
        #
        #     for relation in triple1_dict[ent_id_1][ent_id_2]:
        #         relations.append(relation)
        #
        #     # for relation in triple2_dict[ent_id_1][ent_id_2]:
        #     #     relations.append(relation)
        #
        #     rel = ','.join(relations)
        # except:
        #     rel = rel

        return rel
    def get_subgraph(self, node):
        """

        :return:
        """

        if self.entity_type == 'target':
            subgraph_path = _1_neighbor_subgraph1_path
        elif self.entity_type == 'candidate':
            subgraph_path = _1_neighbor_subgraph2_path

        subgraph_file = subgraph_path + '/{}.graph'.format(node)
        edges = []
        with open(subgraph_file, 'r') as f:
            for line in f.readlines():
                edges.append((line.split(' ')[0], line.split(' ')[1].strip()))
        G = nx.Graph()
        G.add_edges_from(edges)
        return G

    def get_triangle_motif(self, node):
        """

        :param node:
        :return:
        """

        if self.entity_type == 'target':
            subgraph_path = _2_neighbor_subgraph1_path
        elif self.entity_type == 'candidate':
            subgraph_path = _2_neighbor_subgraph2_path

        subgraph_file = subgraph_path + '/{}.graph'.format(node)

        edges = []
        with open(subgraph_file, 'r') as f:
            for line in f.readlines():
                edges.append((line.split(' ')[0], line.split(' ')[1].strip()))
        G = nx.DiGraph()
        G.add_edges_from(edges)

        motifs = find_triangle_or_star_motifs(G, node)


        return motifs


    def get_star_motif(self, node):
        """

        :param node:
        :return:
        """
        if self.entity_type == 'target':
            subgraph_path = _1_neighbor_subgraph1_path
        elif self.entity_type == 'candidate':
            subgraph_path = _1_neighbor_subgraph2_path

        subgraph_file = subgraph_path + '/{}.graph'.format(node)

        edges = []
        with open(subgraph_file, 'r') as f:
            for line in f.readlines():
                edges.append((line.split(' ')[0], line.split(' ')[1].strip()))
        G = nx.DiGraph()
        G.add_edges_from(edges)
        motifs = find_star_motifs(G, node)


        return motifs

    def get_motifs_promts(self, node, motifs):
        """

        :param motifs:
        :return:
        """
        ##获取三角形prompts
        motifs_prompts = ''
        for idx, subgraph in enumerate(motifs):
            if node in subgraph.nodes:
                # try:
                    if self.entity_type == 'target':
                        motifs_prompts += ' , '.join([node, id_ent_dict1[node], f"Motif {idx + 1}:\n"])
                    elif self.entity_type == 'candidate':
                        motifs_prompts += ' , '.join([node, id_ent_dict2[node], f"Motif {idx + 1}:\n"])
                    # nodes = ','.join([id_ent_dict[idx] for idx in subgraph.nodes()])
                    # edges = ','.join(['(' + id_ent_dict[i] + ',' + id_ent_dict[j] + ')' for i, j in subgraph.edges()])
                    for i, j in subgraph.edges():

                        if self.entity_type == 'target':
                            relationship = self.get_relation(G1, i, j)
                            motifs_prompts += id_ent_dict1[i] + relationship + id_ent_dict1[j] + '\n'
                        elif self.entity_type == 'candidate':
                            relationship = self.get_relation(G2, i, j)
                            motifs_prompts += id_ent_dict2[i] + relationship + id_ent_dict2[j] + '\n'


                    # motifs_prompts += nodes + '\n\n'
                    # motifs_prompts += edges + '\n\n'
                # except:
                #     pass

        return motifs_prompts

    def get_candidates(self, entity_name):
        """

        :param node:
        :return:
        """

        return candidates[entity_name]


    def get_prompts_with_text_motif(self):
        """
        :param node:
        :return:
        """
        triangle_motifs = self.get_triangle_motif(self.entity_id)

        # star_motifs = self.get_star_motif(self.entity_id)

        triangle_motifs_prompts = self.get_motifs_promts(self.entity_id, triangle_motifs)

        # star_motifs_prompts = self.get_motifs_promts(self.entity_id, star_motifs)

        prompts = """
        You are a Entity Alignment expert, your task is according to the information I give to find the most similar entity
        from the given candidate list for the given entity. Please note that Motif is refers to a recurring subgraph pattern that appears
        within a larger graph. These motifs are typically small, distinct, and repeated structures that provide insights into 
        the structural and functional aspects of the graph.
        1. Please encapsulate the answer within <output> </output>.
        2. Please note the forms with and without underscores for entities.
        3. Please focus on entities with a small edit distance from the original entity.
        
        === Target Entities Info starts: ===
        Entity Name: {}
        
        Below are the motif information of the target entity. Please notice that every motif is represented as
        "Node", "Entity Name", Motif "i":
        entity1 reletions1 entity2
        entity2 relations2 entity3
        entity1 relations3 entity3
        Please notice that relation can have mutiple relation and joined by ','
        {}
        [Important!]Please used the motif information given above to help you find corrected Entity in candidates.
        === Target Entities Info end ===
        
        === Candidate Entities starts: ===
        {}
        === Candidate Entities end ===
        
        --- Your Task starts: ---
        Aligned Entity: {}
        
        ---output format: ----
        <output> xxxx </output>
        
        """.format(self.entity_name,
                   triangle_motifs_prompts,
                   self.get_candidates(self.entity_name),
                   self.entity_name)

        return prompts

    def get_prompts_with_code_motif(self):
        """
        :param node:
        :return:
        """

        prompts = """
        You are a Entity Alignment expert, your task is according to the information I give to find the most similar entity
        from the given candidate list for the given entity. Please note that Motif is refers to a recurring subgraph pattern that appears
        within a larger graph. These motifs are typically small, distinct, and repeated structures that provide insights into 
        the structural and functional aspects of the graph. Here are some rulse:
        1. Please encapsulate the answer within <output> </output>.
        2. Please note the forms with and without underscores for entities.
        3. Please focus on entities with a small edit distance from the original entity.


        === Target Entities Info starts: ===
        Entity Name: {}
        
        Below are the motif information of the target entity. Please notice that every motif is represented as
        "Node", "Entity Name", Motif "i":
        entity1 reletions1 entity2
        entity2 relations2 entity3
        entity1 relations3 entity3
        Please notice that relation can have mutiple relation and joined by ','
        {}
        [Important!]Please used the motif information given above to help you find corrected Entity in candidates.
        === Target Entities Info end ===

        === Candidate Entities starts: ===
        {}
        === Candidate Entities end ===

        --- Your Task starts: ---
        Aligned Entity: {}

        ---output format: ----
        <output> xxxx </output>

        """.format(self.entity_name,
                   tmp,
                   self.get_candidates(self.entity_name),
                   self.entity_name)
        return prompts

    def get_baseline_prompts(self):
        """
        :return:
        """
        prompts = """
                You are a Entity Alignment expert, your task is according to the information I give to find the most similar entity
                from the given candidate list for the given entity. Please note that Motif is refers to a recurring subgraph pattern that appears
                within a larger graph. These motifs are typically small, distinct, and repeated structures that provide insights into 
                the structural and functional aspects of the graph.
                1. Please encapsulate the answer within <output> </output>.
                2. Please note the forms with and without underscores for entities.
                3. Please focus on entities with a small edit distance from the original entity.

                === Target Entities Info starts: ===
                Entity Name: {}

                === Target Entities Info end ===

                === Candidate Entities starts: ===
                {}
                === Candidate Entities end ===

                --- Your Task starts: ---
                Aligned Entity: {}

                ---output format: ----
                <output> xxxx </output>

                """.format(self.entity_name,
                           self.get_candidates(self.entity_name),
                           self.entity_name)

        return self.entity_name, self.get_candidates(self.entity_name), prompts


    def get_only_motif_information(self):
        """
        :return:
        """

        triangle_motifs = self.get_triangle_motif(self.entity_id)

        triangle_motifs_prompts = self.get_motifs_promts(self.entity_id, triangle_motifs)

        return triangle_motifs_prompts

        # star_motifs = self.get_star_motif(self.entity_id)
        #
        # star_motifs_prompts = self.get_motifs_promts(self.entity_id, star_motifs)
        #
        # return star_motifs_prompts

    def get_only_1_neighbor_information(self):
        """
        :return:
        """
        star_motifs = self.get_star_motif(self.entity_id)

        star_motifs_prompts = self.get_motifs_promts(self.entity_id, star_motifs)

        return star_motifs_prompts


    def get_LLM_output(self, prompts):
        """
        :param prompts:
        :return:
        """


if __name__ == '__main__':

    entity_type = 'candidate'
    # entity_type = 'target'
    if entity_type == ('target'):
        ent_id_dict = get_ent_id_dict(ent_id_1_path)

    elif entity_type == 'candidate':
        ent_id_dict = get_ent_id_dict(ent_id_2_path)

    entity = """Institutional Revolutionary Party"""
    entity_id = ent_id_dict[entity]

    entity = Entity(entity, entity_id, entity_type)
    prompts = entity.get_only_1_neighbor_information()

    print(prompts)