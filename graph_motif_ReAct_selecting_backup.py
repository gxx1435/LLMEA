motif_ReAct_example_prompt_cn100_cn50 = ("""
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

NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select 50 most similar answer and 1 most similar entity from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: The most similar 50 entities are: <most>['Ne Win', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia']</most> and Terminate['Ne Win'].

------------------------------ Example End ------------------------------ 

------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Give me 50 most similar entities in list format and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The format is The most similar 50 entities are: <most>[]</most> and Terminate[answer]. You have at most 4 turns to finish the task. The target entity is:
'Salauddin'

The Candidate entities list is: 
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Sukarno', 'Mao Zedong', 'Benin', 'Sam Sesay', 'Poland', 'Ron Wyden', 'Japan', 'Somalia', 'Suharto', 'Vanuatu', 'Panama', 'Ramdev', 'Hamas', 'Lara Giddings', 'Cambodia', 'Sweden', 'Kalyan Singh', 'Aung Min', 'Su Chi', 'Sylvia Lim', 'Ānanda', 'Dan Burton', 'La Nación', 'Khakassia', 'Politiken', 'Kashmir', 'Kashmir', 'Slovenia', 'Samoa', 'Canada', 'Paula Cox', 'Wales', 'Barbados', 'Jay Nixon', 'Bermuda', 'Télam', 'Haaretz', 'Madeira', 'Navarre', 'Sirius XM', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Talal Arslan', 'Raúl', 'Shaul Mofaz', 'Isa Yuguda', 'Imran Khan', 'Yabloko', 'Sima Samar', 'Abdulla Kurd']

NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

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
  
NOTE: 
1. You have at most 4 turns to generate final results. Please follow my example between "Example Start" and "Example End" above to answer task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem. 
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! Otherwise, you will be punished.
Thought 1:

"""
.format(
    # 'Swaziland Youth Congress',
    # ['World Jewish Congress', 'Iraqi National Congress', 'Trades Union Congress', 'World Uyghur Congress', "Uganda People's Congress", 'Armenian National Congress', "National People's Congress", 'Hassan Younes', 'Jharkhand Mukti Morcha', 'SWAPO Party Youth League', 'Sarath Fonseka', 'Suez Canal Authority', 'Sandra Torres', 'Hassan Rouhani', 'Latvian Naval Forces', 'Zuzana Roithová', 'Dan Lungren', 'Santiago Creel', 'Denzil Douglas', 'Suleiman Frangieh', 'South Korea', 'Bernard Kouchner', 'Standard Chartered', 'Hamadoun Touré', 'Fesshaye Yohannes', 'Carolyn Rodrigues', 'Fernando Flores', 'Silvan Shalom', 'Sinaloa Cartel', 'Kwabena Duffuor', 'South America', 'Raila Odinga', 'Sirindhorn', 'Aaron Motsoaledi', 'Pravind Jugnauth', 'Kgalema Motlanthe', 'Ferdinand Marcos', 'Sylvain Ndoutingai', 'Simon Coveney', 'Shah Mahmood Qureshi', 'League of Women Voters', 'Sondhi Limthongkul', 'Sally Kosgei', 'Pravin Gordhan', 'Jaswant Singh', 'Maxine Waters', 'Sajjan Kumar', 'Shimon Peres', 'Salvador Namburete', 'Kahinda Otafiire', 'Russian Air Force', 'Julian Assange', 'Martin McGuinness', 'Sten Tolgfors', 'Danilo Astori', 'Ramin Mehmanparast', 'Iranian Space Agency', 'Klaus Wowereit', 'Paulo Portas', 'Harald V of Norway', 'Haqqani network', 'Dragan Šutanovac', 'Davinder Singh', 'Rajnath Singh', 'Panitan Wattanayagorn', 'Denis Sassou Nguesso', 'Vladimiro Montesinos', 'Garibaldi Alves', 'Jean-Louis Borloo', 'Mamadou Tandja', 'Richard Bruton', 'Ricardo Lagos', 'Jiang Tianyong', 'Bala Mohammed', 'William Joseph Burns', 'Sarabjit Singh', 'Sarabjit Singh', 'Shahin Mustafayev', 'Anote Tong', 'Dési Bouterse', 'Daily Nation', 'Daily Nation', 'Maghreb Arabe Press', 'Roland Dumas', 'Yasin Abu Bakr', 'Royal Bank of Canada', 'Crin Antonescu', 'Javier Diez Canseco', 'Milan Kučan', 'Chiang Ching-kuo', 'Alexandr Vondra', 'Harmony Centre', 'Susana Martinez', 'Manuel Chaves', 'Claudio Bonadio', 'Pablo Longueira', 'Johnny Araya Monge', 'Julio Borges', 'Camillo Gonsalves', 'David Johnston', "People's United Democratic Movement"]
    'Víctor Quispe Palomino',
    ['Voltaire Gazmin', 'Vítor Constâncio', 'Vítor Gaspar', 'Viktor Uspaskich', 'Victor Ponta', 'Louisa Hanoune',
     'Boris Yeltsin', 'Scottish Parliament', 'Viktor Yushchenko', 'Marcos Valério', 'Sule Lamido', 'Tomaz Salomão',
     'Borut Pahor', 'Otto Pérez Molina', 'Georgi Parvanov', 'Vittorio Grilli', 'François Baroin', 'Patricio Aylwin',
     'Verónica Macamo', 'Luis Walton', 'Viktor Pshonka', 'Viktor Ivanov', 'Artis Pabriks', 'Clive Palmer',
     'Isatou Njie-Saidy', 'Boris Tadić', 'Vladimír Palko', 'Louise Arbour', 'Viktor Zubkov', 'Fatos Nano',
     'Moshe Kahlon', 'Giorgio Napolitano', 'Bantu Holomisa', 'Josip Manolić', 'Caroline Flint', 'Peter Costello',
     'Viktor Ishayev', 'Victor Ndoma-Egba', 'Nicolai Wammen', 'Henrique Salas Feo', 'Víctor Julio Suárez Rojas',
     'Ariel Querubin', 'Camilo Escalona', 'Javier Diez Canseco', 'Anthony Garotinho', 'Joaquim Chissano',
     'Festus Keyamo', 'Antonio Patriota', 'Otto Guevara', 'Comrade Artemio', 'Florencio Randazzo', 'Grete Faremo',
     'Andrés Allamand', 'Ignatius Chombo', 'Nicolás Maduro', 'Cyrus Jirongo', 'Keriako Tobiko', 'Marta Suplicy',
     'Sithembiso Nyoni', 'Johannes Tomana', 'Henri Djombo', 'Carlos Zannini', 'Patricia Bullrich', 'Vitalie Marinuța',
     'Julius Malema', 'Utoni Nujoma', 'Abdo Hussameddin', 'Viviane Reding', 'Raymond Benjamin', 'Bujar Nishani',
     'Denis Napthine', 'Toke Talagi', 'Aaron Motsoaledi', 'Ante Gotovina', 'Ivo Opstelten', 'Anton Siluanov',
     'Jacques Delors', 'Yossi Beilin', 'Felipe Calderón', 'Brigi Rafini', 'Amadou Sanogo', 'Cecilia Muñoz-Palma',
     'Francis Pangilinan', 'Cheikh Tidiane Gadio', 'Peter Esele', 'Peter Murcott Bunting', 'Ram Vilas Paswan',
     'Dmitry Rogozin', 'Valérie Pécresse', 'Emomali Rahmon', 'Christine Boutin', 'Irene Muloni', 'Boris Johnson',
     'Kayode Fayemi', 'Nicolas Schmit', 'Peter Gibson', 'Chris Bowen', 'Grigory Karasin', 'Philip Hammond',
     'Jean-Louis Tauran', 'Comrade José']

))

