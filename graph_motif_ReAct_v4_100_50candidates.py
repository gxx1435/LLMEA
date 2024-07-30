motif_ReAct_example_prompt = """
You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity], which requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 50 entities are: []. Terminate[answer], which returns the answer and finishes the task.
Here are two examples.
Compare the background information of entities carefully to see if they are similar. 
------------------------------# Example1 Start ------------------------------ 

[USER (Boss)]: Give me the most aligned entity of the target entity from candidates entity list. If there is same entity, please select directly. The target entity is:
'Ne Win'

The Candidate entities list is: 
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia', 'India', 'Namibia', 'China', 'Jordan', 'Tony Tan', 'Iran', 'Fatah', 'Norway', 'Japan', 'Kenya', 'Khin Yi', 'Sweden', 'Madrid', 'Germany', 'Syria', 'Mexico', 'Brazil', 'Lebanon', 'Peter Hain', 'Peru', 'Qin Gang', 'Sukarno', 'Teng Biao', 'Tuva', 'Laos', 'Mike DeWine', 'Shas', 'UNITA', 'Diena', 'Togo', 'Umar', 'Pape Diop', 'Komeito', 'Yukos', 'Pete Wilson', 'Naruhito', 'Ānanda', 'Joe Walsh', 'ANTEL', 'Raúl', 'Ron Kirk', 'Penny Wong', 'Giza', 'Mike Rann', 'Ramdev', 'Wu Aiying', 'Boediono', 'MPLA', 'Bob Rae', 'Guinea']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select 10 most similar answer from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: The most similar 50 entities are: ['Ne Win', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia']. Terminate['Ne Win']

------------------------------# Example1 End ------------------------------ 

------------------------------ Example2 Start ------------------------------ 

[USER (Boss)]: Give me the most aligned entity of the target entity from candidates entity list. If there is same entity, please select directly. The target entity is:
'Salauddin'

The Candidate entities list is: 
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Sukarno', 'Mao Zedong', 'Benin', 'Sam Sesay', 'Poland', 'Ron Wyden', 'Japan', 'Somalia', 'Suharto', 'Vanuatu', 'Panama', 'Ramdev', 'Hamas', 'Lara Giddings', 'Cambodia', 'Sweden', 'Kalyan Singh', 'Aung Min', 'Su Chi', 'Sylvia Lim', 'Ānanda', 'Dan Burton', 'La Nación', 'Khakassia', 'Politiken', 'Kashmir', 'Kashmir', 'Slovenia', 'Samoa', 'Canada', 'Paula Cox', 'Wales', 'Barbados', 'Jay Nixon', 'Bermuda', 'Télam', 'Haaretz', 'Madeira', 'Navarre', 'Sirius XM', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Talal Arslan', 'Raúl', 'Shaul Mofaz', 'Isa Yuguda', 'Imran Khan', 'Yabloko', 'Sima Samar', 'Abdulla Kurd']

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
Act 4:The most similar 50 entities are: ['Abdulla Kurd', 'Sule Lamido','Salam Fayyad','Saad Hariri','Shwe Mann','Shaul Mofaz','Soe Thein','Susan Rice','Sukarno','Suharto','Sam Sesay','Sung Kim','Sima Samar','Sylvia Lim','Sam Nujoma','Su Chi','Samoa','Shas','San Marino','Sinn Féin','Kalyan Singh','Aung Min','Sirindhorn','Hamid Mir','Fatah','Kadima','Babar Awan','Gilad Erdan','Paul Martin','Joe Biden','Ma Kai','Chea Sim','Ron Wyden','Imran Khan','Jawed Ludin','Mali','Malawi','Cambodia','Sweden','Spain','Somalia','Slovenia','Qatar','Kuwait','Oman','Bahrain','Malaysia','Raila Odinga','Benin','Jamaica']. Terminate['Abdulla Kurd']

------------------------------ Example2 End ------------------------------ 


[USER (Boss)]: Give me the 50 most aligned entity and the most aligned entity of the target entity from candidates entity list. If there is same entity, please select directly. Please select from candiates! The target entity is:
Swaziland Youth Congress

The Candidate entities list is: 
['World Jewish Congress', 'Iraqi National Congress', 'Trades Union Congress', 'World Uyghur Congress', "Uganda People's Congress", 'Armenian National Congress', "National People's Congress", 'Hassan Younes', 'Jharkhand Mukti Morcha', 'SWAPO Party Youth League', 'Sarath Fonseka', 'Suez Canal Authority', 'Sandra Torres', 'Hassan Rouhani', 'Latvian Naval Forces', 'Zuzana Roithová', 'Dan Lungren', 'Santiago Creel', 'Denzil Douglas', 'Suleiman Frangieh', 'South Korea', 'Bernard Kouchner', 'Standard Chartered', 'Hamadoun Touré', 'Fesshaye Yohannes', 'Carolyn Rodrigues', 'Fernando Flores', 'Silvan Shalom', 'Sinaloa Cartel', 'Kwabena Duffuor', 'South America', 'Raila Odinga', 'Sirindhorn', 'Aaron Motsoaledi', 'Pravind Jugnauth', 'Kgalema Motlanthe', 'Ferdinand Marcos', 'Sylvain Ndoutingai', 'Simon Coveney', 'Shah Mahmood Qureshi', 'League of Women Voters', 'Sondhi Limthongkul', 'Sally Kosgei', 'Pravin Gordhan', 'Jaswant Singh', 'Maxine Waters', 'Sajjan Kumar', 'Shimon Peres', 'Salvador Namburete', 'Kahinda Otafiire', 'Russian Air Force', 'Julian Assange', 'Martin McGuinness', 'Sten Tolgfors', 'Danilo Astori', 'Ramin Mehmanparast', 'Iranian Space Agency', 'Klaus Wowereit', 'Paulo Portas', 'Harald V of Norway', 'Haqqani network', 'Dragan Šutanovac', 'Davinder Singh', 'Rajnath Singh', 'Panitan Wattanayagorn', 'Denis Sassou Nguesso', 'Vladimiro Montesinos', 'Garibaldi Alves', 'Jean-Louis Borloo', 'Mamadou Tandja', 'Richard Bruton', 'Ricardo Lagos', 'Jiang Tianyong', 'Bala Mohammed', 'William Joseph Burns', 'Sarabjit Singh', 'Sarabjit Singh', 'Shahin Mustafayev', 'Anote Tong', 'Dési Bouterse', 'Daily Nation', 'Daily Nation', 'Maghreb Arabe Press', 'Roland Dumas', 'Yasin Abu Bakr', 'Royal Bank of Canada', 'Crin Antonescu', 'Javier Diez Canseco', 'Milan Kučan', 'Chiang Ching-kuo', 'Alexandr Vondra', 'Harmony Centre', 'Susana Martinez', 'Manuel Chaves', 'Claudio Bonadio', 'Pablo Longueira', 'Johnny Araya Monge', 'Julio Borges', 'Camillo Gonsalves', 'David Johnston', "People's United Democratic Movement"]

NOTE: Please follow my example between "Example i Start" and "Example i End" above to answer task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem. 

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'. Your answer must be in candidate list, otherwise, you will got fired. 
Thought 1:

"""

