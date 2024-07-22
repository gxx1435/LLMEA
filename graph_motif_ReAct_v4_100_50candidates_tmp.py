motif_ReAct_example_prompt = """
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
