"""
2. Generate only 'Thought' and 'Act' steps, and wait for the User to generate 'Observation'.
"""
prompts = """
    You are doing an entity alignment task of two knowledge graphs (KGs), where you need to find the equivalent entity of the target entity. You have two task, one is generating new entity alignment rules, another is regenerate the correct reasoing process for the entity alignment case given. In the process of aligning the target entity to the correct answer, you MUST summarize some experience or rules in bullet point format that leads to correct answer.
    As a good learner, you learn from good and bad experiences of entity alignment task and want to regenerate a process lead to correct answer. You will solve the task using a series of interleaving Thought, Action, and Observation steps. Thought can reason about the current situation, and Action can only be one of the following two types:
    
    - Request[entity]: Requests the context information of the entity from external Knowledge Graphs. You can only request one entity in each turn, and it must be from the candidate list or the target entity itself.
    - The most similar 50 entities are: <MOST>[]</MOST> and Terminate[answer]: Returns the answer and finishes the task. This action can only occur when you finish the task! When you decide to use terminate action, you mush put the most similar 50 entities into: "<MOST>[]</MOST>". Please note that if there is a direct match, please use act Terminate[] directly to end the precess.

    You must have an act from above two actions per turn no matter it is request or terminate. The act can only be two types. 

    ------
    **Rules for Entity alignment**
    {}
    Task 1: Please add, delete, update the above entity alignment rules and keep it no more than 20 rules. Please enclose all the generated rules in a '<rule>' and '</rule>' tags like:
    
    Task 2: You should regenerate the following case later according to the target entity and correct answer. Remember use code motif for each request action in the regenerated process!!! 
    **Regenerated rules**: 
    1. Please read the case carefully and regenerate the step-by-step thought process of the case leading to the final correct answer.  
    2. Please follow the rules you generate during the regenerated process. 
    3. You must terminate the process with correct answer!
    4. Please pay attention to the correct answer in the last.
    5. Use code motif for each request action in the regenerated process!!!
    6. Please put the entity terminated with in the first entity of the reranked list!!!

    Below is the case of reasoning process need to be regenerated.
    ------
    **Case**:
    {}
    
    ------
    **Rule summarization & Regeneration**:
    ** Please generate some experience or rules in bullet point format that leads to correct answer.
    ** The case above is {}! Please generate the correct reasoning process of above case including observations, make target entity aligned with the correct answer. 
    The target entity is:
    {}
    
    [**Important!**]The correct answer(aligned entity) is:
    {}

    The candidate entities list is: 
    {}    

"""