motif_ReAct_example_prompt_cn100_cn40 = """
You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity]. It requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 40 entities are: <most>[]</most> and Terminate[answer]. It returns the answer and finishes the task. It can only occur once!
Here are two examples.
Compare the background information of entities carefully to see if they are similar. 
------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Give me 40 most similar entities in list format and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly, the format is: The most similar 40 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Ne Win'

The Candidate entities list is: 
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia', 'India', 'Namibia', 'China', 'Jordan', 'Tony Tan', 'Iran', 'Fatah', 'Norway', 'Japan', 'Kenya', 'Khin Yi', 'Sweden', 'Madrid', 'Germany', 'Syria', 'Mexico', 'Brazil', 'Lebanon', 'Peter Hain', 'Peru', 'Qin Gang', 'Sukarno', 'Teng Biao', 'Tuva', 'Laos', 'Mike DeWine', 'Shas', 'UNITA', 'Diena', 'Togo', 'Umar', 'Pape Diop', 'Komeito', 'Yukos', 'Pete Wilson', 'Naruhito', 'Ānanda', 'Joe Walsh', 'ANTEL', 'Raúl', 'Ron Kirk', 'Penny Wong', 'Giza', 'Mike Rann', 'Ramdev', 'Wu Aiying', 'Boediono', 'MPLA', 'Bob Rae', 'Guinea']

NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select 40 most similar answer and 1 most similar entity from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: The most similar 40 entities are: <most>['Ne Win', 'Than Shwe', 'Maung Aye', 'Myanmar', 'Tin Oo', 'Aung San', 'Thein Sein', 'Shwe Mann', 'Myint Swe', 'Htin Kyaw', 'Aung Gyi', 'Sao Shwe Thaik', 'Kyaw Zaw', 'Maung Maung', 'Kyaw Htin', 'Hla Myint', 'Ba Hein', 'Sao Kya Seng', 'Aung Kyi', 'Htin Kyaw', 'Aung Hla Tun', 'Saw Maung', 'Thura Shwe Mann', 'Kyi Maung', 'Thein Sein', 'San Yu', 'Tin Aung Myint Oo', 'Tatmadaw', 'Zaw Win', 'Aung Zaw', 'Thein Sein', 'Win Myint', 'Myint Swe', 'Htin Kyaw', 'Khin Nyunt', 'Tin Oo', 'Kyi Maung', 'San Yu', 'Than Shwe']</most> and Terminate['Ne Win'].

------------------------------ Example End ------------------------------ 

------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Give me 40 most not 100 similar entities in list format and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The format is The most similar 40 entities are: <most>[]</most> and Terminate[answer]. You have at most 4 turns to finish the task. The target entity is:
'Salauddin'

The Candidate entities list is: 
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Sukarno', 'Mao Zedong', 'Benin', 'Sam Sesay', 'Poland', 'Ron Wyden', 'Japan', 'Somalia', 'Suharto', 'Vanuatu', 'Panama', 'Ramdev', 'Hamas', 'Lara Giddings', 'Cambodia', 'Sweden', 'Kalyan Singh', 'Aung Min', 'Su Chi', 'Sylvia Lim', 'Ānanda', 'Dan Burton', 'La Nación', 'Khakassia', 'Politiken', 'Kashmir', 'Kashmir', 'Slovenia', 'Samoa', 'Canada', 'Paula Cox', 'Wales', 'Barbados', 'Jay Nixon', 'Bermuda', 'Télam', 'Haaretz', 'Madeira', 'Navarre', 'Sirius XM', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Talal Arslan', 'Raúl', 'Shaul Mofaz', 'Isa Yuguda', 'Imran Khan', 'Yabloko', 'Sima Samar', 'Abdulla Kurd']

NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide the final answer. 
Thought 1: I can find a direct match.
Act 1: The most similar 40 entities are: <most>['Abdulla Kurd', 'Salou Djibo', 'Sukarno', 'Suharto', 'Imran Khan', 'Isa Yuguda', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Talal Arslan', 'Ron Wyden', 'Joe Biden', 'Dan Burton', 'Paul Martin', 'Jay Nixon', 'Hamid Mir', 'Aung Min', 'Su Chi', 'Naruhito', 'Naoto Kan', 'Ne Win', 'Shwe Mann', 'Malawi', 'Somalia', 'Maldives', 'Malaysia', 'Mali', 'Malta', 'Paula Cox', 'Madeira', 'Madrid', 'Sam Nujoma', 'Alexandria', 'Carl Levin', 'Susan Rice', 'Raila Odinga', 'Ramdev', 'Kadima', 'Sinn Féin']</most> and Terminate['Abdulla Kurd'].

------------------------------ Example End ------------------------------ 

[USER (Boss)]: Give me 40 most similar entities and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The format is The most similar 40 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
Swaziland Youth Congress

The Candidate entities list is: 
['World Jewish Congress', 'Iraqi National Congress', 'Trades Union Congress', 'World Uyghur Congress', "Uganda People's Congress", 'Armenian National Congress', "National People's Congress", 'Hassan Younes', 'Jharkhand Mukti Morcha', 'SWAPO Party Youth League', 'Sarath Fonseka', 'Suez Canal Authority', 'Sandra Torres', 'Hassan Rouhani', 'Latvian Naval Forces', 'Zuzana Roithová', 'Dan Lungren', 'Santiago Creel', 'Denzil Douglas', 'Suleiman Frangieh', 'South Korea', 'Bernard Kouchner', 'Standard Chartered', 'Hamadoun Touré', 'Fesshaye Yohannes', 'Carolyn Rodrigues', 'Fernando Flores', 'Silvan Shalom', 'Sinaloa Cartel', 'Kwabena Duffuor', 'South America', 'Raila Odinga', 'Sirindhorn', 'Aaron Motsoaledi', 'Pravind Jugnauth', 'Kgalema Motlanthe', 'Ferdinand Marcos', 'Sylvain Ndoutingai', 'Simon Coveney', 'Shah Mahmood Qureshi', 'League of Women Voters', 'Sondhi Limthongkul', 'Sally Kosgei', 'Pravin Gordhan', 'Jaswant Singh', 'Maxine Waters', 'Sajjan Kumar', 'Shimon Peres', 'Salvador Namburete', 'Kahinda Otafiire', 'Russian Air Force', 'Julian Assange', 'Martin McGuinness', 'Sten Tolgfors', 'Danilo Astori', 'Ramin Mehmanparast', 'Iranian Space Agency', 'Klaus Wowereit', 'Paulo Portas', 'Harald V of Norway', 'Haqqani network', 'Dragan Šutanovac', 'Davinder Singh', 'Rajnath Singh', 'Panitan Wattanayagorn', 'Denis Sassou Nguesso', 'Vladimiro Montesinos', 'Garibaldi Alves', 'Jean-Louis Borloo', 'Mamadou Tandja', 'Richard Bruton', 'Ricardo Lagos', 'Jiang Tianyong', 'Bala Mohammed', 'William Joseph Burns', 'Sarabjit Singh', 'Sarabjit Singh', 'Shahin Mustafayev', 'Anote Tong', 'Dési Bouterse', 'Daily Nation', 'Daily Nation', 'Maghreb Arabe Press', 'Roland Dumas', 'Yasin Abu Bakr', 'Royal Bank of Canada', 'Crin Antonescu', 'Javier Diez Canseco', 'Milan Kučan', 'Chiang Ching-kuo', 'Alexandr Vondra', 'Harmony Centre', 'Susana Martinez', 'Manuel Chaves', 'Claudio Bonadio', 'Pablo Longueira', 'Johnny Araya Monge', 'Julio Borges', 'Camillo Gonsalves', 'David Johnston', "People's United Democratic Movement"]

  
NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! Otherwise, you will be punished.
Thought 1:

"""

