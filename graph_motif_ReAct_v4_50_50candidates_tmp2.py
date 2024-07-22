motif_ReAct_example_prompt = """
You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity]. It requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 50 entities after sort are: <most>[]</most> and Terminate[answer]. It returns the answer and finishes the task.
Here are two examples.
Compare the background information of entities carefully to see if they are similar. 
------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity from candidates list. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly, the format is: The most similar 50 entities after sort are: <most>[]</most> and Terminate[answer]. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! The target entity is:
'Ne Win'

The Candidate entities list is: 
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select 50 most similar answer after sort and 1 most similar entity from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: The most similar 50 entities after sort are: <most>['Ne Win', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia']</most> and Terminate['Ne Win'].

------------------------------ Example End ------------------------------ 

------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity from candidates list. If there is same entity, please select directly. The format is The most similar 50 entities after sort are: <most>[]</most> and Terminate[answer]. You have at most 4 turns to finish the task. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! The target entity is:
'Salauddin'

The Candidate entities list is: 
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Abdulla Kurd']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide the final answer. 
Thought 1: I can find a direct match.
Act 1: The most similar 50 entities after are: <most>['Abdulla Kurd', 'Salam Fayyad', 'Hamid Mir', 'Salou Djibo', 'Soe Thein', 'Sukarno', 'Jean Ping', 'Chea Sim', 'Shwe Mann', 'Aung Min', 'Ne Win', 'Gilad Erdan', 'Ramdev', 'Paul Martin', 'Sam Sesay', 'Ma Kai', 'Fatah', 'Sinn Féin', 'Somalia', 'Mao Zedong', 'Hla Min', 'Hla Tun', 'Panama', 'Hamas', 'Suharto', 'Attajdid', 'Talal Arslan', 'Isa Yuguda', 'Saad Hariri', 'Shaul Mofaz', 'Alexandria', 'Carl Levin', 'Sam Nujoma', 'Dan Burton', 'Ron Wyden', 'Kadima', 'Raila Odinga', 'Sylvia Lim', 'Susan Rice', 'Babar Awan', 'Sima Samar', 'Aung San', 'Jawed Ludin', 'Imran Khan', 'Navarre', 'Poland', 'Wales', 'Soe Aung', 'Malawi', 'Benin', 'Tatarstan']</most> and Terminate['Abdulla Kurd'].

------------------------------ Example End ------------------------------ 


[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity from candidates list. If there is same entity, please select directly. The format is The most similar 50 entities after sort are: <most>[]</most> and Terminate[answer]. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! The target entity is:
'Coalition for Democratic Unity'

The Candidate entities list is: 
['Croatian Democratic Union', 'Christian Democratic Party', 'Maldivian Democratic Party', 'Gabonese Democratic Party', 'National Democratic Institute', 'Kurdistan Democratic Party', 'Botswana Democratic Party', 'Slovenian Democratic Party', 'Forum for Democratic Change', 'Party of Democratic Action', 'Lebanese Democratic Party', 'United Social Democratic Party', 'Rally of Democratic Forces', 'Fresh Democratic Party', 'Nationwide Social Democratic Party', 'National Union for Democratic Progress', 'Brazilian Social Democracy Party', 'New Democratic Party', 'Senegalese Democratic Party', 'Organisation of African Unity', 'Democratic Party', "United Peoples' Democratic Party", 'Christian Democratic Movement', 'African Christian Democratic Party', 'National Patriotic Party', 'National Resurrection Party', 'United Democratic Movement', 'National Umma Party', 'Popular Democratic Movement', 'National Coalition Party', 'Orange Democratic Movement', 'Croatian Peasant Party', "Convention People's Party", 'National League for Democracy', 'Cairo University', 'Independent Democrats', 'Tunisian Pirate Party', 'Dalton McGuinty', 'Sprint Corporation', 'Oracle Corporation', 'Lesotho Congress for Democracy', 'Pakistan Peoples Party', "Kurdistan Workers' Party", 'Caribbean Community', 'National Medical Library', 'Bharatiya Janata Party', 'National Defense University', 'Verizon Communications', "People's United Democratic Movement", 'National Endowment for Democracy', 'Democratic Unity Roundtable']
  
NOTE: You have at most 4 turns to generate final results. Please follow my example between "Example Start" and "Example End" above to answer task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem. 

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! Otherwise, you will be punished.
Thought 1:

"""