prompts_0822 = """
    You are doing an entity alignment task of two knowledge graphs (KGs), where you need to find the equivalent entity of the target entity. You have two task, one is generating new entity alignment rules, another is regenerate the correct reasoing process for the entity alignment case given. In the process of aligning the target entity to the correct answer, you MUST summarize some experience or rules in bullet point format that leads to correct answer.
    As a good learner, you learn from good and bad experiences of entity alignment task and want to regenerate a process lead to correct answer. You will solve the task using a series of interleaving Thought, Action, and Observation steps. Thought can reason about the current situation, and Action can only be one of the following two types:
    
    - Request[entity]: Requests the context information of the entity from external Knowledge Graphs. You can only request one entity in each turn, and it must be from the candidate list or the target entity itself.
    - The most similar 50 entities are: <MOST>[]</MOST> and Terminate[answer]: Returns the answer and finishes the task. This action can only occur when you finish the task! When you decide to use terminate action, you mush put the most similar 50 entities into: "<MOST>[]</MOST>". Please note that if there is a direct match, please use act Terminate[] directly to end the precess.

    You must have an act from above two actions per turn no matter it is request or terminate. The act can only be two types. 

    ------
    **Rules for Entity alignment**
    <rule>
    1. You have at most 4 turns to generate the final result. Please answer the task with interleaving Thought, Code, Action, Result turns. 
    2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
    3. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!!
    4. If you are very sure about the answer, please answer directly. 
    5. If there is the same entity in the candidate list as the target entity, please select it directly and terminate the process. 
    6. You must have an act from above two actions per turn no matter it is request or terminate. The act can only be two types.
    7. Please follow the example format: thought, action, observation steps. Do not generate response by yourself.
    8. If you can find a direct match, please use act "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[]" directly and do no need to confirm another entity.
    11. The output format is "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[answer]".
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
    </rule>
    Task 1: Please add, delete, update the above entity alignment rules and keep it no more than 20 rules. Please enclose all the generated rules in a '<rule>' and '</rule>' tags.
    
    Task 2: You should regenerate the following case later according to the target entity and correct answer. Remember use code motif for each request action in the regenerated process!!! 
    **Regenerated rules**: 
    1. Please generate the step-by-step thought process leading to the final correct answer.
    2. You must use Code Motif in the reasoning path. Refer to the Case provided.
    3. The final answer in 'Terminate[answer]' should be the aligned entity given.
    4. please use code motif each turn in the reasoning process.
    5. You must align the target entity with correct answer given after the regeneration process.
    7. You must terminate with correct answer!
    8. Apply the entity alignment rules to the regeneration process.

    Below is the case of reasoning process need to be regenerated.
    ------
    **Case**:
    
    [USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it directly. 

    **The target entity is:** 
    Ruam Jai Thai

    **The candidate entities list is:**
    ['Rami Jarrah', 'Karam Ali Shah', 'Zhao Lianhai', 'Sai Mauk Kham', 'Luan Rama', 'Puan Maharani', 'Tan Jee Say', 'Hamzah Haz', 'Hamshahri', 'Rabi Ray', 'Bamir Topi', 'Chaman Lal', 'Hamada Madi', 'Fuad Qalaf', 'Cui Tiankai', 'Aamir Khan', 'Munir Said Thalib', 'Rudy Giuliani', 'Jamaica', 'Chiam See Tong', 'Chan Santokhi', 'Ma Kai', 'Tea Banh', 'Jaak Aab', 'Kundi Paihama', 'Sam Abal', 'Toomas Savi', 'Nur Misuari', 'Tulsi Giri', 'Fuat Oktay', 'Dullah Omar', 'Royal Thai Navy', 'Pap Saine', 'Pak Ui-chun', 'Michael Tsai', 'Yushau Shuaib', 'Ilham Tohti', 'Eda Rivas', 'Đinh La Thăng', 'Aamulehti', 'Liam Lawlor', 'Malalai Joya', 'Burhan Wani', 'Siim Kallas', 'Henry Van Thio', 'Russ Feingold', 'Rupiah Banda', 'Tin Naing Thein', 'Themba Godi', 'Hasan Tiro']

    NOTE:
    1. You have at most 4 turns to generate the final result. Please follow my examples above to answer the task with interleaving Thought, Code, Action, Result turns. 
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

    [YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment

    ### Turn 1: (3 turns left to use "Terminate" action to provide final answer.)
    **Thought 1:**
    Given the target entity "Ruam Jai Thai" and the candidate list provided, there is no direct match in the candidate list for "Ruam Jai Thai." Therefore, I cannot terminate the process immediately by selecting a direct match. To proceed, I need to request more information about the target entity "Ruam Jai Thai" or entities closely related to it from the candidate list to make an informed decision. Since "Ruam Jai Thai" directly translates to a concept of unity or coalition in Thai, and considering the context might be political or social, I should look for entities that could be related in terms of geography or domain. However, without direct knowledge or a clear match, I need to request information on the target entity itself if possible or a closely related entity from the list that might share a similar context, such as political figures or organizations from Thailand. Since I cannot request information on "Ruam Jai Thai" directly as it's not in the candidate list and no entity in the list directly matches or suggests being "Ruam Jai Thai," I will choose an entity that might have a contextual or geographical connection to the target entity.

    **Act 1:**
    Request[Royal Thai Navy]Observation 1: The background information of the entity is below which is given in code format motifs: 

    import location

    class Royal_Thai_Navy(object):

        def __init__(self, Royal_Thai_Navy, Bangkok):
            ## This is initial function
            self.Royal_Thai_Navy = Royal_Thai_Navy
            self.Bangkok = Bangkok

        def Royal_Thai_Navy_location(self):
            self.Royal_Thai_Navy = location(self.Bangkok)

            return self.Royal_Thai_Navy, self.Bangkok
    ``### Turn 2: (2 turns left to use "Terminate" action to provide final answer.)
    **Thought 2:**
    The information received about the Royal Thai Navy confirms its location in Bangkok, Thailand, which aligns with the geographical context I was considering for "Ruam Jai Thai." Given that "Ruam Jai Thai" could be related to a political or social coalition in Thailand, and the Royal Thai Navy is a significant entity within Thailand, this connection, however, does not directly help in identifying "Ruam Jai Thai" among the candidate entities. Since "Ruam Jai Thai" does not directly match any entity in the candidate list and the Royal Thai Navy, while relevant geographically, does not provide a direct link to the target entity, I need to consider other entities that might have a more direct connection to political or social movements or figures within Thailand. Looking at the candidate list again, I don't see entities that directly suggest a political party or coalition by name, which means I might need to request information on another entity that could potentially have a connection to Thai politics or social movements to narrow down the possibilities further.

    **Act 2:**
    Request[Tin Naing Thein]Observation 2: The background information of the entity is below which is given in code format motifs: 

    import has_occupation, birth_place, nationality, member_of, is_connected_with

    class Tin_Naing_Thein(object):

        def __init__(self, Tin_Naing_Thein, Politician, Myanmar, Union_Solidarity_and_Development_Party):
            ## This is initial function
            self.Tin_Naing_Thein = Tin_Naing_Thein
            self.Politician = Politician
            self.Myanmar = Myanmar
            self.Union_Solidarity_and_Development_Party = Union_Solidarity_and_Development_Party

        def Tin_Naing_Thein_Profile(self):
            self.Tin_Naing_Thein = has_occupation(self.Politician)
            self.Tin_Naing_Thein += birth_place(self.Myanmar)
            self.Tin_Naing_Thein += nationality(self.Myanmar)
            self.Tin_Naing_Thein += member_of(self.Union_Solidarity_and_Development_Party)

            self.Politician = is_connected_with(self.Tin_Naing_Thein)
            self.Myanmar = is_connected_with(self.Tin_Naing_Thein)
            self.Union_Solidarity_and_Development_Party = is_connected_with(self.Tin_Naing_Thein)

            return self.Tin_Naing_Thein, self.Politician, self.Myanmar, self.Union_Solidarity_and_Development_Party
            
    ``### Turn 3: (1 turn left to use "Terminate" action to provide final answer.)
    **Thought 3:**
    The information on Tin Naing Thein, a politician from Myanmar associated with the Union Solidarity and Development Party, does not directly aid in identifying "Ruam Jai Thai" as it shifts the geographical focus away from Thailand. This indicates that my strategy of selecting entities based on potential political or geographical relevance might need adjustment. Given the lack of direct matches or clear connections to "Ruam Jai Thai" from the entities requested so far, and considering the urgency to make a decision with only one turn left, it might be prudent to select an entity that could potentially have a broader or more symbolic connection to the concept of unity or coalition within the context of Southeast Asia, if no direct information on "Ruam Jai Thai" is available. However, without a clear candidate that represents "Ruam Jai Thai" or its values, and with limited information to make a direct connection, the task becomes significantly challenging. At this point, a strategic guess based on the available information and the context of the entities might be necessary.

    **Act 3:**
    Request[Puan Maharani]Observation 3: The background information of the entity is below which is given in code format motifs: 

    import is_connected_with, has_child

    class Puan_Maharani(object):

        def __init__(self, Indonesia, Megawati_Sukarnoputri, Puan_Maharani, Indonesian_Democratic_Party_of_Struggle, Politician):
            ## This is initial function
            self.Indonesia = Indonesia
            self.Megawati_Sukarnoputri = Megawati_Sukarnoputri
            self.Puan_Maharani = Puan_Maharani
            self.Indonesian_Democratic_Party_of_Struggle = Indonesian_Democratic_Party_of_Struggle
            self.Politician = Politician

        def Indonesia_connected_with_Megawati_and_Puan(self):
            self.Indonesia = is_connected_with(self.Megawati_Sukarnoputri)
            self.Indonesia = is_connected_with(self.Puan_Maharani)
            self.Megawati_Sukarnoputri = has_child(self.Puan_Maharani)

            return self.Indonesia, self.Megawati_Sukarnoputri, self.Puan_Maharani

        def Indonesian_Democratic_Party_of_Struggle_connected_with_Megawati_and_Puan(self):
            self.Indonesian_Democratic_Party_of_Struggle = is_connected_with(self.Megawati_Sukarnoputri)
            self.Indonesian_Democratic_Party_of_Struggle = is_connected_with(self.Puan_Maharani)
            self.Megawati_Sukarnoputri = has_child(self.Puan_Maharani)

            return self.Indonesian_Democratic_Party_of_Struggle, self.Megawati_Sukarnoputri, self.Puan_Maharani

        def Generic_connected_with_Megawati_and_Puan(self):
            # Assuming '~' represents a generic or unspecified entity
            self.Generic = is_connected_with(self.Megawati_Sukarnoputri)
            self.Generic = is_connected_with(self.Puan_Maharani)
            self.Megawati_Sukarnoputri = has_child(self.Puan_Maharani)

            return self.Generic, self.Megawati_Sukarnoputri, self.Puan_Maharani

        def Generic_connected_with_Indonesia_and_Puan(self):
            # Assuming '~' represents a generic or unspecified entity
            self.Generic = is_connected_with(self.Indonesia)
            self.Generic = is_connected_with(self.Puan_Maharani)
            self.Indonesia = is_connected_with(self.Puan_Maharani)

            return self.Generic, self.Indonesia, self.Puan_Maharani

        def Politician_connected_with_Megawati_and_Puan(self):
            self.Politician = is_connected_with(self.Megawati_Sukarnoputri)
            self.Politician = is_connected_with(self.Puan_Maharani)
            self.Megawati_Sukarnoputri = has_child(self.Puan_Maharani)

            return self.Politician, self.Megawati_Sukarnoputri, self.Puan_Maharani
    ``### Turn 4: (Last turn to use "Terminate" action to provide final answer.)
    **Thought 4:**
    The information on Puan Maharani, a prominent politician from Indonesia connected with the Indonesian Democratic Party of Struggle, and being the child of Megawati Sukarnoputri, provides a significant insight into political lineage and influence within Indonesia. However, this information, while valuable, does not directly assist in identifying "Ruam Jai Thai" within the context of the candidate list, as it shifts the focus to Indonesia rather than Thailand. Given the turns taken and the information gathered from the requested entities, it's clear that a direct connection to "Ruam Jai Thai" or a direct match within the candidate list is not evident based on the entities explored. With the final turn at hand and considering the geographical and political context explored so far, without a clear or direct match to "Ruam Jai Thai," I must conclude the task based on the information available and the context provided by the entities explored.

    **Act 4:**
    The most similar 50 entities are:<MOST>['Royal Thai Navy', 'Tin Naing Thein', 'Puan Maharani', 'Rami Jarrah', 'Karam Ali Shah', 'Zhao Lianhai', 'Sai Mauk Kham', 'Luan Rama', 'Tan Jee Say', 'Hamzah Haz', 'Hamshahri', 'Rabi Ray', 'Bamir Topi', 'Chaman Lal', 'Hamada Madi', 'Fuad Qalaf', 'Cui Tiankai', 'Aamir Khan', 'Munir Said Thalib', 'Rudy Giuliani', 'Jamaica', 'Chiam See Tong', 'Chan Santokhi', 'Ma Kai', 'Tea Banh', 'Jaak Aab', 'Kundi Paihama', 'Sam Abal', 'Toomas Savi', 'Nur Misuari', 'Tulsi Giri', 'Fuat Oktay', 'Dullah Omar', 'Pap Saine', 'Pak Ui-chun', 'Michael Tsai', 'Yushau Shuaib', 'Ilham Tohti', 'Eda Rivas', 'Đinh La Thăng', 'Aamulehti', 'Liam Lawlor', 'Malalai Joya', 'Burhan Wani', 'Siim Kallas', 'Henry Van Thio', 'Russ Feingold', 'Rupiah Banda', 'Themba Godi', 'Hasan Tiro']</MOST> and Terminate['Royal Thai Navy']

    ------
    **Entity alignment rule summarization & Regeneration**:
    ** Please generate some experience or rules in bullet point format that leads to correct answer.
    ** The case above is wrong! Please generate the correct reasoning process of above case including observations, make target entity aligned with the correct answer. 
    
    [**Important!**]The correct answer(aligned entity) is:
    'Thais United'

    The candidate entities list is: 
    ['Rami Jarrah', 'Karam Ali Shah', 'Zhao Lianhai', 'Sai Mauk Kham', 'Luan Rama', 'Puan Maharani', 'Tan Jee Say', 'Hamzah Haz', 'Hamshahri', 'Rabi Ray', 'Bamir Topi', 'Chaman Lal', 'Hamada Madi', 'Fuad Qalaf', 'Cui Tiankai', 'Aamir Khan', 'Munir Said Thalib', 'Rudy Giuliani', 'Jamaica', 'Chiam See Tong', 'Chan Santokhi', 'Ma Kai', 'Tea Banh', 'Jaak Aab', 'Kundi Paihama', 'Sam Abal', 'Toomas Savi', 'Nur Misuari', 'Tulsi Giri', 'Fuat Oktay', 'Dullah Omar', 'Royal Thai Navy', 'Pap Saine', 'Pak Ui-chun', 'Michael Tsai', 'Yushau Shuaib', 'Ilham Tohti', 'Eda Rivas', 'Đinh La Thăng', 'Aamulehti', 'Liam Lawlor', 'Malalai Joya', 'Burhan Wani', 'Siim Kallas', 'Henry Van Thio', 'Russ Feingold', 'Rupiah Banda', 'Tin Naing Thein', 'Themba Godi', 'Thais United']
    
"""

