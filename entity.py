import networkx as nx
from collections import Counter, defaultdict
from run.utils import get_id_entity_dict, get_ent_id_dict
from graph_motif_counts import get_subgraph_within_k_per_node, read_graph
# from graph_motif_LLM import (id_ent_dict1, id_ent_dict2,
#                              rel_1_dict, rel_2_dict, G1, G2,
#                              _1_neighbor_subgraph1_path, _2_neighbor_subgraph1_path,
#                              _1_neighbor_subgraph2_path, _2_neighbor_subgraph2_path)
from graph_motif_LLM import find_triangle_or_star_motifs, find_star_motifs


def get_paths():
    dataset = 'icews_yago'
    sematic_embedding_candidates_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_100_3765_all add_corrected.txt'

    from ReAct_API_call_Nan import dataset, sematic_embedding_candidates_path

    ent_id_1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1'.format(dataset)
    ent_id_2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_2_aligned'.format(dataset)

    _2_neighbor_subgraph1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/2_neighbor_subgraph_1'.format(dataset)
    _1_neighbor_subgraph1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/1_neighbor_subgraph_1'.format(dataset)
    _2_neighbor_subgraph2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/2_neighbor_subgraph_2'.format(dataset)
    _1_neighbor_subgraph2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/1_neighbor_subgraph_2'.format(dataset)

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
            '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/ent_ids_1'.format(dataset))
    id_ent_dict2 = get_id_entity_dict(
            '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/ent_ids_2'.format(dataset))
    return id_ent_dict1, id_ent_dict2
id_ent_dict1, id_ent_dict2 = get_id_ent_dict()


def get_candidates():
    ## 获取candidates文件
    entity_keys = [line.split('\t')[0].strip() for line in open(sematic_embedding_candidates_path).readlines()]
    cand_list_values = [line.split('\t')[1].strip().split(',') for line in
                        open(sematic_embedding_candidates_path).readlines()]
    candidates = dict(zip(entity_keys, cand_list_values))
    return candidates
candidates = get_candidates()

def get_Graph():
    """
    :return:
    """
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
    return G1, G2
G1, G2 = get_Graph()

def get_rel_dict():
    ##  获取relation of two nodes
    rel_1_dict = dict()
    rel_ids_1 = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/rel_ids_1'.format(dataset)
    with open(rel_ids_1) as f:
            for line in f.readlines():
                rel_1_dict.update({line.split('\t')[0]: line.split('\t')[1].strip()})

    rel_2_dict = dict()
    rel_ids_2 = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/rel_ids_2'.format(dataset)
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
        try:
            with open(subgraph_file, 'r') as f:
                for line in f.readlines():
                    edges.append((line.split(' ')[0], line.split(' ')[1].strip()))
            G = nx.DiGraph()
            G.add_edges_from(edges)
        except:

            if self.entity_type == 'target':
                newgraph_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/newgraph_1'.format(dataset)
            elif self.entity_type == 'candidate':
                newgraph_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/newgraph_2'.format(dataset)

            graph_edges_kg = read_graph(newgraph_path)
            kg = nx.Graph()
            kg.add_edges_from(graph_edges_kg)

            G = get_subgraph_within_k_per_node(kg, node, 2)

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
                Target Entity: {}

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

        return

def main():

    ent_id_1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1'.format(dataset)
    ent_id_2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_2_aligned'.format(dataset)

    entity_type = 'candidate'
    # entity_type = 'target'

    if entity_type == ('target'):
        ent_id_dict = get_ent_id_dict(ent_id_1_path)

    elif entity_type == 'candidate':
        ent_id_dict = get_ent_id_dict(ent_id_2_path)

    entity = """José Bové"""
    entity_id = ent_id_dict[entity]

    entity = Entity(entity, entity_id, entity_type)

    # _, _, prompts = entity.get_baseline_prompts()
    prompts = entity.get_only_motif_information()

    print(prompts)

if __name__ == '__main__':

    main()