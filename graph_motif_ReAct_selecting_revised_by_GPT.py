motif_ReAct_example_prompt_cn100_cn50 = """
You are a programmer tasked with solving a question-answering problem involving entity alignment. You are allowed to request context information for entities from a candidate list but cannot request irrelevant entities. If you do, you will be fired.

Your approach should involve interleaving Thought, Action, and Observation steps:

Thought: Reason about the current situation and determine the next step.
Action: You can only perform one of the following actions:
Request[entity]: Request the entity’s context information from the Knowledge Graphs. You can request only once per turn, and each request must be for an entity from the candidate list.
Terminate[answer]: Return the answer and finish the task. This can only occur once.
Examples:

Example 1:

[USER (Boss)]: "Give me 50 most similar entities in list format and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is a direct match with the target entity in the candidate list, please select it directly. The format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer]. The target entity is: 'Ne Win'."

The Candidate Entities List: ['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia', 'India', 'Namibia', 'China', 'Jordan', 'Tony Tan', 'Iran', 'Fatah', 'Norway', 'Japan', 'Kenya', 'Khin Yi', 'Sweden', 'Madrid', 'Germany', 'Syria', 'Mexico', 'Brazil', 'Lebanon', 'Peter Hain', 'Peru', 'Qin Gang', 'Sukarno', 'Teng Biao', 'Tuva', 'Laos', 'Mike DeWine', 'Shas', 'UNITA', 'Diena', 'Togo', 'Umar', 'Pape Diop', 'Komeito', 'Yukos', 'Pete Wilson', 'Naruhito', 'Ānanda', 'Joe Walsh', 'ANTEL', 'Raúl', 'Ron Kirk', 'Penny Wong', 'Giza', 'Mike Rann', 'Ramdev', 'Wu Aiying', 'Boediono', 'MPLA', 'Bob Rae', 'Guinea']

[YOU (Programmer)]:

Turn 1:
Thought 1: I notice that 'Ne Win' is present in the candidate list, which is a direct match.
Act 1: The most similar 50 entities are: <most>['Ne Win', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia']</most> and Terminate['Ne Win'].

Example 2:

[USER (Boss)]: "Give me 50 most similar entities in list format and select 1 most similar entity from it to terminate. If there is a direct match, please select it directly. The format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer]. You have at most 4 turns to finish the task. The target entity is: 'Salauddin'."

The Candidate Entities List: ['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Sukarno', 'Mao Zedong', 'Benin', 'Sam Sesay', 'Poland', 'Ron Wyden', 'Japan', 'Somalia', 'Suharto', 'Vanuatu', 'Panama', 'Ramdev', 'Hamas', 'Lara Giddings', 'Cambodia', 'Sweden', 'Kalyan Singh', 'Aung Min', 'Su Chi', 'Sylvia Lim', 'Ānanda', 'Dan Burton', 'La Nación', 'Khakassia', 'Politiken', 'Kashmir', 'Kashmir', 'Slovenia', 'Samoa', 'Canada', 'Paula Cox', 'Wales', 'Barbados', 'Jay Nixon', 'Bermuda', 'Télam', 'Haaretz', 'Madeira', 'Navarre', 'Sirius XM', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Talal Arslan', 'Raúl', 'Shaul Mofaz', 'Isa Yuguda', 'Imran Khan', 'Yabloko', 'Sima Samar', 'Abdulla Kurd']

[YOU (Programmer)]:

Turn 1:
Thought 1: I see that 'Salauddin' matches directly with 'Abdulla Kurd' in the candidate list.
Act 1: The most similar 50 entities are: <most>['Abdulla Kurd', 'Salam Fayyad', 'Hamid Mir', 'Salou Djibo', 'Soe Thein', 'Sukarno', 'Jean Ping', 'Chea Sim', 'Shwe Mann', 'Aung Min', 'Ne Win', 'Gilad Erdan', 'Ramdev', 'Paul Martin', 'Sam Sesay', 'Ma Kai', 'Fatah', 'Sinn Féin', 'Somalia', 'Mao Zedong', 'Hla Min', 'Hla Tun', 'Panama', 'Hamas', 'Suharto', 'Attajdid', 'Talal Arslan', 'Isa Yuguda', 'Saad Hariri', 'Shaul Mofaz', 'Alexandria', 'Carl Levin', 'Sam Nujoma', 'Dan Burton', 'Ron Wyden', 'Kadima', 'Raila Odinga', 'Sylvia Lim', 'Susan Rice', 'Babar Awan', 'Sima Samar', 'Aung San', 'Jawed Ludin', 'Imran Khan', 'Navarre', 'Poland', 'Wales', 'Soe Aung', 'Malawi', 'Benin', 'Tatarstan']</most> and Terminate['Abdulla Kurd'].

Instructions:
You have at most 4 turns to generate the final results, meaning you must provide the answer by Thought 4 or earlier.
If you are very sure about the answer, you may provide it directly. Otherwise, use the allowed actions to gather more information before finalizing the answer.
The entity in the Terminate action must be the first entity in the list returned in the Action step.

[YOU (Programmer)]:
Turn 1:
Thought 1:

"""
# .format(
#     'Jomo Gbomo',
#     ['John Nkomo', 'Comoros', 'Fred Gumo', 'Tony Momoh', 'José Bové', 'Jaime Trobo', 'John Hogg', 'Colombia', 'Morocco',
#      'Bode George', 'Tonio Borg', 'Gideon Gono', 'Seiso Moyo', 'John Dalli', 'Joker Arroyo', 'Rosatom', 'Komeito',
#      'Tom Ridge', 'Alan Gross', 'John Mahama', 'Boediono', 'Sam Nujoma', 'José Anaya', 'José Serra', 'John Garang',
#      'John Key', 'Jim Cooper', 'Phil Goff', 'Roilo Golez', 'Joe Walsh', 'Julio Cobos', 'Tomaz Salomão', 'Jim Molan',
#      'Boko Haram', 'Jacob Zuma', 'James Soong', 'Kosovo', 'Joe Biden', 'John Bercow', 'John Tsang', 'Hong Kong',
#      'John Kerry', 'John Bruton', 'Jim Inhofe', 'Jordan', 'Gabon', 'Zimbabwe', 'Zambia', 'Cameroon', 'Namibia',
#      'Somalia', 'Moldova', 'Romania', 'Cambodia', 'Jerry Gana', 'Eskom', 'Lovemore Moyo', 'Issa Aremu', 'Jean Ping',
#      'Codelco', 'Don Polye', 'Anote Tong', 'J. S. Verma', 'Banobras', 'Tom Thabane', 'Adamu Bello', 'Jason Yuan',
#      'Abdou Labo', 'Edi Rama', 'Koffi Sama', 'Toyota', 'Jason Hu', 'John Mutorwa', 'Hugo Yasky', 'Dave Camp',
#      'Karl Hood', 'Monsanto', 'Jubo League', 'Aliyu Doma', 'James Orengo', 'Guy Scott', 'Qin Gang', 'Tião Viana',
#      'Aldo Bumçi', 'John Luk Jok', 'Naoki Inose', 'Guam', 'Kommersant', 'Pape Diop', 'Tony Tan', 'Tommy Thompson',
#      'Joe Hockey', 'Google', 'Gordon Brown', 'Jay Nixon', 'Omar Bongo', 'Naoto Kan', 'Chea Sim', 'Kyodo News',
#      'Sung Kim', 'Henry Okah']
# )

