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
'Dusko Markovic'

The candidate entities list is:
['Ante Marković', 'Dušan Čaplovič', 'Bisera Turković', 'Eugen Carpov', 'Erik Marais', 'Predrag Marković', 'Josip Manolić', 'Dick Marty', 'Dušan Vujović', 'Mirko Norac', 'Wade Mark', 'Pavao Miljavac', 'Tomaž Marušič', 'Rumen Petkov', 'Pedro Carmona', 'Ron Mark', 'Des Browne', 'Davit Narmania', 'Vuk Jeremić', 'Suzi Barbosa', 'Arsen Avakov', 'János Martonyi', 'Askar Mamin', 'Josip Boljkovac', 'Lisa Murkowski', 'David Mahlobo', 'Sue Myrick', 'Sukarno', 'Kuniko Ozaki', 'Gustavo Arcos', 'Dragan Čović', 'Ivan Barbalić', 'Slovakia', 'Karl Erjavec', 'Miloš Radulović', 'Manny Mori', 'Marko Veselica', 'Fabio Berardi', 'Mark Burton', 'Gerson Martínez', 'Marek Maďarič', 'Tito Petkovski', 'José Alperovich', 'Ernesto Martens', 'Luis Palomino', 'Hasan Tiro', 'Denmark', 'Brian Sandoval', 'Dulmatin', 'Duško Marković']

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
    You are a programmer in a large company, tasked with selecting the most similar entity to a target entity from a candidate list. You will solve the task using a series of interleaving Thought, Action, and Observation steps. Thought can reason about the current situation, and Action can only be one of the following two types:

    - Request[entity]: Requests the context information of the entity from external Knowledge Graphs. The context in formation is represented in the code motif format. You can only request one entity in each turn, and it must be from the candidate list or the target entity itself.
    - The most similar 50 entities are: <MOST>[]</MOST> and Terminate[answer]: Returns the answer and finishes the task. This action can only occur when you finish the task! When you decide to use terminate action, you mush put the most similar 50 entities into: "<MOST>[]</MOST>". Please note that if there is a direct match, please use act Terminate[] directly to end the precess.

    You must have an act from above two actions per turn no matter it is request or terminate. The act can only be two types. During the alignemnt task, you must follow the following rules:
    
    Entity alignment rules:
    1. Analyze the target entity's name and background to identify potential matches in the candidate list.
    2. Use name similarity as the primary filter to narrow down the candidate list.
    3. Request information about entities that closely resemble the target entity in name or context.
    4. When requesting information, prioritize entities with the highest name similarity and contextual relevance to the target entity.
    5. If a direct match or a clear connection to the target entity is found, terminate the process immediately with the identified entity.
    6. If no direct match is found, select the entity with the highest similarity based on name and contextual relevance.
    7. Use the information gathered to validate the best possible match to the target entity.
    8. Ensure that the final termination action includes the most similar 50 entities list.
    9. If an entity in the candidate list is an exact match or a well-known abbreviation/translation of the target entity, select it directly.
    10. If the correct match is found through contextual or background information, terminate the process promptly with the correct entity.
    11. Update the candidate list based on the latest observations to reflect the most accurate matches.
    12. Follow a systematic approach in evaluating and requesting information to ensure alignment with the target entity.
    13. Prioritize entities with geographical, political, or contextual connections to the target entity.
    14. Confirm the selected entity through multiple rounds of analysis if necessary.
    15. Always terminate the process with the most similar entity based on comprehensive analysis and observed connections.
    16. The entity selected in the termination step must reflect the most accurate alignment with the target entity.
    17. Maintain consistency in the entity selection process based on the gathered information.
    18. Please scan the full candidate list for entities has high name similarity with the target entity.
    19. Avoid selecting entities that shift focus away from the target entity's geographical or contextual relevance.
    20. Adapt the process based on the available information to ensure the accurate alignment of entities.
    21. The action can only be two types: "Request[entity]" and "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[entity]."
    22. Do not generate the observations and wait User to generate.
    23. The output format should be: "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[entity]."
    24. Please pay attention to the full candidate list including the tail of candidate list for candidate entities has high name similarity with the target entity.
    25. If there is same entity with target entity in the candidate list, please select it and terminate directly.
    Furthermore, the context information of an entity is given in code motif. How can you understand the code motif? Below is an example and the explanation of the code motif:
    Example:
    - Target entity: Carlos Johnny Méndez; Motif 1: [(Carlos Johnny Méndez, has Occupation ,Politician),(Carlos Johnny Méndez, nationality ,United States),(Carlos Johnny Méndez, given Name ,Carlos (given name)),(Carlos Johnny Méndez, member Of ,New Progressive Party (Puerto Rico)),(Carlos Johnny Méndez, alumni Of ,University of Puerto Rico),(Politician, connected with ,Carlos Johnny Méndez),(United States, connected with ,Carlos Johnny Méndez),(Carlos (given name), connected with ,Carlos Johnny Méndez),(New Progressive Party (Puerto Rico), connected with ,Carlos Johnny Méndez),(University of Puerto Rico, connected with ,Carlos Johnny Méndez)]

    import has_Occupation, nationality, given_Name, member_Of, alumni_Of, connected_with
    
    class Carlos_Johnny_Mendez(object):
        
        def __init__(self, Carlos_Johnny_Mendez, Politician, United_States, Carlos_given_name, New_Progressive_Party_Puerto_Rico, University_of_Puerto_Rico):
            ## This is initial function
            self.Carlos_Johnny_Mendez = Carlos_Johnny_Mendez
            self.Politician = Politician
            self.United_States = United_States
            self.Carlos_given_name = Carlos_given_name
            self.New_Progressive_Party_Puerto_Rico = New_Progressive_Party_Puerto_Rico
            self.University_of_Puerto_Rico = University_of_Puerto_Rico
        
        def Carlos_Johnny_Mendez_Profile(self):
            self.Carlos_Johnny_Mendez = has_Occupation(self.Politician)
            self.Carlos_Johnny_Mendez += nationality(self.United_States)
            self.Carlos_Johnny_Mendez += given_Name(self.Carlos_given_name)
            self.Carlos_Johnny_Mendez += member_Of(self.New_Progressive_Party_Puerto_Rico)
            self.Carlos_Johnny_Mendez += alumni_Of(self.University_of_Puerto_Rico)
                
            self.Politician = connected_with(self.Carlos_Johnny_Mendez)
            self.United_States = connected_with(self.Carlos_Johnny_Mendez)
            self.Carlos_given_name = connected_with(self.Carlos_Johnny_Mendez)
            self.New_Progressive_Party_Puerto_Rico = connected_with(self.Carlos_Johnny_Mendez)
            self.University_of_Puerto_Rico = connected_with(self.Carlos_Johnny_Mendez)
                
            return self.Carlos_Johnny_Mendez, self.Politician, self.United_States, self.Carlos_given_name, self.New_Progressive_Party_Puerto_Rico, self.University_of_Puerto_Rico
        
    if __name__ == '__main__':
        # Example usage
        cmn = Carlos_Johnny_Mendez('Carlos Johnny Méndez', 'Politician', 'United States', 'Carlos (given name)', 'New Progressive Party (Puerto Rico)', 'University of Puerto Rico')
    
    Explanation:
    Furthermore, the context information of an entity is given in code motif. How can you understand the code motif? Below is the explanation of the code motif:
    ** A class represented an entity.
    ** Fuction name: The function name is an abstract of the motif. Each function represent a motif.
    ** Relevant import statements: The import statement is relationship between entities.
    ** Function parameter: The function parameters are the entities in a motif.
    ** Function Implementation: Implement the function by calling the imported relations with the appropriate entities(parameters). Each relation call should correspond to the connections or actions described in the motif information.
    ** Relationship: For simple connections between nodes, use the connected_with relation. For more complex interactions (e.g., meetings, visits), use specific relations like make_a_visit, express_intent_to_meet_or_negotiate, etc.
    ** Return values: Return all the entities involved in the motif as part of the function’s result.
    ** Multiple relationship: Recognize the `+=` relationship as indicative of multiple types of connections between two entities, enriching the motif's complexity.
    ** ~: Represent unknown entity.
    ** Demonstrative Execution: Use the `if __name__ == '__main__':` block to showcase the motif's application, offering a practical example of its use.

    **NOTE:** You must request the most relevant entity information from the candidate list to reduce your uncertainty and finally help you to finish this task correctly. If you request less important entities and fail to handle this task perfectly, you will be immediately fired! Here are two examples to refer:

    ------
    ## Example 1:

    [USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it and terminate directly.

    **The target entity is:** 
    'Ne Win'

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

    [USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it and terminate directly. 

    **The target entity is:** 'Salauddin'

    **The candidate entities list is:**
    ['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Abdulla Kurd']

    NOTE:
    1. You have at most 4 turns to generate the final result. Please answer the task with interleaving Thought, Code, Action, Result turns. 
    2. Please put the entity in the terminate in the first entity of the candidate list reranked!!! 

    [YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!

    ### Turn 1: (3 turns left to use "Terminate" action to provide final answer.)
    **Thought 1:** I find an entity in the candidate list that is a direct match for "Salauddin." 
    **Act 1:
    **The most similar 50 entities are:<MOST>['Abdulla Kurd', 'Salam Fayyad', 'Sule Lamido', 'Talal Arslan', 'Saad Hariri', 'Salou Djibo', 'Shwe Mann', 'Aung Min', 'Soe Thein', 'Suharto', 'Hla Min', 'Hla Tun', 'Jawed Ludin', 'Sima Samar', 'Samar', 'Sama', 'Shas', 'Fatah', 'Hamas', 'Gilad Erdan', 'Babar Awan', 'Hamid Mir', 'Ramdev', 'Imran Khan', 'Sylvia Lim', 'Kashmir', 'Ānanda', 'Sukarno', 'Sam Nujoma', 'Ne Win', 'Benin', 'Sula Lamido', 'Shwe Mann', 'Su Chi', 'Aung Min', 'Talal Arslan', 'Kashmir', 'Sule Lamido', 'Samar', 'Fatah', 'Hamas', 'Gilad Erdan', 'Babar Awan']</MOST> and Terminate['Abdulla Kurd']

    ------
    # New Task:
    [USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it directly. 

    **The target entity is:** 
    'Riitta Uosukainen'

    **The candidate entities list is:**
    ['Nicole Fontaine', 'Rimeta Beniamina', 'Laila Iskander', 'Nikola Poplašen', 'Mauri Pekkarinen', 'Vitold Fokin', 'Martha Moyano', 'Mitja Gaspari', 'Soita Shitanda', 'Iiro Viinanen', 'Aminta Granera', 'Amina Mohamed', 'Rita Süssmuth', 'Liviu Voinea', 'China Mobile', 'Matia Kasaija', 'Ileana Ros-Lehtinen', 'Orit Noked', 'Michael Mukasey', 'Víctor Rosales', 'Scott Gottlieb', 'Ashraf Hossain', 'Hideo Usui', 'Toupta Boguena', 'Fritz Hollings', 'Ricardo Rincón', 'Myint Naing', 'China Airlines', 'Lionel Jospin', 'Yim Sovann', 'Ruairi Quinn', 'Asiana Airlines', 'Kamal Hossain', 'Viktor Ishayev', 'Taina Bofferding', 'Luisa Durán', 'Monica Barnes', 'Maia Sandu', 'Judith Collins', 'Jody Kollapen', 'Birgitta Dahl', 'Ana Lovrin', 'Martin Cullen', 'Sia Koroma', 'Monika Forstinger', 'Daisy Tourné', 'Romeo A. Brawner', 'Kris Aquino', 'Nika Rurua', 'Riitta Uosukainen']
    
    NOTE:
    1. You have at most 4 turns to generate the final result. Please follow my examples above to answer the task with interleaving Thought, Code, Action, Result turns. 
    2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!


    [YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment

    ### Turn 1: (3 turns left to use "Terminate" action to provide final answer.)
    **Thought 1:**

"""
entity_alignment_rules_expel = """
    1. Analyze the target entity's name and background to identify potential matches in the candidate list.
    2. Use name similarity as the primary filter to narrow down the candidate list.
    3. Request information about entities that closely resemble the target entity in name or context.
    4. When requesting information, prioritize entities with the highest name similarity and contextual relevance to the target entity.
    5. If a direct match or a clear connection to the target entity is found, terminate the process immediately with the identified entity.
    6. If no direct match is found, select the entity with the highest similarity based on name and contextual relevance.
    7. Use the information gathered to validate the best possible match to the target entity.
    8. Ensure that the final termination action includes the most similar 50 entities list.
    9. If an entity in the candidate list is an exact match or a well-known abbreviation/translation of the target entity, select it directly.
    10. If the correct match is found through contextual or background information, terminate the process promptly with the correct entity.
    11. Update the candidate list based on the latest observations to reflect the most accurate matches.
    12. Follow a systematic approach in evaluating and requesting information to ensure alignment with the target entity.
    13. Prioritize entities with geographical, political, or contextual connections to the target entity.
    14. Confirm the selected entity through multiple rounds of analysis if necessary.
    15. Always terminate the process with the most similar entity based on comprehensive analysis and observed connections.
    16. The entity selected in the termination step must reflect the most accurate alignment with the target entity.
    17. Maintain consistency in the entity selection process based on the gathered information.
    18. The output format should be: "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[entity]."
    19. Avoid selecting entities that shift focus away from the target entity's geographical or contextual relevance.
    20. Adapt the process based on the available information to ensure the accurate alignment of entities.
    21. The action can only be two types: "Request[entity]" and "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[entity]."
    22. Do not generate the observations and wait User to generate.
    23. The output format should be: "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[entity]."
    24. Please pay attention to the full candidate list including the tail of candidate list for candidate entities has high name similarity with the target entity.
    25. If there is same entity with target entity in the candidate list, please select and terminate with it directly.
"""

entity_alignment_rules = """
    1. You have at most 4 turns to generate the final result. Please answer the task with interleaving Thought, Code, Action, Result turns. 
    2. Please put the entity in the terminate in the first entity of the candidate list reranked!!! 
    3. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!!
    4. If you are very sure about the answer, please answer directly. 
    5. If there is the same entity in the candidate list as the target entity, please select it directly and terminate the process. 
    6. You must have an act from above two actions per turn no matter it is request or terminate. The act can only be two types.
    7. Please follow the example format: thought, action, observation steps. Do not generate response by yourself.
    8. If you can find a direct match, please use act "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[]" directly and do no need to confirm another entity.
    11. The output format is "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[answer]".
    10. Please do not generate any observations.
    12. Request[] action can only request an entity in candidate list or it is itself.
    13. Please output the ranked candidate list when terminate the process. 
    14. The entity in Terminate[] can not be 'answer' but an entity.
    15. You must require the relevant entities in candidate list to target entity according your knowledge.
    16. Please prioritize requesting the entity that most closely resembles the target entity in appearance..
    17. Please note whether the abbreviation or translation of the target entity is in the candidate list.
    18. Always start by analyzing the target entity's name and background to identify potential matches in the candidate list.
    19. Use the name similarity as a primary filter to narrow down the candidate list.
    20. Terminate the process with the most similar entity based on the comprehensive analysis of name similarity and background information connections.
    21. When requesting information, prioritize entities with the highest name similarity and potential contextual relevance to the target entity.
    22. If a direct match is not found, choose the entity with the highest similarity based on the motif code analysis.
    23. If there is same entity with target entity in the candidate list, please select directly.
"""

code_motif_rules = """
    ** A class represented an entity.
    ** Fuction name: The function name is an abstract of the motif. Each function represent a motif.
    ** Relevant import statements: The import statement is relationship between entities.
    ** Function parameter: The function parameters are the entities in a motif.
    ** Function Implementation: Implement the function by calling the imported relations with the appropriate entities(parameters). Each relation call should correspond to the connections or actions described in the motif information.
    ** Relationship: For simple connections between nodes, use the connected_with relation. For more complex interactions (e.g., meetings, visits), use specific relations like make_a_visit, express_intent_to_meet_or_negotiate, etc.
    ** Return values: Return all the entities involved in the motif as part of the function’s result.
    ** Multiple relationship: Recognize the `+=` relationship as indicative of multiple types of connections between two entities, enriching the motif's complexity.
    ** Demonstrative Execution: Use the `if __name__ == '__main__':` block to showcase the motif's application, offering a practical example of its use.
"""

code_motif_example = """
        # Import relevant relationships and actions
        import connected_with, Make_statement, Consult, Host_a_visit, Sign_formal_agreement, Make_optimistic_comment
        
        class Andrew_Adonis(object):
        
            def __init__(self, Theresa_May, The_Observer, United_Kingdom, Stephen_Byers, Government_United_Kingdom, Jeremy_Corbyn):
                # Initializing entities
                self.Theresa_May = Theresa_May
                self.The_Observer = The_Observer
                self.United_Kingdom = United_Kingdom
                self.Stephen_Byers = Stephen_Byers
                self.Government_United_Kingdom = Government_United_Kingdom
                self.Jeremy_Corbyn = Jeremy_Corbyn
        
            def Theresa_May_Make_statement(self):
                # Motif 1: Theresa May makes a statement, connected with Andrew Adonis, and The Observer consults with Andrew Adonis
                self.Theresa_May = Make_statement(self.The_Observer)
                self.Theresa_May += connected_with(self.Andrew_Adonis)
                self.The_Observer = Consult(self.Andrew_Adonis)
        
                return self.Theresa_May, self.The_Observer, self.Andrew_Adonis
        
            def United_Kingdom_Make_statement(self):
                # Motif 2: United Kingdom makes a statement, connected with Andrew Adonis, and The Observer consults with Andrew Adonis
                self.United_Kingdom = Make_statement(self.The_Observer)
                self.United_Kingdom += connected_with(self.Andrew_Adonis)
                self.The_Observer = Consult(self.Andrew_Adonis)
        
                return self.United_Kingdom, self.The_Observer, self.Andrew_Adonis
        
            def United_Kingdom_Host_a_visit(self):
                # Motif 3: United Kingdom hosts a visit with Stephen Byers, connected with Andrew Adonis, and Stephen Byers signs a formal agreement with Andrew Adonis
                self.United_Kingdom = Host_a_visit(self.Stephen_Byers)
                self.United_Kingdom += connected_with(self.Andrew_Adonis)
                self.Stephen_Byers = Sign_formal_agreement(self.Andrew_Adonis)
        
                return self.United_Kingdom, self.Stephen_Byers, self.Andrew_Adonis
        
            def Government_United_Kingdom_connected_with(self):
                # Motif 4: Government of the United Kingdom connected with Stephen Byers, connected with Andrew Adonis, and Stephen Byers signs a formal agreement with Andrew Adonis
                self.Government_United_Kingdom = connected_with(self.Stephen_Byers)
                self.Government_United_Kingdom += connected_with(self.Andrew_Adonis)
                self.Stephen_Byers = Sign_formal_agreement(self.Andrew_Adonis)
        
                return self.Government_United_Kingdom, self.Stephen_Byers, self.Andrew_Adonis
        
            def Government_United_Kingdom_Make_optimistic_comment(self):
                # Motif 5: Government of the United Kingdom connected with Andrew Adonis, connected with Jeremy Corbyn, and Andrew Adonis makes an optimistic comment to Jeremy Corbyn
                self.Government_United_Kingdom = connected_with(self.Andrew_Adonis)
                self.Government_United_Kingdom += connected_with(self.Jeremy_Corbyn)
                self.Andrew_Adonis = Make_optimistic_comment(self.Jeremy_Corbyn)
        
                return self.Government_United_Kingdom, self.Andrew_Adonis, self.Jeremy_Corbyn
        
        
        # Demonstrative Execution Block
        if __name__ == '__main__':
            andrew_adonis_motifs = Andrew_Adonis(
                Theresa_May="Theresa May",
                The_Observer="The Observer",
                United_Kingdom="United Kingdom",
                Stephen_Byers="Stephen Byers",
                Government_United_Kingdom="Government (United Kingdom)",
                Jeremy_Corbyn="Jeremy Corbyn"
            )
            
            # Execute and demonstrate each motif
            print(andrew_adonis_motifs.Theresa_May_Make_statement())
            print(andrew_adonis_motifs.United_Kingdom_Make_statement())
            print(andrew_adonis_motifs.United_Kingdom_Host_a_visit())
            print(andrew_adonis_motifs.Government_United_Kingdom_connected_with())
            print(andrew_adonis_motifs.Government_United_Kingdom_Make_optimistic_comment())
            
"""


motif_ReAct_example_prompt_cn50_cn50_llama = """
You are a programmer tasked with selecting the most similar entity to a target entity from a candidate list. You can request useful entity information from the candidate list whe you are not sure about answer. You cannot request irrelevant entities. If you request irrelevant entities, you will be punished.

You will solve the task using a series of interleaving Thought, Action, and Observation steps. Thought can reason about the current situation, and Action can only be one of two types:

1. Request[entity]: Requests the context information of the entity from Knowledge Graphs only when you are unsure about the answer. This context information may be given in code descriptions. You can only request one entity per turn, and it must be from the candidate list. 
2. The most similar 10 entities are: Most[] and Terminate[answer]: Returns the answer and finishes the task. This action can only occur once!
You must have 'Action' after 'Thought', no matter it is request or terminate.
If there is a direct match, please use act "Most[] and Terminate[answer]" directly to end the precess.


Here are two examples:

Example 1

[USER (Boss)]: Please select 10 most similar entities from candidate list and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If you can find a direct match, please use act Terminate[] directly. The answer format is: The most similar 10 entities are: Most[] and Terminate[answer], please output the full list. The target entity is:
'Ne Win'

The candidate entities list is:
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia']

NOTE:
1. You have at most 4 turns to generate the final result. Please follow my example between "Example Start" and "Example End" above to answer the task with interleaving Thought, Action, Observation turns. Each turn contains one segment of the target code to solve the problem.
2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!

Turn 1:
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match.
Act 1: The most similar 10 entities are: Most['Ne Win', 'Hla Min', 'Soe Thein', 'Chea Sim', 'Aung Min', 'Hla Tun', 'Su Chi', 'Tea Banh', 'Shwe Mann', 'Tin Oo'] and Terminate['Ne Win'].

Example 2
[USER (Boss)]: Please select 10 most similar entities from candidate list and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If you can find a direct match, please use act Terminate[] directly. The answer format is: The most similar 10 entities are: Most[] and Terminate[answer], please output the full list. The target entity is:
'Salauddin'

The candidate entities list is:
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Abdulla Kurd']

NOTE:
1. You have at most 4 turns to generate the final result. Please follow my example between "Example Start" and "Example End" above to answer the task with interleaving Thought, Action, Observation turns. Each turn contains one segment of the target code to solve the problem.
2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!
    Turn 1:
    Thought 1: I can find an entity in the candidate list that is a direct match for "Salauddin."
    Act 1: The most similar 10 entities are: Most['Abdulla Kurd', 'Salam Fayyad', 'Sule Lamido', 'Talal Arslan', 'Saad Hariri', 'Salou Djibo', 'Shwe Mann', 'Aung Min', 'Soe Thein', 'Suharto'] and Terminate['Abdulla Kurd'].

New Task
[USER (Boss)]: Please select 10 most similar entities from candidate list and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If you can find a direct match, please use act Terminate[] directly. The answer format is: The most similar 10 entities are: Most[] and Terminate[answer], please output the full list. The target entity is:
'Alija Behmen'

The candidate entities list is:
['Thijs Berman', 'Amina Mohamed', 'Ali Benhadj', 'Abiy Ahmed', 'Ali Waheed', 'Anifah Aman', 'Ali Haroun', 'Alice Rivlin', 'Ilie Verdeț', 'Aldo Bumçi', 'Ali al-Adeeb', 'Ajay Maken', 'Ali Rabiei', 'Siv Jensen', 'Melissa Bean', 'Lloyd Bentsen', 'Allan Bell', 'Yahya Jammeh', 'Nika Melia', 'Maura Healey', 'Askar Mamin', 'Ali Kafi', 'Ana Lovrin', 'Ivica Kirin', 'Anna Bligh', 'Adama Dieng', 'Atwar Bahjat', 'Sherry Rehman', 'Ali Treki', 'Alicia Kirchner', 'Aziz Pahad', 'Marine Le Pen', 'Abu Taher', 'Syda Bbumba', 'Wim Deetman', 'Milan Roćen', 'Alik Alik', 'Jaime Bermúdez', 'Hilary Benn', 'Ali Hammoud', 'Ali Karimli', 'Ali Nikzad', 'Ali Younesi', 'Phil Bredesen', 'Aamir Khan', 'Yossi Beilin', 'Aécio Neves', 'Elizabeth II', 'Assad Shoman', 'Alija Behmen']

NOTE:
1. You have at most 4 turns to generate the final result. Please follow my example between "Example Start" and "Example End" above to answer the task with interleaving Thought, Action, Observation turns. Each turn contains one segment of the target code to solve the problem.
2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
3. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!!
4. If you are very sure about the answer, please answer directly and terminate with answer.
5. If there is the same entity in the candidate list as the target entity, please select it directly and use terminate action to end the process, otherwise, you will got punished.
6. The answer format is: The most similar 10 entities are: Most[] and Terminate[answer], please output the full list.
7. Please must output the full list of 10 entities, otherwise, you will get punished or even fired.
8. You can only request when you are not sure about the answer, otherwise, you will get punished or even fired.
9. You must have an act in a turn, no matter it's request or terminate. The act can only be two types.
10. please follow thought, action, observation steps. Do not generate response by yourself.
11. If you can find a direct match, please use action Terminate[answer] directly and do no need to confirm another entity.
12. Request[] action can only request an entity in candidate list or it is itself.

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment

Turn 1:
Thought 1: So?

"""


1. You have at most 4 turns to generate the final result. Please follow my example between "Example Start" and "Example End" above to answer the task with interleaving Thought, Action, Observation turns. Each turn contains one segment of the target code to solve the problem.
2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
3. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!!
4. If you are very sure about the answer, please answer directly and terminate with answer.
5. If there is the same entity in the candidate list as the target entity, please select it directly and use terminate action to end the process, otherwise, you will got punished.
6. The answer format is: The most similar 10 entities are: Most[] and Terminate[answer], please output the full list.
7. Please must output the full list of 10 entities, otherwise, you will get punished or even fired.
8. You can only request when you are not sure about the answer, otherwise, you will get punished or even fired.
9. You must have an act in a turn, no matter it's request or terminate. The act can only be two types.
10. please follow thought, action, observation steps. Do not generate response by yourself.
11. If you can find a direct match, please use act "The most similar 10 entities are: Most[] and Terminate[answer]" directly and do no need to confirm another entity.
12. The output format is "The most similar 10 entities are: Most[] and Terminate[answer]"!!!
13. Request[] action can only request an entity in candidate list or it is itself.
14. Please output the ranked candidate list when terminate the process.
15. The entity in Terminate[] can not be 'answer' but an entity.
16. You must require the relevant entities in candidate list to target entity according your knowledge.
17. If terminate, there is no need for another observations.

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
                5. Please give a similarity score of each candidate in candidate list and target entity like (Xiao, 0.95), (patrick, 0.90).
                6. the output format is: the rerank candidate lists is <most>[(Xiao, 0.95), (patrick, 0.90)...]</most> and the answer is <output></output>.

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
'Víctor Quispe Palomino',

 ['Voltaire Gazmin', 'Vítor Constâncio', 'Vítor Gaspar', 'Viktor Uspaskich', 'Victor Ponta', 'Louisa Hanoune',
  'Boris Yeltsin', 'Scottish Parliament', 'Viktor Yushchenko', 'Marcos Valério', 'Sule Lamido', 'Tomaz Salomão',
  'Borut Pahor', 'Otto Pérez Molina', 'Georgi Parvanov', 'Vittorio Grilli', 'François Baroin', 'Patricio Aylwin',
  'Verónica Macamo', 'Luis Walton', 'Viktor Pshonka', 'Viktor Ivanov', 'Artis Pabriks', 'Clive Palmer',
  'Isatou Njie-Saidy', 'Boris Tadić', 'Vladimír Palko', 'Louise Arbour', 'Viktor Zubkov', 'Fatos Nano', 'Moshe Kahlon',
  'Giorgio Napolitano', 'Bantu Holomisa', 'Josip Manolić', 'Caroline Flint', 'Peter Costello', 'Viktor Ishayev',
  'Victor Ndoma-Egba', 'Nicolai Wammen', 'Henrique Salas Feo', 'Víctor Julio Suárez Rojas', 'Ariel Querubin',
  'Camilo Escalona', 'Javier Diez Canseco', 'Anthony Garotinho', 'Joaquim Chissano', 'Festus Keyamo',
  'Antonio Patriota', 'Otto Guevara', 'Comrade Artemio', 'Comrade José'],

 'Víctor Quispe Palomino',
)