motif_ReAct_example_prompt_cn10_cn10 = """
You are a programmer tasked with selecting the most similar entity to a target entity from a candidate list. You must request useful entity information from the candidate list, but you cannot request irrelevant entities. If you request irrelevant entities, you will be fired.

You will solve the task using a series of interleaving Thought, Action, and Observation steps. Thought can reason about the current situation, and Action can only be one of two types:

1. Request[entity]: Requests the context information of the entity from Knowledge Graphs. This context information may be given in code descriptions. You can only request one entity per turn, and it must be from the candidate list.
2. The most similar 10 entities are: <most>[]</most> and Terminate[answer]: Returns the answer and finishes the task. This action can only occur once!
Compare the background information of entities carefully to determine similarity.

Here are two examples:

Example 1

[USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is the same entity in the candidate list as the target entity, please select it directly. The answer format is: The most similar 10 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Ne Win'

The candidate entities list is:
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen']

NOTE:
1. You have at most 4 turns to generate the final result. Please follow my example between "Example Start" and "Example End" above to answer the task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem.
2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
3. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!!
4. If you are very sure about the answer, please answer directly. 
5. If there is the same entity in the candidate list as the target entity, please select it directly. 
6. The answer format is: The most similar 10 entities are: <most>[]</most> and Terminate[answer].

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!

Turn 1:
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match.
Act 1: The most similar 10 entities are: <most>[Ne Win, Hla Min, Soe Thein, Chea Sim, Hun Sen, Yen Ming, Benin, Jean Ping, Femen, Nokia]</most> and Terminate['Ne Win'].

Example 2
[USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is the same entity in the candidate list as the target entity, please select it directly. The answer format is: The most similar 10 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Salauddin'

The candidate entities list is:
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Salahuddin of Selangor', 'Spain', 'Valdivia', 'Abdulla Kurd']

NOTE:
1. You have at most 4 turns to generate the final result. Please follow my example between "Example Start" and "Example End" above to answer the task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem.
2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
3. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!!
4. If you are very sure about the answer, please answer directly. 
5. If there is the same entity in the candidate list as the target entity, please select it directly. 
6. The answer format is: The most similar 10 entities are: <most>[]</most> and Terminate[answer].

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!
    Turn 1:
    Thought 1: I cannot find an entity in the candidate list that is a direct match for "Salauddin." I need more information about "Salauddin" to make an informed decision.
    Act 1: Request['Salauddin']
    Observation 1:

    import engage_in_symbolic_act, provide_aid, impose_curfew, praise_or_endorse, express_intent_to_change_institutions_regime, occupy_territory, express_intent_to_cooperate_militarily
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
    Thought 2: Based on the observation, 'Salauddin' has connections with Bangladesh, India, and Pervez Musharraf. Considering this information, I should now request information about the most relevant candidate entity.
    Act 2: Request['Abdulla Kurd']
    Observation 2:

    import connected_with

    def Abdulla_Kurd_connected_with_1(Abdulla_Kurd, Turkey):
        unknown_entity = connected_with(Turkey)
        unknown_entity += connected_with(Abdulla_Kurd)
        Turkey = connected_with(Abdulla_Kurd)
        return unknown_entity, Turkey, Abdulla_Kurd

    Turn 3:
    Thought 3: Based on the observation, 'Abdulla Kurd' has connections with Turkey. Since 'Salauddin' has connections with regions including Bangladesh and India, I need to evaluate if there is a stronger match in the candidate list. Given this context, I should now request information about another potentially relevant candidate entity.
    Act 3: Request['Salahuddin of Selangor']
    Observation 3:

    import connected_with, educated_at, continent

    def Kuala_Lumpur_connected_with_Salahuddin_of_Selangor(Kuala_Lumpur, Salahuddin_of_Selangor, Malaysia):
        Kuala_Lumpur = connected_with(Salahuddin_of_Selangor)
        Kuala_Lumpur += educated_at(Malaysia)
        Salahuddin_of_Selangor = continent(Malaysia)
        return Kuala_Lumpur, Salahuddin_of_Selangor, Malaysia

    Turn 4:
    Thought 4: Based on the observation, 'Salahuddin of Selangor' is connected with Kuala Lumpur and Malaysia. This information is not as relevant as the connections 'Salauddin' has with Bangladesh, India, and Pervez Musharraf. The connections of 'Abdulla Kurd' with Turkey seem more aligned with the context of 'Salauddin'.
    Act 4:The most similar 10 entities are: <most>['Abdulla Kurd', 'Salou Djibo', 'Hla Min', 'Attajdid', 'Raila Odinga', 'Malawi', 'Bahrain', 'Malaysia', 'Spain', 'Valdivia']</most> and Terminate['Abdulla Kurd'].

New Task
[USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is the same entity in the candidate list as the target entity, please select it directly. The answer format is: The most similar 10 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Víctor Quispe Palomino'

The candidate entities list is:
['Voltaire Gazmin', 'Vítor Constâncio', 'Vítor Gaspar', 'Viktor Uspaskich', 'Victor Ponta', 'Louisa Hanoune', 'Boris Yeltsin', 'Scottish Parliament', 'Viktor Yushchenko', 'Marcos Valério', 'Comrade José']
 
NOTE:
1. You have at most 4 turns to generate the final result. Please follow my example between "Example Start" and "Example End" above to answer the task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem.
2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
3. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!!
4. If you are very sure about the answer, please answer directly. 
5. If there is the same entity in the candidate list as the target entity, please select it directly. 
6. The answer format is: The most similar 10 entities are: <most>[]</most> and Terminate[answer].

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment

Turn 1:
Thought 1:

"""