tmp = """
You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity], which requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 50 entities are: ['xxx', 'xxx', 'xxx'] and Terminate[answer], which returns the answer and finishes the task.
Here are two examples.
Compare the background information of entities carefully to see if they are similar. 
------------------------------# Example1 Start ------------------------------ 

[USER (Boss)]: Give me 50 most similar entities and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The target entity is:
'Ne Win'

The Candidate entities list is: 
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia', 'India', 'Namibia', 'China', 'Jordan', 'Tony Tan', 'Iran', 'Fatah', 'Norway', 'Japan', 'Kenya', 'Khin Yi', 'Sweden', 'Madrid', 'Germany', 'Syria', 'Mexico', 'Brazil', 'Lebanon', 'Peter Hain', 'Peru', 'Qin Gang', 'Sukarno', 'Teng Biao', 'Tuva', 'Laos', 'Mike DeWine', 'Shas', 'UNITA', 'Diena', 'Togo', 'Umar', 'Pape Diop', 'Komeito', 'Yukos', 'Pete Wilson', 'Naruhito', 'Ānanda', 'Joe Walsh', 'ANTEL', 'Raúl', 'Ron Kirk', 'Penny Wong', 'Giza', 'Mike Rann', 'Ramdev', 'Wu Aiying', 'Boediono', 'MPLA', 'Bob Rae', 'Guinea']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select 10 most similar answer from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: The most similar 50 entities are: ['Ne Win', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia'] and Terminate['Ne Win'].

------------------------------# Example1 End ------------------------------ 

[USER (Boss)]: Give me 50 most similar entities and select 1 most similar entity from it to terminate. If there is same entity, please select directly. Please select from candiates! The target entity is:
Swaziland Youth Congress

The Candidate entities list is: 
['World Jewish Congress', 'Iraqi National Congress', 'Trades Union Congress', 'World Uyghur Congress', "Uganda People's Congress", 'Armenian National Congress', "National People's Congress", 'Hassan Younes', 'Jharkhand Mukti Morcha', 'SWAPO Party Youth League', 'Sarath Fonseka', 'Suez Canal Authority', 'Sandra Torres', 'Hassan Rouhani', 'Latvian Naval Forces', 'Zuzana Roithová', 'Dan Lungren', 'Santiago Creel', 'Denzil Douglas', 'Suleiman Frangieh', 'South Korea', 'Bernard Kouchner', 'Standard Chartered', 'Hamadoun Touré', 'Fesshaye Yohannes', 'Carolyn Rodrigues', 'Fernando Flores', 'Silvan Shalom', 'Sinaloa Cartel', 'Kwabena Duffuor', 'South America', 'Raila Odinga', 'Sirindhorn', 'Aaron Motsoaledi', 'Pravind Jugnauth', 'Kgalema Motlanthe', 'Ferdinand Marcos', 'Sylvain Ndoutingai', 'Simon Coveney', 'Shah Mahmood Qureshi', 'League of Women Voters', 'Sondhi Limthongkul', 'Sally Kosgei', 'Pravin Gordhan', 'Jaswant Singh', 'Maxine Waters', 'Sajjan Kumar', 'Shimon Peres', 'Salvador Namburete', 'Kahinda Otafiire', 'Russian Air Force', 'Julian Assange', 'Martin McGuinness', 'Sten Tolgfors', 'Danilo Astori', 'Ramin Mehmanparast', 'Iranian Space Agency', 'Klaus Wowereit', 'Paulo Portas', 'Harald V of Norway', 'Haqqani network', 'Dragan Šutanovac', 'Davinder Singh', 'Rajnath Singh', 'Panitan Wattanayagorn', 'Denis Sassou Nguesso', 'Vladimiro Montesinos', 'Garibaldi Alves', 'Jean-Louis Borloo', 'Mamadou Tandja', 'Richard Bruton', 'Ricardo Lagos', 'Jiang Tianyong', 'Bala Mohammed', 'William Joseph Burns', 'Sarabjit Singh', 'Sarabjit Singh', 'Shahin Mustafayev', 'Anote Tong', 'Dési Bouterse', 'Daily Nation', 'Daily Nation', 'Maghreb Arabe Press', 'Roland Dumas', 'Yasin Abu Bakr', 'Royal Bank of Canada', 'Crin Antonescu', 'Javier Diez Canseco', 'Milan Kučan', 'Chiang Ching-kuo', 'Alexandr Vondra', 'Harmony Centre', 'Susana Martinez', 'Manuel Chaves', 'Claudio Bonadio', 'Pablo Longueira', 'Johnny Araya Monge', 'Julio Borges', 'Camillo Gonsalves', 'David Johnston', "People's United Democratic Movement"]

NOTE: Please follow my example between "Example i Start" and "Example i End" above to answer task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem. 

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'. Your answer must be in candidate list, otherwise, you will got fired. 
Thought 1:

"""

tmp1 = """
You are an programmer and you are solving a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity]. It requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 50 entities are: [] and Terminate[answer]. It returns the answer and finishes the task.
Here are some examples. Compare the background information of entities carefully to see if they are similar. 

------------------------------ Example Start ------------------------------ 
[USER (Boss)]: Give me 50 most not 100 similar entities in list format and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The format is The most similar 50 entities are: [] and Terminate[answer]. The target entity is:
'Swaziland Youth Congress'

The Candidate entities list is: 
['World Jewish Congress', 'Iraqi National Congress', 'Trades Union Congress', 'World Uyghur Congress', "Uganda People's Congress", 'Armenian National Congress', "National People's Congress", 'Hassan Younes', 'Jharkhand Mukti Morcha', 'SWAPO Party Youth League', 'Sarath Fonseka', 'Suez Canal Authority', 'Sandra Torres', 'Hassan Rouhani', 'Latvian Naval Forces', 'Zuzana Roithová', 'Dan Lungren', 'Santiago Creel', 'Denzil Douglas', 'Suleiman Frangieh', 'South Korea', 'Bernard Kouchner', 'Standard Chartered', 'Hamadoun Touré', 'Fesshaye Yohannes', 'Carolyn Rodrigues', 'Fernando Flores', 'Silvan Shalom', 'Sinaloa Cartel', 'Kwabena Duffuor', 'South America', 'Raila Odinga', 'Sirindhorn', 'Aaron Motsoaledi', 'Pravind Jugnauth', 'Kgalema Motlanthe', 'Ferdinand Marcos', 'Sylvain Ndoutingai', 'Simon Coveney', 'Shah Mahmood Qureshi', 'League of Women Voters', 'Sondhi Limthongkul', 'Sally Kosgei', 'Pravin Gordhan', 'Jaswant Singh', 'Maxine Waters', 'Sajjan Kumar', 'Shimon Peres', 'Salvador Namburete', 'Kahinda Otafiire', 'Russian Air Force', 'Julian Assange', 'Martin McGuinness', 'Sten Tolgfors', 'Danilo Astori', 'Ramin Mehmanparast', 'Iranian Space Agency', 'Klaus Wowereit', 'Paulo Portas', 'Harald V of Norway', 'Haqqani network', 'Dragan Šutanovac', 'Davinder Singh', 'Rajnath Singh', 'Panitan Wattanayagorn', 'Denis Sassou Nguesso', 'Vladimiro Montesinos', 'Garibaldi Alves', 'Jean-Louis Borloo', 'Mamadou Tandja', 'Richard Bruton', 'Ricardo Lagos', 'Jiang Tianyong', 'Bala Mohammed', 'William Joseph Burns', 'Sarabjit Singh', 'Sarabjit Singh', 'Shahin Mustafayev', 'Anote Tong', 'Dési Bouterse', 'Daily Nation', 'Daily Nation', 'Maghreb Arabe Press', 'Roland Dumas', 'Yasin Abu Bakr', 'Royal Bank of Canada', 'Crin Antonescu', 'Javier Diez Canseco', 'Milan Kučan', 'Chiang Ching-kuo', 'Alexandr Vondra', 'Harmony Centre', 'Susana Martinez', 'Manuel Chaves', 'Claudio Bonadio', 'Pablo Longueira', 'Johnny Araya Monge', 'Julio Borges', 'Camillo Gonsalves', 'David Johnston', "People's United Democratic Movement"]

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide the final answer. 
Thought 1: The target entity 'Swaziland Youth Congress' is a political entity from Swaziland, which is now Eswatini. To identify the most similar entity, I need to look for other political youth organizations or congresses with a similar profile or regional context.
Act 1: The most similar 50 entities are: ['People's United Democratic Movement', 'SWAPO Party Youth League', 'Hassan Younes', 'Jharkhand Mukti Morcha', 'Sarath Fonseka', 'Sondhi Limthongkul', 'Fernando Flores', 'Sylvain Ndoutingai', 'Simeon Saxe-Coburg-Gotha', 'Ali Mazrui', 'Mamadou Tandja', 'Sarabjit Singh', 'Sarabjit Singh', 'Sajjan Kumar', 'Shaul Mofaz', 'Saad Hariri', 'Salvador Namburete', 'Shahin Mustafayev', 'Anote Tong', 'Dési Bouterse', 'Javier Diez Canseco', 'Pablo Longueira', 'Johnny Araya Monge', 'Julio Borges', 'Camillo Gonsalves', 'David Johnston', 'Sirindhorn', 'Yasin Abu Bakr', 'Roland Dumas', 'Dragan Šutanovac', 'Davinder Singh', 'Rajnath Singh', 'Denis Sassou Nguesso', 'Vladimiro Montesinos', 'Garibaldi Alves', 'Jean-Louis Borloo', 'Richard Bruton', 'Ricardo Lagos', 'Jiang Tianyong', 'Bala Mohammed', 'William Joseph Burns', 'Klaus Wowereit', 'Paulo Portas', 'Haqqani network', 'Kgalema Motlanthe', 'Panitan Wattanayagorn', 'Paul Martin', 'Bayan Muna', 'Paula Cox', 'Barbados'] and Terminate['People's United Democratic Movement'].
------------------------------ Example End ------------------------------

[USER (Boss)]: Give me 50 most not 100 similar entities in list format and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! The target entity is:
'Jomo Gbomo'

The Candidate entities list is: 
['John Nkomo', 'Comoros', 'Fred Gumo', 'Tony Momoh', 'José Bové', 'Jaime Trobo', 'John Hogg', 'Colombia', 'Morocco', 'Bode George', 'Tonio Borg', 'Gideon Gono', 'Seiso Moyo', 'John Dalli', 'Joker Arroyo', 'Rosatom', 'Komeito', 'Tom Ridge', 'Alan Gross', 'John Mahama', 'Boediono', 'Sam Nujoma', 'José Anaya', 'José Serra', 'John Garang', 'John Key', 'Jim Cooper', 'Phil Goff', 'Roilo Golez', 'Joe Walsh', 'Julio Cobos', 'Tomaz Salomão', 'Jim Molan', 'Boko Haram', 'Jacob Zuma', 'James Soong', 'Kosovo', 'Joe Biden', 'John Bercow', 'John Tsang', 'Hong Kong', 'John Kerry', 'John Bruton', 'Jim Inhofe', 'Jordan', 'Gabon', 'Zimbabwe', 'Zambia', 'Cameroon', 'Namibia', 'Somalia', 'Moldova', 'Romania', 'Cambodia', 'Jerry Gana', 'Eskom', 'Lovemore Moyo', 'Issa Aremu', 'Jean Ping', 'Codelco', 'Don Polye', 'Anote Tong', 'J. S. Verma', 'Banobras', 'Tom Thabane', 'Adamu Bello', 'Jason Yuan', 'Abdou Labo', 'Edi Rama', 'Koffi Sama', 'Toyota', 'Jason Hu', 'John Mutorwa', 'Hugo Yasky', 'Dave Camp', 'Karl Hood', 'Monsanto', 'Jubo League', 'Aliyu Doma', 'James Orengo', 'Guy Scott', 'Qin Gang', 'Tião Viana', 'Aldo Bumçi', 'John Luk Jok', 'Naoki Inose', 'Guam', 'Kommersant', 'Pape Diop', 'Tony Tan', 'Tommy Thompson', 'Joe Hockey', 'Google', 'Gordon Brown', 'Jay Nixon', 'Omar Bongo', 'Naoto Kan', 'Chea Sim', 'Kyodo News', 'Sung Kim', 'Henry Okah']

NOTE: You have at most 4 turns to generate final results. Please follow my examples between "Example Start" and "Example End" above to answer task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem. 

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! Otherwise, you will be punished.
Thought 1:
"""

