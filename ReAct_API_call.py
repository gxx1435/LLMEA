import json
import re
import os.path
import sys
import random
import numpy as np
import argparse
from run.utils import get_ent_id_dict, get_id_entity_dict
# from API_bank_multi import collect_response
from graph_motif_ReAct_selecting import *
from graph_motif_ReAct_reranking import *
from graph_motif_ReAct_reranking_code import *
from graph_motif_ReAct_reranking_text import *


# def dynamic_import(module_name):
#     module = __import__(module_name)
#     return module


def read_idx_entity_file():
    """
    :param dataset_file: idx entity corresponding file
    :return:
    """
    dataset_file = ent_ids_1_path
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
    from entity import Entity

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

    if not os.path.exists('output/{}/{}/baseline'.format(LLM_type, save_dir)):
        os.mkdir('output/{}/{}/baseline'.format(LLM_type, save_dir))

    with open('output/{}/{}/baseline/idx_prompt_dict_baseline.json'.format(LLM_type, save_dir), 'w') as f:
        json.dump(idx_prompt_dict, f, indent=4)

    return idx_prompt_dict

def get_baseline_responses(idx_prompt_dict):
    kwargs = {
        'max_tokens': 2000,
        'stop': None
    }
    message_list = [[{'role': 'user', 'content': prompt}] for prompt in idx_prompt_dict.values()]

    responses = collect_response(message_list, LLM_type, **kwargs)

    def get_output(s):
        start_idx = s.find('<output>')
        end_idx = s.find('</output>')
        output = s[start_idx+8: end_idx]
        return output

    def find_most_list(s):
        # start_idx = s.find('<most>')
        # end_idx = s.find('</msot>')
        # return s[start_idx+6: end_idx]

        # 正则表达式模式，匹配 <most> 和 </most> 标签之间的内容
        pattern = r'<MOST>(.*?)</MOST>'
        # 使用 re.findall() 提取所有匹配的内容
        matches = re.search(pattern, s)
        if matches:
            return matches.group(1)

        return -1

    def find_most_list_llama(text):
        match = re.search(r"Most\[(.*?)\]", text)

        if match:
            extracted_list = match.group(1).encode().decode('unicode_escape')
            extracted_list = eval('['+extracted_list+']')

            return extracted_list
        else:
            return -1

    responses = [response for response in responses]

    responses_dict = dict(zip(idx_prompt_dict.keys(), responses))

    with open('output/{}/{}/baseline/idx_prompt_dict_baseline_responses.json'.format(LLM_type,save_dir), 'w') as f:
        json.dump(responses_dict, f, indent=4)

    final_anses = []
    most_lists = []


    for key in responses_dict.keys():

            ans = get_output(responses_dict[key])

            if 'llama' in LLM_type:
                wordlist = find_most_list_llama(responses_dict[key])
            else:
                wordlist = find_most_list(responses_dict[key])

            wordlist = wordlist.split(',')
            wordlist[0] = wordlist[0][1:]
            wordlist[-1] = wordlist[-1][:-1]
            final_anses.append(ans)
            most_lists.append(wordlist)

    idx_ent1_dict = get_id_entity_dict(ent_ids_1_path)
    final_ans_dict = dict(zip([idx_ent1_dict[key] for key in idx_prompt_dict.keys()], final_anses))
    most_list_dict = dict(zip([idx_ent1_dict[key] for key in idx_prompt_dict.keys()], most_lists))

    with open('output/{}/{}/baseline/idx_prompt_dict_baseline_final_ans.json'.format(LLM_type, save_dir), 'w') as f:
        json.dump(final_ans_dict, f, indent=4)

    with open('output/{}/{}/baseline/idx_prompt_dict_baseline_most_list.json'.format(LLM_type, save_dir), 'w') as f:
        json.dump(most_list_dict, f, indent=4)

    return