'Víctor Quispe Palomino'
['Voltaire Gazmin', 'Vítor Constâncio', 'Vítor Gaspar', 'Viktor Uspaskich', 'Victor Ponta', 'Louisa Hanoune',
 'Boris Yeltsin', 'Scottish Parliament', 'Viktor Yushchenko', 'Marcos Valério', 'Comrade José']

'Party of the Revolution'
['Party of Regions', 'Rally of the Republicans', 'State of Law Coalition', 'Party of Democratic Action', 'Christine Boutin', 'Carlos De León', 'Beatrix of the Netherlands', 'Park Tae-joon', 'Sprint Corporation', 'Daily Nation', 'Chama Cha Mapinduzi']


motif_ReAct_example_prompt_cn20_cn20 = """
You are a programmer tasked with selecting the most similar entity to a target entity from a candidate list. You must request useful entity information from the candidate list, but you cannot request irrelevant entities. If you request irrelevant entities, you will be fired.

You will solve the task using a series of interleaving Thought, Action, and Observation steps. Thought can reason about the current situation, and Action can only be one of two types:

1. Request[entity]: Requests the context information of the entity from Knowledge Graphs. This context information may be given in code descriptions. You can only request one entity per turn, and it must be from the candidate list.
2. The most similar 20 entities are: <most>[]</most> and Terminate[answer]: Returns the answer and finishes the task. This action can only occur once!
Compare the background information of entities carefully to determine similarity.

Here are two examples:

Example 1

[USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is the same entity in the candidate list as the target entity, please select it directly. The answer format is: The most similar 20 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Ne Win'

The candidate entities list is:
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh']

NOTE:
1. You have at most 4 turns to generate the final result. Please follow my example between "Example Start" and "Example End" above to answer the task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem.
2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
3. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!!
4. If you are very sure about the answer, please answer directly. 
5. If there is the same entity in the candidate list as the target entity, please select it directly. 
6. The answer format is: The most similar 20 entities are: <most>[]</most> and Terminate[answer].

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!

Turn 1:
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match.
Act 1: The most similar 20 entities are: <most>['Ne Win', 'Hla Min', 'Soe Thein', 'Aung Min', 'Hla Tun', 'Chea Sim', 'Hun Sen', 'Yen Ming', 'Bev Oda', 'Jean Ping', 'Ma Kai', 'Su Chi', 'Ta Nea', 'Meretz', 'Femen', 'Nokia', 'Spain', 'Benin', 'Serbia', 'Tea Banh']</most> and Terminate['Ne Win'].

Example 2
[USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is the same entity in the candidate list as the target entity, please select it directly. The answer format is: The most similar 20 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Salauddin'

The candidate entities list is:
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Abdulla Kurd']

NOTE:
1. You have at most 4 turns to generate the final result. Please follow my example between "Example Start" and "Example End" above to answer the task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem.
2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
3. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!!
4. If you are very sure about the answer, please answer directly. 
5. If there is the same entity in the candidate list as the target entity, please select it directly. 
6. The answer format is: The most similar 20 entities are: <most>[]</most> and Terminate[answer].

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!
    Turn 1:
    Thought 1: I cannot find an entity in the candidate list that is a direct match for "Salauddin." I need more information about "Salauddin" to make an informed decision.
    Act 1: Request['Salauddin']
    Observation 1:

    import engage_in_symbolic_act, provide_aid, impose_curfew, praise_or_endorse, express_intent_to_change_institutions_regime, occupy_territory, express_intent_to_cooperate_militarily
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
    Thought 2: Based on the observation, 'Salauddin' has connections with Bangladesh, India, and Pervez Musharraf. Considering this information, I should now request information about the most relevant candidate entity.
    Act 2: Request['Abdulla Kurd']
    Observation 2:

    import connected_with

    def Abdulla_Kurd_connected_with_1(Abdulla_Kurd, Turkey):
        unknown_entity = connected_with(Turkey)
        unknown_entity += connected_with(Abdulla_Kurd)
        Turkey = connected_with(Abdulla_Kurd)
        return unknown_entity, Turkey, Abdulla_Kurd

    Turn 3:
    Thought 3: Based on the observation, 'Abdulla Kurd' has connections with Turkey. Since 'Salauddin' has connections with regions including Bangladesh and India, I need to evaluate if there is a stronger match in the candidate list. Given this context, I should now request information about another potentially relevant candidate entity.
    Act 3: Request['Salahuddin of Selangor']
    Observation 3:

    import connected_with, educated_at, continent

    def Kuala_Lumpur_connected_with_Salahuddin_of_Selangor(Kuala_Lumpur, Salahuddin_of_Selangor, Malaysia):
        Kuala_Lumpur = connected_with(Salahuddin_of_Selangor)
        Kuala_Lumpur += educated_at(Malaysia)
        Salahuddin_of_Selangor = continent(Malaysia)
        return Kuala_Lumpur, Salahuddin_of_Selangor, Malaysia

    Turn 4:
    Thought 4: Based on the observation, 'Salahuddin of Selangor' is connected with Kuala Lumpur and Malaysia. This information is not as relevant as the connections 'Salauddin' has with Bangladesh, India, and Pervez Musharraf. The connections of 'Abdulla Kurd' with Turkey seem more aligned with the context of 'Salauddin'.
    Act 4: The most similar 20 entities are: <most>['Abdulla Kurd', 'Salou Djibo', 'Attajdid', 'Hla Min', 'Hla Tun', 'Bahrain', 'Malaysia', 'Palau', 'San Marino', 'Soe Thein', 'Spain', 'Valdivia', 'Malawi', 'Sinn Féin', 'Carl Levin', 'Tatarstan', 'Salzburg', 'Macau', 'Sirindhorn', 'Jawed Ludin']</most> and Terminate['Abdulla Kurd'].

New Task
[USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is the same entity in the candidate list as the target entity, please select it directly. The answer format is: The most similar 20 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Víctor Quispe Palomino'

The candidate entities list is:
['Voltaire Gazmin', 'Vítor Constâncio', 'Vítor Gaspar', 'Viktor Uspaskich', 'Victor Ponta', 'Louisa Hanoune', 'Boris Yeltsin', 'Scottish Parliament', 'Viktor Yushchenko', 'Marcos Valério', 'Sule Lamido', 'Tomaz Salomão', 'Borut Pahor', 'Otto Pérez Molina', 'Georgi Parvanov', 'Vittorio Grilli', 'François Baroin', 'Patricio Aylwin', 'Verónica Macamo', 'Luis Walton', 'Comrade José']

NOTE:
1. You have at most 4 turns to generate the final result. Please follow my example between "Example Start" and "Example End" above to answer the task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem.
2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
3. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!!
4. If you are very sure about the answer, please answer directly. 
5. If there is the same entity in the candidate list as the target entity, please select it directly. 
6. The answer format is: The most similar 20 entities are: <most>[]</most> and Terminate[answer].

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment

Turn 1:
Thought 1:

"""