tmp2 = """
You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity]. It requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 50 entities are: <most>[]</most> and Terminate[answer]. It returns the answer and finishes the task. It can only occur once!
Here are two examples.
Compare the background information of entities carefully to see if they are similar. 
------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Give me 50 most similar entities in list format and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly, the format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Ne Win'

The Candidate entities list is: 
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia', 'India', 'Namibia', 'China', 'Jordan', 'Tony Tan', 'Iran', 'Fatah', 'Norway', 'Japan', 'Kenya', 'Khin Yi', 'Sweden', 'Madrid', 'Germany', 'Syria', 'Mexico', 'Brazil', 'Lebanon', 'Peter Hain', 'Peru', 'Qin Gang', 'Sukarno', 'Teng Biao', 'Tuva', 'Laos', 'Mike DeWine', 'Shas', 'UNITA', 'Diena', 'Togo', 'Umar', 'Pape Diop', 'Komeito', 'Yukos', 'Pete Wilson', 'Naruhito', 'Ānanda', 'Joe Walsh', 'ANTEL', 'Raúl', 'Ron Kirk', 'Penny Wong', 'Giza', 'Mike Rann', 'Ramdev', 'Wu Aiying', 'Boediono', 'MPLA', 'Bob Rae', 'Guinea']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select 50 most similar answer and 1 most similar entity from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: The most similar 50 entities are: <most>['Ne Win', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia']</most> and Terminate['Ne Win'].

------------------------------ Example End ------------------------------ 

------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Give me 50 most not 100 similar entities in list format and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The format is The most similar 50 entities are: <most>[]</most> and Terminate[answer]. You have at most 4 turns to finish the task. The target entity is:
'Salauddin'

The Candidate entities list is: 
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Sukarno', 'Mao Zedong', 'Benin', 'Sam Sesay', 'Poland', 'Ron Wyden', 'Japan', 'Somalia', 'Suharto', 'Vanuatu', 'Panama', 'Ramdev', 'Hamas', 'Lara Giddings', 'Cambodia', 'Sweden', 'Kalyan Singh', 'Aung Min', 'Su Chi', 'Sylvia Lim', 'Ānanda', 'Dan Burton', 'La Nación', 'Khakassia', 'Politiken', 'Kashmir', 'Kashmir', 'Slovenia', 'Samoa', 'Canada', 'Paula Cox', 'Wales', 'Barbados', 'Jay Nixon', 'Bermuda', 'Télam', 'Haaretz', 'Madeira', 'Navarre', 'Sirius XM', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Talal Arslan', 'Raúl', 'Shaul Mofaz', 'Isa Yuguda', 'Imran Khan', 'Yabloko', 'Sima Samar', 'Abdulla Kurd']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide the final answer. 
Thought 1: I can find a direct match.
Act 1: The most similar 50 entities are: <most>['Abdulla Kurd', 'Salam Fayyad', 'Hamid Mir', 'Salou Djibo', 'Soe Thein', 'Sukarno', 'Jean Ping', 'Chea Sim', 'Shwe Mann', 'Aung Min', 'Ne Win', 'Gilad Erdan', 'Ramdev', 'Paul Martin', 'Sam Sesay', 'Ma Kai', 'Fatah', 'Sinn Féin', 'Somalia', 'Mao Zedong', 'Hla Min', 'Hla Tun', 'Panama', 'Hamas', 'Suharto', 'Attajdid', 'Talal Arslan', 'Isa Yuguda', 'Saad Hariri', 'Shaul Mofaz', 'Alexandria', 'Carl Levin', 'Sam Nujoma', 'Dan Burton', 'Ron Wyden', 'Kadima', 'Raila Odinga', 'Sylvia Lim', 'Susan Rice', 'Babar Awan', 'Sima Samar', 'Aung San', 'Jawed Ludin', 'Imran Khan', 'Navarre', 'Poland', 'Wales', 'Soe Aung', 'Malawi', 'Benin', 'Tatarstan']</most> and Terminate['Abdulla Kurd'].

------------------------------ Example End ------------------------------ 

[USER (Boss)]: Give me 50 not 100 most similar entities and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The format is The most similar 50 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
{}

The Candidate entities list is: 
{}
  
NOTE: You have at most 4 turns to generate final results. Please follow my example between "Example Start" and "Example End" above to answer task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem. 

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! Otherwise, you will be punished.
Thought 1:

"""

