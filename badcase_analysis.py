import json
import argparse
from run.utils import get_ent_id_dict
import run_single_time
def dynamic_import(module_name):
    module = __import__(module_name)
    return module

def run_single_time(prompt):
    """
    :param prompt:
    :return:
    """

    return """
    <code>
    import is_connected_with, make_a_visit, express_intent_to_meet_or_negotiate, engage_in_negotiation
    import engage_in_diplomatic_cooperation, meet_at_a_third_location, rally_opposition_against, make_an_appeal_or_request
    import consult, sign_formal_agreement, praise_or_endorse, declare_truce_ceasefire, host_a_visit
    
    def execute_actions(entity1, entity2, actions):
        for action in actions:
            entity1 = action(entity2)
        return entity1
    
    def Motif(entity1, entity2, organization, actions_entity2, actions_organization):
        entity1 = execute_actions(entity1, entity2, actions_entity2)
        entity1 = is_connected_with(organization)
        entity2 = execute_actions(entity2, organization, actions_organization)
        return entity1, entity2, organization
    
    def Austria_Slovenia_OECD_Motif(Austria, Slovenia, Organization_for_Economic_Cooperation_and_Development):
        actions_entity2 = [
            express_intent_to_engage_in_diplomatic_cooperation, 
            express_intent_to_meet_or_negotiate, 
            engage_in_negotiation, 
            engage_in_diplomatic_cooperation, 
            meet_at_a_third_location
        ]
        actions_organization = [
            express_intent_to_meet_or_negotiate
        ]
        return Motif(Austria, Slovenia, Organization_for_Economic_Cooperation_and_Development, actions_entity2, actions_organization)
    
    def Arab_League_Vietnam_OECD_Motif(Arab_League, Vietnam, Organization_for_Economic_Cooperation_and_Development):
        actions_entity2 = [
            is_connected_with
        ]
        actions_organization = [
            rally_opposition_against
        ]
        return Motif(Arab_League, Vietnam, Organization_for_Economic_Cooperation_and_Development, actions_entity2, actions_organization)
    
    def Lee_Myung_Bak_Canada_OECD_Motif(Lee_Myung_Bak, Canada, Organization_for_Economic_Cooperation_and_Development):
        actions_entity2 = [
            make_an_appeal_or_request, 
            express_intent_to_meet_or_negotiate, 
            make_a_visit
        ]
        actions_organization = [
            make_an_appeal_or_request
        ]
        return Motif(Lee_Myung_Bak, Canada, Organization_for_Economic_Cooperation_and_Development, actions_entity2, actions_organization)
    
    def Ethiopia_Canada_OECD_Motif(Ethiopia, Canada, Organization_for_Economic_Cooperation_and_Development):
        actions_entity2 = [
            engage_in_diplomatic_cooperation, 
            consult, 
            sign_formal_agreement, 
            make_a_visit, 
            praise_or_endorse
        ]
        actions_organization = [
            is_connected_with
        ]
        return Motif(Ethiopia, Canada, Organization_for_Economic_Cooperation_and_Development, actions_entity2, actions_organization)
    
    def Ukraine_Lithuania_OECD_Motif(Ukraine, Lithuania, Organization_for_Economic_Cooperation_and_Development):
        actions_entity2 = [
            declare_truce_ceasefire, 
            engage_in_negotiation, 
            praise_or_endorse, 
            engage_in_diplomatic_cooperation, 
            consult
        ]
        actions_organization = [
            engage_in_negotiation, 
            engage_in_diplomatic_cooperation, 
            host_a_visit
        ]
        return Motif(Ukraine, Lithuania, Organization_for_Economic_Cooperation_and_Development, actions_entity2, actions_organization)
    
    if __name__ == '__main__':
        Austria, Slovenia, OECD = Austria_Slovenia_OECD_Motif('Austria', 'Slovenia', 'Organization_for_Economic_Cooperation_and_Development')
        Arab_League, Vietnam, OECD = Arab_League_Vietnam_OECD_Motif('Arab_League', 'Vietnam', 'Organization_for_Economic_Cooperation_and_Development')
        Lee_Myung_Bak, Canada, OECD = Lee_Myung_Bak_Canada_OECD_Motif('Lee_Myung_Bak', 'Canada', 'Organization_for_Economic_Cooperation_and_Development')
        Ethiopia, Canada, OECD = Ethiopia_Canada_OECD_Motif('Ethiopia', 'Canada', 'Organization_for_Economic_Cooperation_and_Development')
        Ukraine, Lithuania, OECD = Ukraine_Lithuania_OECD_Motif('Ukraine', 'Lithuania', 'Organization_for_Economic_Cooperation_and_Development')
    </code>
    <rule>
    1. The code motif should be concise and avoid redundancy.
    2. Summarize the relationship by using a generic function to handle actions between entities.
    3. Note the inter-call relationship of the entities by iterating through actions in a loop within the generic function.
    4. Use the generic function to encapsulate common patterns and simplify motif definitions.
    5. Define specific action lists for interactions between entity pairs and between entities and organizations.
    </rule>
    """
def badcase_analysis(final_answer, is_correct):
    """
    handle with hallucination
    :param observations:
    :param is_correct:
    :return:
    """
    from entity import Entity
    def find_code(s):
        start_idx = s.find('<code>')
        end_idx = s.find("</code>")
        if start_idx != -1:
            return s[start_idx + 6: end_idx]

        start_idx = s.find('<CODE>')
        end_idx = s.find("</CODE>")
        if start_idx != -1:
            return s[start_idx + 6: end_idx]

        start_idx = s.find('python')
        if start_idx != -1:
            return s[start_idx + 6: -1]

        return 'no code observation for this entity.'

    def find_rules(s):
        start_idx = s.find('<rule>')
        end_idx = s.find("</rule>")
        if start_idx != -1:
            return s[start_idx + 6: end_idx]
        return -1

    rules = []
    for entity_name in final_answer.keys():
        if is_correct[entity_name] == -1:
            ent_id_dict = get_ent_id_dict(ent_id_1_path)
            entity_id = ent_id_dict[entity_name]
            entity = Entity(entity_name, entity_id, 'target')

            for step in [1,2,3,4]:
                with open('output/{}/LLM_response_{}/observations_{}.json'.format(save_dir, info_type, step)) as f:
                    observations = json.load(f)
                    for idx in observations.keys():
                        if idx == entity_id:
                            prompts = """
                            The code motif is not very good because it lead to a wrong answer, please help me regenerate the code follow the rules:
                            1. The code motif can not be too long
                            2. Summarize the relationship
                            3. Please note the inter call relationship of the entities
                            {}
                            The original code motif is {}    
                
                            You need to finish the following task:
                            1. Please encapsulate the new generated code within <code> </code>.
                            2. generate the rules how to better generate the code motif within <rule> </rule>
                      
                            """.format('\n'.join(rules), observations[idx])
                            ans = run_single_time(prompts)
                            new_code = find_code(ans)
                            rule = find_rules(ans)
                            rules.append(rule)





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


    exit()