motif_ReAct_example_prompt_cn100_cn40 = """
You are a programmer. You can request useful entities from a candidate list, but you cannot request irrelevant entities. Otherwise, you will be fired. Solve a question-answering task with interleaving Thought, Action, and Observation steps. Thought can reason about the current situation, and Action can only be of two types:

Request[entity]: This requests the entity's context information from Knowledge Graphs. The context information may be given in code description. You can only request one entity at a time and only entities from the candidate list.
The most similar 40 entities are: <most>[]</most> and Terminate[answer]: This returns the answer and finishes the task. It can only occur once!
Here are two examples. Compare the background information of entities carefully to see if they are similar.

Example 1
[USER (Boss)]: Give me 40 most similar entities in list format and select 1 most similar entity from it to terminate. You have at most 4 turns to finish the task. If there is the same entity in the candidate list for the target entity, please select it directly. The format is: The most similar 40 entities are: <most>[]</most> and Terminate[answer]. The target entity is: 'Ne Win'

Candidate entities list:
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia', 'India', 'Namibia', 'China', 'Jordan', 'Tony Tan', 'Iran', 'Fatah', 'Norway', 'Japan', 'Kenya', 'Khin Yi', 'Sweden', 'Madrid', 'Germany', 'Syria', 'Mexico', 'Brazil', 'Lebanon', 'Peter Hain', 'Peru', 'Qin Gang', 'Sukarno', 'Teng Biao', 'Tuva', 'Laos', 'Mike DeWine', 'Shas', 'UNITA', 'Diena', 'Togo', 'Umar', 'Pape Diop', 'Komeito', 'Yukos', 'Pete Wilson', 'Naruhito', 'Ānanda', 'Joe Walsh', 'ANTEL', 'Raúl', 'Ron Kirk', 'Penny Wong', 'Giza', 'Mike Rann', 'Ramdev', 'Wu Aiying', 'Boediono', 'MPLA', 'Bob Rae', 'Guinea']

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!

Turn 1:
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match.
Act 1: The most similar 40 entities are: <most>['Ne Win', 'Than Shwe', 'Maung Aye', 'Myanmar', 'Tin Oo', 'Aung San', 'Thein Sein', 'Shwe Mann', 'Myint Swe', 'Htin Kyaw', 'Aung Gyi', 'Sao Shwe Thaik', 'Kyaw Zaw', 'Maung Maung', 'Kyaw Htin', 'Hla Myint', 'Ba Hein', 'Sao Kya Seng', 'Aung Kyi', 'Htin Kyaw', 'Aung Hla Tun', 'Saw Maung', 'Thura Shwe Mann', 'Kyi Maung', 'Thein Sein', 'San Yu', 'Tin Aung Myint Oo', 'Tatmadaw', 'Zaw Win', 'Aung Zaw', 'Thein Sein', 'Win Myint', 'Myint Swe', 'Htin Kyaw', 'Khin Nyunt', 'Tin Oo', 'Kyi Maung', 'San Yu', 'Than Shwe']</most> and Terminate['Ne Win'].

Example 2
[USER (Boss)]: Give me 40 most similar entities in list format and select 1 most similar entity from it to terminate. If there is the same entity, please select it directly. The format is The most similar 40 entities are: <most>[]</most> and Terminate[answer]. The target entity is: 'Salauddin'

Candidate entities list:
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Sukarno', 'Mao Zedong', 'Benin', 'Sam Sesay', 'Poland', 'Ron Wyden', 'Japan', 'Somalia', 'Suharto', 'Vanuatu', 'Panama', 'Ramdev', 'Hamas', 'Lara Giddings', 'Cambodia', 'Sweden', 'Kalyan Singh', 'Aung Min', 'Su Chi', 'Sylvia Lim', 'Ānanda', 'Dan Burton', 'La Nación', 'Khakassia', 'Politiken', 'Kashmir', 'Kashmir', 'Slovenia', 'Samoa', 'Canada', 'Paula Cox', 'Wales', 'Barbados', 'Jay Nixon', 'Bermuda', 'Télam', 'Haaretz', 'Madeira', 'Navarre', 'Sirius XM', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Talal Arslan', 'Raúl', 'Shaul Mofaz', 'Isa Yuguda', 'Imran Khan', 'Yabloko', 'Sima Samar', 'Abdulla Kurd']

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!

Turn 1:
Thought 1: I can find a direct match.
Act 1: The most similar 40 entities are: <most>['Abdulla Kurd', 'Salou Djibo', 'Sukarno', 'Suharto', 'Imran Khan', 'Isa Yuguda', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Talal Arslan', 'Ron Wyden', 'Joe Biden', 'Dan Burton', 'Paul Martin', 'Jay Nixon', 'Hamid Mir', 'Aung Min', 'Su Chi', 'Naruhito', 'Naoto Kan', 'Ne Win', 'Shwe Mann', 'Malawi', 'Somalia', 'Maldives', 'Malaysia', 'Mali', 'Malta', 'Paula Cox', 'Madeira', 'Madrid', 'Sam Nujoma', 'Alexandria', 'Carl Levin', 'Susan Rice', 'Raila Odinga', 'Ramdev', 'Kadima', 'Sinn Féin']</most> and Terminate['Abdulla Kurd'].

Instructions:
1. You have at most 4 turns to generate the final results, meaning you must provide the answer by Thought 4 or earlier.
2. If you are very sure about the answer, you may provide it directly. Otherwise, use the allowed actions to gather more information before finalizing the answer.
3. The entity in the Terminate action must be the first entity in the list returned in the Action step.

New Task
[USER (Boss)]: Give me 40 most similar entities and select 1 most similar entity from it to terminate. If there is the same entity, please select it directly. The format is The most similar 40 entities are: <most>[]</most> and Terminate[answer]. The target entity is: {}

Candidate entities list:
{]

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!

Turn 1:
Thought 1:

"""

