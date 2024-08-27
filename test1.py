# import numpy as np
# from run.utils import compute_csls
#
# # Example usage
# # X_src = np.random.rand(100, 50)  # 100 samples, 50 features in source domain
# # X_tgt = np.random.rand(100, 50)  # 100 samples, 50 features in target domain
# #
# # csls_matrix = compute_csls(X_src, X_tgt, k=10)
# # print(csls_matrix.shape)
# # x = np.array([1,4,3,-1,6,9])
# # x.argsort()
# # print(np.argsort(x))
# # x = [3, 0, 2, 1, 4, 5]
# # y = [0, 2, 5, 3, 4, 1]
# # rank = [(x[i], y[i]) for i in range(len(x))]
# # rank.sort(key=lambda x: (x[0], x[1]))
# # print(rank)
#
# # x = np.array([[1,2,4,5,6],
# #               [3,4,5,6,7]])
# #
# # y = np.array([[2,3,4,5,6],
# #               [2,2,3,4,5]])
# # print(x+y)
#
# # import sys
# # import subprocess
# #
# # # 确保包已安装
# # def install(package):
# #     subprocess.check_call([sys.executable, "-m", "pip", "install", package])
# #
# # try:
# #     import editdistance
# # except ImportError:
# #     install('editdistance')
# #     import editdistance
# #
# # import editdistance
# # print(editdistance.eval('banana', 'bahama'))
#
# import networkx as nx
#
# # # 创建一个示例图（可以根据实际情况加载你的图数据）
# # G = nx.Graph()
# # G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (4, 6)])
# #
# # # 找到图中所有的三角形子图
# # triangles = list(nx.enumerate_all_cliques(G))
# #
# # # 遍历并打印每个三角形子图的节点和边信息
# # for triangle_nodes in triangles:
# #     if len(triangle_nodes) == 3:  # 确保是三角形
# #         subgraph = G.subgraph(triangle_nodes)
# #         print("Nodes:", list(subgraph.nodes()))
# #         print("Edges:", list(subgraph.edges()))
# #         print()
# import networkx as nx
#
# # # 创建图
# # G = nx.Graph()
# # edges = [
# #     ('A', 'B', 1), ('A', 'C', 2), ('B', 'C', 3),
# #     ('B', 'D', 4), ('C', 'D', 5), ('D', 'E', 6),
# #     ('C', 'E', 7)
# # ]
# # G.add_weighted_edges_from(edges)
# #
# # # 生成最小生成树
# # T = nx.minimum_spanning_tree(G)
# #
# # # 打印最小生成树的边
# # print("Edges in the Minimum Spanning Tree:")
# # for edge in T.edges(data=True):
# #     print(edge)
#
# # import networkx as nx
# #
# # # 创建一个图
# # G = nx.Graph()
# # G.add_edges_from([(1, 2), (2, 3), (3, 1), (2, 4), (3, 4)])
# #
# # # 使用 networkx 自带的函数找出所有的三角形
# # triangles = list(nx.enumerate_all_cliques(G))
# #
# # print("Triangles in the graph:")
# # for triangle in triangles:
# #     if len(triangle) == 3:  # 确保是三角形
# #         print(triangle, type(triangles))
# #
# # import networkx as nx
#
#
# # def find_star_motifs( G):
# #     """
# #     Find all star motifs in the graph and return them as subgraphs.
# #
# #     :param graph: A NetworkX graph
# #     :return: A list of subgraphs, each representing a star motif
# #     """
# #     stars = []
# #
# #     # Iterate over nodes to find stars
# #     for node in G.nodes():
# #         neighbors = list(G.neighbors(node))
# #         if len(neighbors) > 1:  # Node has more than one neighbor
# #             star_nodes = [node] + neighbors
# #             star = G.subgraph(star_nodes).copy()
# #             stars.append(star)
# #
# #     return stars
# #
# #
# # # 示例用法
# # if __name__ == "__main__":
# #     G = nx.Graph()
# #     G.add_edges_from([(1, 2), (1, 3), (1, 4), (3, 5), (5, 6), (5, 7), (5, 8)])
# #
# #     star_motifs = find_star_motifs(G)
# #     print("Star motifs in the graph:")
# #     for subgraph in star_motifs:
# #         print(subgraph.nodes())
# # #         print(subgraph.edges())
# # import networkx as nx
# # from heapq import nlargest
# #
# #
# # def find_top_shared_triangles(graph, target_node, top_n=10):
# #     # 获取目标节点的邻居
# #     neighbors = set(graph.neighbors(target_node))
# #
# #     # 字典来记录每个邻居节点与目标节点共享的三角形列表
# #     shared_triangles = {neighbor: [] for neighbor in neighbors}
# #
# #     # 遍历每个邻居节点，找出共享三角形
# #     for neighbor in neighbors:
# #         # 获取邻居节点的邻居
# #         neighbors_of_neighbor = set(graph.neighbors(neighbor))
# #
# #         # 找出共同邻居（即三角形中的第三个节点）
# #         common_neighbors = neighbors & neighbors_of_neighbor
# #
# #         # 记录共享三角形
# #         for common_neighbor in common_neighbors:
# #             triangle = tuple(sorted((target_node, neighbor, common_neighbor)))
# #             shared_triangles[neighbor].append(triangle)
# #
# #     # 将所有共享三角形收集到一个列表中
# #     all_shared_triangles = []
# #     for triangles in shared_triangles.values():
# #         all_shared_triangles.extend(triangles)
# #
# #     # 找出前 top_n 个共享次数最多的三角形
# #     top_shared_triangles = nlargest(top_n, set(all_shared_triangles), key=lambda t: all_shared_triangles.count(t))
# #
# #     # 构建包含这些三角形motif的子图
# #     motif_graph = nx.Graph()
# #     for triangle in top_shared_triangles:
# #         motif_graph.add_edges_from([(triangle[0], triangle[1]), (triangle[1], triangle[2]), (triangle[2], triangle[0])])
# #
# #     return motif_graph, top_shared_triangles
# #
# #
#
# #
# # # 目标节点
# # target_node = 1
# #
# # # 找出与目标节点共享三角形最多的前10个共享三角形及所有共享次数最多的三角形motif的子图
# # motif_graph, top_triangles = find_top_shared_triangles(G, target_node, top_n=10)
# #
# # # 输出结果
# # print("共享次数最多的前10个共享三角形的所有三角形motif子图中的边:")
# # print(motif_graph.edges())
# #
# # print("\n不重复的三角形列表:")
# # for triangle in top_triangles:
# #     print(triangle)
# #
# # # 可视化结果（如果需要）
# # import matplotlib.pyplot as plt
# #
# # nx.draw(motif_graph, with_labels=True, node_color='lightblue', edge_color='gray')
# # plt.show()
# # import networkx as nx
# #
# # # Create a directed multi-graph (MultiDiGraph)
# # G = nx.MultiDiGraph()
# #
# # # Add multiple edges between nodes with different relations
# # G.add_edge("NodeA", "NodeB", relation="friend")
# # G.add_edge("NodeA", "NodeB", relation="colleague")
# # G.add_edge("NodeA", "NodeB", relation="partner")
# # G.add_edge("NodeB", "NodeC", relation="neighbor")
# #
# # # Function to get all relations between two nodes
# # def get_relations(G, node1, node2):
# #     if G.has_edge(node1, node2):
# #         relations = [G[node1][node2][key]['relation'] for key in G[node1][node2]]
# #         return ','.join(relations)
# #     else:
# #         return None
# #
# # # Test the function
# # relations = get_relations(G, "NodeA", "NodeB")
# # print(f"Relations between NodeA and NodeB: {relations}")
# #
# # relations = get_relations(G, "NodeA", "NodeC")
# # print(f"Relations between NodeA and NodeC: {relations}")  # This will return None since there are no edges
# #
# # relations = get_relations(G, "NodeB", "NodeC")
# # print(f"Relations between NodeB and NodeC: {relations}")
# #
# # import json
# # with open('prompts_naive.json', 'r') as f:
# #     texts = json.load(f)
# #     print(texts['webthink_simple6'])
# # import networkx as nx
# # from collections import Counter
# #
# # # 创建有向图
# # G = nx.DiGraph()
# #
# # # 添加有向边，这里使用一个简单的例子：
# # edges = [(1, 2), (2, 3), (3, 1), (2, 4), (4, 1), (3, 4), (4, 5), (5, 3)]
# # G.add_edges_from(edges)
# #
# # # 找到所有节点对 (u, v, w) 其中存在 u -> v -> w -> u 的三角形
# # from collections import defaultdict, Counter
# #
# #
# # def find_triangles(G):
# #     triangles = []
# #     for u in G.nodes():
# #         for v in G.successors(u):
# #             for w in G.successors(v):
# #                 if u in G.successors(w):
# #                     triangles.append((u, v, w))
# #     return triangles
# #
# #
# # def find_top_triangle_subgraphs(G, top_count=5):
# #     triangle_counts = Counter(find_triangles(G))
# #     top_triangles = triangle_counts.most_common(top_count)
# #
# #     top_triangle_subgraphs = defaultdict(lambda: {'subgraph': None, 'count': 0})
# #
# #     for triangle, count in top_triangles:
# #         u, v, w = triangle
# #         subgraph_nodes = tuple(sorted([u, v, w]))
# #         if top_triangle_subgraphs[subgraph_nodes]['subgraph'] is None:
# #             subgraph = G.subgraph([u, v, w])
# #             top_triangle_subgraphs[subgraph_nodes] = {'subgraph': subgraph, 'count': count}
# #         else:
# #             top_triangle_subgraphs[subgraph_nodes]['count'] += count
# #
# #     return top_triangle_subgraphs
# #
# #
# # # 示例用法：
# # # 假设 G 是你的图对象
# # top_triangle_subgraphs = find_top_triangle_subgraphs(G)
# #
# # # 打印每个三角形子图的节点和边，以及计数
# # for subgraph_nodes, data in top_triangle_subgraphs.items():
# #     print(f"Triangle Nodes: {subgraph_nodes}, Count: {data['count']}")
# #     subgraph = data['subgraph']
# #     print("Nodes:", list(subgraph.nodes()))
# #     print("Edges:", list(subgraph.edges()))
#
# # from collections import defaultdict, Counter
# # import networkx as nx
# # import matplotlib.pyplot as plt
# #
# #
# # def find_top_triangle_subgraphs(G, top_count=5):
# #     triangle_counts = Counter()
# #
# #     # 遍历图中的每条边，查找三角形
# #     for u, v in G.edges():
# #         neighbors_u = set(G.neighbors(u))
# #         neighbors_v = set(G.neighbors(v))
# #         common_neighbors = neighbors_u & neighbors_v
# #
# #         # 对每对共同邻居节点进行遍历，构成三角形
# #         for w in common_neighbors:
# #             if u < v < w:  # 确保每个三角形的顺序唯一
# #                 triangle = tuple(sorted([u, v, w]))
# #                 triangle_counts[triangle] += 1
# #
# #     # 找出出现次数最多的三角形
# #     top_triangles = triangle_counts.most_common(top_count)
# #
# #     # 创建字典存储出现次数最多的三角形子图及其计数
# #     top_triangle_subgraphs = {}
# #     for triangle, count in top_triangles:
# #         u, v, w = triangle
# #         subgraph_nodes = tuple(sorted([u, v, w]))
# #         if subgraph_nodes not in top_triangle_subgraphs:
# #             subgraph = G.subgraph([u, v, w])
# #             top_triangle_subgraphs[subgraph_nodes] = {
# #                 'subgraph': subgraph,
# #                 'count': count
# #             }
# #
# #     return top_triangle_subgraphs
# #
# #
# # # 示例用法：
# # G = nx.Graph()  # 创建一个NetworkX的无向图对象
# # # 在这里添加节点和边，以及相应的数据
# # edges = [(1, 2), (2, 3), (3, 1), (2, 4), (4, 1), (3, 4), (4, 5), (5, 3)]
# # G.add_edges_from(edges)
# #
# # top_triangle_subgraphs = find_top_triangle_subgraphs(G)
# #
# # # 打印每个三角形子图的节点和边，以及计数
# # for subgraph_nodes, data in top_triangle_subgraphs.items():
# #     print(f"Triangle Nodes: {subgraph_nodes}, Count: {data['count']}")
# #     subgraph = data['subgraph']
# #     print("Nodes:", list(subgraph.nodes()))
# #     print("Edges:", list(subgraph.edges()))
# #
# #     # 绘制子图
# #     plt.figure(figsize=(5, 5))
# #     pos = nx.spring_layout(subgraph)
# #     nx.draw(subgraph, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
# #     nx.draw_networkx_edge_labels(subgraph, pos, edge_labels={(u, v): f'{u}->{v}' for u, v in subgraph.edges()})
# #     plt.title(f"Triangle Nodes: {subgraph_nodes}, Count: {data['count']}")
# #     plt.show()
#
# # import networkx as nx
# # import matplotlib.pyplot as plt
# #
# # # 创建一个有向图
# # G = nx.DiGraph()
# #
# # # 添加节点和边以形成一个star结构
# # # 假设中心节点是 'center'，叶节点是 'leaf1', 'leaf2', 'leaf3', 'leaf4'
# # center = 'center'
# # leaves = ['leaf1', 'leaf2', 'leaf3', 'leaf4']
# #
# # # 添加边
# # for leaf in leaves:
# #     G.add_edge(center, leaf)
# #     G.add_edge(leaf, center)
# #
# # # 绘制图形
# # plt.figure(figsize=(8, 8))
# # pos = nx.spring_layout(G)
# # nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
# # nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{u}->{v}' for u, v in G.edges()})
# # plt.title("Star Motif")
# # plt.show()
#
# # import networkx as nx
# # from collections import Counter
# #
# # # 创建一个有向图
# # G = nx.DiGraph()
# # # 添加边
# # edges = [
# #     ('A', 'B'), ('A', 'C'), ('A', 'D'),
# #     ('B', 'C'),
# #     ('C', 'A'), ('C', 'D'),
# #     ('D', 'B'),
# #     ('E', 'A'), ('E', 'B'), ('E', 'C'), ('E', 'D'),
# #     ('F', 'A'),
# #     ('G', 'E'),
# #     ('H', 'F'),
# #     # 其他边
# # ]
# # G.add_edges_from(edges)
# #
# # # 计算每个节点的出度和入度
# # out_degree = dict(G.out_degree())
# # in_degree = dict(G.in_degree())
# #
# # # 计算每个节点的总度数（出度 + 入度）
# # total_degree = {node: out_degree[node] + in_degree[node] for node in G.nodes()}
# #
# # # 按总度数排序，选择top 5的节点
# # top_nodes = sorted(total_degree, key=total_degree.get, reverse=True)[:5]
# #
# # # 构建星型motif子图
# # def build_star_motif(graph, center_node):
# #     neighbors = list(graph.successors(center_node)) + list(graph.predecessors(center_node))
# #     star_motif = nx.DiGraph()
# #     for neighbor in neighbors:
# #         if graph.has_edge(center_node, neighbor):
# #             star_motif.add_edge(center_node, neighbor)
# #         if graph.has_edge(neighbor, center_node):
# #             star_motif.add_edge(neighbor, center_node)
# #     return star_motif
# #
# # top_star_motifs = {node: build_star_motif(G, node) for node in top_nodes}
# #
# # # 输出结果
# # for node, motif in top_star_motifs.items():
# #     print(f"Star Motif centered at {node}:")
# #     print(motif.edges)
# #     print()
#
# # import matplotlib.pyplot as plt
# # import networkx as nx
# #
# # # Define the nodes and edges for the graph
# # nodes = ['Bev_Oda', 'Canada', 'Conservative_Party_of_Canada', 'New_Node']
# # edges = [('Bev_Oda', 'Canada'),
# #          ('Bev_Oda', 'Conservative_Party_of_Canada'),
# #          # ('Canada', 'Conservative_Party_of_Canada'),
# #          ('New_Node', 'Bev_Oda'),
# #          ('New_Node', 'Canada'),
# #          ('New_Node', 'Conservative_Party_of_Canada')]
# #
# # # Create the graph
# # G = nx.Graph()
# # G.add_nodes_from(nodes)
# # G.add_edges_from(edges)
# #
# # # Draw the graph
# # pos = nx.spring_layout(G)
# # nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold')
# # nx.draw_networkx_edge_labels(G, pos, edge_labels={('Bev_Oda', 'Canada'): 'continent',
# #                                                   ('Bev_Oda', 'Conservative_Party_of_Canada'): 'country_of_citizenship',
# #
# #                                                   ('New_Node', 'Bev_Oda'): 'is_connected_with',
# #                                                   ('New_Node', 'Canada'): 'is_connected_with',
# #                                                   ('New_Node', 'Conservative_Party_of_Canada'): 'is_connected_with'})
# #
# # # Show the plot
# # plt.title("Triangle Motif with an Additional Node")
# # plt.show()
#
# import networkx as nx
# from heapq import nlargest
#
# # def find_top_shared_triangles(graph, node, top_n):
# #     # 获取目标节点的邻居
# #     neighbors = set(graph.neighbors(node))
# #
# #     # 字典来记录每个邻居节点与目标节点共享的三角形列表
# #     shared_triangles = {neighbor: [] for neighbor in neighbors}
# #
# #     # 遍历每个邻居节点，找出共享三角形
# #     for neighbor in neighbors:
# #         # 获取邻居节点的邻居
# #         neighbors_of_neighbor = set(graph.neighbors(neighbor))
# #
# #         # 找出共同邻居（即三角形中的第三个节点）
# #         common_neighbors = neighbors & neighbors_of_neighbor
# #
# #         # 记录共享三角形
# #         for common_neighbor in common_neighbors:
# #             triangle = tuple(sorted((node, neighbor, common_neighbor)))
# #             shared_triangles[neighbor].append(triangle)
# #
# #     # 将所有共享三角形收集到一个列表中
# #     all_shared_triangles = []
# #     for triangles in shared_triangles.values():
# #         all_shared_triangles.extend(triangles)
# #
# #     # 找出前 top_n 个共享次数最多的三角形
# #     top_shared_triangles = nlargest(top_n, set(all_shared_triangles), key=lambda t: all_shared_triangles.count(t))
# #
# #     # 构建包含这些三角形motif的子图
# #     motif_graphs = []
# #     for triangle in top_shared_triangles:
# #         motif_graph = nx.Graph()
# #         motif_graph.add_edges_from(
# #             [(triangle[0], triangle[1]), (triangle[1], triangle[2]), (triangle[2], triangle[0])]
# #         )
# #         motif_graphs.append(motif_graph)
# #
# #     return motif_graphs
# #
# # # 示例使用
# # G = nx.Graph()
# # # 添加示例节点和边
# # G.add_edges_from([
# #     (1, 2), (1, 3), (1, 4),
# #     (2, 3), (2, 4),
# #     (3, 4), (3, 5),
# #     (4, 5)
# # ])
# #
# # node = 1
# # top_n = 5
# #
# # motifs = find_top_shared_triangles(G, node, top_n)
# # for i, motif in enumerate(motifs):
# #     print(f"Motif {i+1}:")
# #     print(motif.edges())
#
#
#
# # s = ('qwhjahsnwnu Thought1:..........................'
# #      'Act1:..................')
# # thought_idx = s.find('Thought')
# # act_idx = s.find('Act')
# # thought = s[thought_idx:act_idx-1]
# # act = s[act_idx:-1]
# # print(thought + '\n' + act)
# #
# #
# # def find_requests(s):
# #      start_idx = s.find('Request[')
# #      end_idx = s.find(']')
# #      if start_idx != -1:
# #           return s[start_idx + 8: end_idx]
# #      return -1
# # print(find_requests('Requst[end]'))
# #
# # def find_code(s):
# #      start_idx = s.find('<code>')
# #      end_idx = s.find("</code>")
# #      return s[start_idx + 6: end_idx]
# #
# # s  = '<code>2344455</code>'
# # print(find_code(s))
#
# import json
#
# # with open('idx_prompt_dict_step_00.json', 'r') as f:
# #      step_00 = json.load(f)
# #
# # with open('idx_prompt_dict_step_00_format.json', 'w') as f:
# #      json.dump(step_00, f, indent=4)
# import re
#
#
# # def extract_target_entity(text):
# #      # 优先匹配带单引号的目标实体
# #      pattern_single_quote = r"Terminate\['(.*?)'\]"
# #      match_single_quote = re.search(pattern_single_quote, text)
# #
# #      if match_single_quote:
# #           return match_single_quote.group(1)
# #
# #      # 如果没有匹配到带单引号的目标实体，则匹配不带引号的目标实体
# #      pattern_no_quote = r"Terminate\[(.*?)\]"
# #      match_no_quote = re.search(pattern_no_quote, text)
# #
# #      if match_no_quote:
# #           return match_no_quote.group(1)
# #
# #      return -1
# #
# # with open('output/icews_yago/LLM_response_code_motif/thought_and_acts_01.json') as f:
# #      lines = json.load(f)
# #      for line in lines:
# #           terminate = extract_target_entity(line)
# #           print(terminate)
#
# import argparse
#
# # # 创建 ArgumentParser 对象
# # parser = argparse.ArgumentParser(description="It's a test")
# #
# # parser.add_argument('-d', '--dataset', type=str, help='dataset name')
# #
# # parser.add_argument('-i', '--info_type', type=str, help='code_motif,text_motif,1_neighbor')
# #
# # parser.add_argument('-l', '--llm_type', type=str, help='LLM type')
# #
# # # # 添加可选参数（带默认值）
# # # parser.add_argument('-n', '--number', type=int, default=42, help='要处理的数字')
# #
# # # 解析参数
# # args = parser.parse_args()
# #
# # dataset = args.dataset
# # info_type = args.info_type
# # LLM_type = args.llm_type
# # print(dataset)
# # print(info_type)
# # print(LLM_type)
# # random_sample = 0.3
# # f = "new_ent_ids_1_random_sample_{}".format(random_sample)
# # print(f)

