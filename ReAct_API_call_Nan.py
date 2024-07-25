import json
import re
import os.path
import sys
import random
import numpy as np
import argparse
from run.utils import get_ent_id_dict, get_id_entity_dict
# from API_bank_multi import collect_response
# from graph_motif_ReAct_v4_100_50candidates_tmp2 import motif_ReAct_example_prompt
from graph_motif_prompt import code_motif_prompts_generate


def dynamic_import(module_name):
    module = __import__(module_name)
    return module

def hit_1_10_rate(final_anwser_file, type='hit1'):
    """
    :param final_anwser_file:
    :param type:
    :return:
    """
    dataset = 'icews_yago'
    ent_id_1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1'.format(dataset)
    ent_id_2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_2_aligned'.format(dataset)

    ent_ids_1 = []
    with open(ent_id_1_path, 'r') as f:
        for line in f.readlines():
            ent_ids_1.append(line.split('\t')[1].strip())

    ent_ids_2_aligned = []
    with open(ent_id_2_path, 'r') as f:
        for line in f.readlines():
            ent_ids_2_aligned.append(line.split('\t')[1].strip())

    ent_ids_12_dict = dict(zip(ent_ids_1, ent_ids_2_aligned))
    print(ent_ids_12_dict)

    hit1 = 0
    hit10 = 0
    with open(final_anwser_file, 'r') as f:
        final_answer = json.load(f)
        for key in final_answer.keys():


            if type == 'hit1':
                if final_answer[key] == ent_ids_12_dict[key]:
                    hit1 += 1
            elif type == 'hit10':
                if ent_ids_12_dict[key] in final_answer[key]:
                    hit10 += 1

    return float(hit1/len(final_answer)) if type == 'hit1' else float(hit10/len(final_answer))


def mean_reciprocal_rank(final_ranks):
    """
    计算Mean Reciprocal Rank (MRR)

    参数:
    final_ranks (list): 每个查询的第一个相关结果的排名的列表

    返回:
    float: 平均MRR值
    """
    mrrs = []
    for ranks in final_ranks:

        reciprocal_ranks = [1.0 / rank for rank in ranks]

        mrr = sum(reciprocal_ranks) / len(ranks)
        mrrs.append(mrr)
    return np.mean(mrrs)

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

    with open('output/{}/idx_prompt_dict_baseline.json'.format(save_dir), 'w') as f:
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

    responses = [get_output(response) for response in responses]

    responses_dict = dict(zip(idx_prompt_dict.keys(), responses))

    with open('output/{}/idx_prompt_dict_baseline_responses.json'.format(save_dir), 'w') as f:
        json.dump(responses_dict, f, indent=4)

    return