motif_ReAct_example_prompt_cn100_cn30 = """
You are a programmer tasked with identifying the most similar entity from a list of candidates. You must follow specific rules to avoid selecting irrelevant entities. Failure to adhere to these rules could result in termination.

Task Overview
Thought: Reason about the current situation and decide on the next step.
Action: You have two types of actions:
1. Request[entity]: Request context information for a specific entity from the Knowledge Graph. You can only request one entity per turn and only from the candidate list.
2. The most similar 30 entities are: <most>[]</most> and Terminate[answer]: Return a list of the 30 most similar entities and terminate the task with the selected answer. This action can only be performed once.

Example Scenarios
Example 1
[USER (Boss)]: Provide a list of the 30 most similar entities and select the most similar entity to terminate. You have at most 4 turns. If the target entity is present in the candidate list, select it directly.

Target Entity: 'Ne Win'

Candidate Entities List:
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia', 'India', 'Namibia', 'China', 'Jordan', 'Tony Tan', 'Iran', 'Fatah', 'Norway', 'Japan', 'Kenya', 'Khin Yi', 'Sweden', 'Madrid', 'Germany', 'Syria', 'Mexico', 'Brazil', 'Lebanon', 'Peter Hain', 'Peru', 'Qin Gang', 'Sukarno', 'Teng Biao', 'Tuva', 'Laos', 'Mike DeWine', 'Shas', 'UNITA', 'Diena', 'Togo', 'Umar', 'Pape Diop', 'Komeito', 'Yukos', 'Pete Wilson', 'Naruhito', 'Ānanda', 'Joe Walsh', 'ANTEL', 'Raúl', 'Ron Kirk', 'Penny Wong', 'Giza', 'Mike Rann', 'Ramdev', 'Wu Aiying', 'Boediono', 'MPLA', 'Bob Rae', 'Guinea']

[YOU (Programmer)]:
Turn 1:
You have 4 turns to provide the final answer. Select the 30 most similar entities from the list and choose one entity to terminate. If you are confident about the answer, provide it directly. Otherwise, request additional information to increase your confidence. Remember, you can only request one entity per turn and must avoid irrelevant entities.

Thought 1: There is a direct match for the target entity in the candidate list.
Act 1: The most similar 30 entities are: <most> ['Ne Win', 'Aung San', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Hla Min', 'Soe Thein', 'Hla Tun', 'Su Chi', 'Khin Yi', 'Aung Min', 'Chea Sim', 'Jean Ping', 'Sung Kim', 'Joe Biden', 'Tony Tan', 'Penny Wong', 'Raúl', 'Fatah', 'UNITA', 'MPLA', 'Serbia', 'Latvia', 'Madrid', 'Germany', 'Syria', 'Brazil', 'Lebanon', 'Iran', 'China']</most> and Terminate['Ne Win'].

Example 2
[USER (Boss)]: Provide a list of 30 entities that are not the 100 most similar and select 1 most similar entity to terminate. If the target entity is present in the list, select it directly.

Target Entity: 'Salauddin'

Candidate Entities List:
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Sukarno', 'Mao Zedong', 'Benin', 'Sam Sesay', 'Poland', 'Ron Wyden', 'Japan', 'Somalia', 'Suharto', 'Vanuatu', 'Panama', 'Ramdev', 'Hamas', 'Lara Giddings', 'Cambodia', 'Sweden', 'Kalyan Singh', 'Aung Min', 'Su Chi', 'Sylvia Lim', 'Ānanda', 'Dan Burton', 'La Nación', 'Khakassia', 'Politiken', 'Kashmir', 'Slovenia', 'Samoa', 'Canada', 'Paula Cox', 'Wales', 'Barbados', 'Jay Nixon', 'Bermuda', 'Télam', 'Haaretz', 'Madeira', 'Navarre', 'Sirius XM', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Talal Arslan', 'Raúl', 'Shaul Mofaz', 'Isa Yuguda', 'Imran Khan', 'Yabloko', 'Sima Samar', 'Abdulla Kurd']

[YOU (Programmer)]:
Turn 1:
You have 4 turns to provide the final answer. If confident, provide it directly. Otherwise, generate 'Thought' and 'Act' and wait for 'Observation' from the User.

Thought 1: I can find a direct match.
Act 1: The most similar 30 entities are: <most>[Abdulla Kurd, Salou Djibo, Sam Nujoma, Salim Ahmed, Syed Salahuddin, Ahmadinejad, Aung Min, Shwe Mann, Sam Sesay, Babar Awan, Muhammad Yunus, Salam Fayyad, Chea Sim, Khakassia, Sule Lamido, Su Chi, Kalyan Singh, Ramdev, Imran Khan, Jawed Ludin, Ma Kai, Naoto Kan, Dan Burton, Talal Arslan, Jafar Panahi, Larissa Reis, Saad Hariri, Shaul Mofaz, Hasan Rouhani, Jean Ping]</most> and Terminate['Abdulla Kurd'].

New Task
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
You are restricted to requesting information only from the candidate list and must not request irrelevant entities. Failure to adhere to these restrictions will result in termination.

Examples:

Example 1:
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

Example 2:

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

New Task
[USER (Boss)]: Give me 10 not 100 most similar entities and select 1 most similar entity from it to terminate. If there is same entity, please select directly. The format is The most similar 10 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
{}

The Candidate entities list is: 
{}
  
Notes:
1. You have at most 4 turns to provide the final answer. If you are confident about the answer, you may provide it earlier.
2. The entity in the termination step must be the first entity in the list of the 10 most similar entities returned.

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!! Otherwise, you will be punished.
Thought 1:
"""