def generate_message_lists(threshold):
    """
    generates all prompts list
    :return:
    """
    from entity import Entity
    try:
        with open('output/{}/{}/idx_prompt_dict_step_00.json'.format(LLM_type, save_dir), 'r') as f:
            idx_prompt_dict = json.load(f)

        entity_list = []
        id_entity_dict = get_id_entity_dict(ent_ids_1_path)
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
            # if 'code_motif' in info_type:
            #
            #     prompt = motif_ReAct_example_prompt_code.format(entity_name, cand_list, i=i)
            #
            # elif 'text_motif' in info_type:
            #
            #     prompt = motif_ReAct_example_prompt_text.format(entity_name, cand_list, i=i)
            #
            # else:

            prompt = motif_ReAct_example_prompt.format(entity_name, cand_list, i=i)

            idx_prompt_dict.update({idx: prompt})
            entity_list.append(entity)

        with open('output/{}/{}/idx_prompt_dict_step_00.json'.format(LLM_type, save_dir), 'w') as f:
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
            Act 1: Terminate['Institutional Revolutionary Party'] xxxxxxxxxxxxxxxxxxx.
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
    from entity import Entity
    if if_expel:
        from graph_motif_code_generated_expel_version import code_motif_prompts_generate
    else:
        from graph_motif_code_generated import code_motif_prompts_generate

    def find_thought_and_act(s):
        thought_idx = s.find('Thought')
        act_idx = s.find('Act')
        thought = s[thought_idx + 7: act_idx-1]
        act = s[act_idx + 3:-1]
        return 'Thought {}:'.format(idx)+thought + '\n'+"Act {}:".format(idx) + act

    def find_requests(s):
        # start_idx = s.find('Request[')
        # end_idx = s.find(']')
        # if start_idx != -1:
        #     entity = s[start_idx + 8: end_idx]
        #     return entity
        def extract_target_entity(text):
            # 优先匹配带单引号的目标实体
            pattern_single_quote = r"Request\['(.*?)'\]"
            match_single_quote = re.search(pattern_single_quote, text)

            if match_single_quote:
                return match_single_quote.group(1)

            # 如果没有匹配到带单引号的目标实体，则匹配不带引号的目标实体
            pattern_no_quote = r"Request\[(.*?)\]"
            match_no_quote = re.search(pattern_no_quote, text)

            if match_no_quote:
                return match_no_quote.group(1)

            return -1

        return extract_target_entity(s)

    def find_Terminate(s):
        def extract_target_entity(text):
            # 优先匹配带单引号的目标实体
            pattern_single_quote = r"Terminate\['(.*?)'\]"
            match_single_quote = re.search(pattern_single_quote, text)

            if match_single_quote:
                return match_single_quote.group(1)

            # 如果没有匹配到带单引号的目标实体，则匹配不带引号的目标实体
            pattern_no_quote = r"Terminate\[(.*?)\]"
            match_no_quote = re.search(pattern_no_quote, text)

            if match_no_quote:
                return match_no_quote.group(1)

            return -1

        # start_idx = s.find('Terminate[')
        # end_idx = s.find("]")
        # ans = s[start_idx+10: end_idx]

        return extract_target_entity(s)

    def find_most_list(s):
        # start_idx = s.find('<most>')
        # end_idx = s.find('</msot>')
        # return s[start_idx+6: end_idx]

        # 正则表达式模式，匹配 <most> 和 </most> 标签之间的内容
        pattern = r'<MOST>(.*?)</MOST>'
        # 使用 re.findall() 提取所有匹配的内容
        matches = re.search(pattern, s)
        if matches:
            return matches.group(1)

        return -1

    def find_most_list_llama(text):
        match = re.search(r"Most\[(.*?)\]", text)

        if match:
            extracted_list = match.group(1).encode().decode('unicode_escape')
            extracted_list = eval('[' + extracted_list + ']')

            return extracted_list
        else:
            return -1

    def find_code(s):
        start_idx = s.find('<code>')
        end_idx = s.find("</code>")
        if start_idx != -1:
            return s[start_idx+6: end_idx]

        start_idx = s.find('<CODE>')
        end_idx = s.find("</CODE>")
        if start_idx != -1:
            return s[start_idx+6: end_idx]

        start_idx = s.find('python')
        if start_idx != -1:
            return s[start_idx+6: -1]

        return 'no code observation for this entity.'

        # # 正则表达式模式，匹配 <code> 和 </code> 标签之间的内容
        # pattern = r'<code>(.*?)</code>'
        # # 使用 re.findall() 提取所有匹配的内容
        # matches = re.search(pattern, s)
        # print(s, matches)
        # if matches:
        #     return matches.group(1)
        #
        # return 'no code observation for this entity.'

    try:
        with open('output/{}/{}/LLM_response_{}/thought_and_acts_{}.json'.format(LLM_type, save_dir, info_type, step), 'r') as f:
            thought_and_acts = json.load(f)

        with open('output/{}/{}/LLM_response_{}/requests_{}.json'.format(LLM_type,save_dir, info_type, step), 'r') as f:
            requests = json.load(f)

        with open('output/{}/{}/LLM_response_{}/observations_{}.json'.format(LLM_type, save_dir, info_type, step),
                  'w') as f:
            observations = json.load(f)

        with open('output/{}/{}/most_list_{}_{}.json'.format(LLM_type, save_dir, info_type, step), 'r') as f:
            most_list_dict = json.load(f)

        with open('output/{}/{}/final_answer_{}_{}.json'.format(LLM_type, save_dir, info_type, step), 'r') as f:
            terminate_dict = json.load(f)

        with open('output/{}/{}/idx_prompt_dict_{}_step_{}.json'.format(LLM_type, save_dir, info_type, step), 'r') as f:
            new_idx_prompt_dict = json.load(f)

        # new_idx_prompt_dict = {}
        # for i, idx in enumerate(idx_prompt_dict.keys()):
        #     if requests[i] != -1:
        #         new_idx_prompt_dict.update({idx: idx_prompt_dict[idx]+thoughts_and_acts[i] +'Observation {}: No obersvation.\n'.format(step)})


        new_entity_list = []
        id_entity_dict = get_id_entity_dict(ent_ids_1_path)
        for idx in new_idx_prompt_dict.keys():
            entity_type = 'target'
            entity = Entity(id_entity_dict[idx], idx, entity_type)
            new_entity_list.append(entity)

    except:

        if not os.path.exists('output/{}/{}/LLM_response_{}'.format(LLM_type, save_dir, info_type)):
            os.mkdir('output/{}/{}/LLM_response_{}'.format(LLM_type, save_dir, info_type))

        kwargs = {
            'max_tokens': 2000,
            'stop': None
        }

        message_list = [[{'role': 'user', 'content': prompt}] for prompt in idx_prompt_dict.values()]


        if step == '1':

            if os.path.exists('output/{}/{}/thought_and_acts_{}.json'.format(LLM_type, dataset+"_"+first_step_setting,  step)):

                with open('output/{}/{}/thought_and_acts_{}.json'.format(LLM_type, dataset+"_"+first_step_setting, step)) as f:
                    thought_and_acts = json.load(f)

                with open('output/{}/{}/requests_{}.json'.format(LLM_type, dataset+"_"+first_step_setting, step)) as f:
                    requests = json.load(f)

            else:
                responses = collect_response(message_list, LLM_type, **kwargs)
                thought_and_acts = [response for response in responses]
                thought_and_acts = dict(zip(idx_prompt_dict.keys(), thought_and_acts))

                with open('output/{}/{}/thought_and_acts_{}.json'.format(LLM_type, dataset+"_"+first_step_setting, step),
                          'w') as f:
                    json.dump(thought_and_acts, f, indent=4)

                requests = [find_requests(response) for response in responses]
                with open('output/{}/{}/requests_{}.json'.format(LLM_type, dataset+"_"+first_step_setting, step), 'w') as f:
                    json.dump(requests, f, indent=4)

        else:

            if os.path.exists('output/{}/{}/LLM_response_{}/thought_and_acts_{}.json'.format(LLM_type, save_dir, info_type, step)):
                with open('output/{}/{}/LLM_response_{}/thought_and_acts_{}.json'.format(LLM_type, save_dir, info_type, step)) as f:
                    thought_and_acts = json.load(f)

                with open('output/{}/{}/LLM_response_{}/requests_{}.json'.format(LLM_type, save_dir, info_type, step)) as f:
                    requests = json.load(f)

            else:

                responses = collect_response(message_list, LLM_type, **kwargs)
                thought_and_acts = [response for response in responses]
                thought_and_acts = dict(zip(idx_prompt_dict.keys(), thought_and_acts))

                with open('output/{}/{}/LLM_response_{}/thought_and_acts_{}.json'.format(LLM_type, save_dir, info_type, step), 'w') as f:
                    json.dump(thought_and_acts, f, indent=4)

                requests = [find_requests(response) for response in responses]
                with open('output/{}/{}/LLM_response_{}/requests_{}.json'.format(LLM_type, save_dir, info_type, step), 'w') as f:
                    json.dump(requests, f, indent=4)


        observations = {}
        code_motif_prompts = {}
        for i in range(len(entity_list)):
            entity_id = entity_list[i].entity_id
            if requests[i] != -1:
                request_entity = requests[i]

                if "\"" in request_entity[0] and "\"" in request_entity[-1]:
                    request_entity = request_entity[1:-1]

                elif "'" in request_entity[0] and "'" in request_entity[-1]:
                    request_entity = request_entity[1:-1]

                if (request_entity == entity_list[i].entity_name
                        or request_entity.lower() == entity_list[i].entity_name.lower()):
                    entity_type = 'target'
                else:
                    entity_type = 'candidate'

                ent_id_dict = {}
                if entity_type == 'target':
                    ent_id_dict = get_ent_id_dict(ent_ids_1_path)
                elif entity_type == 'candidate':
                    ent_id_dict = get_ent_id_dict(ent_ids_2_path)

                if 'entity:' in request_entity:
                    request_entity = request_entity.split(":")[1].strip()

                print(request_entity, entity_list[i].entity_name, entity_type)
                try:
                    if entity_type == 'target':
                        request_entity_id = ent_id_dict[entity_list[i].entity_name]
                    else:
                        request_entity_id = ent_id_dict[request_entity]

                    request_entity = Entity(request_entity, request_entity_id, entity_type)
                except:
                    # introduce noise
                    request_entity = Entity(entity_list[i].entity_name,
                                            entity_list[i].entity_id,
                                            'target')

                if info_type == '1_neighbor':

                    _1_neighbor_info = request_entity.get_only_1_neighbor_information(if_triple=1, info_type=info_type, if_keep_top_n=1)
                    print(_1_neighbor_info)
                    observations.update({entity_id: 'Observation {}: \n'.format(step) + _1_neighbor_info})

                elif info_type == 'text_motif_lite':

                    text_motif_info = request_entity.get_only_triangle_information(if_triple=1, info_type=info_type, top_n=top_n, if_keep_top_n=0)
                    print(text_motif_info)
                    observations.update({entity_id: 'Observation {}: \n'.format(step) + text_motif_info})

                elif info_type == 'code_motif_lite':

                    text_motif_info = request_entity.get_only_triangle_information(if_triple=1, info_type=info_type, top_n=top_n, if_keep_top_n=1)
                    print(text_motif_info)

                    if if_expel:
                        with open(os.getcwd() + '/output/code_generated_rules.txt') as f:
                            code_generated_rules = json.load(f)
                            rule = code_generated_rules[-1]
                        code_motif_prompt = code_motif_prompts_generate.format(rule, text_motif_info)
                    else:
                        code_motif_prompt = code_motif_prompts_generate.format(text_motif_info)

                    code_motif_prompts.update({entity_id: code_motif_prompt})

                elif info_type == 'text_motif_base':

                    """To do"""
                    text_motif_info = request_entity.get_dynamic_motifs_information(if_triple=1, info_type=info_type, top_n=top_n, if_keep_top_n=0)
                    print(text_motif_info)
                    observations.update({entity_id: 'Observation {}: \n'.format(step) + text_motif_info})

                elif info_type == 'code_motif_base':

                    """To do"""
                    text_motif_info = request_entity.get_dynamic_motifs_information(if_triple=1, info_type=info_type, top_n=top_n, if_keep_top_n=1)
                    print(text_motif_info)

                    if if_expel:
                        with open(os.getcwd() + '/output/code_generated_rules.txt') as f:
                            code_generated_rules = json.load(f)
                            rule = code_generated_rules[-1]
                        code_motif_prompt = code_motif_prompts_generate.format(rule, text_motif_info)
                    else:
                        code_motif_prompt = code_motif_prompts_generate.format(text_motif_info)

                    code_motif_prompts.update({entity_id: code_motif_prompt})


        if 'code_motif' in info_type:

            with open('output/{}/{}/LLM_response_{}/code_motif_prompts_{}.json'.format(LLM_type, save_dir, info_type, step), 'w') as f:
                json.dump(code_motif_prompts, f, indent=4)

            kwargs = {
                'max_tokens': 2000,
                'stop': None
            }
            message_list = [[{'role': 'user', 'content': prompt}] for prompt in code_motif_prompts.values()]

            if os.path.exists('output/{}/{}/LLM_response_{}/code_generated_{}.json'.format(LLM_type, save_dir, info_type, step)):
                with open('output/{}/{}/LLM_response_{}/code_generated_{}.json'.format(LLM_type, save_dir, info_type, step)) as f:

                    code_generated_responses = json.load(f)

            else:
                code_generated_responses = collect_response(message_list, LLM_type, **kwargs)
                # code_generated_responses = dict(zip(code_motif_prompts.keys(), code_generated_responses))

                with open('output/{}/{}/LLM_response_{}/code_generated_{}.json'.format(LLM_type, save_dir, info_type, step), 'w') as f:

                    json.dump(code_generated_responses, f, indent=4)

            code_generated = ['Observation {}: The background information of the entity is below which is given in code format motifs: \n'.format(step) + find_code(code_response) for code_response in code_generated_responses]

            with open('output/{}/{}/LLM_response_{}/code_{}.json'.format(LLM_type, save_dir, info_type, step), 'w') as f:
                json.dump(code_generated, f, indent=4)

            observations = dict(zip(code_motif_prompts.keys(), code_generated))

            with open('output/{}/{}/LLM_response_{}/observations_{}.json'.format(LLM_type,save_dir, info_type, step), 'w') as f:
                json.dump(observations, f, indent=4)
        else:

            with open('output/{}/{}/LLM_response_{}/observations_{}.json'.format(LLM_type, save_dir, info_type, step), 'w') as f:
                json.dump(observations, f, indent=4)

        new_idx_prompt_dict = {}
        new_entity_list = []
        terminate_dict = {}
        most_list_dict = {}
        for i in range(len(entity_list)):
            entity_id = entity_list[i].entity_id
            if requests[i] != -1:
                new_entity_list.append(entity_list[i])
                new_idx_prompt_dict.update({
                    entity_id:
                        idx_prompt_dict[entity_id] + thought_and_acts[entity_id] + observations[entity_id]
                })
            else:
                if 'llama' in info_type:
                    most_list_dict.update({entity_list[i].entity_name: find_most_list_llama(thought_and_acts[entity_id])})
                else:
                    most_list_dict.update({entity_list[i].entity_name: find_most_list(thought_and_acts[entity_id])})

                terminate_dict.update({entity_list[i].entity_name: find_Terminate(thought_and_acts[entity_id])})

        with open('output/{}/{}/most_list_{}_{}.json'.format(LLM_type, save_dir, info_type, step), 'w') as f:
            json.dump(most_list_dict, f, indent=4)

        with open('output/{}/{}/final_answer_{}_{}.json'.format(LLM_type, save_dir, info_type, step), 'w') as f:
            json.dump(terminate_dict, f, indent=4)

        with open('output/{}/{}/idx_prompt_dict_{}_step_{}.json'.format(LLM_type, save_dir, info_type, step), 'w') as f:
            json.dump(new_idx_prompt_dict, f, indent=4)


    return new_idx_prompt_dict, new_entity_list

