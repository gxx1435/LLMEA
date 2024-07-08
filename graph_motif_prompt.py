import os.path
import networkx as nx
from itertools import combinations

import numpy as np

from run.utils import get_id_entity_dict, get_ent_id_dict

def find_triangle_motifs(graph):
    """
    Find all triangle motifs in the graph and return them as subgraphs.

    :param graph: A NetworkX graph
    :return: A list of subgraphs, each representing a triangle motif
    """
    triangles = [clique for clique in nx.enumerate_all_cliques(graph) if len(clique) == 3]
    subgraphs = []

    for triangle in triangles:
        subgraph = graph.subgraph(triangle).copy()
        subgraphs.append(subgraph)

    return subgraphs

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


def find_star_motifs(graph):
    """
    Find all star motifs in the graph and return them as subgraphs.

    :param graph: A NetworkX graph
    :return: A list of subgraphs, each representing a star motif
    """
    stars = []

    # Iterate over nodes to find stars
    for node in graph.nodes():
        neighbors = list(graph.neighbors(node))
        if len(neighbors) > 1:  # Node has more than one neighbor
            star_nodes = [node] + neighbors
            star = graph.subgraph(star_nodes).copy()
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
    triangle_motifs = find_triangle_motifs(G)

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
        motifs = find_triangle_motifs(G)
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

dataset = 'icews_wiki'

id_ent_dict = get_id_entity_dict(
    '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/ent_ids_1'.format(dataset))
# ent_id_dict = get_ent_id_dict(
#     '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/ent_ids_1'.format(dataset))

_2_neighbor_subgraph_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/2_neighbor_subgraph_1'.format(dataset)
_1_neighbor_subgraph_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/1_neighbor_subgraph_1'.format(dataset)

ent_id_1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1'.format(dataset)
ent_id_2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_2'.format(dataset)
entity_left_value = [line.split('\t')[1].split('/')[-1].strip() for line in open(ent_id_1_path).readlines()]
entity_left_id = [line.split('\t')[0] for line in open(ent_id_1_path).readlines()]
entity_left_id_dict = dict(zip(entity_left_id, range(len(entity_left_id))))

entity_right_value = [line.split('\t')[1].split('/')[-1].strip() for line in open(ent_id_2_path).readlines()]
entity_right_value_dict = dict(zip(range(len(entity_right_value)), entity_right_value))

sematic_embedding_candidates_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/candiadtes_semantic_embed_100_3000_all.txt'.format(dataset)
candidates = [[int(idx) for idx in line.strip().split(',')] for line in open(sematic_embedding_candidates_path).readlines()]
candidates = [[entity_right_value_dict[idx] for idx in line] for line in candidates]

class Entity:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_subgraph(self, node):
        """

        :return:
        """
        subgraph_file = _1_neighbor_subgraph_path + '/{}.graph'.format(node)
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

        subgraph_file = _2_neighbor_subgraph_path+'/{}.graph'.format(node)
        edges = []
        with open(subgraph_file, 'r') as f:
            for line in f.readlines():
                edges.append((line.split(' ')[0], line.split(' ')[1].strip()))
        G = nx.Graph()
        G.add_edges_from(edges)
        motifs = find_triangle_motifs(G)

        return motifs


    def get_star_motif(self, node):
        """

        :param node:
        :return:
        """
        subgraph_file = _1_neighbor_subgraph_path + '/{}.graph'.format(node)
        edges = []
        with open(subgraph_file, 'r') as f:
            for line in f.readlines():
                edges.append((line.split(' ')[0], line.split(' ')[1].strip()))
        G = nx.Graph()
        G.add_edges_from(edges)
        motifs = find_star_motifs(G)


        return motifs

    def get_motifs_promts(self, node, motifs):
        """

        :param motifs:
        :return:
        """
        ##获取三角形prompts
        motifs_prompts = ''
        for i, subgraph in enumerate(motifs):
            if node in subgraph.nodes:
                # try:
                    motifs_prompts += ','.join([node, id_ent_dict[node], '\t', f"{i + 1}:"])
                    nodes = ','.join([id_ent_dict[idx] for idx in subgraph.nodes()])
                    edges = ','.join(['(' + id_ent_dict[i] + ',' + id_ent_dict[j] + ')' for i, j in subgraph.edges()])
                    motifs_prompts += nodes + '\n'
                    motifs_prompts += edges + '\n'
                # except:
                #     pass

        return motifs_prompts

    def get_candidates(self, node):
        """

        :param node:
        :return:
        """

        return candidates[entity_left_id_dict[node]]


    def get_prompts_with_motif(self):
        """
        :param node:
        :return:
        """
        # triangle_motifs = self.get_triangle_motif(self.id)

        star_motifs = self.get_star_motif(self.id)

        # triangle_motifs_prompts = self.get_motifs_promts(self.id, triangle_motifs)

        star_motifs_prompts = self.get_motifs_promts(self.id, star_motifs)

        prompts = """
        You are a Entity Alignment expert, your task is according to the information I give to find the most similar entity
        from the given candidate list for the given entity. Please note that Motif is refers to a recurring subgraph pattern that appears
        within a larger graph. These motifs are typically small, distinct, and repeated structures that provide insights into 
        the structural and functional aspects of the graph.
        
        === Target Entities Info starts: ===
        Entity Name: {}
        
        Star Motif Neighbors:
        {}

        === Target Entities Info end ===
        
        === Candidate Entities starts: ===
        {}
        === Candidate Entities end ===
        
        --- Your Task starts: ---
        Aligned Entity: {}
        
        ---output format: ----
        xxxx
        
        """.format(self.name,
                   star_motifs_prompts,
                   self.get_candidates(self.id),
                   self.name)


        return prompts

    def get_prompts_without_motif(self):
        """
        :return:
        """
        prompts = """
                You are a Entity Alignment expert, your task is according to the information I give to find the most similar entity
                from the given candidate list for the given entity. Please note that Motif is refers to a recurring subgraph pattern that appears
                within a larger graph. These motifs are typically small, distinct, and repeated structures that provide insights into 
                the structural and functional aspects of the graph.

                === Target Entities Info starts: ===
                Entity Name: {}

                === Target Entities Info end ===

                === Candidate Entities starts: ===
                {}
                === Candidate Entities end ===

                --- Your Task starts: ---
                Aligned Entity: {}

                ---output format: ----
                xxxx

                """.format(self.name,
                           self.get_candidates(self.id),
                           self.name)
        return prompts

    def get_LLM_output(self, prompts):
        """
        :param prompts:
        :return:
        """


if __name__ == '__main__':

    # entity = Entity('游騎兵8號', '182')
    entity = Entity('Vitaly Ivanovich Churkin', '6209')
    # prompts = entity.get_prompts_without_motif()
    prompts = entity.get_prompts_with_motif()
    print(prompts)
    exit()