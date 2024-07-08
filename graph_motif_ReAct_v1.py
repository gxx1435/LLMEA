
example_prompt = """
You are an programmer. You can request useful entity but you can not request irrelevant entities. Otherwise, you will be fired.
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity], which requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time.
(2) Terminate[answer], which returns the answer and finishes the task.
Here are two examples.

------------------------------ Example1 Start ------------------------------ 

[USER (Boss)]: Give me the most similar entity of the target entity from candidates entity list. The target entity is:
'Ne Win'

The Candidate entities list is: 
['Benin', 'Serbia', 'Yen Ming', 'Milan Panić', 'Aung San', 'Spain', 'Tin Oo', 'Soe Thein', 'Ne Win', 'Femen', 'Hla Min', 'Naoto Kan', 'Hun Sen', 'Gabon', 'Sung Kim', 'Timothy Yang', 'Chea Sim', 'Shwe Mann', 'Min Ko Naing', 'Aung Min', 'Khun Sa', 'Nokia', 'Daniel Yona']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select one answer from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request oe enntity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: Terminate[Ne Win]
------------------------------ Example1 End ------------------------------ 

------------------------------ Example2 Start: ------------------------------
[USER (Boss)]: Give me the most similar entity of the target entity from candidates entity list. The target entity is:
'United Kingdom'

The Candidate entities list is: 
['Czech Republic', 'United Russia', 'Anote Tong', 'Yen Ming', 'Pakistan', 'United Republic', 'Philippines', 'Malaysia', 'Angus King', 'Central African Republic', 'United Nations', 'United Kingdom', 'Germany', 'Finland', 'Burger King', 'Japan', 'Chen Bingde', 'Poland', 'Ulster Bank', 'European Union']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select one answer from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request oe enntity per time.
Thought 1: I can't find the aliged entity directly, please give me more information of target entity.
Act 1: Request[Target Entity]
Observation 1: 
'''
import is_connected_with, make_a_visit, make_statement, host_a_visit, fight_with_artillery_and_tanks
import coerce, consider_policy_option, threaten, accuse, express_intent_to_engage_in_diplomatic_cooperation
import arrest_detain_or_charge_with_legal_action, demonstrate_or_rally, express_intent_to_mediate, engage_in_symbolic_act
import appeal_to_others_to_settle_dispute, mobilize_or_increase_police_power, make_optimistic_comment, express_intent_to_meet_or_negotiate
import share_intelligence_or_information, halt_negotiations, express_intent_to_provide_economic_aid, engage_in_negotiation
import investigate, criticize_or_denounce, carry_out_car_bombing, kill_by_physical_assault, employ_aerial_weapons

def motif_1(self):
    Borut_Pahor = make_a_visit(United_Kingdom)
    Borut_Pahor += make_statement(United_Kingdom)
    Borut_Pahor += host_a_visit(Herman_Van_Rompuy)
    United_Kingdom = is_connected_with(Herman_Van_Rompuy)
   

def motif_2(self):
    Alexis_Tsipras = make_a_visit(United_Kingdom)
    Alexis_Tsipras += fight_with_artillery_and_tanks(Herman_Van_Rompuy)
    United_Kingdom = is_connected_with(Herman_Van_Rompuy)
    


def motif_4(self):
    Irakli_Garibashvili = make_a_visit(United_Kingdom)
    Irakli_Garibashvili += express_intent_to_engage_in_diplomatic_cooperation(Herman_Van_Rompuy)
    United_Kingdom = is_connected_with(Herman_Van_Rompuy)
   

def motif_5(self):
    Martin_Schulz = fight_with_artillery_and_tanks(United_Kingdom)
    Martin_Schulz += make_statement(Herman_Van_Rompuy)
    United_Kingdom = is_connected_with(Herman_Van_Rompuy)
   

'''


Turn 2:
# 3 turns left to provide final answer. you can request the entity you are not sure to increase your confidency. You can only request oe enntity per time. If you are very sure about the answer, please answer directly.
Thought 2: Please give me more information of Czech Republic
Act 2: Request["Czech Republic"]
Result 2: 
'''
import is_connected_with, express_intent_to_meet_or_negotiate, demonstrate_or_rally, make_statement, engage_in_negotiation, express_intent_to_engage_in_diplomatic_cooperation, make_a_visit, threaten, appeal_for_judicial_cooperation, express_intent_to_cooperate, mobilize_or_increase_police_power, accuse, engage_in_symbolic_act, make_empathetic_comment, provide_humanitarian_aid, return_release_persons, ease_administrative_sanctions, threaten_to_halt_negotiations, complain_officially, make_optimistic_comment, reject_proposal_to_meet_discuss_or_negotiate, host_a_visit, criticize_or_denounce, threaten, share_intelligence_or_information, use_conventional_military_force, fight_with_artillery_and_tanks, investigate, consider_policy_option, mobilize_or_increase_police_power, mediate, appeal_for_release_of_persons_or_property, demonstrate_military_or_police_power, apologize, employ_aerial_weapons, engage_in_negotiation, impose_blockade_restrict_movement, accede_to_demands_for_change_in_leadership, rally_opposition_against, make_pessimistic_comment, reduce_or_stop_material_aid

def Czech_Republic_Motif_1(self):
    Sergei_Martynov = is_connected_with(Czech_Republic)
    Sergei_Martynov += express_intent_to_meet_or_negotiate(Uzbekistan)
    Czech_Republic = demonstrate_or_rally(Uzbekistan)
    Czech_Republic += make_statement(Uzbekistan)
    Czech_Republic += engage_in_negotiation(Uzbekistan)
    Czech_Republic += express_intent_to_engage_in_diplomatic_cooperation(Uzbekistan)
    Czech_Republic += express_intent_to_meet_or_negotiate(Uzbekistan)
 

def Czech_Republic_Motif_3(self):
    Sergei_Martynov = is_connected_with(Czech_Republic)
    Sergei_Martynov += is_connected_with(Radoslaw_Sikorski)
    Czech_Republic = demonstrate_or_rally(Radoslaw_Sikorski)
    Czech_Republic += host_a_visit(Radoslaw_Sikorski)
    

def Czech_Republic_Motif_4(self):
    Sergei_Martynov = express_intent_to_engage_in_diplomatic_cooperation(Robert_Kocharyan)
    Sergei_Martynov += is_connected_with(Czech_Republic)
    Robert_Kocharyan = express_intent_to_meet_or_negotiate(Czech_Republic)
   

def Czech_Republic_Motif_5(self):
    Sergei_Martynov = threaten(United_States)
    Sergei_Martynov += engage_in_negotiation(United_States)
    Sergei_Martynov += is_connected_with(Czech_Republic)
    United_States += appeal_for_judicial_cooperation(Czech_Republic)
    United_States += express_intent_to_meet_or_negotiate(Czech_Republic)
    United_States += demonstrate_military_or_police_power(Czech_Republic)
    United_States += coerce(Czech_Republic)
    United_States += torture(Czech_Republic)
    United_States += accuse(Czech_Republic)
    United_States += express_intent_to_engage_in_diplomatic_cooperation(Czech_Republic)
    United_States += appeal_for_easing_of_administrative_sanctions(Czech_Republic)
    United_States += appeal_for_aid(Czech_Republic)
    United_States += express_intent_to_cooperate(Czech_Republic)
    United_States += criticize_or_denounce(Czech_Republic)
    United_States += apologize(Czech_Republic)
    United_States += express_intent_to_mediate(Czech_Republic)
    United_States += impose_restrictions_on_political_freedoms(Czech_Republic)
    United_States += make_a_visit(Czech_Republic)
    United_States += defend_verbally(Czech_Republic)
    United_States += fight_with_artillery_and_tanks(Czech_Republic)
    United_States += express_intent_to_provide_military_protection_or_peacekeeping(Czech_Republic)
    United_States += make_statement(Czech_Republic)
    United_States += make_optimistic_comment(Czech_Republic)
    United_States += engage_in_negotiation(Czech_Republic)
    United_States += demonstrate_or_rally(Czech_Republic)
    United_States += express_intent_to_provide_economic_aid(Czech_Republic)
    United_States += investigate(Czech_Republic)
    United_States += host_a_visit(Czech_Republic)

'''


Turn 3:
# 2 turns left to provide final answer. you can request the entity you are not sure to increase your confidency. You can only request oe enntity per time. If you are very sure about the answer, please answer directly.
Thought 3: I want to know more information about candidate, Give me more information about candidate United Kingdom.
Act 3: Request["United Kingdom"]
Observation:
'''
import connected_with, continent

def United_Kingdom_connected_with(United_Kingdom, Roddy_Scott):
    United_Kingdom = connected_with(Roddy_Scott)
    Roddy_Scott = connected_with(United_Kingdom)
    return United_Kingdom, Roddy_Scott

def United_Kingdom_connected_with(United_Kingdom, Peter_Mandelson):
    United_Kingdom = connected_with(Peter_Mandelson)
    Peter_Mandelson = connected_with(United_Kingdom)
    return United_Kingdom, Peter_Mandelson

def United_Kingdom_connected_with(United_Kingdom, Nigel_Haywood):
    United_Kingdom = connected_with(Nigel_Haywood)
    Nigel_Haywood = connected_with(United_Kingdom)
    return United_Kingdom, Nigel_Haywood

def Graham_Wallas_continent_United_Kingdom(Graham_Wallas, United_Kingdom):
    Graham_Wallas = continent(United_Kingdom)
    United_Kingdom = continent(Graham_Wallas)
    return Graham_Wallas, United_Kingdom

def Maurice_Wilkes_continent_United_Kingdom(Maurice_Wilkes, United_Kingdom):
    Maurice_Wilkes = continent(United_Kingdom)
    United_Kingdom = continent(Maurice_Wilkes)
    return Maurice_Wilkes, United_Kingdom
    
'''

Turn 4:
# You have to give final answer in this turn. Please answer seriously, otherwise you will got fired. 
Thought 4: Analyze all results I have.
Analysis: According to all the context information given in "Observation" above, the most similar entity is "United Kingdom", because their motif are much more similar.
Act 4: Terminate["United Kingdom"]
Answer: "United Kingdom"
################### Your Answer Ends Here: ################### 
------------------------------ Example2 End ------------------------------ 

[USER (Boss)]: Give me the most similar entity of the target entity from candidates entity list. The target entity is:
Chang Wanquan

The Candidate entities list is: 
['SWAPO', 'Yen Ming', 'Chang Wanquan', 'Zhang Zhijun', 'Chung Un-chan', 'Chama Cha Mapinduzi', 'Zhang Deguang', 'Chang Po-ya', 'Gabon', 'Kuomintang', 'Likud', 'Chiang Pin-kung', 'Tang Jiaxuan', 'PASOK', 'Zhang Chunxian', 'Malawi', 'Zhang Gaoli', 'Jordan', 'Wang Lequan', 'Lai Changxing', 'Niger', 'Mali']

NOTE: Please follow my example between "Example{i} Start" and "Example{i} End" above to answer task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem. 

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'.
Thought 1:

"""