# 创建 ArgumentParser 对象
parser = argparse.ArgumentParser(description="It's a test")

parser.add_argument('-d', '--dataset', type=str, help='dataset name')

parser.add_argument('-i', '--info_type', type=str, help='code_motif,text_motif,1_neighbor')

parser.add_argument('-l', '--llm_type', type=str, help='LLM type')

parser.add_argument('-t', '--threshold', type=int, default=300, help='阈值')

parser.add_argument('-r', '--react_file', type=str, default='graph_motif_ReAct_v4_100_50candidates_tmp2', help='ReAct File')

parser.add_argument('-s', '--sematic_embedding_candidates_path', type=str, help='semantic cadidate path')

parser.add_argument('-cn1', '--candidate_num_1', type=int, help='candidate number of target entity in start')

parser.add_argument('-cn2', '--candidate_num_2', type=int, help='candidate number of target entity in the answer')

parser.add_argument('-ent1', '--ent_ids_1', type=str, help='ent ids 1 file')

parser.add_argument('-ent2', '--ent_ids_2', type=str, help='ent ids 2 file')

parser.add_argument('-top_n', '--top_n', type=int, help='How much motif we output')

parser.add_argument('-v', '--version', default='', type=str, help='version control')

parser.add_argument('-e', '--expel', default=False, type=bool, help='If use expel mudule')