'Party of the Revolution',
['Party of Regions', 'Rally of the Republicans', 'State of Law Coalition', 'Party of Democratic Action', 'Christine Boutin', 'Carlos De León', 'Park Taejoon', 'Beatrix of the Netherlands', 'Sprint Corporation', 'Daily Nation', 'Daily Nation', 'Oracle Corporation', 'Friends of the Earth', 'All Basotho Convention', 'Alliance for the Republic', 'Bank of Spain', 'Raymond Benjamin', 'Margaret Wilson', 'Marcos Valério', 'Bank of Mexico', 'Chama Cha Mapinduzi']


motif_ReAct_example_prompt_cn50_cn50 = """
You are a programmer tasked with selecting the most similar entity to a target entity from a candidate list. You must request useful entity information from the candidate list, but you cannot request irrelevant entities. If you request irrelevant entities, you will be fired.

You will solve the task using a series of interleaving Thought, Action, and Observation steps. Thought can reason about the current situation, and Action can only be one of two types:

1. Request[entity]: Requests the context information of the entity from Knowledge Graphs. This context information may be given in code descriptions. You can only request one entity per turn, and it must be from the candidate list.
2. The most similar 50 entities are: <most>[]</most> and Terminate[answer]: Returns the answer and finishes the task. This action can only occur once!
Compare the background information of entities carefully to determine similarity.

Here are two examples:

Example 1

[USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is the same entity in the candidate list as the target entity, please select it directly. The answer format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Ne Win'

The candidate entities list is:
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia']

NOTE:
1. You have at most 4 turns to generate the final result. Please follow my example between "Example Start" and "Example End" above to answer the task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem.
2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
3. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!!
4. If you are very sure about the answer, please answer directly. 
5. If there is the same entity in the candidate list as the target entity, please select it directly. 
6. The answer format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer].

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!

Turn 1:
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match.
Act 1: The most similar 50 entities are: <most>['Ne Win', 'Hla Min', 'Soe Thein', 'Chea Sim', 'Aung Min', 'Hla Tun', 'Su Chi', 'Tea Banh', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Benin', 'Yen Ming', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Serbia', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Ukraine', 'Zambia']</most> and Terminate['Ne Win'].

Example 2
[USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is the same entity in the candidate list as the target entity, please select it directly. The answer format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Salauddin'

The candidate entities list is:
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Abdulla Kurd']

NOTE:
1. You have at most 4 turns to generate the final result. Please follow my example between "Example Start" and "Example End" above to answer the task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem.
2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
3. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!!
4. If you are very sure about the answer, please answer directly. 
5. If there is the same entity in the candidate list as the target entity, please select it directly. 
6. The answer format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer].

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!
    Turn 1:
    Thought 1: I cannot find an entity in the candidate list that is a direct match for "Salauddin." I need more information about "Salauddin" to make an informed decision.
    Act 1: Request['Salauddin']
    Observation 1:
    
    import engage_in_symbolic_act, provide_aid, impose_curfew, praise_or_endorse, express_intent_to_change_institutions_regime, occupy_territory, express_intent_to_cooperate_militarily
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
    Thought 2: Based on the observation, 'Salauddin' has connections with Bangladesh, India, and Pervez Musharraf. Considering this information, I should now request information about the most relevant candidate entity.
    Act 2: Request['Abdulla Kurd']
    Observation 2:

    import connected_with
    
    def Abdulla_Kurd_connected_with_1(Abdulla_Kurd, Turkey):
        unknown_entity = connected_with(Turkey)
        unknown_entity += connected_with(Abdulla_Kurd)
        Turkey = connected_with(Abdulla_Kurd)
        return unknown_entity, Turkey, Abdulla_Kurd
        
    Turn 3:
    Thought 3: Based on the observation, 'Abdulla Kurd' has connections with Turkey. Since 'Salauddin' has connections with regions including Bangladesh and India, I need to evaluate if there is a stronger match in the candidate list. Given this context, I should now request information about another potentially relevant candidate entity.
    Act 3: Request['Salahuddin of Selangor']
    Observation 3:
    
    import connected_with, educated_at, continent
    
    def Kuala_Lumpur_connected_with_Salahuddin_of_Selangor(Kuala_Lumpur, Salahuddin_of_Selangor, Malaysia):
        Kuala_Lumpur = connected_with(Salahuddin_of_Selangor)
        Kuala_Lumpur += educated_at(Malaysia)
        Salahuddin_of_Selangor = continent(Malaysia)
        return Kuala_Lumpur, Salahuddin_of_Selangor, Malaysia
        
    Turn 4:
    Thought 4: Based on the observation, 'Salahuddin of Selangor' is connected with Kuala Lumpur and Malaysia. This information is not as relevant as the connections 'Salauddin' has with Bangladesh, India, and Pervez Musharraf. The connections of 'Abdulla Kurd' with Turkey seem more aligned with the context of 'Salauddin'.
    Act 4: The most similar 50 entities are: <most>['Abdulla Kurd', 'Salam Fayyad', 'Sule Lamido', 'Talal Arslan', 'Saad Hariri', 'Salou Djibo', 'Shwe Mann', 'Aung Min', 'Soe Thein', 'Suharto', 'Hla Min', 'Hla Tun', 'Jawed Ludin', 'Sima Samar', 'Samar', 'Sama', 'Shas', 'Fatah', 'Hamas', 'Gilad Erdan', 'Babar Awan', 'Hamid Mir', 'Ramdev', 'Imran Khan', 'Sylvia Lim', 'Kashmir', 'Ānanda', 'Sukarno', 'Sam Nujoma', 'Ne Win', 'Benin', 'Sula Lamido', 'Shwe Mann', 'Su Chi', 'Aung Min', 'Talal Arslan', 'Kashmir', 'Sule Lamido', 'Samar', 'Fatah', 'Hamas', 'Gilad Erdan', 'Babar Awan']</most> and Terminate['Abdulla Kurd'].

New Task
[USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is the same entity in the candidate list as the target entity, please select it directly. The answer format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Party of the Revolution'

The candidate entities list is:
['Party of Regions', 'Rally of the Republicans', 'State of Law Coalition', 'Party of Democratic Action',
 'Christine Boutin', 'Carlos De León', 'Beatrix of the Netherlands', 'Park Tae-joon', 'Sprint Corporation',
 'Daily Nation', 'Daily Nation', 'Oracle Corporation', 'Friends of the Earth', 'All Basotho Convention',
 'Alliance for the Republic', 'Bank of Spain', 'Raymond Benjamin', 'Margaret Wilson', 'Marcos Valério',
 'Bank of Mexico', 'Ralph Recto', 'Caroline Flint', 'Catherine Ashton', 'Harry Reid', 'Prince Johnson',
 'Perry Christie', 'Pete Wilson', 'Bank of China', 'Carl Levin', 'Bank of Ireland', 'Bornito de Sousa',
 'Arab Maghreb Union', 'Jay Weatherill', 'Mario Monti', 'Roy Chaderton', 'Parti Rakyat Malaysia', 'Marita Petersen',
 'Carlos Guerrero', 'Maroš Šefčovič', 'World Trade Organization', 'Pakalitha Mosisili', 'Carolina Cerqueira',
 'Arthur Chaskalson', 'Bank of America', 'Masayoshi Son', 'María Ángela Holguín', 'Rauf Aregbesola', 'Moshe Kahlon',
 'Carlos Gomes Júnior', 'Marwan Barghouti', 'Chama Cha Mapinduzi']


NOTE:
1. You have at most 4 turns to generate the final result. Please follow my example between "Example Start" and "Example End" above to answer the task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem.
2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
3. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!!
4. If you are very sure about the answer, please answer directly. 
5. If there is the same entity in the candidate list as the target entity, please select it directly. 
6. The answer format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer].

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment

Turn 1:
Thought 1:

"""