motif_ReAct_example_prompt_cn100_cn30 = """
You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity]. It requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 30 entities are: <most>[]</most> and Terminate[answer]. It returns the answer and finishes the task. It can only occur once!
Here are two examples.
Compare the background information of entities carefully to see if they are similar. 
------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Give me 30 most similar entities in list format and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly, the format is: The most similar 30 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Ne Win'

The Candidate entities list is: 
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia', 'India', 'Namibia', 'China', 'Jordan', 'Tony Tan', 'Iran', 'Fatah', 'Norway', 'Japan', 'Kenya', 'Khin Yi', 'Sweden', 'Madrid', 'Germany', 'Syria', 'Mexico', 'Brazil', 'Lebanon', 'Peter Hain', 'Peru', 'Qin Gang', 'Sukarno', 'Teng Biao', 'Tuva', 'Laos', 'Mike DeWine', 'Shas', 'UNITA', 'Diena', 'Togo', 'Umar', 'Pape Diop', 'Komeito', 'Yukos', 'Pete Wilson', 'Naruhito', 'Ānanda', 'Joe Walsh', 'ANTEL', 'Raúl', 'Ron Kirk', 'Penny Wong', 'Giza', 'Mike Rann', 'Ramdev', 'Wu Aiying', 'Boediono', 'MPLA', 'Bob Rae', 'Guinea']

NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select 30 most similar answer and 1 most similar entity from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: The most similar 30 entities are: <most> ['Ne Win', 'Aung San', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Hla Min', 'Soe Thein', 'Hla Tun', 'Su Chi', 'Khin Yi', 'Aung Min', 'Chea Sim', 'Jean Ping', 'Sung Kim', 'Joe Biden', 'Tony Tan', 'Penny Wong', 'Raúl', 'Fatah', 'UNITA', 'MPLA', 'Serbia', 'Latvia', 'Madrid', 'Germany', 'Syria', 'Brazil', 'Lebanon', 'Iran', 'China']</most> and Terminate['Ne Win'].

------------------------------ Example End ------------------------------ 

------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Give me 30 most not 100 similar entities in list format and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The format is The most similar 30 entities are: <most>[]</most> and Terminate[answer]. You have at most 4 turns to finish the task. The target entity is:
'Salauddin'

The Candidate entities list is: 
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Sukarno', 'Mao Zedong', 'Benin', 'Sam Sesay', 'Poland', 'Ron Wyden', 'Japan', 'Somalia', 'Suharto', 'Vanuatu', 'Panama', 'Ramdev', 'Hamas', 'Lara Giddings', 'Cambodia', 'Sweden', 'Kalyan Singh', 'Aung Min', 'Su Chi', 'Sylvia Lim', 'Ānanda', 'Dan Burton', 'La Nación', 'Khakassia', 'Politiken', 'Kashmir', 'Kashmir', 'Slovenia', 'Samoa', 'Canada', 'Paula Cox', 'Wales', 'Barbados', 'Jay Nixon', 'Bermuda', 'Télam', 'Haaretz', 'Madeira', 'Navarre', 'Sirius XM', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Talal Arslan', 'Raúl', 'Shaul Mofaz', 'Isa Yuguda', 'Imran Khan', 'Yabloko', 'Sima Samar', 'Abdulla Kurd']

NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide the final answer. 
Thought 1: I can find a direct match.
Act 1: The most similar 30 entities are: <most>[Abdulla Kurd, Salou Djibo, Sam Nujoma, Salim Ahmed, Syed Salahuddin, Ahmadinejad, Aung Min, Shwe Mann, Sam Sesay, Babar Awan, Muhammad Yunus, Salam Fayyad, Chea Sim, Khakassia, Sule Lamido, Su Chi, Kalyan Singh, Ramdev, Imran Khan, Jawed Ludin, Ma Kai, Naoto Kan, Dan Burton, Talal Arslan, Jafar Panahi, Larissa Reis, Saad Hariri, Shaul Mofaz, Hasan Rouhani, Jean Ping]</most> and Terminate['Abdulla Kurd'].

------------------------------ Example End ------------------------------ 

[USER (Boss)]: Give me 30 not 100 most similar entities and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The format is The most similar 30 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
{}

The Candidate entities list is: 
{}
  
NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! Otherwise, you will be punished.
Thought 1:
"""

