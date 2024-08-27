import os

import networkx as nx
from collections import Counter, defaultdict
from run.utils import split_camel_case, standarlize_entity
from run.utils import get_id_entity_dict, get_ent_id_dict
from graph_motif_counts import get_subgraph_within_k_per_node, read_graph
# from graph_motif_LLM import (id_ent_dict1, id_ent_dict2,
#                              rel_1_dict, rel_2_dict, G1, G2,
#                              _1_neighbor_subgraph1_path, _2_neighbor_subgraph1_path,
#                              _1_neighbor_subgraph2_path, _2_neighbor_subgraph2_path)
from graph_motif import (find_triangle_or_star_motifs, find_star_motifs,
                             find_tree_motifs, find_four_cycles, find_chain_motifs,
                             find_star_triangle_motifs)

current_dir = os.getcwd()
save_dir = current_dir + '/data'
def get_paths():
    dataset = 'icews_yago'
    sematic_embedding_candidates_path = '{}/{}/candiadtes_semantic_embed_50_5041_all add_put_correct_ans_last.txt'.format(save_dir, dataset)

    # from ReAct_API_call import dataset, sematic_embedding_candidates_path

    ent_id_1_path = '{}/{}/new_ent_ids_1'.format(save_dir, dataset)
    ent_id_2_path = '{}/{}/new_ent_ids_2_aligned'.format(save_dir, dataset)

    _2_neighbor_subgraph1_path = '{}/{}/2_neighbor_subgraph_1'.format(save_dir,dataset)
    _1_neighbor_subgraph1_path = '{}/{}/1_neighbor_subgraph_1'.format(save_dir,dataset)
    _2_neighbor_subgraph2_path = '{}/{}/2_neighbor_subgraph_2'.format(save_dir,dataset)
    _1_neighbor_subgraph2_path = '{}/{}/1_neighbor_subgraph_2'.format(save_dir,dataset)

    return (dataset, sematic_embedding_candidates_path,
            ent_id_1_path, ent_id_2_path,
            _1_neighbor_subgraph1_path, _1_neighbor_subgraph2_path,
            _2_neighbor_subgraph1_path, _2_neighbor_subgraph2_path)

(dataset, sematic_embedding_candidates_path,
 ent_id_1_path, ent_id_2_path,
 _1_neighbor_subgraph1_path, _1_neighbor_subgraph2_path,
 _2_neighbor_subgraph1_path, _2_neighbor_subgraph2_path) = get_paths()

def get_id_ent_dict():
    id_ent_dict1 = get_id_entity_dict(
            '{}/{}/ent_ids_1'.format(save_dir, dataset))
    id_ent_dict2 = get_id_entity_dict(
            '{}/{}/ent_ids_2'.format(save_dir, dataset))
    return id_ent_dict1, id_ent_dict2
id_ent_dict1, id_ent_dict2 = get_id_ent_dict()


def get_candidates():
    ## 获取candidates文件
    entity_keys = [line.split('\t')[0].strip() for line in
                   open(sematic_embedding_candidates_path).readlines()]
    cand_list_values = [line.split('\t')[1].strip().split(',') for line in
                        open(sematic_embedding_candidates_path).readlines()]
    candidates = dict(zip(entity_keys, cand_list_values))
    return candidates
candidates = get_candidates()

def get_Graph():
    """
    :return:
    """
    triple1 = '{}/{}/triples_1'.format(save_dir,dataset)
    triple2 = '{}/{}/triples_2'.format(save_dir,dataset)
    new_triples1 = '{}/{}/new_triples_1'.format(save_dir,dataset)
    new_triples2 = '{}/{}/new_triples_2'.format(save_dir, dataset)
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
    return G1, G2
G1, G2 = get_Graph()