'Coalition for Democratic Unity'
['Croatian Democratic Union', 'Christian Democratic Party', 'Maldivian Democratic Party', 'Gabonese Democratic Party',
 'National Democratic Institute', 'Kurdistan Democratic Party', 'Botswana Democratic Party',
 'Slovenian Democratic Party', 'Forum for Democratic Change', 'Party of Democratic Action', 'Lebanese Democratic Party',
 'United Social Democratic Party', 'Rally of Democratic Forces', 'Fresh Democratic Party',
 'Nationwide Social Democratic Party', 'National Union for Democratic Progress', 'Brazilian Social Democracy Party',
 'New Democratic Party', 'Senegalese Democratic Party', 'Organisation of African Unity', 'Democratic Party',
 "United Peoples' Democratic Party", 'Christian Democratic Movement', 'African Christian Democratic Party',
 'National Patriotic Party', 'National Resurrection Party', 'United Democratic Movement', 'National Umma Party',
 'Popular Democratic Movement', 'National Coalition Party', 'Orange Democratic Movement', 'Croatian Peasant Party',
 "Convention People's Party", 'National League for Democracy', 'Cairo University', 'Independent Democrats',
 'Tunisian Pirate Party', 'Dalton McGuinty', 'Sprint Corporation', 'Oracle Corporation',
 'Lesotho Congress for Democracy', 'Pakistan Peoples Party', "Kurdistan Workers' Party", 'Caribbean Community',
 'National Medical Library', 'Bharatiya Janata Party', 'National Defense University', 'Verizon Communications',
 "People's United Democratic Movement", 'National Endowment for Democracy', 'Democratic Unity Roundtable']

