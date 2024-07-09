import os
from openai import AzureOpenAI
import json
import urllib.request
import ssl
import time
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import inspect
import copy


def get_gpt_4_turbo(messages, engine="gpt-4-turbo", temperature=0, max_tokens=2000, top_p=1, frequency_penalty=0, presence_penalty=0, timeout=10, stop=None):  
    client = AzureOpenAI(
        azure_endpoint="xxxxxxxxxxxxxxxx", 
        api_key="xxxxxxxxx",  
        api_version="xxxxx"
    )
    while 1:
        flag = 0
        try:
            completion = client.chat.completions.create(
                model=engine,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                stop=stop
            )
            flag = 1
            
        except Exception as e:
            print(e)
            time.sleep(1)
        if flag == 1:
            break

    return completion.choices[0].message.content


def choose_LLM(LLM_name, messages_input, max_new_tokens=2000):
    if LLM_name == "gpt_4_turbo":
        return get_gpt_4_turbo(messages_input, max_tokens=max_new_tokens)
    else:
        print("Error LLM name!")
        raise AssertionError


def inspect_para(func):
    signature = inspect.signature(func)
    parameters_with_defaults = {}
    for name, param in signature.parameters.items():
        if param.default is inspect.Parameter.empty:
            parameters_with_defaults[name] = None
        else:
            parameters_with_defaults[name] = param.default
    return parameters_with_defaults


def collect_response(message_list, model_name, num_threads = 10, **kwargs):
    func_name = f"get_{model_name}"
    func = globals()[func_name]
    
    def multi_thread_func(**kwargs):
        id = kwargs.pop('process_id')
        response = func(**kwargs)
        return id, response  
        
    try:
        para_dic = inspect_para(func)
    except:
        raise(ValueError, 'model name does not exist')
    
    for para, value in kwargs.items():
        para_dic[para] = value
    
    tasks = []
    message_key = list(para_dic.keys())[0]
    for i, message in enumerate(message_list):
        para_dic[message_key] = message # should be different format for different models
        para_dic['process_id'] = i
        inp = copy.deepcopy(para_dic)
        tasks.append(inp)
        
    responses = []
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_task = {
            executor.submit(multi_thread_func, **task): task for task in tasks
        }
        for future in tqdm(
            concurrent.futures.as_completed(future_to_task), total=len(tasks)
        ):
            responses.append(future.result())

    responses.sort(key = lambda x:x[0])
    results = list(map(lambda x:x[1], responses))
    return results


if __name__ == '__main__':
    prompt_path = '/Users/quge/HKU/research/birdcode/res/mini_dev/prompts/gpt4/direct_sql_w_all_columns_we.json'
    data_output_path = '/Users/quge/HKU/research/birdcode/res/mini_dev/responses/direct_sql.json'
    prompt_batch = json.load(open(prompt_path, 'r'))
    message_list = [[{'role': 'user', 'content': prompt}] for prompt in prompt_batch.values()]
    # message_list = list(map(lambda x: [x], message_list))[:3]
    # message_list = ['1','2','3']
    
    kwargs = {
        'max_tokens': 2000,
        'stop': None
    }
    
    response = collect_response(message_list, model_name = 'gpt_4_turbo', **kwargs)
    
