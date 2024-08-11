import os.path
from itertools import combinations
from heapq import nlargest
import networkx as nx
from run.utils import get_id_entity_dict, get_ent_id_dict
from collections import Counter


def find_triangle_or_star_motifs(graph, node, top_n=5):
    """
    :param graph:
    :param node:
    :param top_n:
    :return:
    """

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

    try:
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

    except:
        return []


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


def find_star_motifs(graph, node):
    """
    Find all star motifs in the graph and return them as subgraphs.
    :param graph: A NetworkX graph
    :return: A list of subgraphs, each representing a star motif
    """

    def create_star_motif_with_how_many_edges(graph, center_node, num_edges=5):
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

    stars = []

    # Iterate over nodes to find stars

    neighbors = list(graph.neighbors(node))
    if len(neighbors) > 1:  # Node has more than one neighbor
            star_nodes = [node] + neighbors
            star = graph.subgraph(star_nodes).copy()

            star = create_star_motif_with_how_many_edges(star, node, 8)

            stars.append(star)

    return stars


def find_four_cycles(G, node, top_n=5):
    """
    Find all 4 cycle motifs in the graph and return them as subgraphs.

    :param graph: A NetworkX graph
    :return: A list of subgraphs, each representing a 4 cycle motif
    :return:
    """
    quadrilaterals = []
    neighbors = list(G.neighbors(node))

    for i in range(len(neighbors)):
        for j in range(i + 1, len(neighbors)):
            for k in range(j + 1, len(neighbors)):
                if G.has_edge(neighbors[i], neighbors[j]) and G.has_edge(neighbors[j], neighbors[k]) and G.has_edge(
                        neighbors[k], neighbors[i]):
                    quadrilaterals.append((node, neighbors[i], neighbors[j], neighbors[k]))


    quad_counter = Counter(quadrilaterals)
    top_5_quads = quad_counter.most_common(top_n)

    motif_graphs = []
    for idx, (quad, count) in enumerate(top_5_quads):
        motif_graph = nx.Graph()
        motif_graph.add_edges_from(
            [(quad[0], quad[1]),
             (quad[1], quad[2]),
             (quad[2], quad[3]),
             (quad[3], quad[0])]
        )
        motif_graphs.append(motif_graph)

        # # print(quad)
        # motif_nodes = set(quad)
        # subgraph = G.subgraph(motif_nodes).copy()
        # subgraphs.append(subgraph)

    return motif_graphs


def find_chain_motifs(G, node, top_n=5):
    """
    Find all chain motifs of the specified length in the graph and return them as subgraphs.

    :param graph: A NetworkX graph
    :param length: The length of the chain motif
    :return: A list of subgraphs, each representing a chain motif of the specified length
    """
    chain_motifs = []
    neighbors = list(G.neighbors(node))

    for neighbor in neighbors:
        second_neighbors = list(G.neighbors(neighbor))
        for second_neighbor in second_neighbors:
            if second_neighbor != node:
                chain_motifs.append((node, neighbor, second_neighbor))

    chain_counter = Counter(chain_motifs)

    # 找出出现次数最多的前五个chain motif
    top_5_chains = chain_counter.most_common(top_n)

    subgraphs = []
    for idx, (chain, count) in enumerate(top_5_chains):
        motif_nodes = set(chain)
        subgraph = G.subgraph(motif_nodes).copy()
        subgraphs.append(subgraph)

    return subgraphs

def find_tree_motifs(graph, root, size, top_n=5):
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