motif_ReAct_example_prompt_cn100_cn20 = """
You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity]. It requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 20 entities are: <most>[]</most> and Terminate[answer]. It returns the answer and finishes the task. It can only occur once!
Here are two examples.
Compare the background information of entities carefully to see if they are similar. 
------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Give me 20 most similar entities in list format and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly, the format is: The most similar 20 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Ne Win'

The Candidate entities list is: 
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia', 'India', 'Namibia', 'China', 'Jordan', 'Tony Tan', 'Iran', 'Fatah', 'Norway', 'Japan', 'Kenya', 'Khin Yi', 'Sweden', 'Madrid', 'Germany', 'Syria', 'Mexico', 'Brazil', 'Lebanon', 'Peter Hain', 'Peru', 'Qin Gang', 'Sukarno', 'Teng Biao', 'Tuva', 'Laos', 'Mike DeWine', 'Shas', 'UNITA', 'Diena', 'Togo', 'Umar', 'Pape Diop', 'Komeito', 'Yukos', 'Pete Wilson', 'Naruhito', 'Ānanda', 'Joe Walsh', 'ANTEL', 'Raúl', 'Ron Kirk', 'Penny Wong', 'Giza', 'Mike Rann', 'Ramdev', 'Wu Aiying', 'Boediono', 'MPLA', 'Bob Rae', 'Guinea']

NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select 20 most similar answer and 1 most similar entity from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: The most similar 20 entities are: <most>[Ne Win, Chea Sim, Soe Thein, Aung Min, Hla Tun, Shwe Mann, Tin Oo, Aye Maung, Khin Yi, Shas, Sukarno, Iran, Fatah, Jean Ping, Ma Kai, Su Chi, Joe Biden, Naoto Kan, Hun Sen, Aung San]</most> and Terminate['Ne Win'].

------------------------------ Example End ------------------------------ 

------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Give me 20 most not 100 similar entities in list format and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The format is The most similar 20 entities are: <most>[]</most> and Terminate[answer]. You have at most 4 turns to finish the task. The target entity is:
'Salauddin'

The Candidate entities list is: 
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Sukarno', 'Mao Zedong', 'Benin', 'Sam Sesay', 'Poland', 'Ron Wyden', 'Japan', 'Somalia', 'Suharto', 'Vanuatu', 'Panama', 'Ramdev', 'Hamas', 'Lara Giddings', 'Cambodia', 'Sweden', 'Kalyan Singh', 'Aung Min', 'Su Chi', 'Sylvia Lim', 'Ānanda', 'Dan Burton', 'La Nación', 'Khakassia', 'Politiken', 'Kashmir', 'Kashmir', 'Slovenia', 'Samoa', 'Canada', 'Paula Cox', 'Wales', 'Barbados', 'Jay Nixon', 'Bermuda', 'Télam', 'Haaretz', 'Madeira', 'Navarre', 'Sirius XM', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Talal Arslan', 'Raúl', 'Shaul Mofaz', 'Isa Yuguda', 'Imran Khan', 'Yabloko', 'Sima Samar', 'Abdulla Kurd']

NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide the final answer. 
Thought 1: I can find a direct match.
Act 1: The most similar 20 entities are: <most>[Abdulla Kurd, Salou Djibo, Bahrain, Malaysia, Raila Odinga, Valdivia, San Marino, Hla Tun, Carl Levin, Tatarstan, Salzburg, Sinn Féin, Macau, Sirindhorn, Jawed Ludin, Fatah, Kadima, Babar Awan, Hamid Mir, Gilad Erdan]</most> and Terminate['Abdulla Kurd'].

------------------------------ Example End ------------------------------ 

[USER (Boss)]: Give me 20 not 100 most similar entities and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The format is The most similar 20 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
{}

The Candidate entities list is: 
{}
  
NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! Otherwise, you will be punished.
Thought 1:
"""