expel_process_rules_2 = """
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
    18. Ensure that the final termination action adheres to the format: "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[entity]."
    19. Avoid selecting entities that shift focus away from the target entity's geographical or contextual relevance.
    20. Adapt the process based on the available information to ensure the accurate alignment of entities.
"""
expel_process_rules_1 = """
    1. **Direct Match Identification:** If the target entity is directly present in the candidate list, select it immediately for termination.
    2. **Geographical Context Matching:** Consider the geographical context of the target entity. Entities related to the same country or region as the target entity should be prioritized.
    3. **Political and Social Context Matching:** Evaluate the political or social context of entities. Entities related to similar political movements, parties, or social contexts as the target entity should be considered.
    4. **Request Information on Related Entities:** If there is no direct match, request information on entities that might have a contextual or geographical connection to the target entity.
    5. **Prioritize Entities with Similar Contexts:** Request information about entities that could be contextually related to the target entity's domain or focus.
    6. **Minimize Uncertainty:** Make sure to request information that reduces uncertainty about the relationship between the target entity and candidate entities.
    7. **Leverage Similar Concepts:** If the target entity relates to a concept (e.g., a political coalition or social movement), prioritize entities that might represent similar concepts or affiliations.
    8. **Consider Broader Symbolic Connections:** If no direct match or close contextual match is found, consider entities with broader symbolic or thematic connections to the target entity.
    9. **Follow Code Motif:** Incorporate the relevant code motifs for each turn to ensure that the relationships and connections are accurately represented and utilized in the reasoning process.
    10. **Terminate Process with Best Guess:** If direct matches or clear connections are not found after the final turn, make a strategic decision based on the best available information.
    11. **Request and Terminate Actions:** Ensure to use either Request or Terminate actions in each turn, based on the current status of the information available.
    12. **Contextual Relevance:** When requesting entity information, prioritize those that have the highest relevance to the target entity's context.
    13. **Validate Entity Relationships:** Validate the relationships and context of the entities to ensure that they align well with the target entity's characteristics.
    14. **Review Entity Details Carefully:** Thoroughly review the details provided by requested entities to confirm their relevance and similarity to the target entity.
    15. **Limit Requests to Key Entities:** Focus requests on entities that are most likely to yield relevant information, rather than requesting information from less relevant candidates.
    16. **Update Candidate List:** Continuously update and rerank the candidate list based on the information gathered to identify the most similar entity effectively.
    17. **Reassess Strategies:** If initial strategies do not yield results, reassess and adjust the approach to entity alignment based on available information and context.
    18. **Consider Urgency:** Given limited turns, prioritize efficient decision-making to ensure the task is completed within the allowed number of turns.
    19. **Use Similarities as Indicators:** Use similarities in political, social, or geographical contexts as indicators for potential matches.
    20. **Terminate with Reasoned Decision:** After thorough consideration and information gathering, terminate the process with the most reasonable and informed choice.

"""

