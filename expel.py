import argparse
import json
import random
import run_single_time
def split_train_test_dataset():
    """
    :return:
    """
    dataset_file = ent_id_1_path
    entity_list = []
    with open(dataset_file) as f:
        for line in f.readlines()[:3000]:
            entity = line.split('\t')[1].strip()
            entity_list.append(entity)

    sample_train_entity = random.sample(entity_list, 500)
    sample_test_entity = list(set(entity_list) - set(sample_train_entity))

    return sample_train_entity, sample_test_entity

def get_entity_map():
    entity1_list = []
    with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/new_ent_ids_1_strip') as f:
        for i, line in enumerate(f.readlines()):
            if i == threshold: break
            entity1_list.append(line.split('\t')[1].strip())

    entity2_list = []
    with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/new_ent_ids_2_aligned_strip') as f:
        for i, line in enumerate(f.readlines()):
            if i == threshold: break
            entity2_list.append(line.split('\t')[1].strip())

    entity1_map_entity2 = dict(zip(entity1_list, entity2_list))
    new_entity_map = {}

    sample_train_entity, _ = split_train_test_dataset()
    for entity in sample_train_entity:
        new_entity_map.update({entity: entity1_map_entity2[entity]})

    # print(new_entity_map)
    # print(len(new_entity_map))

    return new_entity_map

