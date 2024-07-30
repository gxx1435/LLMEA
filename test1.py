import numpy as np
from run.utils import compute_csls

# Example usage
# X_src = np.random.rand(100, 50)  # 100 samples, 50 features in source domain
# X_tgt = np.random.rand(100, 50)  # 100 samples, 50 features in target domain
#
# csls_matrix = compute_csls(X_src, X_tgt, k=10)
# print(csls_matrix.shape)
# x = np.array([1,4,3,-1,6,9])
# x.argsort()
# print(np.argsort(x))
# x = [3, 0, 2, 1, 4, 5]
# y = [0, 2, 5, 3, 4, 1]
# rank = [(x[i], y[i]) for i in range(len(x))]
# rank.sort(key=lambda x: (x[0], x[1]))
# print(rank)

# x = np.array([[1,2,4,5,6],
#               [3,4,5,6,7]])
#
# y = np.array([[2,3,4,5,6],
#               [2,2,3,4,5]])
# print(x+y)

# import sys
# import subprocess
#
# # 确保包已安装
# def install(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])
#
# try:
#     import editdistance
# except ImportError:
#     install('editdistance')
#     import editdistance
#
# import editdistance
# print(editdistance.eval('banana', 'bahama'))

import networkx as nx

# # 创建一个示例图（可以根据实际情况加载你的图数据）
# G = nx.Graph()
# G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (4, 6)])
#
# # 找到图中所有的三角形子图
# triangles = list(nx.enumerate_all_cliques(G))
#
# # 遍历并打印每个三角形子图的节点和边信息
# for triangle_nodes in triangles:
#     if len(triangle_nodes) == 3:  # 确保是三角形
#         subgraph = G.subgraph(triangle_nodes)
#         print("Nodes:", list(subgraph.nodes()))
#         print("Edges:", list(subgraph.edges()))
#         print()
import networkx as nx

# # 创建图
# G = nx.Graph()
# edges = [
#     ('A', 'B', 1), ('A', 'C', 2), ('B', 'C', 3),
#     ('B', 'D', 4), ('C', 'D', 5), ('D', 'E', 6),
#     ('C', 'E', 7)
# ]
# G.add_weighted_edges_from(edges)
#
# # 生成最小生成树
# T = nx.minimum_spanning_tree(G)
#
# # 打印最小生成树的边
# print("Edges in the Minimum Spanning Tree:")
# for edge in T.edges(data=True):
#     print(edge)

# import networkx as nx
#
# # 创建一个图
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 1), (2, 4), (3, 4)])
#
# # 使用 networkx 自带的函数找出所有的三角形
# triangles = list(nx.enumerate_all_cliques(G))
#
# print("Triangles in the graph:")
# for triangle in triangles:
#     if len(triangle) == 3:  # 确保是三角形
#         print(triangle, type(triangles))
#
# import networkx as nx


# def find_star_motifs( G):
#     """
#     Find all star motifs in the graph and return them as subgraphs.
#
#     :param graph: A NetworkX graph
#     :return: A list of subgraphs, each representing a star motif
#     """
#     stars = []
#
#     # Iterate over nodes to find stars
#     for node in G.nodes():
#         neighbors = list(G.neighbors(node))
#         if len(neighbors) > 1:  # Node has more than one neighbor
#             star_nodes = [node] + neighbors
#             star = G.subgraph(star_nodes).copy()
#             stars.append(star)
#
#     return stars
#
#
# # 示例用法
# if __name__ == "__main__":
#     G = nx.Graph()
#     G.add_edges_from([(1, 2), (1, 3), (1, 4), (3, 5), (5, 6), (5, 7), (5, 8)])
#
#     star_motifs = find_star_motifs(G)
#     print("Star motifs in the graph:")
#     for subgraph in star_motifs:
#         print(subgraph.nodes())
# #         print(subgraph.edges())
# import networkx as nx
# from heapq import nlargest
#
#
# def find_top_shared_triangles(graph, target_node, top_n=10):
#     # 获取目标节点的邻居
#     neighbors = set(graph.neighbors(target_node))
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
#             triangle = tuple(sorted((target_node, neighbor, common_neighbor)))
#             shared_triangles[neighbor].append(triangle)
#
#     # 将所有共享三角形收集到一个列表中
#     all_shared_triangles = []
#     for triangles in shared_triangles.values():
#         all_shared_triangles.extend(triangles)
#
#     # 找出前 top_n 个共享次数最多的三角形
#     top_shared_triangles = nlargest(top_n, set(all_shared_triangles), key=lambda t: all_shared_triangles.count(t))
#
#     # 构建包含这些三角形motif的子图
#     motif_graph = nx.Graph()
#     for triangle in top_shared_triangles:
#         motif_graph.add_edges_from([(triangle[0], triangle[1]), (triangle[1], triangle[2]), (triangle[2], triangle[0])])
#
#     return motif_graph, top_shared_triangles
#
#