# import re
# def find_most_list_llama(text):
#     match = re.search(r"Most\[(.*?)\]", text)
#
#     if match:
#         extracted_list = match.group(1).encode().decode('unicode_escape')
#         extracted_list = eval('[' + extracted_list + ']')
#
#         return extracted_list
#     else:
#         return -1
# text = 'Most[\'Abdulla Kurd\', \'Salam Fayyad\', \'Sule Lamido\', \'Talal Arslan\', \'Saad Hariri\', \'Salou Djibo\', \'Shwe Mann\', \'Aung Min\', \'Soe Thein\', \'Suharto\']'
# print(find_most_list_llama(text))

# prompt = "\nYou are a programmer in a large company, tasked with selecting the most similar entity to a target entity from a candidate list. You will solve the task using a series of interleaving Thought, Action, and Observation steps. Thought can reason about the current situation, and Action can only be one of the following two types:\n\n- Request[entity]: Requests the context information of the entity from external Knowledge Graphs. You can only request one entity in each turn, and it must be from the candidate list or the target entity itself.\n- The most similar 50 entities are: <MOST>[]</MOST> and Terminate[answer]: Returns the answer and finishes the task. This action can only occur when you finish the task! When you decide to use terminate action, you mush put the most similar 50 entities into: \"<MOST>[]</MOST>\". Please note that if there is a direct match, please use act Terminate[] directly to end the precess.\n\nYou must have an act from above two actions per turn no matter it is request or terminate. The act can only be two types. \n\n**NOTE:** You must request the most relevant entity information from the candidate list to reduce your uncertainty and finally help you to finish this task correctly. If you request less important entities and fail to handle this task perfectly, you will be immediately fired! Here are two examples to refer:\n\n------\n## Example 1:\n\n[USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it directly.\n\n**The target entity is:** 'Ne Win'\n\n**The candidate entities list is:**\n['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temel\u00edn', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia']\n\nNOTE:\n1. You have at most 4 turns to generate the final result. Please answer the task with interleaving Thought, Code, Action, Result turns. \n2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!\n\n[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!\n\n### Turn 1: (3 turns left to use \"Terminate\" action to provide final answer.)\n**Thought 1:** I can find the aligned entity directly from the candidate list because there is a direct match.\n**Act 1:\n**The most similar 50 entities are:<MOST>['Ne Win', 'Hla Min', 'Soe Thein', 'Chea Sim', 'Aung Min', 'Hla Tun', 'Su Chi', 'Tea Banh', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Benin', 'Yen Ming', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Serbia', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Temel\u00edn', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Ukraine', 'Zambia']</MOST> and Terminate['Ne Win']\n\n------\n## Example 2\n\n[USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it directly. \n\n**The target entity is:** 'Salauddin'\n\n**The candidate entities list is:**\n['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn F\u00e9in', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Abdulla Kurd']\n\nNOTE:\n1. You have at most 4 turns to generate the final result. Please answer the task with interleaving Thought, Code, Action, Result turns. \n2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!\n\n[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!\n\n### Turn 1: (3 turns left to use \"Terminate\" action to provide final answer.)\n**Thought 1:** I cannot find an entity in the candidate list that is a direct match for \"Salauddin.\" I need more information about \"Salauddin\" to make an informed decision.\n**Act 1: **The most similar 50 entities are:<MOST>['Abdulla Kurd', 'Salam Fayyad', 'Sule Lamido', 'Talal Arslan', 'Saad Hariri', 'Salou Djibo', 'Shwe Mann', 'Aung Min', 'Soe Thein', 'Suharto', 'Hla Min', 'Hla Tun', 'Jawed Ludin', 'Sima Samar', 'Samar', 'Sama', 'Shas', 'Fatah', 'Hamas', 'Gilad Erdan', 'Babar Awan', 'Hamid Mir', 'Ramdev', 'Imran Khan', 'Sylvia Lim', 'Kashmir', '\u0100nanda', 'Sukarno', 'Sam Nujoma', 'Ne Win', 'Benin', 'Sula Lamido', 'Shwe Mann', 'Su Chi', 'Aung Min', 'Talal Arslan', 'Kashmir', 'Sule Lamido', 'Samar', 'Fatah', 'Hamas', 'Gilad Erdan', 'Babar Awan']</MOST> and Terminate['Abdulla Kurd']\n\n------\n# New Task:\n[USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it directly. \n\n**The target entity is:** \nRuam Jai Thai\n\n**The candidate entities list is:**\n['Rami Jarrah', 'Karam Ali Shah', 'Zhao Lianhai', 'Sai Mauk Kham', 'Luan Rama', 'Puan Maharani', 'Tan Jee Say', 'Hamzah Haz', 'Hamshahri', 'Rabi Ray', 'Bamir Topi', 'Chaman Lal', 'Hamada Madi', 'Fuad Qalaf', 'Cui Tiankai', 'Aamir Khan', 'Munir Said Thalib', 'Rudy Giuliani', 'Jamaica', 'Chiam See Tong', 'Chan Santokhi', 'Ma Kai', 'Tea Banh', 'Jaak Aab', 'Kundi Paihama', 'Sam Abal', 'Toomas Savi', 'Nur Misuari', 'Tulsi Giri', 'Fuat Oktay', 'Dullah Omar', 'Royal Thai Navy', 'Pap Saine', 'Pak Ui-chun', 'Michael Tsai', 'Yushau Shuaib', 'Ilham Tohti', 'Eda Rivas', '\u0110inh La Th\u0103ng', 'Aamulehti', 'Liam Lawlor', 'Malalai Joya', 'Burhan Wani', 'Siim Kallas', 'Henry Van Thio', 'Russ Feingold', 'Rupiah Banda', 'Tin Naing Thein', 'Themba Godi', 'Hasan Tiro']\n\nNOTE:\n1. You have at most 4 turns to generate the final result. Please follow my examples above to answer the task with interleaving Thought, Code, Action, Result turns. \n2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!\n3. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!!\n4. If you are very sure about the answer, please answer directly. \n5. If there is the same entity in the candidate list as the target entity, please select it directly and terminate the process. \n6. You must have an act from above two actions per turn no matter it is request or terminate. The act can only be two types.\n7. Please follow the example format: thought, action, observation steps. Do not generate response by yourself.\n8. If you can find a direct match, please use act \"Terminate[]\" directly and do no need to confirm another entity.\n9. If you are can not find a direct match, please request and do not terminate.\n10. Please do not generate any observations.\n11. The output format is \"The most similar 50 entities are: <MOST>[]</MOST> and Terminate[answer]\".\n12. Request[] action can only request an entity in candidate list or it is itself. \n\n[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment\n\n### Turn 1: (3 turns left to use \"Terminate\" action to provide final answer.)\n**Thought 1:**\nGiven the target entity \"Ruam Jai Thai\" and the candidate list provided, there is no direct match in the list. \"Ruam Jai Thai\" suggests a Thai context, possibly related to politics, social movements, or organizations within Thailand. To make an informed decision, it's crucial to understand the nature of \"Ruam Jai Thai\" better. Among the candidates, entities related to Thai politics or society could be more relevant. However, without specific knowledge about \"Ruam Jai Thai,\" it's challenging to pinpoint which candidate might be the most similar based on the names alone. Entities like \"Royal Thai Navy\" hint at a Thai connection but from a different sector. It might be beneficial to request information on \"Ruam Jai Thai\" itself if available to get a clearer understanding of its nature and then find the most similar entity based on that understanding.\n\n**Act 1:** Request[Ruam Jai Thai]Observation 1: The background information of the entity is below which is given in code format motifs: \n\nimport express_intent_to_engage_in_diplomatic_cooperation, make_statement, yield_interaction, demand_interaction, consult_interaction, make_an_appeal_or_request, praise_or_endorse\n\nclass Ruam_Jai_Thai(object):\n\n    def __init__(self, Chavalit_Yongchaiyudh, Ruam_Jai_Thai, Military_Thailand):\n        ## This is initial function\n        self.Chavalit_Yongchaiyudh = Chavalit_Yongchaiyudh\n        self.Ruam_Jai_Thai = Ruam_Jai_Thai\n        self.Military_Thailand = Military_Thailand\n\n    def Chavalit_Yongchaiyudh_engage_Ruam_Jai_Thai(self):\n        self.Chavalit_Yongchaiyudh = express_intent_to_engage_in_diplomatic_cooperation(self.Ruam_Jai_Thai)\n        \n        return self.Chavalit_Yongchaiyudh, self.Ruam_Jai_Thai\n\n    def Chavalit_Yongchaiyudh_interactions_with_Military(self):\n        self.Chavalit_Yongchaiyudh = make_statement(self.Military_Thailand)\n        self.Chavalit_Yongchaiyudh += yield_interaction(self.Military_Thailand)\n        self.Chavalit_Yongchaiyudh += demand_interaction(self.Military_Thailand)\n        self.Chavalit_Yongchaiyudh += consult_interaction(self.Military_Thailand)\n        self.Chavalit_Yongchaiyudh += make_an_appeal_or_request(self.Military_Thailand)\n        \n        return self.Chavalit_Yongchaiyudh, self.Military_Thailand\n\n    def Ruam_Jai_Thai_endorse_Military(self):\n        self.Ruam_Jai_Thai = praise_or_endorse(self.Military_Thailand)\n        \n        return self.Ruam_Jai_Thai, self.Military_Thailand\n``"
# prompt_1 =  "### Turn 2: (2 turns left to use \"Terminate\" action to provide final answer.)\n**Thought 2:**\nThe information provided about \"Ruam Jai Thai\" indicates a strong connection with Thai military and political spheres, specifically mentioning Chavalit Yongchaiyudh, a notable figure in Thai politics and military. This suggests that \"Ruam Jai Thai\" is likely a political or military entity within Thailand. Given this context, the most similar entity from the candidate list would likely be one that has a direct connection to Thai politics or military. \"Royal Thai Navy\" stands out as it is directly related to the military aspect of Thailand. However, it's important to note that \"Ruam Jai Thai\" seems to be more of a political or collective movement rather than a specific military branch. Therefore, while \"Royal Thai Navy\" is closely related, there might not be a direct match in the list that perfectly aligns with \"Ruam Jai Thai\" as a political entity. Given the information and the nature of \"Ruam Jai Thai,\" it's crucial to select an entity that closely aligns with its political and military context within Thailand.\n\n**Act 2:** The most similar 50 entities are:<MOST>['Royal Thai Navy', 'Tan Jee Say', 'Puan Maharani', 'Hamzah Haz', 'Sai Mauk Kham', 'Luan Rama', 'Rami Jarrah', 'Karam Ali Shah', 'Zhao Lianhai', 'Hamshahri', 'Rabi Ray', 'Bamir Topi', 'Chaman Lal', 'Hamada Madi', 'Fuad Qalaf', 'Cui Tiankai', 'Aamir Khan', 'Munir Said Thalib', 'Rudy Giuliani', 'Jamaica', 'Chiam See Tong', 'Chan Santokhi', 'Ma Kai', 'Tea Banh', 'Jaak Aab', 'Kundi Paihama', 'Sam Abal', 'Toomas Savi', 'Nur Misuari', 'Tulsi Giri', 'Fuat Oktay', 'Dullah Omar', 'Pap Saine', 'Pak Ui-chun', 'Michael Tsai', 'Yushau Shuaib', 'Ilham Tohti', 'Eda Rivas', '\u0110inh La Th\u0103ng', 'Aamulehti', 'Liam Lawlor', 'Malalai Joya', 'Burhan Wani', 'Siim Kallas', 'Henry Van Thio', 'Russ Feingold', 'Rupiah Banda', 'Tin Naing Thein', 'Themba Godi', 'Hasan Tiro']</MOST> and Terminate['Royal Thai Navy']"
#
# print(prompt+prompt_1)
#
# exit()
# def find_code(s):
#     start_idx = s.find('<code>')
#     end_idx = s.find("</code>")
#     if start_idx != -1:
#         return s[start_idx + 6: end_idx]
#
#     start_idx = s.find('<CODE>')
#     end_idx = s.find("</CODE>")
#     if start_idx != -1:
#         return s[start_idx + 6: end_idx]
#
#     start_idx = s.find('python')
#     if start_idx != -1:
#         return s[start_idx + 6: -1]
#
#     return 'no code observation for this entity.'