# # 添加可选参数（带默认值）
# parser.add_argument('-n', '--number', type=int, default=42, help='要处理的数字')

# 解析参数
args = parser.parse_args()

dataset = args.dataset
info_type = args.info_type
LLM_type = args.llm_type
threshold = args.threshold
top_n = args.top_n
version = args.version
if_expel = args.expel
# module_name = args.react_file
# ReAct_module = dynamic_import(module_name)
# motif_ReAct_example_prompt = ReAct_module.motif_ReAct_example_prompt

# if args.candidate_num_1 == 100 and args.candidate_num_2 == 50:
#
#     motif_ReAct_example_prompt = motif_ReAct_example_prompt_cn100_cn50
#
# elif args.candidate_num_1 == 100 and args.candidate_num_2 == 40:
#
#     motif_ReAct_example_prompt = motif_ReAct_example_prompt_cn100_cn40
#
# elif args.candidate_num_1 == 100 and args.candidate_num_2 == 30:
#
#     motif_ReAct_example_prompt = motif_ReAct_example_prompt_cn100_cn30
#
# elif args.candidate_num_1 == 100 and args.candidate_num_2 == 20:
#
#     motif_ReAct_example_prompt = motif_ReAct_example_prompt_cn100_cn20
#
# elif args.candidate_num_1 == 100 and args.candidate_num_2 == 10:
#
#     motif_ReAct_example_prompt = motif_ReAct_example_prompt_cn100_cn10