'Party of the Revolution'
['Party of Regions', 'Rally of the Republicans', 'State of Law Coalition', 'Party of Democratic Action',
 'Christine Boutin', 'Carlos De León', 'Beatrix of the Netherlands', 'Park Tae-joon', 'Sprint Corporation',
 'Daily Nation', 'Daily Nation', 'Oracle Corporation', 'Friends of the Earth', 'All Basotho Convention',
 'Alliance for the Republic', 'Bank of Spain', 'Raymond Benjamin', 'Margaret Wilson', 'Marcos Valério',
 'Bank of Mexico', 'Ralph Recto', 'Caroline Flint', 'Catherine Ashton', 'Harry Reid', 'Prince Johnson',
 'Perry Christie', 'Pete Wilson', 'Bank of China', 'Carl Levin', 'Bank of Ireland', 'Bornito de Sousa',
 'Arab Maghreb Union', 'Jay Weatherill', 'Mario Monti', 'Roy Chaderton', 'Parti Rakyat Malaysia', 'Marita Petersen',
 'Carlos Guerrero', 'Maroš Šefčovič', 'World Trade Organization', 'Pakalitha Mosisili', 'Carolina Cerqueira',
 'Arthur Chaskalson', 'Bank of America', 'Masayoshi Son', 'María Ángela Holguín', 'Rauf Aregbesola', 'Moshe Kahlon',
 'Carlos Gomes Júnior', 'Marwan Barghouti', 'Chama Cha Mapinduzi']