#
# # 目标节点
# target_node = 1
#
# # 找出与目标节点共享三角形最多的前10个共享三角形及所有共享次数最多的三角形motif的子图
# motif_graph, top_triangles = find_top_shared_triangles(G, target_node, top_n=10)
#
# # 输出结果
# print("共享次数最多的前10个共享三角形的所有三角形motif子图中的边:")
# print(motif_graph.edges())
#
# print("\n不重复的三角形列表:")
# for triangle in top_triangles:
#     print(triangle)
#
# # 可视化结果（如果需要）
# import matplotlib.pyplot as plt
#
# nx.draw(motif_graph, with_labels=True, node_color='lightblue', edge_color='gray')
# plt.show()
# import networkx as nx
#
# # Create a directed multi-graph (MultiDiGraph)
# G = nx.MultiDiGraph()
#
# # Add multiple edges between nodes with different relations
# G.add_edge("NodeA", "NodeB", relation="friend")
# G.add_edge("NodeA", "NodeB", relation="colleague")
# G.add_edge("NodeA", "NodeB", relation="partner")
# G.add_edge("NodeB", "NodeC", relation="neighbor")
#
# # Function to get all relations between two nodes
# def get_relations(G, node1, node2):
#     if G.has_edge(node1, node2):
#         relations = [G[node1][node2][key]['relation'] for key in G[node1][node2]]
#         return ','.join(relations)
#     else:
#         return None
#
# # Test the function
# relations = get_relations(G, "NodeA", "NodeB")
# print(f"Relations between NodeA and NodeB: {relations}")
#
# relations = get_relations(G, "NodeA", "NodeC")
# print(f"Relations between NodeA and NodeC: {relations}")  # This will return None since there are no edges
#
# relations = get_relations(G, "NodeB", "NodeC")
# print(f"Relations between NodeB and NodeC: {relations}")
#
# import json
# with open('prompts_naive.json', 'r') as f:
#     texts = json.load(f)
#     print(texts['webthink_simple6'])
# import networkx as nx
# from collections import Counter
#
# # 创建有向图
# G = nx.DiGraph()
#
# # 添加有向边，这里使用一个简单的例子：
# edges = [(1, 2), (2, 3), (3, 1), (2, 4), (4, 1), (3, 4), (4, 5), (5, 3)]
# G.add_edges_from(edges)
#
# # 找到所有节点对 (u, v, w) 其中存在 u -> v -> w -> u 的三角形
# from collections import defaultdict, Counter
#
#
# def find_triangles(G):
#     triangles = []
#     for u in G.nodes():
#         for v in G.successors(u):
#             for w in G.successors(v):
#                 if u in G.successors(w):
#                     triangles.append((u, v, w))
#     return triangles
#
#
# def find_top_triangle_subgraphs(G, top_count=5):
#     triangle_counts = Counter(find_triangles(G))
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
#
# # 示例用法：
# # 假设 G 是你的图对象
# top_triangle_subgraphs = find_top_triangle_subgraphs(G)
#
# # 打印每个三角形子图的节点和边，以及计数
# for subgraph_nodes, data in top_triangle_subgraphs.items():
#     print(f"Triangle Nodes: {subgraph_nodes}, Count: {data['count']}")
#     subgraph = data['subgraph']
#     print("Nodes:", list(subgraph.nodes()))
#     print("Edges:", list(subgraph.edges()))