if args.candidate_num_1 == 10 and args.candidate_num_2 == 10:

    motif_ReAct_example_prompt = motif_ReAct_example_prompt_cn10_cn10
    motif_ReAct_example_prompt_code = motif_ReAct_example_prompt_cn10_cn10_code
    motif_ReAct_example_prompt_text = motif_ReAct_example_prompt_cn10_cn10_text

elif args.candidate_num_1 == 20 and args.candidate_num_2 == 20:

    motif_ReAct_example_prompt = motif_ReAct_example_prompt_cn20_cn20
    motif_ReAct_example_prompt_code = motif_ReAct_example_prompt_cn20_cn20_code
    motif_ReAct_example_prompt_text = motif_ReAct_example_prompt_cn20_cn20_text

elif args.candidate_num_1 == 50 and args.candidate_num_2 == 50:
    if 'llama' in LLM_type:
        motif_ReAct_example_prompt = motif_ReAct_example_prompt_cn50_cn50_llama
    else:
        if version == 'v0':
            motif_ReAct_example_prompt = motif_ReAct_example_prompt_cn50_cn50_v0
        elif version == 'v1':
            motif_ReAct_example_prompt = motif_ReAct_example_prompt_cn50_cn50_v1
        else:
            motif_ReAct_example_prompt = motif_ReAct_example_prompt_cn50_cn50

        motif_ReAct_example_prompt_code = motif_ReAct_example_prompt_cn50_cn50_code
        motif_ReAct_example_prompt_text = motif_ReAct_example_prompt_cn50_cn50_text