prompts_0820 = """
    As a good learner, you learn from good and bad experiences of entity alignment task and want to generate a better motif code template for it. Motifs are recurrent and statistically significant subgraphs or patterns of a knowledge graph. A motif code template is a consistent and repeatable structure of code that uses specific behaviors, interactions, or relationships in the code to describe a motif. It serves as a template that helps the AI model understand and generate the required output for entity alignment tasks. 
    ------
    **Rules for generating motif code template**
      1. Function Name: Use a descriptive name for the function that represents the relationship between the nodes. The function name should indicate the type of relationship or action involving the nodes which is an abstract of the motif.
      2. Import Statements: Import the necessary relations or actions. Use descriptive names that match the relationships in the motif information.
      3. Function Parameters: Include all nodes involved in the motif as parameters to the function.
      4. Function Implementation: Implement the function by calling the imported relations with the appropriate parameters. Each relation call should correspond to the connections or actions described in the motif information.
      5. Connection Relationships: For simple connections between nodes, use the connected_with relation.
      6. Complex Relationships: For more complex interactions (e.g., meetings, visits), use specific relations like make_a_visit, express_intent_to_meet_or_negotiate, etc.
      7. Return Values: Return all the nodes involved in the motif as part of the function’s result. Ensure that the function returns the state or outcome after applying the relationships.
      8. Execution: In the "if __name__ == '__main__':" block, call the defined functions with sample nodes to demonstrate how the motif relationships are applied.
      9. Please note the += relationship which represents multiple relationship between two nodes. It means two nodes have more than 1 type of relationship.
    ------
    **Rules**
    {}
    please add, delete, update the above rules and keep no more than 50 rules. Please enclose the generated experience or rules in '<rule>' and '</rule>' tags.
    
    You are doing an entity alignment task of two knowledge graphs (KGs), where you need to find the equivalent entity of the target entity. The target entity and the equivalent entity both have background information from KGs. The background information is represented by motif code template. You should align the target entity and equivalent entity (correct answer) based on the following rules. In the process of aligning the target entity to the correct answer, you MUST summarize some experience or rules in bullet point format that leads to writing perfect motif code templates.

    You should regenerate the following case later according to the target entity and correct answer. You must follow the correct answer to regenerate the process. Futhermore, you should generate the rules writing better code motifs during the process. 
    
    ------
    # Case:
    {}
    
    Insight summarization & Regenerate the process:
    ** The case above is {}, please generate some experience or rules in bullet point format that leads to writing perfect motif code templates, according to the target entity and correct answer.
    ** Please generate the correct reasoning process of above case, make target entity aligned with the correct answer. The target entity is:
    {}
    
    The correct answer(aligned entity) is:
    {}

    The candidate entities list is: 
    {}
    
    NOTE: 
    Please enclose the generated experience or rules in '<rule>' and '</rule>' tags.
    2. You have at most 4 turns to generate the final result. Please follow my examples above to answer the task with interleaving Thought, Code, Action, Result turns. 
    3. Please generate the step-by-step thought process leading to the final answer.
    4. You must use Code Motif in the reasoning path. Refer to the example provided.
    5. The final answer in 'Terminate[answer]' should be the aligned entity.
    6. please must have observation and code motif each turn in reasoning process.
    
"""
# .format(
#             """
#         1. Function Name: Use a descriptive name for the function that represents the relationship between the nodes. The function name should indicate the type of relationship or action involving the nodes which is an abstract of the motif.
#       2. Import Statements: Import the necessary relations or actions. Use descriptive names that match the relationships in the motif information.
#       3. Function Parameters: Include all nodes involved in the motif as parameters to the function.
#       4. Function Implementation: Implement the function by calling the imported relations with the appropriate parameters. Each relation call should correspond to the connections or actions described in the motif information.
#       5. Connection Relationships: For simple connections between nodes, use the connected_with relation.
#       6. Complex Relationships: For more complex interactions (e.g., meetings, visits), use specific relations like make_a_visit, express_intent_to_meet_or_negotiate, etc.
#       7. Return Values: Return all the nodes involved in the motif as part of the function’s result. Ensure that the function returns the state or outcome after applying the relationships.
#       8. Execution: In the "if __name__ == '__main__':" block, call the defined functions with sample nodes to demonstrate how the motif relationships are applied.
#       9. Please note the += relationship which represents multiple relationship between two nodes. It means two nodes have more than 1 type of relationship.
#
#             """,
#                 'wrong',
#                 'Ruam Jai Thai',
#                 'Thais United',
#                ['Rami Jarrah', 'Karam Ali Shah', 'Zhao Lianhai', 'Sai Mauk Kham', 'Luan Rama', 'Puan Maharani', 'Tan Jee Say', 'Hamzah Haz', 'Hamshahri', 'Rabi Ray', 'Bamir Topi', 'Chaman Lal', 'Hamada Madi', 'Fuad Qalaf', 'Cui Tiankai', 'Aamir Khan', 'Munir Said Thalib', 'Rudy Giuliani', 'Jamaica', 'Chiam See Tong', 'Chan Santokhi', 'Ma Kai', 'Tea Banh', 'Jaak Aab', 'Kundi Paihama', 'Sam Abal', 'Toomas Savi', 'Nur Misuari', 'Tulsi Giri', 'Fuat Oktay', 'Dullah Omar', 'Royal Thai Navy', 'Pap Saine', 'Pak Ui-chun', 'Michael Tsai', 'Yushau Shuaib', 'Ilham Tohti', 'Eda Rivas', 'Đinh La Thăng', 'Aamulehti', 'Liam Lawlor', 'Malalai Joya', 'Burhan Wani', 'Siim Kallas', 'Henry Van Thio', 'Russ Feingold', 'Rupiah Banda', 'Tin Naing Thein', 'Themba Godi', 'Thais United']
# )


