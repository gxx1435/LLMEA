"""
2. Generate only 'Thought' and 'Act' steps, and wait for the User to generate 'Observation'.
"""

prompts = """
    You are a programmer. You can request useful entities from a candidate list but must avoid requesting irrelevant entities. Failure to adhere to this will result in termination. Your task is to solve a question-answering problem using interleaving Thought, Action, and Observation steps.
    
    Thought: Reason about the current situation.
    Action: There are only two types of actions:
    Request[entity] - Requests the entity context information from Knowledge Graphs. The context information may be given in code descriptions. You can only request one entity per turn and it must be from the candidate list.
    Terminate[answer] - Returns the answer and finishes the task.
    Example
    [USER (Boss)]: Give me the most aligned entity of the target entity from the candidates entity list. If there is the same entity, please select it directly. 
    The target entity is: 
    'Salauddin'
    
    The Candidate entities list is:
    ['Salahuddin of Selangor', 'Slovenia', 'Riad Salamé', 'Hla Tun', 'Qadri Jamil', 'Sweden', 'Palau', 'Spain', 'Sheikh Hasina', 'Hla Min', 'Malaysia', 'Mohamed Nasheed', 'Ahmed Chalabi', 'Nabil Shaath', 'Sirindhorn', 'Japan', 'Abdo Hussameddin', 'Macky Sall', 'Salam Fayyad', 'Malawi', 'Mourad Dhina', 'Jawed Ludin', 'Macau', 'Abdulla Kurd']
    
    NOTE: You have at most 4 turns to generate the final results, meaning you must provide the answer by Thought 4. If you are certain about the answer, please answer directly.
    
    [YOU (Programmer)]: Let's break down the task and solve the Entity Alignment problem step-by-step!
    
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
    Act 4: Terminate['Abdulla Kurd']
    
    New Task
    You are performing an entity alignment task.

    [USER (Boss)]: Please sort the candidate list according to similarity to the target entity and select the most aligned entity. You have at most 4 turns to finish the task. If there is the same entity in the candidate list as the target entity, please select it directly. The answer format is: Terminate[answer]. The target entity is:
    The target entity is:
    {}
    
    The aligned entity is:
    {}
    
    The candidate entities list is: 
    {}
    
    Notes:
    1. Please generate the step-by-step thought process leading to the final answer.
    3. You must use Code Motif in the reasoning path. Refer to the example provided.
    4. Please generate some rules on how to write Code Motifs in <rule></rule> tags in the final turn.
    
    """.format('Party of the Revolution',
                'Chama Cha Mapinduzi',
               ['Party of Regions', 'Rally of the Republicans', 'State of Law Coalition', 'Party of Democratic Action',
                'Christine Boutin', 'Carlos De León', 'Park Taejoon', 'Beatrix of the Netherlands',
                'Sprint Corporation', 'Daily Nation', 'Daily Nation', 'Oracle Corporation', 'Friends of the Earth',
                'All Basotho Convention', 'Alliance for the Republic', 'Bank of Spain', 'Raymond Benjamin',
                'Margaret Wilson', 'Marcos Valério', 'Bank of Mexico', 'Chama Cha Mapinduzi'],

               )