elif args.candidate_num_1 == 70 and args.candidate_num_2 == 70:

    motif_ReAct_example_prompt = motif_ReAct_example_prompt_cn70_cn70
    motif_ReAct_example_prompt_code = motif_ReAct_example_prompt_cn70_cn70_code
    motif_ReAct_example_prompt_text = motif_ReAct_example_prompt_cn70_cn70_text

elif args.candidate_num_1 == 100 and args.candidate_num_2 == 100:

    motif_ReAct_example_prompt = motif_ReAct_example_prompt_cn100_cn100
    motif_ReAct_example_prompt_code = motif_ReAct_example_prompt_cn100_cn100_code
    motif_ReAct_example_prompt_text = motif_ReAct_example_prompt_cn100_cn100_text

elif args.candidate_num_1 == 200 and args.candidate_num_2 == 200:

    motif_ReAct_example_prompt = motif_ReAct_example_prompt_cn200_cn200
    motif_ReAct_example_prompt_code = motif_ReAct_example_prompt_cn200_cn200_code
    motif_ReAct_example_prompt_text = motif_ReAct_example_prompt_cn200_cn200_text

sematic_embedding_candidates_path = args.sematic_embedding_candidates_path
if 'orginal_ranking' in sematic_embedding_candidates_path:
    first_step_setting = 'original'
