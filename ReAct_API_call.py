import json
import sys
from run.utils import get_ent_id_dict
from API_call_multithread import collect_response
from graph_motif_ReAct_v2 import motif_ReAct_example_prompt
from graph_motif_LLM import Entity
from graph_motif_prompt import code_motif_prompts_generate

def read_idx_entity_file():
    """
    :param dataset_file: idx entity corresponding file
    :return:
    """
    dataset_file = ent_id_1_path
    idx_entity_dict = {}
    with open(dataset_file) as f:
        for line in f.readlines():
            idx = line.split('\t')[0]
            entity = line.split('\t')[1].strip()
            idx_entity_dict.update({idx: entity})

    return  idx_entity_dict

def generate_message_lists():
    """
    generates all prompts list
    :return:
    """
    idx_entity_dict = read_idx_entity_file()
    idx_prompt_dict = {}
    entity_list = []
    for idx in idx_entity_dict.keys():
        entity_name = idx_entity_dict[idx]

        entity_type = 'target'

        if entity_type == ('target'):
            ent_id_dict = get_ent_id_dict(ent_id_1_path)
        elif entity_type == 'candidate':
            ent_id_dict = get_ent_id_dict(ent_id_2_path)

        entity_id = ent_id_dict[entity_name]
        entity = Entity(entity_name, entity_id, entity_type)
        entity_list.append(entity)

        _, cand_list, _ = entity.get_baseline_prompts()

        prompt = motif_ReAct_example_prompt.format(entity_name, cand_list)
        idx_prompt_dict.update({idx: prompt})

    with open('idx_prompt_dict_step_00.json', 'w') as f:
        json.dump(idx_prompt_dict, f)

    return idx_prompt_dict, entity_list

def step(info_type, idx_prompt_dict, entity_list, step):
    """
    :param dataset_file: idx entity file name
    :param info_type: 1_neighbor, text_motif, code_motif
    :return:
    """
    def find_thought_and_act(s):
        thought_idx = s.find('Thought')
        act_idx = s.find('Act')
        thought = s[thought_idx: act_idx-1]
        act = s[act_idx:-1]
        return thought + '\n' + act

    def find_requests(s):
        start_idx = s.find('Request[')
        end_idx = s.find(']')
        if start_idx != -1:
            return s[start_idx + 8: end_idx]
        return -1

    def find_Terminate(s):
        start_idx = s.find('Terminate[')
        end_idx = s.find("]")
        return s[start_idx+10: end_idx]

    def find_code(s):
        start_idx = s.find('<code>')
        end_idx = s.find("</code>")
        return s[start_idx+6: end_idx]


    responses = collect_response(idx_prompt_dict.values(), 'gpt-4-turbo')
    thought_and_acts = [find_thought_and_act(response) for response in responses]
    requests = [find_requests(thought_and_act) for thought_and_act in thought_and_acts]

    observations = {}
    code_motif_prompts = {}
    for i in range(len(entity_list)):
        entity_id = entity_list[i].entity_id
        if requests[i] != -1:
            request_entity = requests[i]

            entity_type = 'target'
            if entity_type == ('target'):
                ent_id_dict = get_ent_id_dict(ent_id_1_path)
            elif entity_type == 'candidate':
                ent_id_dict = get_ent_id_dict(ent_id_2_path)

            request_entity_id = ent_id_dict[request_entity]
            request_entity = Entity(request_entity, request_entity_id, entity_type)

            if info_type == '1_neighbor':
                _1_neighbor_info = request_entity.get_only_1_neighbor_information()
                observations.update({entity_id:_1_neighbor_info})
            elif info_type == 'text_motif':
                text_motif_info = request_entity.get_only_motif_information()
                observations.update({entity_id:text_motif_info})
            elif info_type == 'code_motif':
                text_motif_info = request_entity.get_only_motif_information()
                code_motif_prompt = code_motif_prompts_generate.format(text_motif_info)
                code_motif_prompts.update({entity_id:code_motif_prompt})


    if info_type == 'code_motif':
        code_generated_responses = collect_response(code_motif_prompts.values(), 'gpt-4-turbo')
        code_generated = [find_code(code_response) for code_response in code_generated_responses]
        observations = dict(zip(code_motif_prompts.keys(), code_generated))

    observations = [(idx, 'Observation 1: \n' + observation) for (idx, observation) in observations.items()]

    new_idx_prompt_dict = {}
    new_entity_list = []
    terminate_dict = {}
    for i in range(len(entity_list)):
        if requests[i] != -1:
            entity_id = entity_list[i].entity_id
            new_entity_list.append(entity_list[i])
            new_idx_prompt_dict.update({
                entity_id:
                    idx_prompt_dict[entity_id] + thought_and_acts[i] + observations[entity_id]
            })
        else:
            terminate_dict.update({entity_list[i].entity_name: find_Terminate(thought_and_acts[i])})

    with open('final_answer_{}.json'.format(step), 'w') as f:
        json.dump(terminate_dict, f)

    with open('idx_prompt_dict_step_{}.json'.format(step), 'w') as f:
        json.dump(new_idx_prompt_dict, f)

    return new_idx_prompt_dict, new_entity_list



if __name__ == '__main__':
    dataset = sys.argv[1]

    ent_id_1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1'.format(dataset)
    ent_id_2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_2_aligned'.format(dataset)

    step0_idx_prompt_dict, step0_entity_list = generate_message_lists()
    step1_idx_prompt_dict, step1_entity_list = step('text_motif', step0_idx_prompt_dict, step0_entity_list, '01')
    step2_idx_prompt_dict, step2_entity_list = step('text_motif', step1_idx_prompt_dict, step1_entity_list, '02')
    step3_idx_prompt_dict, step3_entity_list = step('text_motif', step2_idx_prompt_dict, step2_entity_list, '03')
    step('text_motif', step3_idx_prompt_dict, step3_entity_list, '04')
