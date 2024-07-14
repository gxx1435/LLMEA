import json
import os.path
import sys
import random
from run.utils import get_ent_id_dict, get_id_entity_dict
# from API_call_multithread import collect_response
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

def baseline():

    """
    generates all prompts list
    :return:
    """
    idx_entity_dict = read_idx_entity_file()
    idx_prompt_dict = {}
    i = 0
    for idx in idx_entity_dict.keys():
        entity_name = idx_entity_dict[idx]
        entity_id = idx
        entity_type = 'target'
        try:
                entity = Entity(entity_name, entity_id, entity_type)
                _, cand_list, prompt = entity.get_baseline_prompts()
        except:
                continue

        i += 1
        if i == threshold: break

        print(entity_name, cand_list)

        idx_prompt_dict.update({idx: prompt})

    with open('output/{}/idx_prompt_dict_baseline.json'.format(dataset), 'w') as f:
        json.dump(idx_prompt_dict, f, indent=4)

    return idx_prompt_dict

def get_baseline_responses(idx_prompt_dict):
    kwargs = {
        'max_tokens': 2000,
        'stop': None
    }
    message_list = [[{'role': 'user', 'content': prompt}] for prompt in idx_prompt_dict.values()]

    responses = collect_response(message_list, 'gpt_4_turbo', **kwargs)

    def get_output(s):
        start_idx = s.find('<output>')
        end_idx = s.find('</output>')
        output = s[start_idx+8: end_idx]
        return output

    responses = [get_output(response) for response in responses]

    responses_dict = dict(zip(idx_prompt_dict.keys(), responses))

    with open('output/{}/idx_prompt_dict_baseline_responses.json'.format(dataset), 'w') as f:
        json.dump(responses_dict, f, indent=4)

    return

def generate_message_lists(threshold):
    """
    generates all prompts list
    :return:
    """
    try:
        with open('output/{}/idx_prompt_dict_step_00.json'.format(dataset), 'r') as f:
            idx_prompt_dict = json.load(f)

        entity_list = []
        id_entity_dict = get_id_entity_dict(ent_id_1_path)
        for idx in idx_prompt_dict.keys():
            entity_type = 'target'
            entity = Entity(id_entity_dict[idx], idx, entity_type)
            entity_list.append(entity)

    except:
        idx_entity_dict = read_idx_entity_file()
        idx_prompt_dict = {}
        entity_list = []
        i = 0
        for idx in idx_entity_dict.keys():
            entity_name = idx_entity_dict[idx]
            entity_type = 'target'

            try:
                entity_id = idx
                entity = Entity(entity_name, entity_id, entity_type)
                _, cand_list, _ = entity.get_baseline_prompts()
            except:
                continue

            i += 1
            if i == threshold: break

            print(entity_name, cand_list)
            prompt = motif_ReAct_example_prompt.format(entity_name, cand_list, i=i)
            idx_prompt_dict.update({idx: prompt})
            entity_list.append(entity)

        with open('output/{}/idx_prompt_dict_step_00.json'.format(dataset), 'w') as f:
            json.dump(idx_prompt_dict, f, indent=4)

    return idx_prompt_dict, entity_list


def collect_response(message_list, model_name, num_threads = 10, **kwargs):
    """

    :return:
    """
    responses = []
    for i in range(len(message_list)):
        seed = random.random()
        if seed > 0.5:
            response = """
            Thought 1: xxxxxxxxxxxxxxxxxxx.
            Act 1: Request[Institutional Revolutionary Party] xxxxxxxxxxxxxxxxxxx.
            <code>
            xxxxxxxxxxxxxx
            xxxxxxxxxxxxxx
            </code>
            <output>None</output>
            """
        else:

            response = """
            Thought 1: xxxxxxxxxxxxxxxxxxx.
            Act 1: Terminate[Institutional Revolutionary Party] xxxxxxxxxxxxxxxxxxx.
            <code>
            xxxxxxxxxxxxxx
            xxxxxxxxxxxxxx
            </code>
            <output>None</output>
            """
        responses.append(
            response
        )
    return responses