'Shin Corp'
['Shin Bet', 'Tin Oo', 'Khin Yi', 'Sirindhorn', 'Phil Goff', 'Shiv Sena', 'Singapore', 'Su Chi', 'Peace Corps',
 'Khun Sa', 'Qin Gang', 'Shinzo Abe', 'Eric Chu', 'Nuon Chea', 'Shwe Mann', 'Jim Cooper', 'Sinn Féin', 'Tonio Borg',
 'Yin Zhuo', 'Bob Carr', 'Dave Camp', 'Sinopec', 'Than Shwe', 'Ron Kirk', 'Seiso Moyo', 'Selim Hoss', 'Emil Boc',
 'Than Htay', 'John Hogg', 'Manny Mori', 'Shimon Peres', 'Equinor', 'China', 'Ieng Sary', 'Citigroup', 'Sung Kim',
 'Sony', 'Civic Forum', 'Chea Sim', 'Hun Sen', 'Lin Yi-fu', 'Maung Oo', 'Shining Path', 'Ilir Meta', 'Penny Wong',
 'Don Polye', 'Hong Kong', 'Thein Nyunt', 'Fine Gael', 'Vic Toews', 'Intouch Holdings']

'Chui Sai On'
['Chea Sim', 'Ali Salman', 'Khun Sa', 'China', 'Wu Sike', 'Heng Samrin', 'Shwe Mann', 'Cui Tiankai', 'Aung San',
 'Xu Caihou', 'Abu Salem', 'Luis Walton', 'Hun Sen', 'Chris Bowen', 'Liu Zhijun', 'Paul Martin', 'Chen Zhili',
 'Ali Haroun', 'Abu Sayyaf', 'Ehud Barak', 'Ma Kai', 'Su Chi', 'The Gambia', 'Thailand', 'Sri Lanka', 'Pakistan',
 'Cuba', 'Chile', 'Wu Aiying', 'Spain', 'Chen Bingde', 'Baso Sangqu', 'Hui Liangyu', 'Your Party', 'Maung Oo', 'Crimea',
 'La Nación', 'Ne Win', 'Tony Tan', 'Chai Chidchob', 'Chang Wanquan', 'Li Baodong', 'Chee Soon Juan', 'Buju Banton',
 'Ieng Sary', 'Khin Yi', 'Edi Rama', 'Mus Sema', 'Chen Quanguo', 'Amos Sawyer', 'Fernando Chui']