elif 'put_correct_ans_last' in sematic_embedding_candidates_path:
    first_step_setting = 'corrected'

candidate_num_1 = str(args.candidate_num_1)
candifate_num_2 = str(args.candidate_num_2)

ent_ids_1 = args.ent_ids_1
ent_ids_2 = args.ent_ids_2
current_path = os.getcwd()
ent_ids_1_path = current_path + '/data/{}/{}'.format(dataset, ent_ids_1)
ent_ids_2_path = current_path + '/data/{}/{}'.format(dataset, ent_ids_2)

if version != '':
    save_dir = dataset+"_"+'t'+str(threshold)+'_'+candidate_num_1+"_"+candifate_num_2+'_' + first_step_setting+"_{}motif".format(top_n)+"_" + version
else:
    save_dir = dataset+"_"+'t'+str(threshold)+'_'+candidate_num_1+"_"+candifate_num_2+'_' + first_step_setting+"_{}motif".format(top_n)

if __name__ == '__main__':

    if not os.path.exists(current_path +'/output/{}'.format(dataset)):
        os.mkdir(current_path +'/output/{}'.format(dataset))

    if not os.path.exists(current_path +'/output/{}'.format(LLM_type)):
        os.mkdir(current_path +'/output/{}'.format(LLM_type))

    if not os.path.exists(current_path +'/output/{}/{}'.format(LLM_type, first_step_setting)):
        os.mkdir(current_path +'/output/{}/{}'.format(LLM_type, first_step_setting))

    if not os.path.exists(current_path+ '/output/{}/{}'.format(LLM_type, save_dir)):
        os.mkdir(current_path+'/output/{}/{}'.format(LLM_type, save_dir))

    if info_type == 'baseline':
        idx_prompt_dict = baseline()
        get_baseline_responses(idx_prompt_dict)

    else:

        step0_idx_prompt_dict, step0_entity_list = generate_message_lists(threshold)

        step1_idx_prompt_dict, step1_entity_list = step(info_type, step0_idx_prompt_dict, step0_entity_list, '1', 1)
        step2_idx_prompt_dict, step2_entity_list = step(info_type, step1_idx_prompt_dict, step1_entity_list, '2', 2)
        step3_idx_prompt_dict, step3_entity_list = step(info_type, step2_idx_prompt_dict, step2_entity_list, '3', 3)
        step(info_type, step3_idx_prompt_dict, step3_entity_list, '4', 4)
