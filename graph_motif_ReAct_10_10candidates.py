motif_ReAct_example_prompt = """
You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity], which requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 50 entities after sort are: <most>[]</most> and Terminate[answer], which returns the answer and finishes the task.
Here are two examples.
Compare the background information of entities carefully to see if they are similar. 
------------------------------# Example1 Start ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity from candidates list. If there is same entity, please select directly. The target entity is:
'Ne Win'

The Candidate entities list is: 
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen']
 
NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select 10 most similar answer from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: The most similar 10 entities are: <most>['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen']</most> and Terminate['Ne Win']
------------------------------# Example1 End ------------------------------ 

------------------------------ Example2 Start ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity from candidates list. If there is same entity, please select directly. The target entity is:
'Salauddin'

The Candidate entities list is: 
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'Abdulla Kurd']

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
Act 4:The most similar 10 entities are: <most>['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'Abdulla Kurd']</most> and Terminate['Abdulla Kurd']

------------------------------ Example2 End ------------------------------ 


[USER (Boss)]:  Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity from candidates list. If there is same entity, please select directly. Please select from candiates! The target entity is:
Jomo Gbomo

The Candidate entities list is: 
['John Nkomo', 'Comoros', 'Fred Gumo', 'Tony Momoh', 'José Bové', 'Jaime Trobo', 'John Hogg', 'Colombia', 'Morocco', 'Bode George', 'Henry Okah']

NOTE: Please follow my example between "Example i Start" and "Example i End" above to answer task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem. 

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'. Your answer must be in candidate list, otherwise, you will got fired. 
Thought 1:

"""