'Baba Suwe',
['Babar Awan', 'Than Shwe', 'Bayan Muna', 'Bob Hawke', 'Bob Rae', 'Abu Salem', 'Mark Rutte', 'Hla Tun', 'Béla Bugár',
 'Csaba Hende', 'Palau', 'Wu Sike', 'Chea Sim', 'Bob Carr', 'Mike Duke', 'Barbados', 'Holy See', 'Macau', 'Navarre',
 'Khun Sa', 'Bola Tinubu', 'Baleka Mbete', 'Max Sisulu', 'Mus Sema', 'Fatah', 'Paul Biya', 'Aung San', 'Sam Sesay',
 'Malawi', 'Ambika Soni', 'Jacob Zuma', 'Pagan Amum', 'Kumba Ialá', 'Ratan Tata', 'Ma Kai', 'Ioan Rus', 'Bev Oda',
 'Fred Gumo', 'Marian Lupu', 'Sima Samar', 'Macky Sall', 'Bamir Topi', 'Hun Sen', 'Pape Diop', 'Basij', 'Hasan Bozer',
 'Gary Locke', 'David Laws', 'Susan Rice', 'Nika Rurua', 'Babatunde Omidina']

'Jomo Gbomo',
['John Nkomo', 'Comoros', 'Fred Gumo', 'Tony Momoh', 'José Bové', 'Jaime Trobo', 'John Hogg', 'Colombia', 'Morocco',
 'Bode George', 'Tonio Borg', 'Gideon Gono', 'Seiso Moyo', 'John Dalli', 'Joker Arroyo', 'Rosatom', 'Komeito',
 'Tom Ridge', 'Alan Gross', 'John Mahama', 'Boediono', 'Sam Nujoma', 'José Anaya', 'José Serra', 'John Garang',
 'John Key', 'Jim Cooper', 'Phil Goff', 'Roilo Golez', 'Joe Walsh', 'Julio Cobos', 'Tomaz Salomão', 'Jim Molan',
 'Boko Haram', 'Jacob Zuma', 'James Soong', 'Kosovo', 'Joe Biden', 'John Bercow', 'John Tsang', 'Hong Kong',
 'John Kerry', 'John Bruton', 'Jim Inhofe', 'Jordan', 'Gabon', 'Zimbabwe', 'Zambia', 'Cameroon', 'Namibia',
 'Henry Okah']