tmp3 = """
You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity]. It requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 50 entities are: [] and Terminate[answer]. It returns the answer and finishes the task.
Here are two examples.
Compare the background information of entities carefully to see if they are similar. 

------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Give me 50 most not 100 similar entities in list format and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! The target entity is:
'Salauddin'

The Candidate entities list is: 
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Sukarno', 'Mao Zedong', 'Benin', 'Sam Sesay', 'Poland', 'Ron Wyden', 'Japan', 'Somalia', 'Suharto', 'Vanuatu', 'Panama', 'Ramdev', 'Hamas', 'Lara Giddings', 'Cambodia', 'Sweden', 'Kalyan Singh', 'Aung Min', 'Su Chi', 'Sylvia Lim', 'Ānanda', 'Dan Burton', 'La Nación', 'Khakassia', 'Politiken', 'Kashmir', 'Kashmir', 'Slovenia', 'Samoa', 'Canada', 'Paula Cox', 'Wales', 'Barbados', 'Jay Nixon', 'Bermuda', 'Télam', 'Haaretz', 'Madeira', 'Navarre', 'Sirius XM', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Talal Arslan', 'Raúl', 'Shaul Mofaz', 'Isa Yuguda', 'Imran Khan', 'Yabloko', 'Sima Samar', 'Abdulla Kurd']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide the final answer. The target entity 'Salauddin' likely needs a comparison with someone of similar regional or functional background.
Thought 1: I need to focus on entities that have backgrounds in the Middle East, South Asia, or regions with similar socio-political contexts.
Act 1: Request['Abdulla Kurd']
Observation 1: 
import is_connected_with

def Abdulla_Kurd_connected_with(Abdulla_Kurd, Turkey):
    Turkey = is_connected_with(Abdulla_Kurd)
    return Abdulla_Kurd, Turkey

if __name__ == '__main__':
    Abdulla_Kurd, Turkey = Abdulla_Kurd_connected_with('Abdulla_Kurd', 'Turkey')


Turn 2:
[Important!] 3 turns left to provide final answer. 
Thought 2: Given the regional and functional similarity, 'Abdulla Kurd' aligns closely with 'Salauddin'. To ensure a comprehensive comparison, I'll examine another related entity from the list.
Act 2: Request['Hamid Mir']
Observation 2: 
import is_connected_with

def Hamid_Mir_connected_with(Hamid_Mir, Pakistan):
    Hamid_Mir = is_connected_with(Pakistan)
    Pakistan = is_connected_with(Hamid_Mir)
    return Hamid_Mir, Pakistan

if __name__ == '__main__':
    Hamid_Mir, Pakistan = Hamid_Mir_connected_with('Hamid_Mir', 'Pakistan')


Turn 3:
[Important!] 2 turns left to provide final answer. 
Thought 3: 'Hamid Mir' has a different background compared to 'Abdulla Kurd', who aligns more closely with the target entity 'Salauddin'. I need to confirm if there is another candidate with a similar background.
Act 3: Request['Salam Fayyad']
Observation 3: 
import birthDate, hasOccupation, alumniOf

def Salam_Fayyad_relations(Salam_Fayyad):
    Salam_Fayyad = birthDate()
    Salam_Fayyad += hasOccupation('Politician')
    Salam_Fayyad += hasOccupation('Economist')
    Salam_Fayyad += alumniOf('American_University_of_Beirut')
    Salam_Fayyad += alumniOf('University_of_Texas_at_Austin')
    return Salam_Fayyad

if __name__ == '__main__':
    Salam_Fayyad = Salam_Fayyad_relations('Salam_Fayyad')

Turn 4:
[Important!] 1 turn left to provide final answer.
Thought 4: 'Abdulla Kurd' and 'Salam Fayyad' both have political backgrounds, but 'Abdulla Kurd' is more directly aligned with the regional and functional background of 'Salauddin'.
Act 4:The most similar 50 entities are: ['Abdulla Kurd', 'Salam Fayyad', 'Hamid Mir', 'Salou Djibo', 'Soe Thein', 'Sukarno', 'Jean Ping', 'Chea Sim', 'Shwe Mann', 'Aung Min', 'Ne Win', 'Gilad Erdan', 'Ramdev', 'Paul Martin', 'Sam Sesay', 'Ma Kai', 'Fatah', 'Sinn Féin', 'Somalia', 'Mao Zedong', 'Hla Min', 'Hla Tun', 'Panama', 'Hamas', 'Suharto', 'Attajdid', 'Talal Arslan', 'Isa Yuguda', 'Saad Hariri', 'Shaul Mofaz', 'Alexandria', 'Carl Levin', 'Sam Nujoma', 'Dan Burton', 'Ron Wyden', 'Kadima', 'Raila Odinga', 'Sylvia Lim', 'Susan Rice', 'Babar Awan', 'Sima Samar', 'Aung San', 'Jawed Ludin', 'Imran Khan', 'Navarre', 'Poland', 'Wales', 'Soe Aung', 'Malawi', 'Benin', 'Tatarstan'] and Terminate['Abdulla Kurd'].
------------------------------ Example End ------------------------------ 

[USER (Boss)]: Give me 50 most not 100 similar entities in list format and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The format is The most similar 50 entities are: [] and Terminate[answer]. The target entity is:
'Swaziland Youth Congress'

The Candidate entities list is: 
['World Jewish Congress', 'Iraqi National Congress', 'Trades Union Congress', 'World Uyghur Congress', "Uganda People's Congress", 'Armenian National Congress', "National People's Congress", 'Hassan Younes', 'Jharkhand Mukti Morcha', 'SWAPO Party Youth League', 'Sarath Fonseka', 'Suez Canal Authority', 'Sandra Torres', 'Hassan Rouhani', 'Latvian Naval Forces', 'Zuzana Roithová', 'Dan Lungren', 'Santiago Creel', 'Denzil Douglas', 'Suleiman Frangieh', 'South Korea', 'Bernard Kouchner', 'Standard Chartered', 'Hamadoun Touré', 'Fesshaye Yohannes', 'Carolyn Rodrigues', 'Fernando Flores', 'Silvan Shalom', 'Sinaloa Cartel', 'Kwabena Duffuor', 'South America', 'Raila Odinga', 'Sirindhorn', 'Aaron Motsoaledi', 'Pravind Jugnauth', 'Kgalema Motlanthe', 'Ferdinand Marcos', 'Sylvain Ndoutingai', 'Simon Coveney', 'Shah Mahmood Qureshi', 'League of Women Voters', 'Sondhi Limthongkul', 'Sally Kosgei', 'Pravin Gordhan', 'Jaswant Singh', 'Maxine Waters', 'Sajjan Kumar', 'Shimon Peres', 'Salvador Namburete', 'Kahinda Otafiire', 'Russian Air Force', 'Julian Assange', 'Martin McGuinness', 'Sten Tolgfors', 'Danilo Astori', 'Ramin Mehmanparast', 'Iranian Space Agency', 'Klaus Wowereit', 'Paulo Portas', 'Harald V of Norway', 'Haqqani network', 'Dragan Šutanovac', 'Davinder Singh', 'Rajnath Singh', 'Panitan Wattanayagorn', 'Denis Sassou Nguesso', 'Vladimiro Montesinos', 'Garibaldi Alves', 'Jean-Louis Borloo', 'Mamadou Tandja', 'Richard Bruton', 'Ricardo Lagos', 'Jiang Tianyong', 'Bala Mohammed', 'William Joseph Burns', 'Sarabjit Singh', 'Sarabjit Singh', 'Shahin Mustafayev', 'Anote Tong', 'Dési Bouterse', 'Daily Nation', 'Daily Nation', 'Maghreb Arabe Press', 'Roland Dumas', 'Yasin Abu Bakr', 'Royal Bank of Canada', 'Crin Antonescu', 'Javier Diez Canseco', 'Milan Kučan', 'Chiang Ching-kuo', 'Alexandr Vondra', 'Harmony Centre', 'Susana Martinez', 'Manuel Chaves', 'Claudio Bonadio', 'Pablo Longueira', 'Johnny Araya Monge', 'Julio Borges', 'Camillo Gonsalves', 'David Johnston', "People's United Democratic Movement"]

NOTE: You have at most 4 turns to generate final results. Please follow my example between "Example Start" and "Example End" above to answer task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem. 

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! Otherwise, you will be punished.
Thought 1:

"""

tmp4 = """
You are an programmer and you are solving a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity]. It requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 50 entities are: [] and Terminate[answer]. It returns the answer and finishes the task.
Here are some examples. Compare the background information of entities carefully to see if they are similar. 

------------------------------ Example Start ------------------------------ 
[USER (Boss)]: Give me 50 most not 100 similar entities in list format and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The format is The most similar 50 entities are: [] and Terminate[answer]. The target entity is:
'Swaziland Youth Congress'

The Candidate entities list is: 
['World Jewish Congress', 'Iraqi National Congress', 'Trades Union Congress', 'World Uyghur Congress', "Uganda People's Congress", 'Armenian National Congress', "National People's Congress", 'Hassan Younes', 'Jharkhand Mukti Morcha', 'SWAPO Party Youth League', 'Sarath Fonseka', 'Suez Canal Authority', 'Sandra Torres', 'Hassan Rouhani', 'Latvian Naval Forces', 'Zuzana Roithová', 'Dan Lungren', 'Santiago Creel', 'Denzil Douglas', 'Suleiman Frangieh', 'South Korea', 'Bernard Kouchner', 'Standard Chartered', 'Hamadoun Touré', 'Fesshaye Yohannes', 'Carolyn Rodrigues', 'Fernando Flores', 'Silvan Shalom', 'Sinaloa Cartel', 'Kwabena Duffuor', 'South America', 'Raila Odinga', 'Sirindhorn', 'Aaron Motsoaledi', 'Pravind Jugnauth', 'Kgalema Motlanthe', 'Ferdinand Marcos', 'Sylvain Ndoutingai', 'Simon Coveney', 'Shah Mahmood Qureshi', 'League of Women Voters', 'Sondhi Limthongkul', 'Sally Kosgei', 'Pravin Gordhan', 'Jaswant Singh', 'Maxine Waters', 'Sajjan Kumar', 'Shimon Peres', 'Salvador Namburete', 'Kahinda Otafiire', 'Russian Air Force', 'Julian Assange', 'Martin McGuinness', 'Sten Tolgfors', 'Danilo Astori', 'Ramin Mehmanparast', 'Iranian Space Agency', 'Klaus Wowereit', 'Paulo Portas', 'Harald V of Norway', 'Haqqani network', 'Dragan Šutanovac', 'Davinder Singh', 'Rajnath Singh', 'Panitan Wattanayagorn', 'Denis Sassou Nguesso', 'Vladimiro Montesinos', 'Garibaldi Alves', 'Jean-Louis Borloo', 'Mamadou Tandja', 'Richard Bruton', 'Ricardo Lagos', 'Jiang Tianyong', 'Bala Mohammed', 'William Joseph Burns', 'Sarabjit Singh', 'Sarabjit Singh', 'Shahin Mustafayev', 'Anote Tong', 'Dési Bouterse', 'Daily Nation', 'Daily Nation', 'Maghreb Arabe Press', 'Roland Dumas', 'Yasin Abu Bakr', 'Royal Bank of Canada', 'Crin Antonescu', 'Javier Diez Canseco', 'Milan Kučan', 'Chiang Ching-kuo', 'Alexandr Vondra', 'Harmony Centre', 'Susana Martinez', 'Manuel Chaves', 'Claudio Bonadio', 'Pablo Longueira', 'Johnny Araya Monge', 'Julio Borges', 'Camillo Gonsalves', 'David Johnston', "People's United Democratic Movement"]

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide the final answer. 
Thought 1: The target entity 'Swaziland Youth Congress' is a political entity from Swaziland, which is now Eswatini. To identify the most similar entity, I need to look for other political youth organizations or congresses with a similar profile or regional context.
Act 1: Request['People's United Democratic Movement']
Observation 1: 
import foundingDate, connected_with

def People's_United_Democratic_Movement_foundingDate(People's_United_Democratic_Movement):
    return foundingDate(People's_United_Democratic_Movement)

def People's_United_Democratic_Movement_connected_with(People's_United_Democratic_Movement, Mario_Masuku, Sipho_Jele):
    People's_United_Democratic_Movement = connected_with(Mario_Masuku)
    People's_United_Democratic_Movement = connected_with(Sipho_Jele)
    Mario_Masuku = connected_with(People's_United_Democratic_Movement)
    Sipho_Jele = connected_with(People's_United_Democratic_Movement)
    return People's_United_Democratic_Movement, Mario_Masuku, Sipho_Jele

if __name__ == '__main__':
    People's_United_Democratic_Movement = People's_United_Democratic_Movement_foundingDate("People's_United_Democratic_Movement")
    People's_United_Democratic_Movement_connected_with("People's_United_Democratic_Movement", 'Mario_Masuku', 'Sipho_Jele')

Turn 2:
[Important!] 3 turns left to provide final answer. 
Thought 2: 'People's United Democratic Movement' has connections with Mario Masuku and Sipho Jele, indicating its involvement in democratic movements and potentially youth-oriented political activities. This aligns closely with the profile expected for 'Swaziland Youth Congress'.
Act 2: Request['SWAPO Party Youth League']
Observation 2: 
import memberOf

def SWAPO_Party_Youth_League_memberOf(SWAPO_Party_Youth_League, World_Federation_of_Democratic_Youth):
    SWAPO_Party_Youth_League = memberOf(World_Federation_of_Democratic_Youth)
    World_Federation_of_Democratic_Youth = memberOf(SWAPO_Party_Youth_League)
    return SWAPO_Party_Youth_League, World_Federation_of_Democratic_Youth

if __name__ == '__main__':
    SWAPO_Party_Youth_League_memberOf('SWAPO_Party_Youth_League', 'World_Federation_of_Democratic_Youth')


Turn 3:
[Important!] 2 turns left to provide final answer. 
Thought 3: The SWAPO Party Youth League is associated with the World Federation of Democratic Youth, emphasizing its role in youth mobilization within a political framework, similar to what might be expected from the 'Swaziland Youth Congress'.
Act 3: Request['World Uyghur Congress']
Observation 3:


Turn 4:
[Important!] 1 turn left to provide final answer.
Thought 4:  'World Uyghur Congress' focuses on representing the Uyghur people's political interests internationally, which is different from the youth-focused political organizations we've examined. Given the previous observations, 'People's United Democratic Movement' and 'SWAPO Party Youth League' align more closely with the profile of 'Swaziland Youth Congress'.
Act4: The most similar 50 entities are: ['People\'s United Democratic Movement', 'SWAPO Party Youth League', 'Hassan Younes', 'Jharkhand Mukti Morcha', 'Sarath Fonseka', 'Sondhi Limthongkul', 'Fernando Flores', 'Sylvain Ndoutingai', 'Simeon Saxe-Coburg-Gotha', 'Ali Mazrui', 'Mamadou Tandja', 'Sarabjit Singh', 'Sarabjit Singh', 'Sajjan Kumar', 'Shaul Mofaz', 'Saad Hariri', 'Salvador Namburete', 'Shahin Mustafayev', 'Anote Tong', 'Dési Bouterse', 'Javier Diez Canseco', 'Pablo Longueira', 'Johnny Araya Monge', 'Julio Borges', 'Camillo Gonsalves', 'David Johnston', 'Sirindhorn', 'Yasin Abu Bakr', 'Roland Dumas', 'Dragan Šutanovac', 'Davinder Singh', 'Rajnath Singh', 'Denis Sassou Nguesso', 'Vladimiro Montesinos', 'Garibaldi Alves', 'Jean-Louis Borloo', 'Richard Bruton', 'Ricardo Lagos', 'Jiang Tianyong', 'Bala Mohammed', 'William Joseph Burns', 'Klaus Wowereit', 'Paulo Portas', 'Haqqani network', 'Kgalema Motlanthe', 'Panitan Wattanayagorn', 'Paul Martin', 'Bayan Muna', 'Paula Cox', 'Barbados'] and Terminate['People's United Democratic Movement'].
------------------------------ Example End ------------------------------

[USER (Boss)]: Give me 50 most not 100 similar entities in list format and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! The target entity is:
'Salauddin'

The Candidate entities list is: 
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Sukarno', 'Mao Zedong', 'Benin', 'Sam Sesay', 'Poland', 'Ron Wyden', 'Japan', 'Somalia', 'Suharto', 'Vanuatu', 'Panama', 'Ramdev', 'Hamas', 'Lara Giddings', 'Cambodia', 'Sweden', 'Kalyan Singh', 'Aung Min', 'Su Chi', 'Sylvia Lim', 'Ānanda', 'Dan Burton', 'La Nación', 'Khakassia', 'Politiken', 'Kashmir', 'Kashmir', 'Slovenia', 'Samoa', 'Canada', 'Paula Cox', 'Wales', 'Barbados', 'Jay Nixon', 'Bermuda', 'Télam', 'Haaretz', 'Madeira', 'Navarre', 'Sirius XM', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Talal Arslan', 'Raúl', 'Shaul Mofaz', 'Isa Yuguda', 'Imran Khan', 'Yabloko', 'Sima Samar', 'Abdulla Kurd']

NOTE: You have at most 4 turns to generate final results. Please follow my examples between "Example Start" and "Example End" above to answer task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem. 

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! Otherwise, you will be punished.
Thought 1:
"""