def step(info_type, idx_prompt_dict, entity_list, step, idx):
    """
    :param dataset_file: idx entity file name
    :param info_type: 1_neighbor, text_motif, code_motif
    :return:
    """

    def find_thought_and_act(s):
        thought_idx = s.find('Thought')
        act_idx = s.find('Act')
        thought = s[thought_idx + 7: act_idx-1]
        act = s[act_idx + 3:-1]
        return 'Thought {}:'.format(idx)+thought + '\n'+"Act {}:".format(idx) + act

    def find_requests(s):
        start_idx = s.find('Request[')
        end_idx = s.find(']')
        if start_idx != -1:
            entity = s[start_idx + 8: end_idx]
            entity = entity.replace("'", '')
            return entity
        return -1

    def find_Terminate(s):
        if "'" in s:
            s = s.replace("'", '')
        start_idx = s.find('Terminate[')
        end_idx = s.find("]")
        ans = s[start_idx+10: end_idx]
        return ans

    def find_code(s):
        start_idx = s.find('<code>')
        end_idx = s.find("</code>")
        return s[start_idx+6: end_idx]

    try:
        with open('output/{}/final_answer_{}_{}.json'.format(dataset, info_type, step), 'r') as f:
            terminate_dict = json.load(f)

        with open('output/{}/idx_prompt_dict_{}_step_{}.json'.format(dataset, info_type, step), 'r') as f:
            new_idx_prompt_dict = json.load(f)

        new_entity_list = []
        id_entity_dict = get_id_entity_dict(ent_id_1_path)
        for idx in new_idx_prompt_dict.keys():
            entity_type = 'target'
            entity = Entity(id_entity_dict[idx], idx, entity_type)
            new_entity_list.append(entity)

    except:

        if not os.path.exists('output/{}/LLM_response_{}'.format(dataset, info_type)):
            os.mkdir('output/{}/LLM_response_{}'.format(dataset, info_type))

        kwargs = {
            'max_tokens': 2000,
            'stop': None
        }

        message_list = [[{'role': 'user', 'content': prompt}] for prompt in idx_prompt_dict.values()]

        responses = collect_response(message_list, 'gpt_4_turbo', **kwargs)
        with open('output/{}/LLM_response_{}/thought_and_acts_{}.json'.format(dataset,info_type, step), 'w') as f:
            json.dump(responses, f, indent=4)

        thought_and_acts = [find_thought_and_act(response) for response in responses]
        requests = [find_requests(thought_and_act) for thought_and_act in thought_and_acts]

        observations = {}
        code_motif_prompts = {}
        for i in range(len(entity_list)):
            entity_id = entity_list[i].entity_id
            if requests[i] != -1:
                request_entity = requests[i]

                if request_entity == entity_list[i].entity_name:
                    entity_type = 'target'
                else:
                    entity_type = 'candidate'

                if entity_type == 'target':
                    ent_id_dict = get_ent_id_dict(ent_id_1_path)
                elif entity_type == 'candidate':
                    ent_id_dict = get_ent_id_dict(ent_id_2_path)

                # try:
                request_entity_id = ent_id_dict[request_entity]
                request_entity = Entity(request_entity, request_entity_id, entity_type)
                # except:
                #     # introduce noise
                #     request_entity = Entity('Armenia', ent_id_dict['Armenia'], entity_type)

                if info_type == '1_neighbor':
                    _1_neighbor_info = request_entity.get_only_1_neighbor_information()
                    observations.update({entity_id: 'Observation {}: \n'.format(idx) + _1_neighbor_info})
                elif info_type == 'text_motif':
                    text_motif_info = request_entity.get_only_motif_information()
                    observations.update({entity_id: 'Observation {}: \n'.format(idx) + text_motif_info})
                elif info_type == 'code_motif':
                    text_motif_info = request_entity.get_only_motif_information()
                    code_motif_prompt = code_motif_prompts_generate.format(text_motif_info)
                    code_motif_prompts.update({entity_id: code_motif_prompt})


        if info_type == 'code_motif':

            kwargs = {
                'max_tokens': 2000,
                'stop': None
            }
            message_list = [[{'role': 'user', 'content': prompt}] for prompt in code_motif_prompts.values()]
            code_generated_responses = collect_response(message_list, 'gpt_4_turbo', **kwargs)

            with open('output/{}/LLM_response_{}/code_generated_{}.json'.format(dataset, info_type, step), 'w') as f:
                json.dump(code_generated_responses, f, indent=4)

            code_generated = ['Observation {}: \n'.format(idx) + find_code(code_response) for code_response in code_generated_responses]
            observations = dict(zip(code_motif_prompts.keys(), code_generated))


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

        with open('output/{}/final_answer_{}_{}.json'.format(dataset, info_type, step), 'w') as f:
            json.dump(terminate_dict, f, indent=4)

        with open('output/{}/idx_prompt_dict_{}_step_{}.json'.format(dataset, info_type, step), 'w') as f:
            json.dump(new_idx_prompt_dict, f, indent=4)


    return new_idx_prompt_dict, new_entity_list



if __name__ == '__main__':
    dataset = sys.argv[1]
    info_type = sys.argv[2]
    threshold = 300

    if not os.path.exists('output/{}'.format(dataset)):
        os.mkdir('output/{}'.format(dataset))

    ent_id_1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1'.format(dataset)
    ent_id_2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_2_aligned'.format(dataset)

    if info_type == 'baseline':
        idx_prompt_dict = baseline()
        get_baseline_responses(idx_prompt_dict)

    else:

        step0_idx_prompt_dict, step0_entity_list = generate_message_lists(threshold)

        step1_idx_prompt_dict, step1_entity_list = step(info_type, step0_idx_prompt_dict, step0_entity_list, '01', 1)
        step2_idx_prompt_dict, step2_entity_list = step(info_type, step1_idx_prompt_dict, step1_entity_list, '02', 2)
        step3_idx_prompt_dict, step3_entity_list = step(info_type, step2_idx_prompt_dict, step2_entity_list, '03', 3)
        step(info_type, step3_idx_prompt_dict, step3_entity_list, '04', 4)