def generate_message_lists(threshold):
    """
    generates all prompts list
    :return:
    """
    from entity import Entity
    try:
        with open('output/{}/idx_prompt_dict_step_00.json'.format(save_dir), 'r') as f:
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

        with open('output/{}/idx_prompt_dict_step_00.json'.format(save_dir), 'w') as f:
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
        pattern = r'<most>(.*?)</most>'
        # 使用 re.findall() 提取所有匹配的内容
        matches = re.search(pattern, s)
        if matches:
            return matches.group(1)

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
        with open('output/{}/LLM_response_{}/thought_and_acts_{}.json'.format(save_dir, info_type, step), 'r') as f:
            thought_and_acts = json.load(f)

        with open('output/{}/LLM_response_{}/requests_{}.json'.format(save_dir, info_type, step), 'r') as f:
            requests = json.load(f)

        with open('output/{}/most_list_{}_{}.json'.format(save_dir, info_type, step), 'r') as f:
            most_list_dict = json.load(f)

        with open('output/{}/final_answer_{}_{}.json'.format(save_dir, info_type, step), 'r') as f:
            terminate_dict = json.load(f)

        with open('output/{}/idx_prompt_dict_{}_step_{}.json'.format(save_dir, info_type, step), 'r') as f:
            new_idx_prompt_dict = json.load(f)

        # new_idx_prompt_dict = {}
        # for i, idx in enumerate(idx_prompt_dict.keys()):
        #     if requests[i] != -1:
        #         new_idx_prompt_dict.update({idx: idx_prompt_dict[idx]+thoughts_and_acts[i] +'Observation {}: No obersvation.\n'.format(step)})


        new_entity_list = []
        id_entity_dict = get_id_entity_dict(ent_id_1_path)
        for idx in new_idx_prompt_dict.keys():
            entity_type = 'target'
            entity = Entity(id_entity_dict[idx], idx, entity_type)
            new_entity_list.append(entity)

    except:

        if not os.path.exists('output/{}/LLM_response_{}'.format(save_dir, info_type)):
            os.mkdir('output/{}/LLM_response_{}'.format(save_dir, info_type))

        kwargs = {
            'max_tokens': 2000,
            'stop': None
        }

        message_list = [[{'role': 'user', 'content': prompt}] for prompt in idx_prompt_dict.values()]

        if os.path.exists('output/{}/LLM_response_{}/thought_and_acts_{}.json'.format(save_dir, info_type, step)):
            with open('output/{}/LLM_response_{}/thought_and_acts_{}.json'.format(save_dir, info_type, step)) as f:
                thought_and_acts = json.load(f)

            with open('output/{}/LLM_response_{}/requests_{}.json'.format(save_dir, info_type, step)) as f:
                requests = json.load(f)

        else:
            responses = collect_response(message_list, LLM_type, **kwargs)
            thought_and_acts = [response for response in responses]

            with open('output/{}/LLM_response_{}/thought_and_acts_{}.json'.format(save_dir, info_type, step), 'w') as f:
                json.dump(thought_and_acts, f, indent=4)

            requests = [find_requests(response) for response in responses]
            with open('output/{}/LLM_response_{}/requests_{}.json'.format(save_dir, info_type, step), 'w') as f:
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
                    ent_id_dict = get_ent_id_dict(ent_id_1_path)
                elif entity_type == 'candidate':
                    ent_id_dict = get_ent_id_dict(ent_id_2_path)

                print(request_entity, entity_list[i].entity_name, entity_type)
                # try:
                if entity_type == 'target':
                    request_entity_id = ent_id_dict[entity_list[i].entity_name]
                else:
                    request_entity_id = ent_id_dict[request_entity]

                request_entity = Entity(request_entity, request_entity_id, entity_type)
                # except:
                #     # introduce noise
                #     request_entity = Entity('Armenia', ent_id_dict['Armenia'], entity_type)

                if info_type == '1_neighbor':

                    _1_neighbor_info = request_entity.get_only_1_neighbor_information()
                    observations.update({entity_id: 'Observation {}: \n'.format(step) + _1_neighbor_info})

                elif info_type == 'text_motif_lite':

                    text_motif_info = request_entity.get_only_triangle_information()
                    observations.update({entity_id: 'Observation {}: \n'.format(step) + text_motif_info})

                elif info_type == 'code_motif_lite':

                    text_motif_info = request_entity.get_dynamic_motifs_information()
                    print(text_motif_info)
                    code_motif_prompt = code_motif_prompts_generate.format(text_motif_info)
                    code_motif_prompts.update({entity_id: code_motif_prompt})

                elif info_type == 'text_motif_base':
                    """To do"""

                elif info_type == 'code_motif_lite':
                    """To do"""


        if 'code_motif' in info_type:

            kwargs = {
                'max_tokens': 2000,
                'stop': None
            }
            message_list = [[{'role': 'user', 'content': prompt}] for prompt in code_motif_prompts.values()]

            if os.path.exists('output/{}/LLM_response_{}/code_generated_{}.json'.format(save_dir, info_type, step)):
                with open('output/{}/LLM_response_{}/code_generated_{}.json'.format(save_dir, info_type, step)) as f:

                    code_generated_responses = json.load(f)

            else:
                code_generated_responses = collect_response(message_list, LLM_type, **kwargs)

                with open('output/{}/LLM_response_{}/code_generated_{}.json'.format(save_dir, info_type, step), 'w') as f:

                    json.dump(code_generated_responses, f, indent=4)

            code_generated = ['Observation {}: \n'.format(step) + find_code(code_response) for code_response in code_generated_responses]

            with open('output/{}/LLM_response_{}/code_{}.json'.format(save_dir, info_type, step), 'w') as f:
                json.dump(code_generated, f, indent=4)
            observations = dict(zip(code_motif_prompts.keys(), code_generated))


        new_idx_prompt_dict = {}
        new_entity_list = []
        terminate_dict = {}
        most_list_dict ={}
        for i in range(len(entity_list)):
            if requests[i] != -1:
                entity_id = entity_list[i].entity_id
                new_entity_list.append(entity_list[i])
                new_idx_prompt_dict.update({
                    entity_id:
                        idx_prompt_dict[entity_id] + thought_and_acts[i] + observations[entity_id]
                })
            else:
                most_list_dict.update({entity_list[i].entity_name: find_most_list(thought_and_acts[i])})
                terminate_dict.update({entity_list[i].entity_name: find_Terminate(thought_and_acts[i])})

        with open('output/{}/most_list_{}_{}.json'.format(save_dir, info_type, step), 'w') as f:
            json.dump(most_list_dict, f, indent=4)

        with open('output/{}/final_answer_{}_{}.json'.format(save_dir, info_type, step), 'w') as f:
            json.dump(terminate_dict, f, indent=4)

        with open('output/{}/idx_prompt_dict_{}_step_{}.json'.format(save_dir, info_type, step), 'w') as f:
            json.dump(new_idx_prompt_dict, f, indent=4)


    return new_idx_prompt_dict, new_entity_list