tmp5 = """
You are an programmer and you are solving a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity]. It requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 50 entities are: [] and Terminate[answer]. It returns the answer and finishes the task.
Here are some examples. Compare the background information of entities carefully to see if they are similar. 

------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Give me 50 most not 100 similar entities in list format and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! The target entity is:
'Salauddin'

The Candidate entities list is: 
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Sukarno', 'Mao Zedong', 'Benin', 'Sam Sesay', 'Poland', 'Ron Wyden', 'Japan', 'Somalia', 'Suharto', 'Vanuatu', 'Panama', 'Ramdev', 'Hamas', 'Lara Giddings', 'Cambodia', 'Sweden', 'Kalyan Singh', 'Aung Min', 'Su Chi', 'Sylvia Lim', 'Ānanda', 'Dan Burton', 'La Nación', 'Khakassia', 'Politiken', 'Kashmir', 'Kashmir', 'Slovenia', 'Samoa', 'Canada', 'Paula Cox', 'Wales', 'Barbados', 'Jay Nixon', 'Bermuda', 'Télam', 'Haaretz', 'Madeira', 'Navarre', 'Sirius XM', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Talal Arslan', 'Raúl', 'Shaul Mofaz', 'Isa Yuguda', 'Imran Khan', 'Yabloko', 'Sima Samar', 'Abdulla Kurd']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide the final answer. The target entity 'Salauddin' likely needs a comparison with someone of similar regional or functional background.
Thought 1: I need to focus on entities that have backgrounds in the Middle East, South Asia, or regions with similar socio-political contexts.
Act 1: Request['Abdulla Kurd']
Observation 1: 
import is_connected_with

def Abdulla_Kurd_connected_with(Abdulla_Kurd, Turkey):
    Turkey = is_connected_with(Abdulla_Kurd)
    return Abdulla_Kurd, Turkey

if __name__ == '__main__':
    Abdulla_Kurd, Turkey = Abdulla_Kurd_connected_with('Abdulla_Kurd', 'Turkey')


Turn 2:
[Important!] 3 turns left to provide final answer. 
Thought 2: Given the regional and functional similarity, 'Abdulla Kurd' aligns closely with 'Salauddin'. To ensure a comprehensive comparison, I'll examine another related entity from the list.
Act 2: Request['Hamid Mir']
Observation 2: 
import is_connected_with

def Hamid_Mir_connected_with(Hamid_Mir, Pakistan):
    Hamid_Mir = is_connected_with(Pakistan)
    Pakistan = is_connected_with(Hamid_Mir)
    return Hamid_Mir, Pakistan

if __name__ == '__main__':
    Hamid_Mir, Pakistan = Hamid_Mir_connected_with('Hamid_Mir', 'Pakistan')


Turn 3:
[Important!] 2 turns left to provide final answer. 
Thought 3: 'Hamid Mir' has a different background compared to 'Abdulla Kurd', who aligns more closely with the target entity 'Salauddin'. I need to confirm if there is another candidate with a similar background.
Act 3: Request['Salam Fayyad']
Observation 3: 
import birthDate, hasOccupation, alumniOf

def Salam_Fayyad_relations(Salam_Fayyad):
    Salam_Fayyad = birthDate()
    Salam_Fayyad += hasOccupation('Politician')
    Salam_Fayyad += hasOccupation('Economist')
    Salam_Fayyad += alumniOf('American_University_of_Beirut')
    Salam_Fayyad += alumniOf('University_of_Texas_at_Austin')
    return Salam_Fayyad

if __name__ == '__main__':
    Salam_Fayyad = Salam_Fayyad_relations('Salam_Fayyad')

Turn 4:
[Important!] 1 turn left to provide final answer.
Thought 4: 'Abdulla Kurd' and 'Salam Fayyad' both have political backgrounds, but 'Abdulla Kurd' is more directly aligned with the regional and functional background of 'Salauddin'.
Act 4:The most similar 50 entities are: ['Abdulla Kurd', 'Salam Fayyad', 'Hamid Mir', 'Salou Djibo', 'Soe Thein', 'Sukarno', 'Jean Ping', 'Chea Sim', 'Shwe Mann', 'Aung Min', 'Ne Win', 'Gilad Erdan', 'Ramdev', 'Paul Martin', 'Sam Sesay', 'Ma Kai', 'Fatah', 'Sinn Féin', 'Somalia', 'Mao Zedong', 'Hla Min', 'Hla Tun', 'Panama', 'Hamas', 'Suharto', 'Attajdid', 'Talal Arslan', 'Isa Yuguda', 'Saad Hariri', 'Shaul Mofaz', 'Alexandria', 'Carl Levin', 'Sam Nujoma', 'Dan Burton', 'Ron Wyden', 'Kadima', 'Raila Odinga', 'Sylvia Lim', 'Susan Rice', 'Babar Awan', 'Sima Samar', 'Aung San', 'Jawed Ludin', 'Imran Khan', 'Navarre', 'Poland', 'Wales', 'Soe Aung', 'Malawi', 'Benin', 'Tatarstan'] and Terminate['Abdulla Kurd'].
------------------------------ Example End ------------------------------ 

[USER (Boss)]: Give me 50 most not 100 similar entities in list format and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The format is The most similar 50 entities are: [] and Terminate[answer]. The target entity is:
'Swaziland Youth Congress'

The Candidate entities list is: 
['World Jewish Congress', 'Iraqi National Congress', 'Trades Union Congress', 'World Uyghur Congress', "Uganda People's Congress", 'Armenian National Congress', "National People's Congress", 'Hassan Younes', 'Jharkhand Mukti Morcha', 'SWAPO Party Youth League', 'Sarath Fonseka', 'Suez Canal Authority', 'Sandra Torres', 'Hassan Rouhani', 'Latvian Naval Forces', 'Zuzana Roithová', 'Dan Lungren', 'Santiago Creel', 'Denzil Douglas', 'Suleiman Frangieh', 'South Korea', 'Bernard Kouchner', 'Standard Chartered', 'Hamadoun Touré', 'Fesshaye Yohannes', 'Carolyn Rodrigues', 'Fernando Flores', 'Silvan Shalom', 'Sinaloa Cartel', 'Kwabena Duffuor', 'South America', 'Raila Odinga', 'Sirindhorn', 'Aaron Motsoaledi', 'Pravind Jugnauth', 'Kgalema Motlanthe', 'Ferdinand Marcos', 'Sylvain Ndoutingai', 'Simon Coveney', 'Shah Mahmood Qureshi', 'League of Women Voters', 'Sondhi Limthongkul', 'Sally Kosgei', 'Pravin Gordhan', 'Jaswant Singh', 'Maxine Waters', 'Sajjan Kumar', 'Shimon Peres', 'Salvador Namburete', 'Kahinda Otafiire', 'Russian Air Force', 'Julian Assange', 'Martin McGuinness', 'Sten Tolgfors', 'Danilo Astori', 'Ramin Mehmanparast', 'Iranian Space Agency', 'Klaus Wowereit', 'Paulo Portas', 'Harald V of Norway', 'Haqqani network', 'Dragan Šutanovac', 'Davinder Singh', 'Rajnath Singh', 'Panitan Wattanayagorn', 'Denis Sassou Nguesso', 'Vladimiro Montesinos', 'Garibaldi Alves', 'Jean-Louis Borloo', 'Mamadou Tandja', 'Richard Bruton', 'Ricardo Lagos', 'Jiang Tianyong', 'Bala Mohammed', 'William Joseph Burns', 'Sarabjit Singh', 'Sarabjit Singh', 'Shahin Mustafayev', 'Anote Tong', 'Dési Bouterse', 'Daily Nation', 'Daily Nation', 'Maghreb Arabe Press', 'Roland Dumas', 'Yasin Abu Bakr', 'Royal Bank of Canada', 'Crin Antonescu', 'Javier Diez Canseco', 'Milan Kučan', 'Chiang Ching-kuo', 'Alexandr Vondra', 'Harmony Centre', 'Susana Martinez', 'Manuel Chaves', 'Claudio Bonadio', 'Pablo Longueira', 'Johnny Araya Monge', 'Julio Borges', 'Camillo Gonsalves', 'David Johnston', "People's United Democratic Movement"]

NOTE: You have at most 4 turns to generate final results. Please follow my examples between "Example Start" and "Example End" above to answer task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem. 

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! Otherwise, you will be punished.
Thought 1:

"""