# from collections import defaultdict, Counter
# import networkx as nx
# import matplotlib.pyplot as plt
#
#
# def find_top_triangle_subgraphs(G, top_count=5):
#     triangle_counts = Counter()
#
#     # 遍历图中的每条边，查找三角形
#     for u, v in G.edges():
#         neighbors_u = set(G.neighbors(u))
#         neighbors_v = set(G.neighbors(v))
#         common_neighbors = neighbors_u & neighbors_v
#
#         # 对每对共同邻居节点进行遍历，构成三角形
#         for w in common_neighbors:
#             if u < v < w:  # 确保每个三角形的顺序唯一
#                 triangle = tuple(sorted([u, v, w]))
#                 triangle_counts[triangle] += 1
#
#     # 找出出现次数最多的三角形
#     top_triangles = triangle_counts.most_common(top_count)
#
#     # 创建字典存储出现次数最多的三角形子图及其计数
#     top_triangle_subgraphs = {}
#     for triangle, count in top_triangles:
#         u, v, w = triangle
#         subgraph_nodes = tuple(sorted([u, v, w]))
#         if subgraph_nodes not in top_triangle_subgraphs:
#             subgraph = G.subgraph([u, v, w])
#             top_triangle_subgraphs[subgraph_nodes] = {
#                 'subgraph': subgraph,
#                 'count': count
#             }
#
#     return top_triangle_subgraphs
#
#
# # 示例用法：
# G = nx.Graph()  # 创建一个NetworkX的无向图对象
# # 在这里添加节点和边，以及相应的数据
# edges = [(1, 2), (2, 3), (3, 1), (2, 4), (4, 1), (3, 4), (4, 5), (5, 3)]
# G.add_edges_from(edges)
#
# top_triangle_subgraphs = find_top_triangle_subgraphs(G)
#
# # 打印每个三角形子图的节点和边，以及计数
# for subgraph_nodes, data in top_triangle_subgraphs.items():
#     print(f"Triangle Nodes: {subgraph_nodes}, Count: {data['count']}")
#     subgraph = data['subgraph']
#     print("Nodes:", list(subgraph.nodes()))
#     print("Edges:", list(subgraph.edges()))
#
#     # 绘制子图
#     plt.figure(figsize=(5, 5))
#     pos = nx.spring_layout(subgraph)
#     nx.draw(subgraph, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
#     nx.draw_networkx_edge_labels(subgraph, pos, edge_labels={(u, v): f'{u}->{v}' for u, v in subgraph.edges()})
#     plt.title(f"Triangle Nodes: {subgraph_nodes}, Count: {data['count']}")
#     plt.show()

# import networkx as nx
# import matplotlib.pyplot as plt
#
# # 创建一个有向图
# G = nx.DiGraph()
#
# # 添加节点和边以形成一个star结构
# # 假设中心节点是 'center'，叶节点是 'leaf1', 'leaf2', 'leaf3', 'leaf4'
# center = 'center'
# leaves = ['leaf1', 'leaf2', 'leaf3', 'leaf4']
#
# # 添加边
# for leaf in leaves:
#     G.add_edge(center, leaf)
#     G.add_edge(leaf, center)
#
# # 绘制图形
# plt.figure(figsize=(8, 8))
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
# nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{u}->{v}' for u, v in G.edges()})
# plt.title("Star Motif")
# plt.show()

# import networkx as nx
# from collections import Counter
#
# # 创建一个有向图
# G = nx.DiGraph()
# # 添加边
# edges = [
#     ('A', 'B'), ('A', 'C'), ('A', 'D'),
#     ('B', 'C'),
#     ('C', 'A'), ('C', 'D'),
#     ('D', 'B'),
#     ('E', 'A'), ('E', 'B'), ('E', 'C'), ('E', 'D'),
#     ('F', 'A'),
#     ('G', 'E'),
#     ('H', 'F'),
#     # 其他边
# ]
# G.add_edges_from(edges)
#
# # 计算每个节点的出度和入度
# out_degree = dict(G.out_degree())
# in_degree = dict(G.in_degree())
#
# # 计算每个节点的总度数（出度 + 入度）
# total_degree = {node: out_degree[node] + in_degree[node] for node in G.nodes()}
#
# # 按总度数排序，选择top 5的节点
# top_nodes = sorted(total_degree, key=total_degree.get, reverse=True)[:5]
#
# # 构建星型motif子图
# def build_star_motif(graph, center_node):
#     neighbors = list(graph.successors(center_node)) + list(graph.predecessors(center_node))
#     star_motif = nx.DiGraph()
#     for neighbor in neighbors:
#         if graph.has_edge(center_node, neighbor):
#             star_motif.add_edge(center_node, neighbor)
#         if graph.has_edge(neighbor, center_node):
#             star_motif.add_edge(neighbor, center_node)
#     return star_motif
#
# top_star_motifs = {node: build_star_motif(G, node) for node in top_nodes}
#
# # 输出结果
# for node, motif in top_star_motifs.items():
#     print(f"Star Motif centered at {node}:")
#     print(motif.edges)
#     print()

