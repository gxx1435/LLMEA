motif_ReAct_example_prompt = """
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