motif_ReAct_example_prompt_cn100_cn10 = """
You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity]. It requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 10 entities are: <most>[]</most> and Terminate[answer]. It returns the answer and finishes the task. It can only occur once!
Here are two examples.
Compare the background information of entities carefully to see if they are similar. 
------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Give me 10 most similar entities in list format and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly, the format is: The most similar 10 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Ne Win'

The Candidate entities list is: 
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia', 'India', 'Namibia', 'China', 'Jordan', 'Tony Tan', 'Iran', 'Fatah', 'Norway', 'Japan', 'Kenya', 'Khin Yi', 'Sweden', 'Madrid', 'Germany', 'Syria', 'Mexico', 'Brazil', 'Lebanon', 'Peter Hain', 'Peru', 'Qin Gang', 'Sukarno', 'Teng Biao', 'Tuva', 'Laos', 'Mike DeWine', 'Shas', 'UNITA', 'Diena', 'Togo', 'Umar', 'Pape Diop', 'Komeito', 'Yukos', 'Pete Wilson', 'Naruhito', 'Ānanda', 'Joe Walsh', 'ANTEL', 'Raúl', 'Ron Kirk', 'Penny Wong', 'Giza', 'Mike Rann', 'Ramdev', 'Wu Aiying', 'Boediono', 'MPLA', 'Bob Rae', 'Guinea']

NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select 10 most similar answer and 1 most similar entity from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: The most similar 10 entities are: <most>['Ne Win', 'Shwe Mann', 'Aye Maung', 'Tin Oo', 'Su Chi', 'Hla Min', 'Hla Tun', 'Khin Yi', 'Aung San', 'Soe Thein']</most> and Terminate['Ne Win'].

------------------------------ Example End ------------------------------ 

------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Give me 10 most not 100 similar entities in list format and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The format is The most similar 10 entities are: <most>[]</most> and Terminate[answer]. You have at most 4 turns to finish the task. The target entity is:
'Salauddin'

The Candidate entities list is: 
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Sukarno', 'Mao Zedong', 'Benin', 'Sam Sesay', 'Poland', 'Ron Wyden', 'Japan', 'Somalia', 'Suharto', 'Vanuatu', 'Panama', 'Ramdev', 'Hamas', 'Lara Giddings', 'Cambodia', 'Sweden', 'Kalyan Singh', 'Aung Min', 'Su Chi', 'Sylvia Lim', 'Ānanda', 'Dan Burton', 'La Nación', 'Khakassia', 'Politiken', 'Kashmir', 'Kashmir', 'Slovenia', 'Samoa', 'Canada', 'Paula Cox', 'Wales', 'Barbados', 'Jay Nixon', 'Bermuda', 'Télam', 'Haaretz', 'Madeira', 'Navarre', 'Sirius XM', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Talal Arslan', 'Raúl', 'Shaul Mofaz', 'Isa Yuguda', 'Imran Khan', 'Yabloko', 'Sima Samar', 'Abdulla Kurd']

NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide the final answer. 
Thought 1: I can find a direct match.
Act 1: The most similar 10 entities are: <most>['Abdulla Kurd', 'Salou Djibo', 'Hla Tun', 'Soe Thein', 'Jean Ping', 'Naoto Kan', 'Ma Kai', 'Ne Win', 'Chea Sim', 'Shwe Mann']</most> and Terminate['Abdulla Kurd'].

------------------------------ Example End ------------------------------ 

[USER (Boss)]: Give me 10 not 100 most similar entities and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The format is The most similar 10 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
{}

The Candidate entities list is: 
{}
  
NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! Otherwise, you will be punished.
Thought 1:
"""