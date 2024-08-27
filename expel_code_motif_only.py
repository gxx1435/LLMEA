import argparse
import json
import os
import random
from entity_expel import Entity
from run.utils import get_ent_id_dict
# from API_bank import get_gpt_4_turbo

examples = """------
## Example 1:

[USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it directly.

**The target entity is:** 'Ne Win'

**The candidate entities list is:**
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia']

NOTE:
1. You have at most 4 turns to generate the final result. Please answer the task with interleaving Thought, Code, Action, Result turns. 
2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!

### Turn 1: (3 turns left to use "Terminate" action to provide final answer.)
**Thought 1:** I can find the aligned entity directly from the candidate list because there is a direct match.
**Act 1:
**The most similar 50 entities are:<MOST>['Ne Win', 'Hla Min', 'Soe Thein', 'Chea Sim', 'Aung Min', 'Hla Tun', 'Su Chi', 'Tea Banh', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Benin', 'Yen Ming', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Serbia', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Ukraine', 'Zambia']</MOST> and Terminate['Ne Win']

------
## Example 2

[USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it directly. 

**The target entity is:** 'Salauddin'

**The candidate entities list is:**
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Abdulla Kurd']

NOTE:
1. You have at most 4 turns to generate the final result. Please answer the task with interleaving Thought, Code, Action, Result turns. 
2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!

### Turn 1: (3 turns left to use "Terminate" action to provide final answer.)
**Thought 1:** I cannot find an entity in the candidate list that is a direct match for "Salauddin." I need more information about "Salauddin" to make an informed decision.
**Act 1: **The most similar 50 entities are:<MOST>['Abdulla Kurd', 'Salam Fayyad', 'Sule Lamido', 'Talal Arslan', 'Saad Hariri', 'Salou Djibo', 'Shwe Mann', 'Aung Min', 'Soe Thein', 'Suharto', 'Hla Min', 'Hla Tun', 'Jawed Ludin', 'Sima Samar', 'Samar', 'Sama', 'Shas', 'Fatah', 'Hamas', 'Gilad Erdan', 'Babar Awan', 'Hamid Mir', 'Ramdev', 'Imran Khan', 'Sylvia Lim', 'Kashmir', 'Ānanda', 'Sukarno', 'Sam Nujoma', 'Ne Win', 'Benin', 'Sula Lamido', 'Shwe Mann', 'Su Chi', 'Aung Min', 'Talal Arslan', 'Kashmir', 'Sule Lamido', 'Samar', 'Fatah', 'Hamas', 'Gilad Erdan', 'Babar Awan']</MOST> and Terminate['Abdulla Kurd']
"""


# def split_train_test_dataset():
#     """
#     :return:
#     """
#     dataset_file = ent_id_1_path
#     entity_list = []
#     with open(dataset_file) as f:
#         for line in f.readlines()[:threshold]:
#             entity = line.split('\t')[1].strip()
#             entity_list.append(entity)
#
#     random.seed(7)
#
#     sample_train_entity = random.sample(entity_list, 500)
#     sample_test_entity = list(set(entity_list) - set(sample_train_entity))
#
#     return sample_train_entity, sample_test_entity

def split_train_test_dataset():
    """
    :return:
    """
    with open(os.getcwd()+'/output/{}/gpt_4_turbo/icews_yago_t5000_50_50_original_5motif_v4/final_answer_code_motif_lite_1.json'.format(dataset)) as f:
        final_answer = json.load(f)
        sample_test_entity = final_answer.keys()

    final_answers = {}
    for i in [2, 3, 4]:
        with open(os.getcwd() + '/output/{}/gpt_4_turbo/icews_yago_t5000_50_50_original_5motif_v4/final_answer_code_motif_lite_{}.json'.format(
            dataset,
                    i), 'r') as f:
            final_answer = json.load(f)
            final_answers.update(final_answer)
            sample_train_entity = final_answers.keys()

    return sample_train_entity, sample_test_entity

def get_gpt_4_turbo(messages_input, max_tokens=2000):

    return "xxxxxx"