# txt = "```python\nimport is_connected_with\n\nclass Enrique_Mugica(object):\n\n    def __init__(self, Enrique_Mugica, Communist_Party_of_Spain):\n        ## This is initial function\n        self.Enrique_Mugica = Enrique_Mugica\n        self.Communist_Party_of_Spain = Communist_Party_of_Spain\n\n    def Enrique_Mugica_connected_with_Communist_Party(self):\n        # Establishing connections between Enrique M\u00fagica and the Communist Party of Spain\n        self.Communist_Party_of_Spain = is_connected_with(self.Enrique_Mugica)\n        self.Enrique_Mugica = is_connected_with(self.Communist_Party_of_Spain)\n        \n        return self.Enrique_Mugica, self.Communist_Party_of_Spain\n```"
# print(find_code(txt))

# import subprocess
# import sys
#
# def install(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])
#
# # 示例: 安装 requests 库
# install("tiktoken")
#
# exit()

import json
from run.utils import hit_1_10_rate, baseline_hit_rate

dataset = 'icews_yago'
save_dir = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/output/{}/gpt_4_turbo/t5000_50_50_corrected_5motif_v16'.format(dataset)
ent1_f = 'new_ent_ids_1_rs_0.3_new'
ent2_f = 'new_ent_ids_2_aligned_rs_0.3_new'
type = 'recall_all'
method = 'text'