# import matplotlib.pyplot as plt
# import networkx as nx
#
# # Define the nodes and edges for the graph
# nodes = ['Bev_Oda', 'Canada', 'Conservative_Party_of_Canada', 'New_Node']
# edges = [('Bev_Oda', 'Canada'),
#          ('Bev_Oda', 'Conservative_Party_of_Canada'),
#          # ('Canada', 'Conservative_Party_of_Canada'),
#          ('New_Node', 'Bev_Oda'),
#          ('New_Node', 'Canada'),
#          ('New_Node', 'Conservative_Party_of_Canada')]
#
# # Create the graph
# G = nx.Graph()
# G.add_nodes_from(nodes)
# G.add_edges_from(edges)
#
# # Draw the graph
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold')
# nx.draw_networkx_edge_labels(G, pos, edge_labels={('Bev_Oda', 'Canada'): 'continent',
#                                                   ('Bev_Oda', 'Conservative_Party_of_Canada'): 'country_of_citizenship',
#
#                                                   ('New_Node', 'Bev_Oda'): 'is_connected_with',
#                                                   ('New_Node', 'Canada'): 'is_connected_with',
#                                                   ('New_Node', 'Conservative_Party_of_Canada'): 'is_connected_with'})
#
# # Show the plot
# plt.title("Triangle Motif with an Additional Node")
# plt.show()

import networkx as nx
from heapq import nlargest

# def find_top_shared_triangles(graph, node, top_n):
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
#     # 将所有共享三角形收集到一个列表中
#     all_shared_triangles = []
#     for triangles in shared_triangles.values():
#         all_shared_triangles.extend(triangles)
#
#     # 找出前 top_n 个共享次数最多的三角形
#     top_shared_triangles = nlargest(top_n, set(all_shared_triangles), key=lambda t: all_shared_triangles.count(t))
#
#     # 构建包含这些三角形motif的子图
#     motif_graphs = []
#     for triangle in top_shared_triangles:
#         motif_graph = nx.Graph()
#         motif_graph.add_edges_from(
#             [(triangle[0], triangle[1]), (triangle[1], triangle[2]), (triangle[2], triangle[0])]
#         )
#         motif_graphs.append(motif_graph)
#
#     return motif_graphs
#
# # 示例使用
# G = nx.Graph()
# # 添加示例节点和边
# G.add_edges_from([
#     (1, 2), (1, 3), (1, 4),
#     (2, 3), (2, 4),
#     (3, 4), (3, 5),
#     (4, 5)
# ])
#
# node = 1
# top_n = 5
#
# motifs = find_top_shared_triangles(G, node, top_n)
# for i, motif in enumerate(motifs):
#     print(f"Motif {i+1}:")
#     print(motif.edges())



# s = ('qwhjahsnwnu Thought1:..........................'
#      'Act1:..................')
# thought_idx = s.find('Thought')
# act_idx = s.find('Act')
# thought = s[thought_idx:act_idx-1]
# act = s[act_idx:-1]
# print(thought + '\n' + act)
#
#
# def find_requests(s):
#      start_idx = s.find('Request[')
#      end_idx = s.find(']')
#      if start_idx != -1:
#           return s[start_idx + 8: end_idx]
#      return -1
# print(find_requests('Requst[end]'))
#
# def find_code(s):
#      start_idx = s.find('<code>')
#      end_idx = s.find("</code>")
#      return s[start_idx + 6: end_idx]
#
# s  = '<code>2344455</code>'
# print(find_code(s))