def get_entity_map():
    entity1_list = []
    with open(ent_id_1_path) as f:
        for i, line in enumerate(f.readlines()):
            # if i == threshold: break
            entity1_list.append(line.split('\t')[1].strip())

    entity2_list = []
    with open(ent_id_2_path) as f:
        for i, line in enumerate(f.readlines()):
            # if i == threshold: break
            entity2_list.append(line.split('\t')[1].strip())

    entity1_map_entity2 = dict(zip(entity1_list, entity2_list))

    new_entity_map = {}
    sample_train_entity, _ = split_train_test_dataset()
    for entity in sample_train_entity:
        new_entity_map.update({entity: entity1_map_entity2[entity]})

    # print(new_entity_map)
    # print(len(new_entity_map))

    return new_entity_map

def get_case(entity, a_entity):
    """
    :param entity:
    :return:
    """
    t_entity = entity.entity_name
    t_enntity_id = entity.entity_id

    final_answers = {}
    for i in [1, 2, 3, 4]:
        with open(os.getcwd() + '/output/{}/gpt_4_turbo/icews_yago_t5000_50_50_original_5motif_v4/final_answer_code_motif_lite_{}.json'.format(
            dataset,
                        i), 'r') as f:
            final_answer = json.load(f)
            final_answers.update(final_answer)

    if final_answers[t_entity] == a_entity:
        if_wrong = 'Correct'
    else:
        if_wrong = 'Wrong'

    step_idx_prompt = 0
    for i in [4, 3, 2, 1]:
        with open(os.getcwd()+'/output/{}/gpt_4_turbo/icews_yago_t5000_50_50_original_5motif_v4/idx_prompt_dict_code_motif_lite_step_{}.json'.format(dataset, i)) as f:
            idx_prompt = json.load(f)
            idxs = idx_prompt.keys()
            if t_enntity_id in idxs:
                step_idx_prompt = i
                break

    step_thought_and_act = step_idx_prompt+1

    case = ''
    if step_idx_prompt == 0:
        with open(os.getcwd()+'/output/{}/gpt_4_turbo/icews_yago_t5000_50_50_original_5motif_v4/idx_prompt_dict_step_00.json'.format(dataset)) as f:
            idx_prompt = json.load(f)
    else:
        with open(os.getcwd()+'/output/{}/gpt_4_turbo/icews_yago_t5000_50_50_original_5motif_v4/idx_prompt_dict_code_motif_lite_step_{}.json'.format(dataset, step_idx_prompt)) as f:
            idx_prompt = json.load(f)

    case += idx_prompt[t_enntity_id]

    if step_idx_prompt < 4:
        with open(os.getcwd()+'/output/{}/gpt_4_turbo/icews_yago_t5000_50_50_original_5motif_v4/LLM_response_code_motif_lite/thought_and_acts_{}.json'.format(dataset, step_thought_and_act)) as f:
            thought_and_act = json.load(f)
        case += thought_and_act[t_enntity_id]

    case = case.replace(examples, '')

    return if_wrong, case