if dataset == 'icews_wiki':
    length_all = 1496
elif dataset == 'icews_yago':
    length_all = 4999
with open(save_dir + '/final_answer_{}_motif_lite_1.json'.format(method)) as f:
    final_answer_direct_match = json.load(f)
length_recall_all = length_all - len(final_answer_direct_match)


final_answers = {}
if type == 'recall_all':
    for i in [2, 3, 4]:
        with open(save_dir + '/final_answer_{}_motif_lite_{}.json'.format(method, i), 'r') as f:
            final_answer = json.load(f)
            final_answers.update(final_answer)
elif type == 'all':
    for i in [1, 2, 3, 4]:
        with open(save_dir + '/final_answer_{}_motif_lite_{}.json'.format(method, i), 'r') as f:
            final_answer = json.load(f)
            final_answers.update(final_answer)

print(length_all, length_recall_all, len(final_answers))

with open(save_dir+'/final_answer_{}_motif_lite_{}.json'.format(method, type), 'w') as f:
    json.dump(final_answers, f, indent=4)

# baseline_response = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/output/icews_yago_gpt_4_turbo_t5000_50_50_corrected/baseline/idx_prompt_dict_baseline_final_ans.json'
# hit_rate = baseline_hit_rate(baseline_response,dataset, ent1_f, ent2_f, 'hit1')