tmp6 = """
You are an programmer and you are solving a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity]. It requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 50 entities are: [] and Terminate[answer]. It returns the answer and finishes the task.
Here are some examples. Compare the background information of entities carefully to see if they are similar. 

------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Give me 50 most not 100 similar entities in list format and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! The target entity is:
'Víctor Quispe Palomino'

The Candidate entities list is: 
['Voltaire Gazmin', 'Vítor Constâncio', 'Vítor Gaspar', 'Viktor Uspaskich', 'Victor Ponta', 'Louisa Hanoune', 'Boris Yeltsin', 'Scottish Parliament', 'Viktor Yushchenko', 'Marcos Valério', 'Sule Lamido', 'Tomaz Salomão', 'Borut Pahor', 'Otto Pérez Molina', 'Georgi Parvanov', 'Vittorio Grilli', 'François Baroin', 'Patricio Aylwin', 'Verónica Macamo', 'Luis Walton', 'Viktor Pshonka', 'Viktor Ivanov', 'Artis Pabriks', 'Clive Palmer', 'Isatou Njie-Saidy', 'Boris Tadić', 'Vladimír Palko', 'Louise Arbour', 'Viktor Zubkov', 'Fatos Nano', 'Moshe Kahlon', 'Giorgio Napolitano', 'Bantu Holomisa', 'Josip Manolić', 'Caroline Flint', 'Peter Costello', 'Viktor Ishayev', 'Victor Ndoma-Egba', 'Nicolai Wammen', 'Henrique Salas Feo', 'Víctor Julio Suárez Rojas', 'Ariel Querubin', 'Camilo Escalona', 'Javier Diez Canseco', 'Anthony Garotinho', 'Joaquim Chissano', 'Festus Keyamo', 'Antonio Patriota', 'Otto Guevara', 'Comrade Artemio', 'Florencio Randazzo', 'Grete Faremo', 'Andrés Allamand', 'Ignatius Chombo', 'Nicolás Maduro', 'Cyrus Jirongo', 'Keriako Tobiko', 'Marta Suplicy', 'Sithembiso Nyoni', 'Johannes Tomana', 'Henri Djombo', 'Carlos Zannini', 'Patricia Bullrich', 'Vitalie Marinuța', 'Julius Malema', 'Utoni Nujoma', 'Abdo Hussameddin', 'Viviane Reding', 'Raymond Benjamin', 'Bujar Nishani', 'Denis Napthine', 'Toke Talagi', 'Aaron Motsoaledi', 'Ante Gotovina', 'Ivo Opstelten', 'Anton Siluanov', 'Jacques Delors', 'Yossi Beilin', 'Felipe Calderón', 'Brigi Rafini', 'Amadou Sanogo', 'Cecilia Muñoz-Palma', 'Francis Pangilinan', 'Cheikh Tidiane Gadio', 'Peter Esele', 'Peter Murcott Bunting', 'Ram Vilas Paswan', 'Dmitry Rogozin', 'Valérie Pécresse', 'Emomali Rahmon', 'Christine Boutin', 'Irene Muloni', 'Boris Johnson', 'Kayode Fayemi', 'Nicolas Schmit', 'Peter Gibson', 'Chris Bowen', 'Grigory Karasin', 'Philip Hammond', 'Jean-Louis Tauran', 'Comrade José']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide the final answer. 
Thought 1:  The target entity 'Víctor Quispe Palomino' is associated with the Shining Path, a militant group in Peru. To find the most similar entity, I need to identify other individuals or entities connected to militant or insurgent groups with similar profiles.
Act 1: Request['Comrade Artemio']
Observation 1: 
import birthDate, hasOccupation, knowsLanguage, nationality, birthPlace

def Comrade_Artemio_BirthDate_Occupation_Language_Nationality_BirthPlace(Comrade_Artemio, Politician, Spanish_language, Peru, Partisan_military):
    Comrade_Artemio = birthDate()
    Comrade_Artemio = hasOccupation(Politician)
    Comrade_Artemio = knowsLanguage(Spanish_language)
    Comrade_Artemio = nationality(Peru)
    Comrade_Artemio = birthPlace(Peru)
    Comrade_Artemio = hasOccupation(Partisan_military)
    return Comrade_Artemio, Politician, Spanish_language, Peru, Partisan_military

if __name__ == '__main__':
    Comrade_Artemio_BirthDate_Occupation_Language_Nationality_BirthPlace('Comrade_Artemio', 'Politician', 'Spanish_language', 'Peru', 'Partisan_(military)')



Turn 2:
[Important!] 3 turns left to provide final answer. 
Thought 2: The entity 'Comrade Artemio' shares a similar background with 'Víctor Quispe Palomino', both being involved in militant activities in Peru. This makes 'Comrade Artemio' a strong candidate for alignment. To further confirm, I need to explore more entities connected to militant or insurgent groups.
Act 2: Request['Víctor Julio Suárez Rojas']
Observation 2: 
import birthDate, deathDate, nationality, givenName, memberOf

def Victor_Julio_Suarez_Rojas_Relations(Victor_Julio_Suarez_Rojas, Colombia, Jorge, Revolutionary_Armed_Forces_of_Colombia):
    Victor_Julio_Suarez_Rojas = birthDate()
    Victor_Julio_Suarez_Rojas = deathDate()
    Victor_Julio_Suarez_Rojas = nationality(Colombia)
    Victor_Julio_Suarez_Rojas = givenName(Jorge)
    Victor_Julio_Suarez_Rojas = memberOf(Revolutionary_Armed_Forces_of_Colombia)
    return Victor_Julio_Suarez_Rojas, Colombia, Jorge, Revolutionary_Armed_Forces_of_Colombia

if __name__ == '__main__':
    Victor_Julio_Suarez_Rojas_Relations('Victor_Julio_Suarez_Rojas', 'Colombia', 'Jorge', 'Revolutionary_Armed_Forces_of_Colombia')


Turn 3: 
[Important!] 2 turns left to provide final answer. 
Thought 3: 'Víctor Julio Suárez Rojas' shares a similar militant background but is associated with Colombia rather than Peru. Although similar, 'Comrade Artemio' is still a closer match due to the shared nationality with 'Víctor Quispe Palomino'. To further confirm, I will investigate another entity with a militant background.
Act 3: Request['Comrade José']
Observation 3: 
import birthDate, nationality

def Comrade_Jose_Relations(Comrade_Jose, Peru):
    Comrade_Jose = birthDate()
    Comrade_Jose = nationality(Peru)
    return Comrade_Jose, Peru

if __name__ == '__main__':
    Comrade_Jose_Relations('Comrade_Jose', 'Peru')
    

Turn 4:
[Important!] 1 turn left to provide final answer.
Thought 4: Comrade José' also shares a militant background and nationality with 'Víctor Quispe Palomino', making him another strong candidate. Based on the information gathered, both 'Comrade Artemio' and 'Comrade José' are highly similar to 'Víctor Quispe Palomino'. Given the matching nationality and similar backgrounds, either could be the correct answer.
Act 4:The most similar 50 entities are: ['Comrade Artemio', 'Comrade José', 'Víctor Julio Suárez Rojas', 'Viktor Uspaskich', 'Victor Ponta', 'Boris Yeltsin', 'Viktor Yushchenko', 'Marcos Valério', 'Sule Lamido', 'Tomaz Salomão', 'Borut Pahor', 'Otto Pérez Molina', 'Georgi Parvanov', 'Vittorio Grilli', 'François Baroin', 'Patricio Aylwin', 'Verónica Macamo', 'Luis Walton', 'Viktor Pshonka', 'Viktor Ivanov', 'Artis Pabriks', 'Clive Palmer', 'Isatou Njie-Saidy', 'Boris Tadić', 'Vladimír Palko', 'Louise Arbour', 'Viktor Zubkov', 'Fatos Nano', 'Moshe Kahlon', 'Giorgio Napolitano', 'Bantu Holomisa', 'Josip Manolić', 'Caroline Flint', 'Peter Costello', 'Viktor Ishayev', 'Victor Ndoma-Egba', 'Nicolai Wammen', 'Henrique Salas Feo', 'Ariel Querubin', 'Camilo Escalona', 'Javier Diez Canseco', 'Anthony Garotinho', 'Joaquim Chissano', 'Festus Keyamo', 'Antonio Patriota', 'Otto Guevara', 'Florencio Randazzo', 'Grete Faremo', 'Andrés Allamand'] and Terminate['Comrade José'].

------------------------------ Example End ------------------------------ 

[USER (Boss)]: Give me 50 most not 100 similar entities in list format and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! The target entity is:
'Jomo Gbomo'

The Candidate entities list is: 
['John Nkomo', 'Comoros', 'Fred Gumo', 'Tony Momoh', 'José Bové', 'Jaime Trobo', 'John Hogg', 'Colombia', 'Morocco', 'Bode George', 'Tonio Borg', 'Gideon Gono', 'Seiso Moyo', 'John Dalli', 'Joker Arroyo', 'Rosatom', 'Komeito', 'Tom Ridge', 'Alan Gross', 'John Mahama', 'Boediono', 'Sam Nujoma', 'José Anaya', 'José Serra', 'John Garang', 'John Key', 'Jim Cooper', 'Phil Goff', 'Roilo Golez', 'Joe Walsh', 'Julio Cobos', 'Tomaz Salomão', 'Jim Molan', 'Boko Haram', 'Jacob Zuma', 'James Soong', 'Kosovo', 'Joe Biden', 'John Bercow', 'John Tsang', 'Hong Kong', 'John Kerry', 'John Bruton', 'Jim Inhofe', 'Jordan', 'Gabon', 'Zimbabwe', 'Zambia', 'Cameroon', 'Namibia', 'Somalia', 'Moldova', 'Romania', 'Cambodia', 'Jerry Gana', 'Eskom', 'Lovemore Moyo', 'Issa Aremu', 'Jean Ping', 'Codelco', 'Don Polye', 'Anote Tong', 'J. S. Verma', 'Banobras', 'Tom Thabane', 'Adamu Bello', 'Jason Yuan', 'Abdou Labo', 'Edi Rama', 'Koffi Sama', 'Toyota', 'Jason Hu', 'John Mutorwa', 'Hugo Yasky', 'Dave Camp', 'Karl Hood', 'Monsanto', 'Jubo League', 'Aliyu Doma', 'James Orengo', 'Guy Scott', 'Qin Gang', 'Tião Viana', 'Aldo Bumçi', 'John Luk Jok', 'Naoki Inose', 'Guam', 'Kommersant', 'Pape Diop', 'Tony Tan', 'Tommy Thompson', 'Joe Hockey', 'Google', 'Gordon Brown', 'Jay Nixon', 'Omar Bongo', 'Naoto Kan', 'Chea Sim', 'Kyodo News', 'Sung Kim', 'Henry Okah']

NOTE: You have at most 4 turns to generate final results. Please follow my examples between "Example Start" and "Example End" above to answer task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem. 

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! Otherwise, you will be punished.
Thought 1:

"""