def expel():

    """
    :return:
    """

    expel_code_motif_rule = """
    <rule>
    ** Class: A class represented an entity.
    ** Descriptive Function Names: Ensure the function name clearly represents the abstract of the motif. This aids in understanding the motif's purpose at a glance.
    ** Relevant import statements: The import statement is relationship between entities.
    ** Function parameter: The function parameters are all the entities of a motif.
    ** Function Implementation: Implement the function by calling the imported relations with the appropriate entities(parameters). Each relation call should correspond to the connections or actions described in the motif information.
    ** Relationship: For simple connections between nodes, use the connected_with relation. For more complex interactions (e.g., meetings, visits), use specific relations like make_a_visit, express_intent_to_meet_or_negotiate, etc.
    ** Return values: Return all the entities involved in the motif as part of the function’s result.
    ** Multiple relationship: Recognize the `+=` relationship as indicative of multiple types of connections between two entities, enriching the motif's complexity.
    ** Demonstrative Execution: Use the `if __name__ == '__main__':` block to showcase the motif's application, offering a practical example of its use.
    ** Triple: A triple in triangle information represent a motif and is expressed as a function in code motif, like:
    </rule>
    """
    def find_rules(s):
        start_idx = s.find('<rule>')
        end_idx = s.find("</rule>")
        if start_idx != -1:
            return s[start_idx + 6: end_idx]
        return -1


    from expel_code_motif_prompt import prompts


    entity_map = get_entity_map()

    ent_id_dict = get_ent_id_dict(ent_id_1_path)

    if version == '':
        expel_code_motif_file = save_dir + '/output/expel_{}/expel_code_prompts_rules.txt'.format(version)
        expel_code_motif_prompt_file = save_dir + '/output/expel_{}/expel_code_prompts.txt'.format(version)
        expel_code_motif_response_file = save_dir + '/output/expel_{}/expel_code_prompts_response.txt'.format(version)
    else:
        expel_code_motif_file = save_dir + '/output/expel_{}/expel_code_prompts_rules_{}.txt'.format(version, version)
        expel_code_motif_prompt_file = save_dir + '/output/expel_{}/expel_code_prompts_{}.txt'.format(version, version)
        expel_code_motif_response_file = save_dir + '/output/expel_{}/expel_code_prompts_response_{}.txt'.format(version, version)

    with open(expel_code_motif_response_file, 'w') as expel_code_motif_response_f, open(expel_code_motif_prompt_file, 'w') as expel_code_motif_prompt_f, open(expel_code_motif_file, 'w') as expel_code_motif_f:
        for target_entity in entity_map.keys():

            aligned_entity = entity_map[target_entity]
            entity_id = ent_id_dict[target_entity]
            entity = Entity(target_entity, entity_id, 'target')

            _, cand_list, _ = entity.get_baseline_prompts()
            if_wrong, case = get_case(entity, aligned_entity)
            print(target_entity, '\t', aligned_entity, '\t', if_wrong)

            if if_wrong == 'Wrong':
                expel_code_motif_prompts = prompts.format(expel_code_motif_rule, case, aligned_entity, cand_list)

                expel_code_motif_prompt_f.write(expel_code_motif_prompts+'\n')

                msg = expel_code_motif_prompts
                messages_input = [
                    {
                        "role": "user",
                        "content": msg,
                    }
                ]
                LLM_response = get_gpt_4_turbo(messages_input, max_tokens=2000)

                expel_code_motif_response_f.write(LLM_response+'\n')

                expel_code_motif_rule = find_rules(LLM_response)

                expel_code_motif_f.write(str(expel_code_motif_rule)+'\n')

            # expel_process_prompts = expel_process_prompts.format(expel_process_rule, case, if_wrong, target_entity, aligned_entity, cand_list)
            #
            # msg = expel_process_prompts
            # messages_input = [
            #     {
            #         "role": "user",
            #         "content": msg,
            #     }
            # ]
            # LLM_response = get_gpt_4_turbo(messages_input, max_tokens=2000)
            #
            # expel_process_rule = find_rules(LLM_response)
            #
            # expel_process_f.write(str(expel_process_rule)+'\n')


parser = argparse.ArgumentParser(description="It's a test")

parser.add_argument('-d', '--dataset', type=str, help='dataset name')
parser.add_argument('-t', '--threshold', type=int, default=3000, help='dataset name')
parser.add_argument('-v', '--version', type=str, default='', help='version control')

# parser.add_argument('-s', '--sematic_embedding_candidates_path', type=str, help='semantic cadidate path')

args = parser.parse_args()

dataset = args.dataset
threshold = args.threshold
version = args.version
# sematic_embedding_candidates_path = args.sematic_embedding_candidates_path


save_dir = os.getcwd()
ent_id_1_path = save_dir +'/data/{}/new_ent_ids_1_rs_0.3_new'.format(dataset)
ent_id_2_path = save_dir +'/data/{}/new_ent_ids_2_aligned_rs_0.3_new'.format(dataset)

if __name__ == '__main__':

    if not os.path.exists(save_dir + '/output/expel_{}'.format(version)):
        os.mkdir(save_dir + '/output/expel_{}'.format(version))

    expel()