import json

# with open('idx_prompt_dict_step_00.json', 'r') as f:
#      step_00 = json.load(f)
#
# with open('idx_prompt_dict_step_00_format.json', 'w') as f:
#      json.dump(step_00, f, indent=4)
import re


# def extract_target_entity(text):
#      # 优先匹配带单引号的目标实体
#      pattern_single_quote = r"Terminate\['(.*?)'\]"
#      match_single_quote = re.search(pattern_single_quote, text)
#
#      if match_single_quote:
#           return match_single_quote.group(1)
#
#      # 如果没有匹配到带单引号的目标实体，则匹配不带引号的目标实体
#      pattern_no_quote = r"Terminate\[(.*?)\]"
#      match_no_quote = re.search(pattern_no_quote, text)
#
#      if match_no_quote:
#           return match_no_quote.group(1)
#
#      return -1
#
# with open('output/icews_yago/LLM_response_code_motif/thought_and_acts_01.json') as f:
#      lines = json.load(f)
#      for line in lines:
#           terminate = extract_target_entity(line)
#           print(terminate)

import argparse

# # 创建 ArgumentParser 对象
# parser = argparse.ArgumentParser(description="It's a test")
#
# parser.add_argument('-d', '--dataset', type=str, help='dataset name')
#
# parser.add_argument('-i', '--info_type', type=str, help='code_motif,text_motif,1_neighbor')
#
# parser.add_argument('-l', '--llm_type', type=str, help='LLM type')
#
# # # 添加可选参数（带默认值）
# # parser.add_argument('-n', '--number', type=int, default=42, help='要处理的数字')
#
# # 解析参数
# args = parser.parse_args()
#
# dataset = args.dataset
# info_type = args.info_type
# LLM_type = args.llm_type
# print(dataset)
# print(info_type)
# print(LLM_type)
# random_sample = 0.3
# f = "new_ent_ids_1_random_sample_{}".format(random_sample)
# print(f)

# from run.utils import hit_1_10_rate
final_answers = {}
for i in [1, 2, 3, 4]:
    with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/output/icews_yago_gpt_4_turbo_t3000_100_50/most_list_code_motif_base_{}.json'.format(i), 'r') as f:
        final_answer = json.load(f)
        final_answers.update(final_answer)

with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/output/icews_yago_gpt_4_turbo_t3000_100_50/most_list_code_motif_base_all.json', 'w') as f:
    json.dump(final_answers, f, indent=4)


# dataset = 'icews_yago'
# ent_id_1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1_strip'.format(dataset)
# ent_id_2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_2_aligned_strip'.format(dataset)
#
# hit_rate = hit_1_10_rate('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/output/icews_yago_gpt_4_turbo_t3000_100_50/most_list_code_motif_base_all.json', 'hit10')
# print(hit_rate)

from run.utils import mean_reciprocal_rank
mrr = mean_reciprocal_rank(final_answers)
print(mrr)

# id_ent_dict = {}
# idxs = []
# ents =[]
# with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/new_ent_ids_2_aligned') as f:
#
#     for line in f.readlines():
#         idx = line.split('\t')[0]
#         ent = line.split('\t')[1].strip()
#         # ent = ent.split('(')[0]
#         idxs.append(idx)
#         ents.append(ent)
# id_ent_dict = dict(zip(idxs, ents))
#
# print(len(id_ent_dict))
#
# with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/new_ent_ids_2_aligned_strip', 'w') as f:
#     for idx in id_ent_dict.keys():
#         f.write(idx +'\t'+id_ent_dict[idx] +'\n')

# import numpy as np
#
# arr = np.array([3, 1, 2])
# sorted_indices = np.argsort(arr)
#
# print("原数组:", arr)
# print("排序后的索引:", sorted_indices)
# print("排序后的数组:", arr[sorted_indices])