"""
You are a programmer in a large company, tasked with selecting the most similar entity to a target entity from a candidate list. You will solve the task using a series of interleaving Thought, Action, and Observation steps. Thought can reason about the current situation, and Action can only be one of the following two types:

    - Request[entity]: Requests the context information of the entity from external Knowledge Graphs. You can only request one entity in each turn, and it must be from the candidate list or the target entity itself.
    - The most similar 50 entities are: <MOST>[]</MOST> and Terminate[answer]: Returns the answer and finishes the task. This action can only occur when you finish the task! When you decide to use terminate action, you mush put the most similar 50 entities into: "<MOST>[]</MOST>". Please note that if there is a direct match, please use act Terminate[] directly to end the precess.

    You must have an act from above two actions per turn no matter it is request or terminate. The act can only be two types. 

    **NOTE:** You must request the most relevant entity information from the candidate list to reduce your uncertainty and finally help you to finish this task correctly. If you request less important entities and fail to handle this task perfectly, you will be immediately fired! 
    Below is a case task.

    ------
    # New Task:
    [USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it directly. 

    **The target entity is:** 
    Ruam Jai Thai

    **The candidate entities list is:**
    ['Rami Jarrah', 'Karam Ali Shah', 'Zhao Lianhai', 'Sai Mauk Kham', 'Luan Rama', 'Puan Maharani', 'Tan Jee Say', 'Hamzah Haz', 'Hamshahri', 'Rabi Ray', 'Bamir Topi', 'Chaman Lal', 'Hamada Madi', 'Fuad Qalaf', 'Cui Tiankai', 'Aamir Khan', 'Munir Said Thalib', 'Rudy Giuliani', 'Jamaica', 'Chiam See Tong', 'Chan Santokhi', 'Ma Kai', 'Tea Banh', 'Jaak Aab', 'Kundi Paihama', 'Sam Abal', 'Toomas Savi', 'Nur Misuari', 'Tulsi Giri', 'Fuat Oktay', 'Dullah Omar', 'Royal Thai Navy', 'Pap Saine', 'Pak Ui-chun', 'Michael Tsai', 'Yushau Shuaib', 'Ilham Tohti', 'Eda Rivas', 'Đinh La Thăng', 'Aamulehti', 'Liam Lawlor', 'Malalai Joya', 'Burhan Wani', 'Siim Kallas', 'Henry Van Thio', 'Russ Feingold', 'Rupiah Banda', 'Tin Naing Thein', 'Themba Godi', 'Hasan Tiro']

    NOTE:
    1. You have at most 4 turns to generate the final result. Please follow my examples above to answer the task with interleaving Thought, Code, Action, Result turns. 
    2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
    3. The observation should contain code motif. 
    4. If you are very sure about the answer, please answer directly. 
    5. If there is the same entity in the candidate list as the target entity, please select it directly and terminate the process. 
    6. You must have an act from above two actions per turn no matter it is request or terminate. The act can only be two types.
    7. Please follow the example format: thought, action, observation steps. Do not generate response by yourself.
    8. If you can find a direct match, please use act "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[]" directly and do no need to confirm another entity.
    9. If you are can not find a direct match, please request and do not terminate.
    10. The background information in observation is represented by code motif.
    11. The output format is "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[answer]".
    12. Request[] action can only request an entity in candidate list or it is itself.
    13. Please output the ranked candidate list when terminate the process. 
    14. The entity in Terminate[] can not be 'answer' but an entity.


    [YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment

    ### Turn 1: (3 turns left to use "Terminate" action to provide final answer.)
    **Thought 1:**
    Given the target entity "Ruam Jai Thai" and the candidate list provided, there is no direct match in the candidate list for "Ruam Jai Thai." Therefore, I cannot terminate the process immediately by selecting a direct match. To proceed, I need to request more information about the target entity "Ruam Jai Thai" or entities closely related to it from the candidate list to make an informed decision. Since "Ruam Jai Thai" directly translates to a concept of unity or coalition in Thai, and considering the context might be political or social, I should look for entities that could be related in terms of geography or domain. However, without direct knowledge or a clear match, I need to request information on the target entity itself if possible or a closely related entity from the list that might share a similar context, such as political figures or organizations from Thailand. Since I cannot request information on "Ruam Jai Thai" directly as it's not in the candidate list and no entity in the list directly matches or suggests being "Ruam Jai Thai," I will choose an entity that might have a contextual or geographical connection to the target entity.

    **Act 1:**
    Request[Royal Thai Navy]Observation 1: The background information of the entity is below which is given in code format motifs: 

    import location

    class Royal_Thai_Navy(object):

        def __init__(self, Royal_Thai_Navy, Bangkok):
            ## This is initial function
            self.Royal_Thai_Navy = Royal_Thai_Navy
            self.Bangkok = Bangkok

        def Royal_Thai_Navy_location(self):
            self.Royal_Thai_Navy = location(self.Bangkok)

            return self.Royal_Thai_Navy, self.Bangkok
    ``### Turn 2: (2 turns left to use "Terminate" action to provide final answer.)
    **Thought 2:**
    The information received about the Royal Thai Navy confirms its location in Bangkok, Thailand, which aligns with the geographical context I was considering for "Ruam Jai Thai." Given that "Ruam Jai Thai" could be related to a political or social coalition in Thailand, and the Royal Thai Navy is a significant entity within Thailand, this connection, however, does not directly help in identifying "Ruam Jai Thai" among the candidate entities. Since "Ruam Jai Thai" does not directly match any entity in the candidate list and the Royal Thai Navy, while relevant geographically, does not provide a direct link to the target entity, I need to consider other entities that might have a more direct connection to political or social movements or figures within Thailand. Looking at the candidate list again, I don't see entities that directly suggest a political party or coalition by name, which means I might need to request information on another entity that could potentially have a connection to Thai politics or social movements to narrow down the possibilities further.

    **Act 2:**
    Request[Tin Naing Thein]Observation 2: The background information of the entity is below which is given in code format motifs: 

    import has_occupation, birth_place, nationality, member_of, is_connected_with

    class Tin_Naing_Thein(object):

        def __init__(self, Tin_Naing_Thein, Politician, Myanmar, Union_Solidarity_and_Development_Party):
            ## This is initial function
            self.Tin_Naing_Thein = Tin_Naing_Thein
            self.Politician = Politician
            self.Myanmar = Myanmar
            self.Union_Solidarity_and_Development_Party = Union_Solidarity_and_Development_Party

        def Tin_Naing_Thein_Profile(self):
            self.Tin_Naing_Thein = has_occupation(self.Politician)
            self.Tin_Naing_Thein += birth_place(self.Myanmar)
            self.Tin_Naing_Thein += nationality(self.Myanmar)
            self.Tin_Naing_Thein += member_of(self.Union_Solidarity_and_Development_Party)

            self.Politician = is_connected_with(self.Tin_Naing_Thein)
            self.Myanmar = is_connected_with(self.Tin_Naing_Thein)
            self.Union_Solidarity_and_Development_Party = is_connected_with(self.Tin_Naing_Thein)

            return self.Tin_Naing_Thein, self.Politician, self.Myanmar, self.Union_Solidarity_and_Development_Party
            
    ``### Turn 3: (1 turn left to use "Terminate" action to provide final answer.)
    **Thought 3:**
    The information on Tin Naing Thein, a politician from Myanmar associated with the Union Solidarity and Development Party, does not directly aid in identifying "Ruam Jai Thai" as it shifts the geographical focus away from Thailand. This indicates that my strategy of selecting entities based on potential political or geographical relevance might need adjustment. Given the lack of direct matches or clear connections to "Ruam Jai Thai" from the entities requested so far, and considering the urgency to make a decision with only one turn left, it might be prudent to select an entity that could potentially have a broader or more symbolic connection to the concept of unity or coalition within the context of Southeast Asia, if no direct information on "Ruam Jai Thai" is available. However, without a clear candidate that represents "Ruam Jai Thai" or its values, and with limited information to make a direct connection, the task becomes significantly challenging. At this point, a strategic guess based on the available information and the context of the entities might be necessary.

    **Act 3:**
    Request[Puan Maharani]Observation 3: The background information of the entity is below which is given in code format motifs: 

    import is_connected_with, has_child

    class Puan_Maharani(object):

        def __init__(self, Indonesia, Megawati_Sukarnoputri, Puan_Maharani, Indonesian_Democratic_Party_of_Struggle, Politician):
            ## This is initial function
            self.Indonesia = Indonesia
            self.Megawati_Sukarnoputri = Megawati_Sukarnoputri
            self.Puan_Maharani = Puan_Maharani
            self.Indonesian_Democratic_Party_of_Struggle = Indonesian_Democratic_Party_of_Struggle
            self.Politician = Politician

        def Indonesia_connected_with_Megawati_and_Puan(self):
            self.Indonesia = is_connected_with(self.Megawati_Sukarnoputri)
            self.Indonesia = is_connected_with(self.Puan_Maharani)
            self.Megawati_Sukarnoputri = has_child(self.Puan_Maharani)

            return self.Indonesia, self.Megawati_Sukarnoputri, self.Puan_Maharani

        def Indonesian_Democratic_Party_of_Struggle_connected_with_Megawati_and_Puan(self):
            self.Indonesian_Democratic_Party_of_Struggle = is_connected_with(self.Megawati_Sukarnoputri)
            self.Indonesian_Democratic_Party_of_Struggle = is_connected_with(self.Puan_Maharani)
            self.Megawati_Sukarnoputri = has_child(self.Puan_Maharani)

            return self.Indonesian_Democratic_Party_of_Struggle, self.Megawati_Sukarnoputri, self.Puan_Maharani

        def Generic_connected_with_Megawati_and_Puan(self):
            # Assuming '~' represents a generic or unspecified entity
            self.Generic = is_connected_with(self.Megawati_Sukarnoputri)
            self.Generic = is_connected_with(self.Puan_Maharani)
            self.Megawati_Sukarnoputri = has_child(self.Puan_Maharani)

            return self.Generic, self.Megawati_Sukarnoputri, self.Puan_Maharani

        def Generic_connected_with_Indonesia_and_Puan(self):
            # Assuming '~' represents a generic or unspecified entity
            self.Generic = is_connected_with(self.Indonesia)
            self.Generic = is_connected_with(self.Puan_Maharani)
            self.Indonesia = is_connected_with(self.Puan_Maharani)

            return self.Generic, self.Indonesia, self.Puan_Maharani

        def Politician_connected_with_Megawati_and_Puan(self):
            self.Politician = is_connected_with(self.Megawati_Sukarnoputri)
            self.Politician = is_connected_with(self.Puan_Maharani)
            self.Megawati_Sukarnoputri = has_child(self.Puan_Maharani)

            return self.Politician, self.Megawati_Sukarnoputri, self.Puan_Maharani
    ``### Turn 4: (Last turn to use "Terminate" action to provide final answer.)
    **Thought 4:**
    The information on Puan Maharani, a prominent politician from Indonesia connected with the Indonesian Democratic Party of Struggle, and being the child of Megawati Sukarnoputri, provides a significant insight into political lineage and influence within Indonesia. However, this information, while valuable, does not directly assist in identifying "Ruam Jai Thai" within the context of the candidate list, as it shifts the focus to Indonesia rather than Thailand. Given the turns taken and the information gathered from the requested entities, it's clear that a direct connection to "Ruam Jai Thai" or a direct match within the candidate list is not evident based on the entities explored. With the final turn at hand and considering the geographical and political context explored so far, without a clear or direct match to "Ruam Jai Thai," I must conclude the task based on the information available and the context provided by the entities explored.

    **Act 4:**
    The most similar 50 entities are:<MOST>['Royal Thai Navy', 'Tin Naing Thein', 'Puan Maharani', 'Rami Jarrah', 'Karam Ali Shah', 'Zhao Lianhai', 'Sai Mauk Kham', 'Luan Rama', 'Tan Jee Say', 'Hamzah Haz', 'Hamshahri', 'Rabi Ray', 'Bamir Topi', 'Chaman Lal', 'Hamada Madi', 'Fuad Qalaf', 'Cui Tiankai', 'Aamir Khan', 'Munir Said Thalib', 'Rudy Giuliani', 'Jamaica', 'Chiam See Tong', 'Chan Santokhi', 'Ma Kai', 'Tea Banh', 'Jaak Aab', 'Kundi Paihama', 'Sam Abal', 'Toomas Savi', 'Nur Misuari', 'Tulsi Giri', 'Fuat Oktay', 'Dullah Omar', 'Pap Saine', 'Pak Ui-chun', 'Michael Tsai', 'Yushau Shuaib', 'Ilham Tohti', 'Eda Rivas', 'Đinh La Thăng', 'Aamulehti', 'Liam Lawlor', 'Malalai Joya', 'Burhan Wani', 'Siim Kallas', 'Henry Van Thio', 'Russ Feingold', 'Rupiah Banda', 'Themba Godi', 'Hasan Tiro']</MOST> and Terminate['Royal Thai Navy']

"""