tmp7 = """
Help USER finish the following task.
You are an programmer and you are solving a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity]. It requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 50 entities are: <most>[]</most> and Terminate[answer]. It returns the answer and finishes the task.
Here are some examples. Compare the background information of entities carefully to see if they are similar. 

------------------------------ Example1 Start ------------------------------ 

[USER (Boss)]: Give me 50 most similar entities in list format and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly, the format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer]. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! The target entity is:
'Ne Win'

The Candidate entities list is: 
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia', 'India', 'Namibia', 'China', 'Jordan', 'Tony Tan', 'Iran', 'Fatah', 'Norway', 'Japan', 'Kenya', 'Khin Yi', 'Sweden', 'Madrid', 'Germany', 'Syria', 'Mexico', 'Brazil', 'Lebanon', 'Peter Hain', 'Peru', 'Qin Gang', 'Sukarno', 'Teng Biao', 'Tuva', 'Laos', 'Mike DeWine', 'Shas', 'UNITA', 'Diena', 'Togo', 'Umar', 'Pape Diop', 'Komeito', 'Yukos', 'Pete Wilson', 'Naruhito', 'Ānanda', 'Joe Walsh', 'ANTEL', 'Raúl', 'Ron Kirk', 'Penny Wong', 'Giza', 'Mike Rann', 'Ramdev', 'Wu Aiying', 'Boediono', 'MPLA', 'Bob Rae', 'Guinea']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select 50 most similar answer and 1 most similar entity from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: The most similar 50 entities are: <most>['Ne Win', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia']</most> and Terminate['Ne Win'].

------------------------------ Example1 End ------------------------------ 

------------------------------ Example3 Start ------------------------------ 

[USER (Boss)]: Give me 50 most similar entities in list format and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task.  If there is same entity in candidate list for target entity, please select directly, the format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer]. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation. The target entity is:
'Shin Corp'

The Candidate entities list is: 
['Shin Bet', 'Tin Oo', 'Khin Yi', 'Sirindhorn', 'Phil Goff', 'Shiv Sena', 'Singapore', 'Su Chi', 'Peace Corps', 'Khun Sa', 'Qin Gang', 'Shinzo Abe', 'Eric Chu', 'Nuon Chea', 'Shwe Mann', 'Jim Cooper', 'Sinn Féin', 'Tonio Borg', 'Yin Zhuo', 'Bob Carr', 'Dave Camp', 'Sinopec', 'Than Shwe', 'Ron Kirk', 'Seiso Moyo', 'Selim Hoss', 'Emil Boc', 'Than Htay', 'John Hogg', 'Manny Mori', 'Shimon Peres', 'Equinor', 'China', 'Ieng Sary', 'Citigroup', 'Sung Kim', 'Sony', 'Civic Forum', 'Chea Sim', 'Hun Sen', 'Lin Yi-fu', 'Maung Oo', 'Shining Path', 'Ilir Meta', 'Penny Wong', 'Don Polye', 'Hong Kong', 'Thein Nyunt', 'Fine Gael', 'Vic Toews', 'Jim Molan', 'Chang Po-ya', 'Eric Cantor', 'Yen Ming', 'Bamir Topi', 'Shaul Mofaz', 'Mark Kirk', 'Jean Ping', 'Chen Zhili', 'Zhang Gaoli', 'John Key', 'Aliyu Doma', 'Susan Rice', 'David Mark', 'John Kerry', 'Ioan Rus', 'Shas', 'Htay Oo', 'Stephen Rapp', 'Suharto', 'Salzburg', 'Hamid Mir', 'Alan Gross', 'Mindanao', 'San Marino', 'Paula Cox', 'Edwin Snowe', 'Edi Rama', 'Sukh Ram', 'Jim Murphy', 'Xie Xuren', 'Sukarno', 'Chris Bowen', 'Guinea', 'Helen Clark', 'Alain Juppé', 'Liam Fox', 'Angola', 'Saint Lucia', 'Samoa', 'Akihito', 'Sicily', 'Sidwaya', 'Monaco', 'Thad Cochran', 'Julio Cobos', 'Karl Hood', 'Ehud Barak', 'Kevin Rudd', 'John Nkomo', 'Intouch Holdings']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide the final answer. 
Thought 1:  The target entity 'Shin Corp' is a company based in Thailand. To find the most similar entity, I should focus on entities related to companies, especially those with a significant presence in Asia or that share similar characteristics with 'Shin Corp.'
Act 1: Request['Intouch Holdings']
Observation 1: 
import is_connected_with, founder

def Intouch_Holdings_connected_with(Intouch_Holdings, Thaksin_Shinawatra):
    Intouch_Holdings = is_connected_with(Thaksin_Shinawatra)
    Thaksin_Shinawatra = founder(Intouch_Holdings)
    return Intouch_Holdings, Thaksin_Shinawatra

if name == 'main':
Intouch_Holdings, Thaksin_Shinawatra = Intouch_Holdings_connected_with('Intouch_Holdings', 'Thaksin_Shinawatra')

Turn 2:
[Important!] 3 turns left to provide final answer. 
Thought 2:  'Intouch Holdings' is closely related to 'Shin Corp' through its founder Thaksin Shinawatra, who also has a significant connection with 'Shin Corp.' This makes 'Intouch Holdings' a strong candidate. To further confirm, I'll need to check more entities related to companies or those connected to the same region.
Act 2: Request['Shinzo Abe']
Observation 2: 
import is_connected_with, connected_with

def Japan_connected_with(Shinzo_Abe, Japan):
    Japan = is_connected_with(Shinzo_Abe)
    Shinzo_Abe = connected_with(Japan)
    return Japan, Shinzo_Abe

def Liberal_Democratic_Party_connected_with(Shinzo_Abe, Liberal_Democratic_Party_Japan):
    Liberal_Democratic_Party_Japan = is_connected_with(Shinzo_Abe)
    Shinzo_Abe = connected_with(Liberal_Democratic_Party_Japan)
    return Liberal_Democratic_Party_Japan, Shinzo_Abe

def Shinzo_Abe_connected_with_Akie_Abe(Shinzo_Abe, Akie_Abe):
    Shinzo_Abe = connected_with(Akie_Abe)
    Akie_Abe = connected_with(Shinzo_Abe)
    return Shinzo_Abe, Akie_Abe

def Liberal_Democratic_Party_with_Shinzo_Abe_and_Akie_Abe(Liberal_Democratic_Party_Japan, Shinzo_Abe, Akie_Abe):
    Liberal_Democratic_Party_Japan = connected_with(Shinzo_Abe)
    Liberal_Democratic_Party_Japan += connected_with(Akie_Abe)
    Shinzo_Abe = connected_with(Akie_Abe)
    Akie_Abe = connected_with(Shinzo_Abe)
    return Liberal_Democratic_Party_Japan, Shinzo_Abe, Akie_Abe

def Japanese_language_with_Shinzo_Abe_and_Akie_Abe(Japanese_language, Shinzo_Abe, Akie_Abe):
    Japanese_language = connected_with(Shinzo_Abe)
    Japanese_language += connected_with(Akie_Abe)
    Shinzo_Abe = connected_with(Akie_Abe)
    Akie_Abe = connected_with(Shinzo_Abe)
    return Japanese_language, Shinzo_Abe, Akie_Abe

if name == 'main':
    Japan, Shinzo_Abe = Japan_connected_with('Shinzo_Abe', 'Japan')
    Liberal_Democratic_Party_Japan, Shinzo_Abe = Liberal_Democratic_Party_connected_with('Shinzo_Abe', 'Liberal_Democratic_Party_(Japan)')
    Shinzo_Abe, Akie_Abe = Shinzo_Abe_connected_with_Akie_Abe('Shinzo_Abe', 'Akie_Abe')
    Liberal_Democratic_Party_Japan, Shinzo_Abe, Akie_Abe = Liberal_Democratic_Party_with_Shinzo_Abe_and_Akie_Abe('Liberal_Democratic_Party_(Japan)', 'Shinzo_Abe', 'Akie_Abe')
    Japanese_language, Shinzo_Abe, Akie_Abe = Japanese_language_with_Shinzo_Abe_and_Akie_Abe('Japanese_language', 'Shinzo_Abe', 'Akie_Abe')


Turn 3: 
[Important!] 2 turns left to provide final answer. 
Thought 3: 'Shinzo Abe' is a prominent Japanese politician and not directly related to 'Shin Corp.' The strong connection of 'Intouch Holdings' with 'Shin Corp' through Thaksin Shinawatra makes it the closest match. To confirm, I will review another entity closely related to companies or Thailand.
Act 3: Request['Sinopec']
Observation 3: 
import foundingLocation
    def Sinopec_foundingLocation(Sinopec, Beijing):
    Sinopec = foundingLocation(Beijing)
    return Sinopec

if name == 'main':
    Sinopec = Sinopec_foundingLocation('Sinopec', 'Beijing')

Turn 4:
[Important!] 1 turn left to provide final answer.
Thought 4: 'Sinopec' is a major company based in Beijing, China, which is not closely related to 'Shin Corp' based in Thailand. Given the information gathered, 'Intouch Holdings' is clearly more aligned with 'Shin Corp' due to its direct connection through Thaksin Shinawatra.
Act 4:The most similar 50 entities are: <most>['Intouch Holdings', 'Shinzo Abe', 'Sinopec', 'Shin Bet', 'Tin Oo', 'Khin Yi', 'Sirindhorn', 'Phil Goff', 'Shiv Sena', 'Singapore', 'Su Chi', 'Peace Corps', 'Khun Sa', 'Qin Gang', 'Eric Chu', 'Nuon Chea', 'Shwe Mann', 'Jim Cooper', 'Sinn Féin', 'Tonio Borg', 'Yin Zhuo', 'Bob Carr', 'Dave Camp', 'Sinopec', 'Than Shwe', 'Ron Kirk', 'Seiso Moyo', 'Selim Hoss', 'Emil Boc', 'Than Htay', 'John Hogg', 'Manny Mori', 'Shimon Peres', 'Equinor', 'China', 'Ieng Sary', 'Citigroup', 'Sung Kim', 'Sony', 'Civic Forum', 'Chea Sim', 'Hun Sen', 'Lin Yi-fu', 'Maung Oo', 'Shining Path', 'Ilir Meta', 'Penny Wong', 'Don Polye', 'Hong Kong', 'Thein Nyunt', 'Fine Gael']</most> and Terminate['Intouch Holdings'].

------------------------------ Example3 End ------------------------------ 

[USER (Boss)]: Give me 50 most similar entities in list format and select 1 most similar entity from it to terminate. If there is same entity in candidate list for target entity, please select directly, the format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer]. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation. The target entity is:
'Jomo Gbomo'

The Candidate entities list is: 
['John Nkomo', 'Comoros', 'Fred Gumo', 'Tony Momoh', 'José Bové', 'Jaime Trobo', 'John Hogg', 'Colombia', 'Morocco', 'Bode George', 'Tonio Borg', 'Gideon Gono', 'Seiso Moyo', 'John Dalli', 'Joker Arroyo', 'Rosatom', 'Komeito', 'Tom Ridge', 'Alan Gross', 'John Mahama', 'Boediono', 'Sam Nujoma', 'José Anaya', 'José Serra', 'John Garang', 'John Key', 'Jim Cooper', 'Phil Goff', 'Roilo Golez', 'Joe Walsh', 'Julio Cobos', 'Tomaz Salomão', 'Jim Molan', 'Boko Haram', 'Jacob Zuma', 'James Soong', 'Kosovo', 'Joe Biden', 'John Bercow', 'John Tsang', 'Hong Kong', 'John Kerry', 'John Bruton', 'Jim Inhofe', 'Jordan', 'Gabon', 'Zimbabwe', 'Zambia', 'Cameroon', 'Namibia', 'Somalia', 'Moldova', 'Romania', 'Cambodia', 'Jerry Gana', 'Eskom', 'Lovemore Moyo', 'Issa Aremu', 'Jean Ping', 'Codelco', 'Don Polye', 'Anote Tong', 'J. S. Verma', 'Banobras', 'Tom Thabane', 'Adamu Bello', 'Jason Yuan', 'Abdou Labo', 'Edi Rama', 'Koffi Sama', 'Toyota', 'Jason Hu', 'John Mutorwa', 'Hugo Yasky', 'Dave Camp', 'Karl Hood', 'Monsanto', 'Jubo League', 'Aliyu Doma', 'James Orengo', 'Guy Scott', 'Qin Gang', 'Tião Viana', 'Aldo Bumçi', 'John Luk Jok', 'Naoki Inose', 'Guam', 'Kommersant', 'Pape Diop', 'Tony Tan', 'Tommy Thompson', 'Joe Hockey', 'Google', 'Gordon Brown', 'Jay Nixon', 'Omar Bongo', 'Naoto Kan', 'Chea Sim', 'Kyodo News', 'Sung Kim', 'Henry Okah']
  
NOTE: You have at most 4 turns to generate final results. Please follow my examples between "Example 1 Start","Example 1 End", "Example 2 Start","Example 2 End" and "Example 3 Start","Example 3 End" above to answer task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem. 

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If there is same entity, please select directly, the format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer]. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! Otherwise, you will be punished.
Thought 1:

"""