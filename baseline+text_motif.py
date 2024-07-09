import sys

from graph_motif_LLM import Entity
from run.utils import get_ent_id_dict

if __name__ == '__main__':

    dataset = sys.argv[1]

    ent_id_1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1'.format(dataset)
    ent_id_2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_2_aligned'.format(dataset)

    entity_type = 'candidate'
    # entity_type = 'target'
    if entity_type == ('target'):
        ent_id_dict = get_ent_id_dict(ent_id_1_path)

    elif entity_type == 'candidate':
        ent_id_dict = get_ent_id_dict(ent_id_2_path)

    entity = """Institutional Revolutionary Party"""
    entity_id = ent_id_dict[entity]

    entity = Entity(entity, entity_id, entity_type)
    text_motif = entity.get_only_motif_information()

    print(text_motif)