'Víctor Quispe Palomino',
 ['Voltaire Gazmin', 'Vítor Constâncio', 'Vítor Gaspar', 'Viktor Uspaskich', 'Victor Ponta', 'Louisa Hanoune',
  'Boris Yeltsin', 'Scottish Parliament', 'Viktor Yushchenko', 'Marcos Valério', 'Sule Lamido', 'Tomaz Salomão',
  'Borut Pahor', 'Otto Pérez Molina', 'Georgi Parvanov', 'Vittorio Grilli', 'François Baroin', 'Patricio Aylwin',
  'Verónica Macamo', 'Luis Walton', 'Viktor Pshonka', 'Viktor Ivanov', 'Artis Pabriks', 'Clive Palmer',
  'Isatou Njie-Saidy', 'Boris Tadić', 'Vladimír Palko', 'Louise Arbour', 'Viktor Zubkov', 'Fatos Nano', 'Moshe Kahlon',
  'Giorgio Napolitano', 'Bantu Holomisa', 'Josip Manolić', 'Caroline Flint', 'Peter Costello', 'Viktor Ishayev',
  'Victor Ndoma-Egba', 'Nicolai Wammen', 'Henrique Salas Feo', 'Víctor Julio Suárez Rojas', 'Ariel Querubin',
  'Camilo Escalona', 'Javier Diez Canseco', 'Anthony Garotinho', 'Joaquim Chissano', 'Festus Keyamo',
  'Antonio Patriota', 'Otto Guevara', 'Comrade Artemio', 'Comrade José']

"""
                You are a Entity Alignment expert, your task is according to the information I give to find the most similar entity
                from the given candidate list for the given entity. Please note that Motif is refers to a recurring subgraph pattern that appears
                within a larger graph. These motifs are typically small, distinct, and repeated structures that provide insights into 
                the structural and functional aspects of the graph.
                1. Please encapsulate the answer within <output> </output>.
                2. Please note the forms with and without underscores for entities.
                3. Please focus on entities with a small edit distance from the original entity.
                4. Please rerank the candidate list and put the answer in the first place of candidate list.
                5. the output format is: the rerank candidate lists is <most>[]</most> and the answer is <output></output>.

                === Target Entities Info starts: ===
                Entity Name: {}

                === Target Entities Info end ===

                === Candidate Entities starts: ===
                {}
                === Candidate Entities end ===

                --- Your Task starts: ---
                Target Entity: {}

                ---output format: ----
                The rerank candidate list is <most></most> and the answer is <output> xxxx </output>

                """.format(
'Chui Sai On',
['Chea Sim', 'Ali Salman', 'Khun Sa', 'China', 'Wu Sike', 'Heng Samrin', 'Shwe Mann', 'Cui Tiankai', 'Aung San',
 'Xu Caihou', 'Abu Salem', 'Luis Walton', 'Hun Sen', 'Chris Bowen', 'Liu Zhijun', 'Paul Martin', 'Chen Zhili',
 'Ali Haroun', 'Abu Sayyaf', 'Ehud Barak', 'Ma Kai', 'Su Chi', 'The Gambia', 'Thailand', 'Sri Lanka', 'Pakistan',
 'Cuba', 'Chile', 'Wu Aiying', 'Spain', 'Chen Bingde', 'Baso Sangqu', 'Hui Liangyu', 'Your Party', 'Maung Oo', 'Crimea',
 'La Nación', 'Ne Win', 'Tony Tan', 'Chai Chidchob', 'Chang Wanquan', 'Li Baodong', 'Chee Soon Juan', 'Buju Banton',
 'Ieng Sary', 'Khin Yi', 'Edi Rama', 'Mus Sema', 'Chen Quanguo', 'Amos Sawyer', 'Fernando Chui'],
 'Fernando Chui',
)