# 创建 ArgumentParser 对象
parser = argparse.ArgumentParser(description="It's a test")

parser.add_argument('-d', '--dataset', type=str, help='dataset name')

parser.add_argument('-i', '--info_type', type=str, help='code_motif,text_motif,1_neighbor')

parser.add_argument('-l', '--llm_type', type=str, help='LLM type')

parser.add_argument('-t', '--threshold', type=int, default=300, help='阈值')

parser.add_argument('-r', '--react_file', type=str, default='graph_motif_ReAct_v4_100_50candidates_tmp2', help='ReAct File')

parser.add_argument('-s', '--sematic_embedding_candidates_path', default='/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_100_3765_all add_corrected.txt',
                                                                               type=str, help='semantic cadidate path')
parser.add_argument('-cn1', '--candidate_num_1', type=int, help='candidate number of target entity in start')

parser.add_argument('-cn2', '--candidate_num_2', type=int, help='candidate number of target entity in the answer')

# # 添加可选参数（带默认值）
# parser.add_argument('-n', '--number', type=int, default=42, help='要处理的数字')

# 解析参数
args = parser.parse_args()

dataset = args.dataset
info_type = args.info_type
LLM_type = args.llm_type
threshold = args.threshold
module_name = args.react_file

ReAct_module = dynamic_import(module_name)
motif_ReAct_example_prompt = ReAct_module.motif_ReAct_example_prompt
sematic_embedding_candidates_path = args.sematic_embedding_candidates_path
candidate_num_1 = str(args.candidate_num_1)
candifate_num_2 = str(args.candidate_num_2)

ent_id_1_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1_strip'.format(dataset)
ent_id_2_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_2_aligned_strip'.format(dataset)

save_dir = dataset+"_"+LLM_type+"_"+'t'+str(threshold)+'_'+candidate_num_1+"_"+candifate_num_2

if __name__ == '__main__':

    if not os.path.exists('output/{}'.format(save_dir)):
        os.mkdir('output/{}'.format(save_dir))

    if info_type == 'baseline':
        idx_prompt_dict = baseline()
        get_baseline_responses(idx_prompt_dict)

    else:

        step0_idx_prompt_dict, step0_entity_list = generate_message_lists(threshold)

        step1_idx_prompt_dict, step1_entity_list = step(info_type, step0_idx_prompt_dict, step0_entity_list, '1', 1)
        step2_idx_prompt_dict, step2_entity_list = step(info_type, step1_idx_prompt_dict, step1_entity_list, '2', 2)
        step3_idx_prompt_dict, step3_entity_list = step(info_type, step2_idx_prompt_dict, step2_entity_list, '3', 3)
        step(info_type, step3_idx_prompt_dict, step3_entity_list, '4', 4)