def get_rel_dict():
    ##  获取relation of two nodes
    rel_1_dict = dict()
    rel_ids_1 = '{}/{}/rel_ids_1'.format(save_dir, dataset)
    with open(rel_ids_1) as f:
            for line in f.readlines():
                rel_1_dict.update({line.split('\t')[0]: line.split('\t')[1].strip()})

    rel_2_dict = dict()
    rel_ids_2 = '{}/{}/rel_ids_2'.format(save_dir, dataset)
    with open(rel_ids_2) as f:
            for line in f.readlines():
                rel_2_dict.update({line.split('\t')[0]: line.split('\t')[1].strip()})

    return rel_1_dict, rel_2_dict
rel_1_dict, rel_2_dict = get_rel_dict()

class Entity:

    def __init__(self, entity_name, entity_id, entity_type):
        self.entity_name = entity_name
        self.entity_id = entity_id
        self.entity_type = entity_type

    def cut_off_motif_prompts(self, prompts):

        import subprocess
        import sys
        def install(package):
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

        # 安装 tiktoken 库
        try:
            import tiktoken
        except ModuleNotFoundError:
            install("tiktoken")
            import tiktoken

        tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")
        tokens = tokenizer.encode(prompts)
        max_token = 3500
        current_lenngth = 0
        current_chunk = []
        for token in tokens:
            if current_lenngth + 1 > max_token:
                break
            current_chunk.append(token)
            current_lenngth += 1

        text_chunk = tokenizer.decode(current_chunk)

        return text_chunk

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
            top_5_relations = [split_camel_case(relation) for relation in top_5_relations]

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

    def get_subgraph_offline(self, node):
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
        return G

    def get_subgraph_online(self, node, k=2):
        """
        :param node:
        :return:
        """
        if self.entity_type == 'target':
            newgraph_path = current_dir + '/data/{}/newgraph_1'.format(dataset)
        elif self.entity_type == 'candidate':
            if dataset == 'icews_yago':
                newgraph_path = current_dir + '/data/{}/newgraph_2_remove_26863'.format(dataset)
            else:
                newgraph_path = current_dir + '/data/{}/newgraph_2'.format(dataset)

        graph_edges_kg = read_graph(newgraph_path)
        kg = nx.Graph()
        kg.add_edges_from(graph_edges_kg)

        G = get_subgraph_within_k_per_node(kg, node, k)


        return G

    def get_subgraph_of_node(self, node, k=2):
        """
        Default setting: offline and 2 neighbors
        try, except: online computing
        :return:
        """

        # if k == 2:
        #     try:
        #         G = self.get_subgraph_offline(node)
        #     except:
        #
        #         G = self.get_subgraph_online(node, k)
        # else:

        G = self.get_subgraph_online(node, k)

        # G1 = self.get_subgraph_online(node, k)
        # G2 = self.get_subgraph_offline(node)
        # if sorted(G1.edges) == sorted(G2.edges):
        #     return G1
        # else:
        #     return G1


        return G

    def get_triangle_motif(self, node, top_n=5, if_keep_top_n=1):
        """

        :param node:
        :return:
        """

        G = self.get_subgraph_of_node(node, 2)

        motifs = find_triangle_or_star_motifs(G, node, top_n=top_n, if_keep_top_n=if_keep_top_n)

        return motifs

    def get_star_motif(self, node, if_keep_top_n):
        """

        :param node:
        :return:
        """
        G = self.get_subgraph_of_node(node)

        motifs = find_star_motifs(G, node, if_keep_top_n)

        return motifs

    def get_tree_motif(self, node):
        """
        :param node
        :return:
        """
        G = self.get_subgraph_of_node(node)

        motifs = find_tree_motifs(G, node, 3)

        return motifs

    def get_4_cycle_motif(self, node):
        """
        :param node:
        :return:
        """
        G = self.get_subgraph_of_node(node, 3)

        motifs = find_four_cycles(G, node)


        return motifs

    def get_chain_motifs(self, node):
        """
                :param node:
                :return:
                """
        G = self.get_subgraph_of_node(node)

        motifs = find_chain_motifs(G, 3)

        return motifs

    def get_star_triangles(self, node):
        """
                :param node:
                :return:
                """
        G = self.get_subgraph_of_node(node,3)

        motifs = find_star_triangle_motifs(G, node)

        return motifs

    def get_most_representative_motifs(self, node, top_n=5, if_keep_top_n=1):
        """
        :return:
        """
        def find_all_triangle_motifs(G, node):
            try:
                triangles = []
                neighbors = list(G.neighbors(node))

                for i in range(len(neighbors)):
                    for j in range(i + 1, len(neighbors)):
                        if G.has_edge(neighbors[i], neighbors[j]):
                            triangles.append((node, neighbors[i], neighbors[j]))

                return triangles
            except:
                return []

        def find_all_star_motifs(G, node):
            try:
                star_motifs = []
                neighbors = list(G.neighbors(node))

                for neighbor in neighbors:
                    star_motifs.append((node, neighbor))

                return star_motifs
            except:
                return []

        def find_all_chain_motifs(node):
            try:
                chain_motifs = []
                neighbors = list(G.neighbors(node))

                for neighbor in neighbors:
                    second_neighbors = list(G.neighbors(neighbor))
                    for second_neighbor in second_neighbors:
                        if second_neighbor != node:
                            chain_motifs.append((node, neighbor, second_neighbor))

                return chain_motifs
            except:
                return []

        def find_all_four_cycles(G, node):
            try:
                quadrilaterals = []
                neighbors = list(G.neighbors(node))

                for i in range(len(neighbors)):
                    for j in range(i + 1, len(neighbors)):
                        for k in range(j + 1, len(neighbors)):
                            if G.has_edge(neighbors[i], neighbors[j]) and G.has_edge(neighbors[j],
                                                                                     neighbors[k]) and G.has_edge(
                                    neighbors[k], neighbors[i]):
                                quadrilaterals.append((node, neighbors[i], neighbors[j], neighbors[k]))

                return quadrilaterals
            except:
                return []

        def find_all_star_triangle_motifs(G, node):
            try:
                star_triangles = []
                neighbors = list(G.neighbors(node))

                for i in range(len(neighbors)):
                    for j in range(i + 1, len(neighbors)):
                        if G.has_edge(neighbors[i], neighbors[j]):
                            star_triangles.append((node, neighbors[i], neighbors[j]))

                return star_triangles
            except:
                return []

        G = self.get_subgraph_of_node(node, 3)

        triangles = find_all_triangle_motifs(G, node)

        # stars = find_all_star_motifs(G, node)

        # chains = find_all_chain_motifs(G)

        quadrilaterals = find_all_four_cycles(G, node)

        # star_triangles = find_all_star_triangle_motifs(G, node)

        motif_frequencies = {
            "triangle": len(triangles),
            # "star": len(stars),
            # 'chain': len(chains),
            "quadrilateral": len(quadrilaterals),
            # "star_triangle": len(star_triangles)
        }

        most_frequent_motif = max(motif_frequencies, key=motif_frequencies.get)

        print(
            f"The most representative motif is: {most_frequent_motif} with count: {motif_frequencies[most_frequent_motif]}")

        if most_frequent_motif == "triangle":
            motifs = find_triangle_or_star_motifs(G, node, top_n, if_keep_top_n)
        # elif most_frequent_motif == "star":
        #     motifs = find_triangle_or_star_motifs(G, node, top_n, if_keep_top_n)
        elif most_frequent_motif == "quadrilateral":
            motifs = find_four_cycles(G, node, top_n, if_keep_top_n)
        # elif most_frequent_motif == 'chain':
        #     motifs = find_chain_motifs(G, node, top_n, if_keep_top_n)
        # elif most_frequent_motif == 'star_triangle':
        #     motifs = find_star_triangle_motifs(G, node, top_n, if_keep_top_n)
        else:
            motifs = []

        return motifs

        # if most_frequent_motif == "triangle":
        #     motif_instances = triangles
        # elif most_frequent_motif == "star":
        #     motif_instances = stars
        # elif most_frequent_motif == "quadrilateral":
        #     motif_instances = quadrilaterals
        # elif most_frequent_motif == 'chain':
        #     motif_instances = chains
        # elif most_frequent_motif == 'star_triangle':
        #     motif_instances = star_triangles
        #
        # motif_nodes = set()
        # for instance in motif_instances:
        #     motif_nodes.update(instance if isinstance(instance, tuple) else instance[1])
        #
        # valid_motif_nodes = [node for node in motif_nodes if node in G.nodes()]
        #
        # subgraph = G.subgraph(valid_motif_nodes).copy()
        #
        # return [subgraph]

    def get_motifs_promts(self, node, motifs, if_triple=0, info_type='1_neighbor'):
        """

        :param motifs:
        :return:
        """
        ##获取三角形prompts
        motifs_prompts = ''
        for idx, subgraph in enumerate(motifs):
            # print(node, subgraph.nodes)
            # if node in subgraph.nodes:
                # try:
                if self.entity_type == 'target':

                    if info_type == '1_neighbor':

                        motifs_prompts += 'Neighbor of {}: '.format(standarlize_entity(id_ent_dict1[node]))
                    else:
                        if if_triple:
                            motifs_prompts += '- Target entity:'+ standarlize_entity(id_ent_dict1[node]) + ';' + f"Motif {idx + 1}: "
                        else:
                            motifs_prompts += ' , '.join([standarlize_entity(id_ent_dict1[node]), f"Motif {idx + 1}:\n"])

                elif self.entity_type == 'candidate':

                    if info_type == '1_neighbor':

                        motifs_prompts += 'Neighbor of {}: '.format(standarlize_entity(id_ent_dict2[node]))
                    else:
                        if if_triple:
                            motifs_prompts += '- Target entity: ' + standarlize_entity(id_ent_dict2[node]) + '; '+ f"Motif {idx + 1}: "
                        else:
                            motifs_prompts += ' , '.join([standarlize_entity(id_ent_dict2[node]), f"Motif {idx + 1}:\n"])

                # nodes = ','.join([id_ent_dict[idx] for idx in subgraph.nodes()])
                # edges = ','.join(['(' + id_ent_dict[i] + ',' + id_ent_dict[j] + ')' for i, j in subgraph.edges()])
                triples = []
                for i, j in subgraph.edges():

                    if self.entity_type == 'target':

                        relationship = self.get_relation(G1, i, j)

                        # if len(relationship.split(",")) > 2:
                        #     relationships = relationship.split(",")
                        # else:
                        #     relationships = [relationship]
                        #
                        # for rel in relationships:
                        if if_triple:

                                triples.append(
                                    "(" + standarlize_entity(
                                        id_ent_dict1[i]) + "," + relationship + "," + standarlize_entity(
                                        id_ent_dict1[j]) + ")"
                                )
                        else:
                                motifs_prompts += standarlize_entity(id_ent_dict1[i]) + relationship + standarlize_entity(id_ent_dict1[j]) + '\n'

                    elif self.entity_type == 'candidate':

                        relationship = self.get_relation(G2, i, j)

                        # if len(relationship.split(",")) > 2:
                        #     relationships = relationship.split(",")
                        # else:
                        #     relationships = [relationship]
                        #
                        # for rel in relationships:
                        if if_triple:
                                triples.append(
                                    "("+standarlize_entity(
                                        id_ent_dict2[i]) + "," + relationship + "," + standarlize_entity(
                                        id_ent_dict2[j])+")"
                                )
                        else:
                                motifs_prompts += standarlize_entity(id_ent_dict2[i]) + relationship + standarlize_entity(id_ent_dict2[j]) + '\n'

                if if_triple:
                    motifs_prompts += '['+','.join(triples)+']'+'\n'

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
                4. Please rerank the candidate list and put the answer in the first place of candidate list.
                5. Please give a similarity score of each candidate in candidate list and target entity like (Xiao, 0.95), (patrick, 0.90).
                6. the output format is: the rerank candidate lists is <most>[(Xiao, 0.95), (patrick, 0.90)...]</most> and the answer is <output></output>.

                === Target Entities Info starts: ===
                Entity Name: {}

                === Target Entities Info end ===

                === Candidate Entities starts: ===
                {}
                === Candidate Entities end ===

                --- Your Task starts: ---
                Target Entity: {}

                ---output format: ----
                The rerank candidate list is <most></most> and the answer is <output> xxxx </output>

                """.format(self.entity_name,
                           self.get_candidates(self.entity_name),
                           self.entity_name)

        return self.entity_name, self.get_candidates(self.entity_name), prompts

    def get_only_1_neighbor_information(self, if_triple=0, info_type='', if_keep_top_n=1):
        """
        :return:
        """

        star_motifs = self.get_star_motif(self.entity_id, if_keep_top_n)

        star_motifs_prompts = self.get_motifs_promts(self.entity_id, star_motifs, if_triple, info_type)

        prompts = self.cut_off_motif_prompts(star_motifs_prompts)

        return prompts

    def get_only_triangle_information(self, if_triple=0, info_type='', top_n=5, if_keep_top_n=1):
        """
        :return:
        """

        triangle_motifs = self.get_triangle_motif(self.entity_id, top_n=top_n, if_keep_top_n=if_keep_top_n)

        triangle_motifs_prompts = self.get_motifs_promts(self.entity_id, triangle_motifs, if_triple=if_triple, info_type=info_type)

        prompts = self.cut_off_motif_prompts(triangle_motifs_prompts)

        return prompts

    def get_only_star_information(self):
        """
        :return:
        """

        star_motifs = self.get_star_motif(self.entity_id)

        star_motifs_prompts = self.get_motifs_promts(self.entity_id, star_motifs)

        return star_motifs_prompts

    def get_only_tree_information(self):
        """
        :return:
        """
        tree_motifs = self.get_tree_motif(self.entity_id)

        tree_motif_prompts = self.get_motifs_promts(self.entity_id, tree_motifs)

        return tree_motif_prompts

    def get_only_4_cycles_information(self):
        """
        :return:
        """
        _4_cycle = self.get_4_cycle_motif(self.entity_id)

        _4_cycle_prompts = self.get_motifs_promts(self.entity_id, _4_cycle)

        return _4_cycle_prompts

    def get_only_chain_information(self):
        """
        :return:
        """
        chain_motifs = self.get_chain_motifs(self.entity_id)

        chain_motifs_prompts = self.get_motifs_promts(self.entity_id, chain_motifs)

        return chain_motifs_prompts

    def get_only_star_triangle_information(self):
        """
        :return:
        """
        star_traiagles = self.get_star_triangles(self.entity_id)

        star_traiagles_prompts = self.get_motifs_promts(self.entity_id, star_traiagles)

        return star_traiagles_prompts

    def get_dynamic_motifs_information(self, if_triple=0, info_type='', top_n=5, if_keep_top_n=1):
        """
        :return:
        """

        motifs = self.get_most_representative_motifs(self.entity_id, top_n=top_n, if_keep_top_n=if_keep_top_n)

        prompts = self.get_motifs_promts(self.entity_id, motifs, if_triple=if_triple, info_type=info_type)

        prompts = self.cut_off_motif_prompts(prompts)

        return prompts


    def get_LLM_output(self, prompts):
        """
        :param prompts:
        :return:
        """

        return

def main():

    ent_id_1_path = current_dir + '/data/{}/new_ent_ids_1_rs_0.3_new'.format(dataset)
    ent_id_2_path = current_dir + '/data/{}/new_ent_ids_2_aligned_rs_0.3_new'.format(dataset)

    entity_type = 'candidate'
    entity_type = 'target'

    ent_id_dict = {}
    if entity_type == ('target'):
        ent_id_dict = get_ent_id_dict(ent_id_1_path)

    elif entity_type == 'candidate':
        ent_id_dict = get_ent_id_dict(ent_id_2_path)

    entity = """Jimmy Rasta"""
    entity_id = ent_id_dict[entity]

    entity = Entity(entity, entity_id, entity_type)

    # _, _, prompts = entity.get_baseline_prompts()
    prompts = entity.get_only_triangle_information(if_triple=1)
    # prompts = entity.get_dynamic_motifs_information(if_triple=1)

    print(prompts)

if __name__ == '__main__':

    main()