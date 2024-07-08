
example_prompt = """
You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity], which requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) Terminate[answer], which returns the answer and finishes the task.
Here are two examples.
Compare the background information of entities carefully to see if they are similar. 
------------------------------ Example1 Start ------------------------------ 

[USER (Boss)]: Give me the most aligned entity of the target entity from candidates entity list. If there is same entity, please select directly. The target entity is:
'Ne Win'

The Candidate entities list is: 
['Benin', 'Serbia', 'Yen Ming', 'Milan Panić', 'Aung San', 'Spain', 'Tin Oo', 'Soe Thein', 'Ne Win', 'Femen', 'Hla Min', 'Naoto Kan', 'Hun Sen', 'Gabon', 'Sung Kim', 'Timothy Yang', 'Chea Sim', 'Shwe Mann', 'Min Ko Naing', 'Aung Min', 'Khun Sa', 'Nokia', 'Daniel Yona']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select one answer from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: Terminate[Ne Win]
------------------------------ Example1 End ------------------------------ 

------------------------------ Example2 Start: ------------------------------
[USER (Boss)]: Give me the aligned entity of the target entity from candidates entity list. If there is same entity, please select directly. The target entity is:
'Beverley J. Oda'

The Candidate entities list is: 
['George Kunda', 'Sergey Shoygu', 'SWAPO', 'Bev Oda', 'Jerry Gana', 'B. Lynn Pascoe', 'Nevers Mumba', 'Chama Cha Mapinduzi', 'Beverley McLachlin', 'Pierre de Vos', 'Gabon', 'Likud', 'Henry Okah', 'PASOK', 'UNESCO', 'Peter Obi', 'Jordan', 'Interpol', 'Niger', 'Mali', 'Pierre Moussa']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select one answer from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can't find the aliged entity directly, please give me more information of target entity.
Act 1: Request['Beverley J. Oda']
Observation 1: 
'''
import host_a_visit, express_intent_to_engage_in_diplomatic_cooperation, express_intent_to_meet_or_negotiate, make_a_visit, demand_political_reform, mobilize_or_increase_police_power, provide_humanitarian_aid, halt_negotiations, provide_aid, demonstrate_or_rally, engage_in_negotiation

def United_Kingdom_Host_a_visit(United_Kingdom, Hina_Rabbani_Khar, Beverley_J_Oda):
    United_Kingdom = host_a_visit(Hina_Rabbani_Khar)
    United_Kingdom = host_a_visit(Beverley_J_Oda)
    Hina_Rabbani_Khar = express_intent_to_engage_in_diplomatic_cooperation(Beverley_J_Oda)
    return United_Kingdom, Hina_Rabbani_Khar, Beverley_J_Oda

def Beverley_J_Oda_connected_with(Beverley_J_Oda, Stephen_Harper, Business_Canada):
    Beverley_J_Oda = is_connected_with(Stephen_Harper)
    Beverley_J_Oda = express_intent_to_meet_or_negotiate(Business_Canada)
    Stephen_Harper = is_connected_with(Business_Canada)
    return Beverley_J_Oda, Stephen_Harper, Business_Canada

def Government_United_States_Express_intent_to_meet(Government_United_States, Beverley_J_Oda, Haiti):
    Government_United_States = is_connected_with(Beverley_J_Oda)
    Government_United_States += express_intent_to_meet_or_negotiate(Haiti)
    Government_United_States += express_intent_to_engage_in_diplomatic_cooperation(Haiti)
    Government_United_States += demand_political_reform(Haiti)
    Government_United_States += mobilize_or_increase_police_power(Haiti)
    Government_United_States += provide_humanitarian_aid(Haiti)
    Beverley_J_Oda = make_a_visit(Haiti)
    return Government_United_States, Beverley_J_Oda, Haiti

def Government_Canada_Halt_negotiations(Government_Canada, United_States, Beverley_J_Oda):
    Government_Canada = halt_negotiations(United_States)
    Government_Canada = provide_aid(United_States)
    Government_Canada = express_intent_to_meet_or_negotiate(United_States)
    Government_Canada = demonstrate_or_rally(United_States)
    Government_Canada = engage_in_negotiation(United_States)
    Government_Canada = is_connected_with(Beverley_J_Oda)
    United_States = is_connected_with(Beverley_J_Oda)
    return Government_Canada, United_States, Beverley_J_Oda

def Legislature_Canada_Make_a_visit(Legislature_Canada, Kenya, Beverley_J_Oda):
    Legislature_Canada = make_a_visit(Kenya)
    Legislature_Canada = is_connected_with(Beverley_J_Oda)
    Kenya = is_connected_with(Beverley_J_Oda)
    return Legislature_Canada, Kenya, Beverley_J_Oda
'''


Turn 2:
# 3 turns left to provide final answer. you can request the entity you are not sure to increase your confidency. You can only request one entity per time. If you are very sure about the answer, please answer directly.
Thought 2: Please give me more information of Czech Republic
Act 2: Request["Bev Oda"]
Observation 2: 
'''
import is_connected_with, continent, country_of_citizenship

def connect_Bev_Oda_to_Canada(Bev_Oda, Canada, node):
    node = is_connected_with(Bev_Oda)
    node = is_connected_with(Canada)
    Bev_Oda = continent(Canada)
    return Bev_Oda, Canada, node

def connect_Bev_Oda_to_Conservative_Party(Bev_Oda, Conservative_Party_of_Canada, node):
    node = is_connected_with(Bev_Oda)
    node = is_connected_with(Conservative_Party_of_Canada)
    Bev_Oda = country_of_citizenship(Conservative_Party_of_Canada)
    return Bev_Oda, Conservative_Party_of_Canada, node

'''

Turn 3:
# 2 turns left to provide final answer. you can request the entity you are not sure to increase your confidency. You can only request one entity per time. If you are very sure about the answer, please answer directly.
Thought 3: Based on the observation, 'Bev Oda' appears to be highly similar to 'Beverley J. Oda' as they both are associated with Canada and the Conservative Party of Canada. Given the strong similarity in the context, I am confident that 'Bev Oda' is the correct match.
Act 3: Terminate["Bev Oda"]
################### Your Answer Ends Here: ################### 
------------------------------ Example2 End ------------------------------ 

[USER (Boss)]: Give me the aligned entity of the target entity from candidates entity list. If there is same entity, please select directly. Please select from candiates! The target entity is:
Salauddin

The Candidate entities list is: 
['American Institute in Taiwan', 'Liberty Korea Party', 'Shiv Sena', 'National Iranian Oil Company', 'Sprint Corporation', 'Korean Central News Agency', 'Tin Oo', 'Shinzo Abe', 'Intouch Holdings', 'Shin Bet', 'China National Petroleum Corporation', 'Eric Chu', 'Fatos Nano', 'Khin Yi', 'Seoul National University', 'Sirindhorn', 'Singapore', 'Formosa Plastics Group', 'Oracle Corporation', 'Phil Goff', 'Seiso Moyo', 'National League for Democracy', 'Syrian National Council', 'Google']

NOTE: Please follow my example between "Example{i} Start" and "Example{i} End" above to answer task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem. 

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'. Your answer must be in candidate list, otherwise, you will got finned. 
Thought 1:

"""