# # 添加可选参数（带默认值）
# parser.add_argument('-n', '--number', type=int, default=42, help='要处理的数字')
# import argparse
#
# def dynamic_import(module_name):
#     module = __import__(module_name)
#     return module
#
# parser = argparse.ArgumentParser(description="It's a test")
# parser.add_argument('-r', '--react_file', type=str, default='graph_motif_ReAct_v4_100_50candidates_tmp2',
#                     help='ReAct File')
#
# # 解析参数
# args = parser.parse_args()
#
# module_name = args.react_file
#
# ReAct_module = dynamic_import(module_name)
# motif_ReAct_example_prompt = ReAct_module.motif_ReAct_example_prompt
# print(motif_ReAct_example_prompt)

# text = """
# This is a sample text with <code>some code</code> and more text.
# Here is another <code>example code</code> snippet.
# """
#
# # 正则表达式模式，匹配 <code> 和 </code> 标签之间的内容
# pattern = r'<code>(.*?)</code>'
#
# # 使用 re.findall() 提取所有匹配的内容
# matches = re.search(pattern, text)
#
# print(matches.group(1))

# import networkx as nx
# from itertools import combinations
# from collections import Counter
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 创建图结构
# G = nx.Graph()
# edges = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 6), (6, 4), (6, 7), (7, 8), (8, 9), (9, 7)]
# G.add_edges_from(edges)
#
# # 枚举三角形
# def find_triangles(G):
#     triangles = []
#     for node in G.nodes():
#         neighbors = list(G.neighbors(node))
#         for u, v in combinations(neighbors, 2):
#             if G.has_edge(u, v):
#                 triangles.append((node, u, v))
#     return triangles
#
# # 枚举星形（中心节点连接多个外围节点）
# def find_stars(G):
#     stars = []
#     for node in G.nodes():
#         neighbors = list(G.neighbors(node))
#         if len(neighbors) >= 3:
#             stars.append((node, tuple(neighbors)))
#     return stars
#
# # 枚举四边形
# def find_quadrilaterals(G):
#     quadrilaterals = []
#     for node in G.nodes():
#         neighbors = list(G.neighbors(node))
#         for u, v in combinations(neighbors, 2):
#             if G.has_edge(u, v):
#                 for w in neighbors:
#                     if w != u and w != v and G.has_edge(u, w) and G.has_edge(v, w):
#                         quadrilaterals.append((node, u, v, w))
#     return quadrilaterals
#
# # 计算图中各个motif的数量
# triangles = find_triangles(G)
# stars = find_stars(G)
# quadrilaterals = find_quadrilaterals(G)
#
# # 计算各个motif的频率
# motif_frequencies = {
#     "triangle": len(triangles),
#     "star": len(stars),
#     "quadrilateral": len(quadrilaterals)
# }
#
# # 找到频率最高的motif
# most_frequent_motif = max(motif_frequencies, key=motif_frequencies.get)
#
# # 输出最有代表性的motif
# print(f"The most representative motif is: {most_frequent_motif} with count: {motif_frequencies[most_frequent_motif]}")
#
# most_frequent_motif = "star"
# # 提取包含最有代表性motif的实例
# if most_frequent_motif == "triangle":
#     motif_instances = triangles
# elif most_frequent_motif == "star":
#     motif_instances = stars
# elif most_frequent_motif == "quadrilateral":
#     motif_instances = quadrilaterals
#
# # 提取最有代表性的motif实例
# print(motif_instances)
# most_representative_motif_instance = motif_instances[0]
#
# print(f"The most representative motif instance is: {most_representative_motif_instance}")
#
# # 提取子图
# motif_nodes = set(most_representative_motif_instance)
#
# subgraph = G.subgraph(motif_nodes).copy()
#
#
# # 输出子图中的节点和边
# print(f"Nodes in the most representative motif subgraph: {list(subgraph.nodes())}")
# print(f"Edges in the most representative motif subgraph: {list(subgraph.edges())}")
#
# # 可视化子图
# pos = nx.spring_layout(subgraph)
# nx.draw(subgraph, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1500, font_size=20)
# plt.title("Most Representative Motif Subgraph")
# plt.show()

# import re
#
# def split_camel_case(s):
#     return re.sub('([a-z])([A-Z])', r'\1 \2', s)
#
# # 示例用法
# camel_case_string = "hasOccupation"
# split_string = split_camel_case(camel_case_string)
# print(split_string)