def find_star_triangle_motifs(G, node, top_n=5):
    """
    Find all star-triangle motifs in the graph and return them as subgraphs.

    :param graph: A NetworkX graph
    :return: A list of subgraphs, each representing a star-triangle motif
    """

    motifs = []
    try:
        for neighbor1 in G.neighbors(node):
            for neighbor2 in G.neighbors(neighbor1):
                if neighbor2 != node and G.has_edge(node, neighbor2):
                    for neighbor3 in G.neighbors(node):
                        if neighbor3 != neighbor1 and neighbor3 != neighbor2 and G.has_edge(neighbor1,
                                                                                            neighbor3) and G.has_edge(
                                neighbor2, neighbor3):
                            motif = tuple(sorted([node, neighbor1, neighbor2, neighbor3]))
                            motifs.append(motif)

        motif_counter = Counter(motifs)
        top_5_motifs = motif_counter.most_common(top_n)

        subgraphs = []
        for idx, (motif, count) in enumerate(top_5_motifs):
            motif_nodes = set(motif)
            subgraph = G.subgraph(motif_nodes).copy()
            subgraphs.append(subgraph)

        return subgraphs
    except:
        return []

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
    # ent_ids.append((ent_id_1, rel_id, ent_id_2))
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

def test_most_representative_motif():
    import networkx as nx
    from itertools import combinations
    from collections import Counter
    import numpy as np
    import matplotlib.pyplot as plt
    import random

    # 创建图结构
    G = nx.Graph()
    edges = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 6), (6, 4), (6, 7), (7, 8), (8, 9), (9, 10), (7, 10)]
    G.add_edges_from(edges)

    # 枚举三角形
    def find_triangles(G):
        triangles = []
        for node in G.nodes():
            neighbors = list(G.neighbors(node))
            for u, v in combinations(neighbors, 2):
                if G.has_edge(u, v):
                    triangles.append((node, u, v))
        return triangles

    # 枚举星形（中心节点连接多个外围节点）
    def find_stars(G):
        stars = []
        for node in G.nodes():
            neighbors = list(G.neighbors(node))
            if len(neighbors) >= 3:
                stars.append((node, tuple(neighbors)))
        return stars

    # 枚举四边形
    def find_quadrilaterals(G):
        quadrilaterals = []
        for node in G.nodes():
            neighbors = list(G.neighbors(node))
            for u, v in combinations(neighbors, 2):
                if G.has_edge(u, v):
                    for w in neighbors:
                        if w != u and w != v and G.has_edge(u, w) and G.has_edge(v, w):
                            quadrilaterals.append((node, u, v, w))
        return quadrilaterals

    # 计算图中各个motif的数量
    triangles = find_triangles(G)
    stars = find_stars(G)
    quadrilaterals = find_quadrilaterals(G)

    # 计算各个motif的频率
    motif_frequencies = {
        "triangle": len(triangles),
        "star": len(stars),
        "quadrilateral": len(quadrilaterals)
    }

    # 比较频率最高的motif
    most_frequent_motif = max(motif_frequencies, key=motif_frequencies.get)

    # 输出最有代表性的motif
    print(
        f"The most representative motif is: {most_frequent_motif} with count: {motif_frequencies[most_frequent_motif]}")

    # most_frequent_motif = "quadrilateral"
    # 提取包含最有代表性motif的实例
    if most_frequent_motif == "triangle":
        motif_instances = triangles
    elif most_frequent_motif == "star":
        motif_instances = stars
    elif most_frequent_motif == "quadrilateral":
        motif_instances = quadrilaterals


    # 提取最有代表性的motif实例
    most_representative_motif_instance = motif_instances[0]

    print(f"The most representative motif instance is: {most_representative_motif_instance}")

    # 提取子图
    motif_nodes = set()
    for instance in motif_instances:
        motif_nodes.update(instance if isinstance(instance, tuple) else instance[1])

    # 过滤无效节点
    valid_motif_nodes = [node for node in motif_nodes if node in G.nodes()]

    subgraph = G.subgraph(valid_motif_nodes).copy()

    # 输出子图中的节点和边
    print(f"Nodes in the most representative motif subgraph: {list(subgraph.nodes())}")
    print(f"Edges in the most representative motif subgraph: {list(subgraph.edges())}")

    # 可视化子图
    pos = nx.spring_layout(subgraph)
    nx.draw(subgraph, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1500, font_size=20)
    plt.title("Most Representative Motif Subgraph")
    plt.show()

if __name__ == '__main__':
    test_most_representative_motif()