def expel():

    """
    :return:
    """
    def find_rules(s):
        start_idx = s.find('<rule>')
        end_idx = s.find("</rule>")
        if start_idx != -1:
            return s[start_idx + 6: end_idx]
        return -1

    rules = []
    prompts = """
    You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
    Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
    (1) Request[entity], which requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
    (2) Terminate[answer], which returns the answer and finishes the task.
    Here are two examples.
    Compare the background information of entities carefully to see if they are similar. 
    
    ------------------------------ Example Start ------------------------------ 

    [USER (Boss)]: Give me the most aligned entity of the target entity from candidates entity list. If there is same entity, please select directly. The target entity is:
    'Salauddin'
    
    The Candidate entities list is: 
    ['Salahuddin of Selangor', 'Slovenia', 'Riad Salamé', 'Hla Tun', 'Qadri Jamil', 'Sweden', 'Palau', 'Spain', 'Sheikh Hasina', 'Hla Min', 'Malaysia', 'Mohamed Nasheed', 'Ahmed Chalabi', 'Nabil Shaath', 'Sirindhorn', 'Japan', 'Abdo Hussameddin', 'Macky Sall', 'Salam Fayyad', 'Malawi', 'Mourad Dhina', 'Jawed Ludin', 'Macau', 'Abdulla Kurd']
    
    NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
    
    [YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
    ################### Your Answer Starts Here: ################### 
    Turn 1:
    # 4 turns left to provide final answer. Please select one answer from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
    Thought 1: I cannot find an entity in the candidate list that is a direct match for "Salauddin." I need to request more information about the target entity "Salauddin" to increase my confidence and make an informed decision.
    Act 1: Request['Salauddin']
    Observation 1: 
    Observation 1: import engage_in_symbolic_act, provide_aid, impose_curfew, praise_or_endorse, express_intent_to_change_institutions_regime, occupy_territory, express_intent_to_cooperate_militarily
    import express_intent_to_engage_in_diplomatic_cooperation, express_intent_to_meet_or_negotiate, host_a_visit, make_optimistic_comment, make_statement, connected_with, reduce_or_stop_material_aid, accuse
    
    def Salauddin_Engage_in_symbolic_act(Salauddin, Government_Bangladesh, Bangladesh):
        Salauddin = engage_in_symbolic_act(Government_Bangladesh)
        Salauddin += provide_aid(Bangladesh)
        Government_Bangladesh = impose_curfew(Bangladesh)
        Government_Bangladesh += praise_or_endorse(Bangladesh)
        Government_Bangladesh += express_intent_to_change_institutions_regime(Bangladesh)
        Government_Bangladesh += occupy_territory(Bangladesh)
        Government_Bangladesh += express_intent_to_cooperate_militarily(Bangladesh)
        return Salauddin, Government_Bangladesh, Bangladesh
    
    def Salauddin_Express_intent_to_engage_in_diplomatic_cooperation(Salauddin, Ali_Ahsan_Mohammad_Mujahid, Political_Parties_Bangladesh):
        Salauddin = express_intent_to_engage_in_diplomatic_cooperation(Ali_Ahsan_Mohammad_Mujahid)
        Salauddin += express_intent_to_meet_or_negotiate(Political_Parties_Bangladesh)
        Ali_Ahsan_Mohammad_Mujahid = express_intent_to_meet_or_negotiate(Political_Parties_Bangladesh)
        return Salauddin, Ali_Ahsan_Mohammad_Mujahid, Political_Parties_Bangladesh
    
    def Salauddin_Express_intent_to_engage_in_diplomatic_cooperation_with_Qatar(Salauddin, Head_of_Government_Qatar, Pervez_Musharraf):
        Salauddin = express_intent_to_engage_in_diplomatic_cooperation(Head_of_Government_Qatar)
        Salauddin += connected_with(Pervez_Musharraf)
        Head_of_Government_Qatar = host_a_visit(Pervez_Musharraf)
        Head_of_Government_Qatar += make_optimistic_comment(Pervez_Musharraf)
        return Salauddin, Head_of_Government_Qatar, Pervez_Musharraf
    
    def Salauddin_Make_statement(Salauddin, Israel, Pervez_Musharraf):
        Salauddin = make_statement(Israel)
        Salauddin += connected_with(Pervez_Musharraf)
        Israel = connected_with(Pervez_Musharraf)
        return Salauddin, Israel, Pervez_Musharraf
    
    def Salauddin_Connected_with_Police(Salauddin, Police_India, Bangladesh):
        Salauddin = connected_with(Police_India)
        Salauddin += provide_aid(Bangladesh)
        Police_India = make_statement(Bangladesh)
        Police_India += express_intent_to_meet_or_negotiate(Bangladesh)
        Police_India += reduce_or_stop_material_aid(Bangladesh)
        Police_India += accuse(Bangladesh)
        Police_India += express_intent_to_engage_in_diplomatic_cooperation(Bangladesh)
        return Salauddin, Police_India, Bangladesh
    
    Turn 2:
    [Important!] 3 turns left to provide final answer. Based on the observation, 'Salauddin' has connections with Bangladesh, India, and Pervez Musharraf. Considering this information, I should now request information about the most relevant candidate entity.
    Thought 2: I need more information to increase my confidence in selecting the correct aligned entity. Given the context, I will request information about 'Abdulla Kurd,' as it seems a potentially relevant candidate.
    Act 2: Request['Abdulla Kurd']
    Observation 2: 
    
    import connected_with
    
    def Abdulla_Kurd_connected_with_1(Abdulla_Kurd, Turkey):
        unknown_entity = connected_with(Turkey)
        unknown_entity += connected_with(Abdulla_Kurd)
        Turkey = connected_with(Abdulla_Kurd)
        return unknown_entity, Turkey, Abdulla_Kurd
    
    Turn 3:
    [Important!] 2 turns left to provide final answer. Based on the observation, 'Abdulla Kurd' has connections with Turkey. Since 'Salauddin' has connections with regions including Bangladesh and India, I need to evaluate if there is a stronger match in the candidate list. Given this context, I should now request information about another potentially relevant candidate entity.
    Thought 3: I need to request information about another candidate to ensure the most aligned entity is identified. 'Salahuddin of Selangor' could be a relevant entity to explore further connections.
    Act 3: Request['Salahuddin of Selangor']
    Observation 3: import connected_with, educated_at, continent
    
    def Kuala_Lumpur_connected_with_Salahuddin_of_Selangor(Kuala_Lumpur, Salahuddin_of_Selangor, Malaysia):
        Kuala_Lumpur = connected_with(Salahuddin_of_Selangor)
        Kuala_Lumpur += educated_at(Malaysia)
        Salahuddin_of_Selangor = continent(Malaysia)
        return Kuala_Lumpur, Salahuddin_of_Selangor, Malaysia
    
    Turn 4:
    [Important!] 1 turn left to provide final answer. Based on the observation, 'Salahuddin of Selangor' is connected with Kuala Lumpur and Malaysia. This information is not as relevant as the connections 'Salauddin' has with Bangladesh, India, and Pervez Musharraf. The connections of 'Abdulla Kurd' with Turkey seem more aligned with the context of 'Salauddin'.
    Thought 4: Considering all the observations, 'Abdulla Kurd' appears to be the most aligned entity given its connection with Turkey, which aligns with the regional context related to 'Salauddin'. Therefore, I am confident in selecting 'Abdulla Kurd' as the aligned entity.
    Act 4: Terminate['Abdulla Kurd']
    
    ------------------------------ Example End ------------------------------ 
    I am doing a entity alignment task，
    The target entity is {},
    The aligned entity is {},
    Please generate the step-by-step thought which can lead to  the given final answer. 
    Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'. 
    Please note, you MUST use Code Motif in reasoning path. above is an example. Please follow the example.
    Please generate some rules that better write code motif in <rule> </rule> in the final turn.

    """
    entity_map = get_entity_map()
    for target_entity in entity_map.keys():
        aligned_entity = entity_map[target_entity]
        prompts = prompts.format(target_entity, aligned_entity)
        LLM_response = run_single_time(prompts)
        rule = find_rules(LLM_response)
        rules.append(rule)

    with open(save_dir + '/output/rules.txt') as f:
        json.dump(rules, f, indent=4)



parser = argparse.ArgumentParser(description="It's a test")

parser.add_argument('-d', '--dataset', type=str, help='dataset name')
parser.add_argument('-t', '--threshold', type=int, default=3000, help='dataset name')

args = parser.parse_args()

dataset = args.dataset
threshold = args.threshold

save_dir = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao'
ent_id_1_path = save_dir +'/data/{}/new_ent_ids_1_strip'.format(dataset)
ent_id_2_path = save_dir +'/data/{}/new_ent_ids_2_aligned_strip'.format(dataset)

if __name__ == '__main__':
    expel()