if type == 'all':
    length = length_all
elif type == 'recall_all':
    length = length_recall_all

hit_rate = hit_1_10_rate(save_dir+'/final_answer_{}_motif_lite_{}.json'.format(method, type),
                         dataset=dataset,
                         ent1_f=ent1_f,
                         ent2_f=ent2_f,
                         hit='hit1',
                         length=length)
print(hit_rate)

# from run.utils import mean_reciprocal_rank
# mrr = mean_reciprocal_rank(final_answers)
# print(mrr)


# import re
# def find_most_list_llama(text):
#     match = re.search(r"Most\[(.*?)\]", text)
#
#     if match:
#         extracted_list = match.group(1).encode().decode('unicode_escape')
#         extracted_list = eval('['+extracted_list+']')
#
#         return extracted_list
#     else:
#         return -1
#
# text = "I can find a direct match for the target entity \"Keshari Nath Tripathi\" in the candidate list.\n\nAct 1: The most similar 10 entities are: Most['Keshari Nath Tripathi', 'Hridayesh Tripathi', 'Bhrigu Nath Singh', 'Kamal Nath', 'Kehar Singh', 'Dina Nath Sharma', 'Kastriot Islami', 'Nguy\u1ec5n Minh Tri\u1ebft', 'Kukrit Pramoj', 'Kausea Natano'] and Terminate['Keshari Nath Tripathi'].",
# print(find_most_list_llama(str(text)))


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

# import os
#
# # 获取当前工作目录
# current_path = os.getcwd()
#
# # 打印当前工作目录
# print(f"当前路径是：{current_path}")

# list = ['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Abdulla Kurd']
# print(len(list))