prompts_v1 = """
    You are experience learner, you learn from experience and generate better Code motif for a task. Code motif refer to a consistent and repeatable structure of code used to describe a specific behavior, interaction, or relationship in the code. It serves as a template or pattern that helps the AI model understand and generate the required output for similar tasks.

    You are doing an entity alignement task. The target entity and aligned entity both have background information. The backgound information is represented by code motif. You should align the target entity and correct answer based on the following rules.

    In the process of aligning target entity to correct answer, you should summarize some rules that write perfect code motifs.


    ------
    # Case:
    {}
    
    Correction:
    The case above is {}, please according to the target entity and correct answer generate rules write better code motif.


    [USER (Boss)]: Please sort the candidate list according to similarity to the target entity and select the most aligned entity. You have at most 4 turns to finish the task. If there is the same entity in the candidate list as the target entity, please select it directly. The answer format is: Terminate[answer]. The target entity is:
    The target entity is:
    {}

    The aligned entity is:
    {}

    The candidate entities list is: 
    {}

    Notes:
    1. You have at most 4 turns to generate the final result. Please follow my examples above to answer the task with interleaving Thought, Code, Action, Result turns. 
    2. Please generate the step-by-step thought process leading to the final answer.
    3. You must use Code Motif in the reasoning path. Refer to the example provided.
    4. Please summarize some rules on how to write better Code Motifs which can let LLM better understand motif in <rule></rule> tags in the final turn.
    6. The final answer in 'Terminate[answer]' should be the aligned entity.
    7. please must have observation and code motif each turn in reasoning process.

    """


prompts_v0 = """
    You are experience learner, you learn from experience and generate better Code motif for a task. Code motif refer to a consistent and repeatable structure of code used to describe a specific behavior, interaction, or relationship in the code. It serves as a template or pattern that helps the AI model understand and generate the required output for similar tasks.

    You are doing an entity alignement task. The target entity and aligned entity both have background information. The backgound information is represented by code motif. You should align the target entity and correct answer based on the following rules.
    
    In the process of aligning target entity to correct answer, you should summarize some rules that write perfect code motifs.
    
    
    ------
    # Case:
    
    You are a programmer in a large company, tasked with selecting the most similar entity to a target entity from a candidate list. You will solve the task using a series of interleaving Thought, Action, and Observation steps. Thought can reason about the current situation, and Action can only be one of the following two types:

    - Request[entity]: Requests the context information of the entity from external Knowledge Graphs. You can only request one entity in each turn, and it must be from the candidate list or the target entity itself.
    - The most similar 50 entities are: <MOST>[]</MOST> and Terminate[answer]: Returns the answer and finishes the task. This action can only occur when you finish the task! When you decide to use terminate action, you mush put the most similar 50 entities into: "<MOST>[]</MOST>". Please note that if there is a direct match, please use act Terminate[] directly to end the precess.
    
    You must have an act from above two actions per turn no matter it is request or terminate. The act can only be two types. 
    Note:
    1. You have at most 4 turns to generate the final result. Please follow my examples above to answer the task with interleaving Thought, Code, Action, Result turns. 
    2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
    3. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!!
    4. If you are very sure about the answer, please answer directly. 
    5. If there is the same entity in the candidate list as the target entity, please select it directly and terminate the process. 
    6. You must have an act from above two actions per turn no matter it is request or terminate. The act can only be two types.
    7. Please follow the example format: thought, action, observation steps. Do not generate response by yourself.
    8. If you can find a direct match, please use act "Terminate[]" directly and do no need to confirm another entity.
    9. If you are can not find a direct match, please request and do not terminate.
    10. Please do not generate any observations.
    11. The output format is "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[answer]".
    12. Request[] action can only request an entity in candidate list or it is itself. 
    13. please output the full candidate list.
    
    **NOTE:** You must request the most relevant entity information from the candidate list to reduce your uncertainty and finally help you to finish this task correctly. If you request less important entities and fail to handle this task perfectly, you will be immediately fired! 
    
    [USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it directly. 
    
    **The target entity is:** 
    Ruam Jai Thai
    
    **The candidate entities list is:**
    ['Rami Jarrah', 'Karam Ali Shah', 'Zhao Lianhai', 'Sai Mauk Kham', 'Luan Rama', 'Puan Maharani', 'Tan Jee Say', 'Hamzah Haz', 'Hamshahri', 'Rabi Ray', 'Bamir Topi', 'Chaman Lal', 'Hamada Madi', 'Fuad Qalaf', 'Cui Tiankai', 'Aamir Khan', 'Munir Said Thalib', 'Rudy Giuliani', 'Jamaica', 'Chiam See Tong', 'Chan Santokhi', 'Ma Kai', 'Tea Banh', 'Jaak Aab', 'Kundi Paihama', 'Sam Abal', 'Toomas Savi', 'Nur Misuari', 'Tulsi Giri', 'Fuat Oktay', 'Dullah Omar', 'Royal Thai Navy', 'Pap Saine', 'Pak Ui-chun', 'Michael Tsai', 'Yushau Shuaib', 'Ilham Tohti', 'Eda Rivas', 'Đinh La Thăng', 'Aamulehti', 'Liam Lawlor', 'Malalai Joya', 'Burhan Wani', 'Siim Kallas', 'Henry Van Thio', 'Russ Feingold', 'Rupiah Banda', 'Tin Naing Thein', 'Themba Godi', 'Hasan Tiro']
    
    [YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment
    
    ### Turn 1: (3 turns left to use "Terminate" action to provide final answer.)
    **Thought 1:**
    Given the target entity "Ruam Jai Thai" and the candidate list provided, there is no direct match in the list. "Ruam Jai Thai" suggests a Thai context, possibly related to politics, social movements, or organizations within Thailand. To make an informed decision, it's crucial to understand the nature of "Ruam Jai Thai" better. Among the candidates, entities related to Thai politics or society could be more relevant. However, without specific knowledge about "Ruam Jai Thai," it's challenging to pinpoint which candidate might be the most similar based on the names alone. Entities like "Royal Thai Navy" hint at a Thai connection but from a different sector. It might be beneficial to request information on "Ruam Jai Thai" itself if available to get a clearer understanding of its nature and then find the most similar entity based on that understanding.
    
    **Act 1:** Request[Ruam Jai Thai]Observation 1: The background information of the entity is below which is given in code format motifs: 
    
    import express_intent_to_engage_in_diplomatic_cooperation, make_statement, yield_interaction, demand_interaction, consult_interaction, make_an_appeal_or_request, praise_or_endorse
    
    class Ruam_Jai_Thai(object):
    
        def __init__(self, Chavalit_Yongchaiyudh, Ruam_Jai_Thai, Military_Thailand):
            ## This is initial function
            self.Chavalit_Yongchaiyudh = Chavalit_Yongchaiyudh
            self.Ruam_Jai_Thai = Ruam_Jai_Thai
            self.Military_Thailand = Military_Thailand
    
        def Chavalit_Yongchaiyudh_engage_Ruam_Jai_Thai(self):
            self.Chavalit_Yongchaiyudh = express_intent_to_engage_in_diplomatic_cooperation(self.Ruam_Jai_Thai)
            
            return self.Chavalit_Yongchaiyudh, self.Ruam_Jai_Thai
    
        def Chavalit_Yongchaiyudh_interactions_with_Military(self):
            self.Chavalit_Yongchaiyudh = make_statement(self.Military_Thailand)
            self.Chavalit_Yongchaiyudh += yield_interaction(self.Military_Thailand)
            self.Chavalit_Yongchaiyudh += demand_interaction(self.Military_Thailand)
            self.Chavalit_Yongchaiyudh += consult_interaction(self.Military_Thailand)
            self.Chavalit_Yongchaiyudh += make_an_appeal_or_request(self.Military_Thailand)
            
            return self.Chavalit_Yongchaiyudh, self.Military_Thailand
    
        def Ruam_Jai_Thai_endorse_Military(self):
            self.Ruam_Jai_Thai = praise_or_endorse(self.Military_Thailand)
            
            return self.Ruam_Jai_Thai, self.Military_Thailand
    ``### Turn 2: (2 turns left to use "Terminate" action to provide final answer.)
    **Thought 2:**
    The information provided about "Ruam Jai Thai" indicates a strong connection with Thai military and political spheres, specifically mentioning Chavalit Yongchaiyudh, a notable figure in Thai politics and military. This suggests that "Ruam Jai Thai" is likely a political or military entity within Thailand. Given this context, the most similar entity from the candidate list would likely be one that has a direct connection to Thai politics or military. "Royal Thai Navy" stands out as it is directly related to the military aspect of Thailand. However, it's important to note that "Ruam Jai Thai" seems to be more of a political or collective movement rather than a specific military branch. Therefore, while "Royal Thai Navy" is closely related, there might not be a direct match in the list that perfectly aligns with "Ruam Jai Thai" as a political entity. Given the information and the nature of "Ruam Jai Thai," it's crucial to select an entity that closely aligns with its political and military context within Thailand.
    
    **Act 2:** The most similar 50 entities are:<MOST>['Royal Thai Navy', 'Tan Jee Say', 'Puan Maharani', 'Hamzah Haz', 'Sai Mauk Kham', 'Luan Rama', 'Rami Jarrah', 'Karam Ali Shah', 'Zhao Lianhai', 'Hamshahri', 'Rabi Ray', 'Bamir Topi', 'Chaman Lal', 'Hamada Madi', 'Fuad Qalaf', 'Cui Tiankai', 'Aamir Khan', 'Munir Said Thalib', 'Rudy Giuliani', 'Jamaica', 'Chiam See Tong', 'Chan Santokhi', 'Ma Kai', 'Tea Banh', 'Jaak Aab', 'Kundi Paihama', 'Sam Abal', 'Toomas Savi', 'Nur Misuari', 'Tulsi Giri', 'Fuat Oktay', 'Dullah Omar', 'Pap Saine', 'Pak Ui-chun', 'Michael Tsai', 'Yushau Shuaib', 'Ilham Tohti', 'Eda Rivas', 'Đinh La Thăng', 'Aamulehti', 'Liam Lawlor', 'Malalai Joya', 'Burhan Wani', 'Siim Kallas', 'Henry Van Thio', 'Russ Feingold', 'Rupiah Banda', 'Tin Naing Thein', 'Themba Godi', 'Hasan Tiro']</MOST> and Terminate['Royal Thai Navy']

    
    Correction:
    The case above is {}, please according to the target entity and correct answer generate rules write better code motif.
    

    [USER (Boss)]: Please sort the candidate list according to similarity to the target entity and select the most aligned entity. You have at most 4 turns to finish the task. If there is the same entity in the candidate list as the target entity, please select it directly. The answer format is: Terminate[answer]. The target entity is:
    The target entity is:
    {}
    
    The aligned entity is:
    {}
    
    The candidate entities list is: 
    {}
    
    Notes:
    1. You have at most 4 turns to generate the final result. Please follow my examples above to answer the task with interleaving Thought, Code, Action, Result turns. 
    2. Please generate the step-by-step thought process leading to the final answer.
    3. You must use Code Motif in the reasoning path. Refer to the example provided.
    4. Please summarize some rules on how to write better Code Motifs which can let LLM better understand motif in <rule></rule> tags in the final turn.
    6. The final answer in 'Terminate[answer]' should be the aligned entity.
    7. please must have observation and code motif each turn in reasoning process.
    
    """.format('wrong',
                'Ruam Jai Thai',
                'Thais United',
               ['Rami Jarrah', 'Karam Ali Shah', 'Zhao Lianhai', 'Sai Mauk Kham', 'Luan Rama', 'Puan Maharani', 'Tan Jee Say', 'Hamzah Haz', 'Hamshahri', 'Rabi Ray', 'Bamir Topi', 'Chaman Lal', 'Hamada Madi', 'Fuad Qalaf', 'Cui Tiankai', 'Aamir Khan', 'Munir Said Thalib', 'Rudy Giuliani', 'Jamaica', 'Chiam See Tong', 'Chan Santokhi', 'Ma Kai', 'Tea Banh', 'Jaak Aab', 'Kundi Paihama', 'Sam Abal', 'Toomas Savi', 'Nur Misuari', 'Tulsi Giri', 'Fuat Oktay', 'Dullah Omar', 'Royal Thai Navy', 'Pap Saine', 'Pak Ui-chun', 'Michael Tsai', 'Yushau Shuaib', 'Ilham Tohti', 'Eda Rivas', 'Đinh La Thăng', 'Aamulehti', 'Liam Lawlor', 'Malalai Joya', 'Burhan Wani', 'Siim Kallas', 'Henry Van Thio', 'Russ Feingold', 'Rupiah Banda', 'Tin Naing Thein', 'Themba Godi', 'Thais United']
               )

prompts_original = """
    
    You are a programmer. You can request useful entities from a candidate list but must avoid requesting irrelevant entities. Failure to adhere to this will result in termination. Your task is to solve a question-answering problem using interleaving Thought, Action, and Observation steps.
    
    Thought: Reason about the current situation.
    Action: There are only two types of actions:
    Request[entity] - Requests the entity context information from Knowledge Graphs. The context information may be given in code descriptions. You can only request one entity per turn and it must be from the candidate list.
    Terminate[answer] - Returns the answer and finishes the task.
    Example
    [USER (Boss)]: Give me the most aligned entity of the target entity from the candidates entity list. If there is the same entity, please select it directly. The target entity is: 'Salauddin'
    
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

    [USER (Boss)]: Please sort the candidate list according to similarity to the target entity and select the most aligned entity. You have at most 4 turns to finish the task. If there is the same entity in the candidate list as the target entity, please select it directly. The answer format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
    The target entity is {}.
    
    The candidate entities list is:{}
    
    The aligned entity is {}.
    
    Notes:
    1. Please generate the step-by-step thought process leading to the final answer.
    3. You must use Code Motif in the reasoning path. Refer to the example provided.
    4. Please generate some rules on how to write Code Motifs in <rule></rule> tags in the final turn.
    """