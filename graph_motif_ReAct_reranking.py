
motif_ReAct_example_prompt_cn200_cn200 = """
You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity]. It requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 200 entities are: <most>[]</most> and Terminate[answer]. It returns the answer and finishes the task. It can only occur once!
Here are two examples.
Compare the background information of entities carefully to see if they are similar. 
------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly. The answer format is: The most similar 200 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Ne Win'

The Candidate entities list is: 
['Ne Win', 'Wu Jin', 'Hla Min', 'Nani', 'Le Lynx', 'Dexia', 'Serbia', 'Chea Sim', 'Ben Bot', 'Nyan Tun', 'Jean Ping', 'Yemen', 'Aung Min', 'Ma Kai', 'Spain', 'Yang Bin', 'Saw Tun', 'Meretz', 'Niue', 'Luo Gan', 'Qena', 'Wan Li', 'Temelín', 'Tep Vong', 'Tea Banh', 'Basij', 'Ted Poe', 'Fatih', 'Oman', 'Seeka', 'Lukoil', 'Lenovo', 'Nelly Olin', 'NATO', 'Safran', 'Linz', 'Idi Amin', 'Holcim', 'Roshen', 'Bahrain', 'Telmex', 'Boeing', 'Verisign', 'Xerox', 'Niger', 'Sudan', 'Russia', 'Thein Tun', 'Shwe Mann', 'Namibia', 'RENAMO', 'Japan', 'Jordan', 'Aye Maung', 'Germany', 'Syria', 'Sirikit', 'Eswatini', 'Pat Cox', 'Sukarno', 'Kai Ko', 'Togo', 'Mike Eman', 'Đỗ Mười', 'Mike DeWine', 'Jon Kyl', 'Pap Saine', 'Joyce Quin', 'Yukos', 'Dulmatin', 'Komeito', 'Naruhito', 'Taliban', 'Palau', 'Brunei', 'Greg Hunt', 'Vũ Khoan', 'Ānanda', 'Bob Rae', 'Quryna', 'Giza', 'Yesh Atid', 'Lien Chan', 'PORA', 'Syriza', 'Sinn Féin', 'UNITA', 'Rusnano', 'Len Brown', 'Kosovo', 'La Nación', 'Qatar', 'Le Phare', 'Wales', 'UBS', 'El País', 'USKOK', 'Kashmir', 'Intel', 'La Región', 'Akihito', 'Foxconn', 'Télam', 'Eskom', 'Sacyr', 'Jamaica', 'PIMCO', 'CANTV', 'Fiji Sun', 'Petronas', 'Abrar', 'Tuvalu', 'Algeria', 'Zagazig', 'IBM', 'Hyatt', 'Toshiba', 'Guam', 'Subaru', 'Xiaomi', 'Reuters', 'CNN', 'VMware', 'Senegal', 'Turkey', 'Cameroon', 'Khun Sa', 'Estonia', 'Iceland', 'Poland', 'Belarus', 'Thein Swe', 'Wade Mark', 'Rose Akol', 'Liberia', 'Sam Abal', 'Anote Tong', 'Ieng Sary', 'Theo Waigel', 'Ung Huot', 'Jack Ma', 'Hun Manet', 'U Thaung', 'Denmark', 'Jean Obeid', 'Romania', 'Angus King', 'Libya', 'Stern Hu', 'Mike Sonko', 'Chile', 'France', 'Fred Gumo', 'Canada', 'Joseph Zen', 'Tião Viana', 'Des Browne', 'Wayne Swan', 'Suharto', 'Noel Davern', 'Mark Kirk', 'Bill Weld', 'Ali Roba', 'Terry Gou', 'Noemí Sanín', 'Mongolia', 'Lin Chuan', 'Ben Nelson', 'John Bani', 'Anne Holt', 'Sidik Mia', 'Jim Molan', 'Alex Otti', 'Lee Terry', 'Udi Adam', 'Joe Stork', 'Kim Wan-su', 'Jack Lew', 'Jaak Aab', 'Bob Dole', 'Peter Obi', 'Bob Carr', 'Jamie Dimon', 'Nika Melia', 'José Bono', 'Liam Fox', 'Bodoland', 'Maldives', 'Mus Sema', 'Hervé Morin', 'Joe Modise', 'Yane Yanev', 'Timo Soini', 'Mike Rama', 'Pete Geren', 'Than Nyun', 'Dave Camp', 'Monsanto', 'Ethiopia', 'Kyaw Myint']

NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select 200 most similar answer and 1 most similar entity from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: The most similar 200 entities are: <most>['Ne Win', 'Nyan Tun', 'Aung Min', 'Saw Tun', 'Shwe Mann', 'Hla Min', 'Thein Tun', 'Thein Swe', 'U Thaung', 'Than Nyun', 'Khun Sa', 'Chea Sim', 'Ieng Sary', 'Tep Vong', 'Ung Huot', 'Tea Banh', 'Suharto', 'Idi Amin', 'Ben Bot', 'Jean Ping', 'Pat Cox', 'Pap Saine', 'Greg Hunt', 'Dulmatin', 'Joe Stork', 'Sukarno', 'Fred Gumo', 'Rose Akol', 'Jean Obeid', 'Jack Ma', 'Mike Sonko', 'Yane Yanev', 'Mike DeWine', 'Jon Kyl', 'Bob Rae', 'Jaak Aab', 'Anote Tong', 'Stern Hu', 'Kai Ko', 'Mike Eman', 'Ted Poe', 'Fatih', 'Vũ Khoan', 'Sam Abal', 'Lin Chuan', 'Ma Kai', 'Yang Bin', 'Luo Gan', 'Wan Li', 'Sinn Féin', 'Temelín', 'Nani', 'Ted Poe', 'Timo Soini', 'Nelly Olin', 'Noel Davern', 'Alex Otti', 'Bill Weld', 'Pete Geren', 'Wayne Swan', 'Des Browne', 'Jim Molan', 'Noemí Sanín', 'Ben Nelson', 'Peter Obi', 'Bob Carr', 'José Bono', 'Liam Fox', 'Joe Stork', 'Ali Roba', 'Hervé Morin', 'Jack Lew', 'Yemen', 'Jordan', 'Namibia', 'Niger', 'Guam', 'Jamaica', 'Liberia', 'Libya', 'Lesotho', 'Iceland', 'Estonia', 'Belarus', 'Turkey', 'Syria', 'Japan', 'Germany', 'France', 'Chile', 'Canada', 'Senegal', 'Qatar', 'Spain', 'Sudan', 'Russia', 'Serbia', 'Togo', 'Poland', 'Palau', 'Oman', 'Nauru', 'Mongolia', 'Monaco', 'Malta', 'Maldives', 'Lesotho', 'Liberia', 'Libya', 'Lesotho', 'Kyrgyzstan', 'Kosovo', 'Kuwait', 'Kiribati', 'Kenya', 'Kazakhstan', 'Jordan', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Honduras', 'Haiti', 'Greece', 'Ghana', 'Georgia', 'Gabon', 'Finland', 'Fiji', 'El Salvador', 'Dominica', 'Djibouti', 'Denmark', 'Cyprus', 'Cuba', 'Croatia', 'Costa Rica', 'Congo', 'Colombia', 'China', 'Chad', 'Central African Republic', 'Cape Verde', 'Cameroon', 'Burundi', 'Burkina Faso', 'Bulgaria', 'Brunei', 'Brazil', 'Botswana', 'Bosnia and Herzegovina', 'Bhutan', 'Benin', 'Belgium', 'Belize', 'Belarus', 'Barbados', 'Bangladesh', 'Bahrain', 'Bahamas', 'Azerbaijan', 'Austria', 'Australia', 'Armenia', 'Argentina', 'Angola', 'Andorra', 'Algeria', 'Albania', 'Afghanistan']</most> ans Terminate['Ne Win'].
------------------------------ Example End ------------------------------ 

------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly. The answer format is: The most similar 200 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Salauddin'

The Candidate entities list is: 
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Alexandria', 'Kuwait', 'Basij', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Burundi', 'Ma Kai', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Chea Sim', 'Maldives', 'Shwe Mann', 'Sung Kim', 'Hau Lungpin', 'Sukarno', 'Benin', 'Sam Sesay', 'Mao Zedong', 'Poland', 'Ron Wyden', 'Japan', 'Somalia', 'Suharto', 'Vanuatu', 'Panama', 'Hamas', 'Lara Giddings', 'Ramdev', 'Cambodia', 'Sweden', 'Aung Min', 'Kalyan Singh', 'Sylvia Lim', 'Ānanda', 'Dan Burton', 'Su Chi', 'La Nación', 'Khakassia', 'Politiken', 'Kashmir', 'Kashmir', 'Slovenia', 'Canada', 'Samoa', 'Paula Cox', 'Wales', 'Barbados', 'Jay Nixon', 'Bermuda', 'Télam', 'Haaretz', 'Madeira', 'Navarre', 'Sirius XM', 'Salam Fayyad', 'Saad Hariri', 'J B Dauda', 'Sule Lamido', 'Ban Kimoon', 'Talal Arslan', 'Raúl', 'Shaul Mofaz', 'Isa Yuguda', 'Imran Khan', 'Yabloko', 'L K Advani', 'L K Advani', 'Sima Samar', 'Sadullah Ergin', 'Safar Abiyev', 'Sri Mulyani', 'Yair Lapid', 'Likud', 'AlAlam', 'Talla Sylla', 'Taleb Rifai', 'Satsuki Eda', 'Masood Khan', 'Syriza', 'Selim Hoss', 'Mart Laar', 'Paul Biya', 'Mallikarjun', 'Paskal Milo', 'Milan Panić', 'AlAhram', 'Umar', 'ArNamys', 'Vlad Filat', 'Saddam Hussein', 'Al Wefaq', 'Jim Molan', 'Sharad Yadav', 'Bev Oda', 'Salim Saleh', 'Kamal Nath', 'Peter Hain', 'Khalid Ali', 'Ro Tuchol', 'Max Baucus', 'Gabon', 'Sidwaya', 'Sali Berisha', 'Radek John', 'Dharam Singh', 'Matt Mead', 'Danilo Medina', 'Giza', 'César Ham', 'Khun Sa', 'Wu Denyih', 'South Sudan', 'Harry Reid', 'Bangladesh', 'Pagan Amum', 'Hun Sen', 'Baldev Singh', 'Iran', 'Sukh Ram', 'Temelín', 'Ioan Rus', 'Mar Roxas', 'Ivica Kirin', 'Malik Agar', 'Angus King', 'Aung San', 'Jordan', 'Vilma Espín', 'Saint Lucia', 'Khin Yi', 'Mongolia', 'Finland', 'India', 'Kazakhstan', 'Marat Tazhin', 'Cameroon', 'Lamar Smith', 'Pakistan', 'Laos', 'Boediono', 'Milan Kučan', 'Neal S Wolin', 'Honduras', 'Latvia', 'Curaçao', 'Milan Roćen', 'Hilary Onek', 'Sam Ongeri', 'Uganda', 'Bola Tinubu', 'Mark Kirk', 'Moldova', 'Iceland', 'Ukraine', 'Maung Oo', 'Haiti', 'Tony Tan', 'Jason Hu', 'Mauritius', 'Belize', 'Fiji', 'Paraguay', 'South Asia', 'Abdulla Kurd']

NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide the final answer. 
Thought 1: I can find a direct match.
Act 1: The most similar 200 entities are: <most>['Abdulla Kurd', 'Salou Djibo', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Sadullah Ergin', 'Safar Abiyev', 'Sali Berisha', 'Sam Ongeri', 'Salim Saleh', 'Shaul Mofaz', 'Sima Samar', 'Satsuki Eda', 'Sukh Ram', 'Shwe Mann', 'Susan Rice', 'Sylvia Lim', 'Sinn Féin', 'Sukarno', 'Somalia', 'Soe Thein', 'Sung Kim', 'Suharto', 'San Marino', 'Hla Min', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Salzburg', 'Macau', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Alexandria', 'Kuwait', 'Basij', 'Naruhito', 'Jean Ping', 'Oman', 'Naoto Kan', 'Sam Nujoma', 'Joe Biden', 'Burundi', 'Ma Kai', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Chea Sim', 'Maldives', 'Hau Lungpin', 'Benin', 'Sam Sesay', 'Mao Zedong', 'Poland', 'Ron Wyden', 'Japan', 'Vanuatu', 'Panama', 'Hamas', 'Lara Giddings', 'Ramdev', 'Cambodia', 'Sweden', 'Aung Min', 'Kalyan Singh', 'Ānanda', 'Dan Burton', 'Su Chi', 'La Nación', 'Khakassia', 'Politiken', 'Kashmir', 'Slovenia', 'Canada', 'Paula Cox', 'Wales', 'Barbados', 'Jay Nixon', 'Bermuda', 'Télam', 'Haaretz', 'Madeira', 'Navarre', 'Sirius XM', 'J B Dauda', 'Ban Kimoon', 'Talal Arslan', 'Raúl', 'Isa Yuguda', 'Imran Khan', 'Yabloko', 'L K Advani', 'Sima Samar', 'Taleb Rifai', 'Masood Khan', 'Syriza', 'Selim Hoss', 'Mart Laar', 'Paul Biya', 'Mallikarjun', 'Paskal Milo', 'Milan Panić', 'AlAhram', 'Umar', 'ArNamys', 'Vlad Filat', 'Saddam Hussein', 'Al Wefaq', 'Jim Molan', 'Sharad Yadav', 'Bev Oda', 'Kamal Nath', 'Peter Hain', 'Khalid Ali', 'Ro Tuchol', 'Max Baucus', 'Gabon', 'Sidwaya', 'Radek John', 'Dharam Singh', 'Matt Mead', 'Danilo Medina', 'Giza', 'César Ham', 'Khun Sa', 'Wu Denyih', 'South Sudan', 'Harry Reid', 'Bangladesh', 'Pagan Amum', 'Hun Sen', 'Baldev Singh', 'Iran', 'Temelín', 'Ioan Rus', 'Mar Roxas', 'Ivica Kirin', 'Malik Agar', 'Angus King', 'Aung San', 'Jordan', 'Vilma Espín', 'Khin Yi', 'Mongolia', 'Finland', 'India', 'Kazakhstan', 'Marat Tazhin', 'Cameroon', 'Lamar Smith', 'Pakistan', 'Laos', 'Boediono', 'Milan Kučan', 'Neal S Wolin', 'Honduras', 'Latvia', 'Curaçao', 'Milan Roćen', 'Hilary Onek', 'Sam Ongeri', 'Uganda', 'Bola Tinubu', 'Mark Kirk', 'Moldova', 'Iceland', 'Ukraine', 'Maung Oo', 'Haiti', 'Tony Tan', 'Jason Hu', 'Mauritius', 'Belize', 'Fiji', 'Paraguay', 'South Asia']</most> and Terminate[Abdulla Kurd]
------------------------------ Example End ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly. The answer format is: The most similar 200 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
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

motif_ReAct_example_prompt_cn100_cn100 = """
You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity]. It requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 100 entities are: <most>[]</most> and Terminate[answer]. It returns the answer and finishes the task. It can only occur once!
Here are two examples.
Compare the background information of entities carefully to see if they are similar. 
------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly. The answer format is: The most similar 100 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Ne Win'

The Candidate entities list is: 
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia', 'India', 'Namibia', 'China', 'Jordan', 'Tony Tan', 'Iran', 'Fatah', 'Norway', 'Japan', 'Kenya', 'Khin Yi', 'Sweden', 'Madrid', 'Germany', 'Syria', 'Mexico', 'Brazil', 'Lebanon', 'Peter Hain', 'Peru', 'Qin Gang', 'Sukarno', 'Teng Biao', 'Tuva', 'Laos', 'Mike DeWine', 'Shas', 'UNITA', 'Diena', 'Togo', 'Umar', 'Pape Diop', 'Komeito', 'Yukos', 'Pete Wilson', 'Naruhito', 'Ānanda', 'Joe Walsh', 'ANTEL', 'Raúl', 'Ron Kirk', 'Penny Wong', 'Giza', 'Mike Rann', 'Ramdev', 'Wu Aiying', 'Boediono', 'MPLA', 'Bob Rae', 'Guinea']

NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select 100 most similar answer and 1 most similar entity from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: The most similar 100 entities are: <most>['Ne Win', 'Hla Min', 'Hla Tun', 'Soe Thein', 'Aung Min', 'Aung San', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Su Chi', 'Chea Sim', 'Shinzo Abe', 'Sukarno', 'Khin Yi', 'Yen Ming', 'Tea Banh', 'Hla Min', 'Komeito', 'Wu Sike', 'Ma Kai', 'Naoto Kan', 'Shas', 'Femen', 'Teng Biao', 'Boediono', 'Fatah', 'Raúl', 'Wu Aiying', 'Japan', 'Kuwait', 'China', 'Laos', 'Togo', 'Iran', 'Turkey', 'Belize', 'Kenya', 'Fiji', 'India', 'North Korea', 'Jordan', 'Thailand', 'Peru', 'Spain', 'Mexico', 'Lebanon', 'Germany', 'Brazil', 'Syria', 'Ukraine', 'Gabon', 'Namibia', 'Niger', 'Mali', 'Tuva', 'Norway', 'Latvia', 'MPLA', 'UNITA', 'Zambia', 'Benin', 'Togo', 'Argentina', 'Macedonia', 'North Korea', 'Russia', 'Nepal', 'Macedonia', 'Congo', 'Belarus', 'Bulgaria', 'Slovakia', 'Ethiopia', 'Portugal', 'Malaysia', 'South Africa', 'Philippines', 'Colombia', 'Saudi Arabia', 'Algeria', 'Vietnam', 'Cambodia', 'Singapore', 'Malaysia', 'Pakistan', 'Bangladesh', 'Sri Lanka', 'Turkey', 'Iran', 'China', 'Moldova', 'Belize', 'New Zealand', 'Sweden', 'Finland', 'Australia', 'South Korea', 'Philippines', 'Mongolia', 'Hong Kong']</most> ans Terminate['Ne Win'].
------------------------------ Example End ------------------------------ 

------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly. The answer format is: The most similar 100 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
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
Act 1: The most similar 100 entities are: <most>['Abdulla Kurd', 'Hla Min', 'Hla Tun', 'Salou Djibo', 'Sam Nujoma', 'Hamid Mir', 'Shwe Mann', 'Shas', 'Fatah', 'Ma Kai', 'Salam Fayyad', 'Saad Hariri', 'Sule Lamido', 'Talal Arslan', 'Jawed Ludin', 'Imran Khan', 'Sam Sesay', 'Ramdev', 'Aung Min', 'Sylvia Lim', 'Su Chi', 'Chea Sim', 'Kalyan Singh', 'Naoto Kan', 'Paul Martin', 'Dagestan', 'Panama', 'Aung Min', 'Suharto', 'Yabloko', 'Ron Wyden', 'Sima Samar', 'Haaretz', 'Télam', 'Khakassia', 'La Nación', 'Politiken', 'Ānanda', 'Kashmir', 'Canada', 'Barbados', 'Bermuda', 'Wales', 'Paula Cox', 'Navarre', 'Madeira', 'Sirius XM', 'Talal Arslan', 'Imran Khan', 'Sam Sesay', 'Fatah', 'Shas', 'Suharto', 'Malawi', 'Shwe Mann', 'Abdulla Kurd', 'Ron Wyden', 'Jawed Ludin', 'Sam Nujoma', 'Imran Khan', 'Canada', 'Jay Nixon', 'Bermuda', 'Haaretz', 'Politiken', 'Su Chi', 'Sylvia Lim', 'Hong Kong', 'Saad Hariri', 'Naoto Kan', 'Paula Cox', 'Malaysia', 'Salou Djibo', 'Malta', 'Benin', 'Raúl', 'Syria', 'Singapore', 'Télam', 'Chea Sim', 'Laos', 'Fiji', 'Mali', 'Sam Sesay', 'Su Chi', 'Macao', 'Somaliland', 'Laos', 'Kalyan Singh', 'Nepal', 'Seychelles', 'Laos', 'Slovakia', 'Hla Min', 'Sudan', 'Swaziland']</most> and Terminate[Abdulla Kurd]
------------------------------ Example End ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly. The answer format is: The most similar 100 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
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

motif_ReAct_example_prompt_cn70_cn70 = """
You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity]. It requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 70 entities are: <most>[]</most> and Terminate[answer]. It returns the answer and finishes the task. It can only occur once!
Here are two examples.
Compare the background information of entities carefully to see if they are similar. 
------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly. The answer format is: The most similar 70 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Ne Win'

The Candidate entities list is: 
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia', 'India', 'Namibia', 'China', 'Jordan', 'Tony Tan', 'Iran', 'Fatah', 'Norway', 'Japan', 'Kenya', 'Khin Yi', 'Sweden', 'Madrid', 'Germany', 'Syria', 'Mexico', 'Brazil', 'Lebanon', 'Peter Hain', 'Peru']


NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select 70 most similar answer and 1 most similar entity from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: The most similar 70 entities are: <most>['Ne Win', 'Hla Min', 'Hla Tun', 'Soe Thein', 'Aung Min', 'Su Chi', 'Aung San', 'Shwe Mann', 'Tin Oo', 'Khin Yi', 'Benin', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Aye Maung', 'Ukraine', 'Zambia', 'India', 'Namibia', 'China', 'Jordan', 'Tony Tan', 'Iran', 'Fatah', 'Norway', 'Japan', 'Kenya', 'Sweden', 'Madrid', 'Germany', 'Syria', 'Mexico', 'Brazil', 'Lebanon', 'Peter Hain', 'Peru']</most> ans Terminate['Ne Win'].
------------------------------ Example End ------------------------------ 

------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly. The answer format is: The most similar 70 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Salauddin'

The Candidate entities list is: 
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Sukarno', 'Mao Zedong', 'Benin', 'Sam Sesay', 'Poland', 'Ron Wyden', 'Japan', 'Somalia', 'Suharto', 'Vanuatu', 'Panama', 'Ramdev', 'Hamas', 'Lara Giddings', 'Cambodia', 'Sweden', 'Kalyan Singh', 'Aung Min', 'Su Chi', 'Sylvia Lim', 'Abdulla Kurd']


NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide the final answer. 
Thought 1: I can find a direct match.
Act 1: The most similar 70 entities are: <most>['Abdulla Kurd'，'Hla Min', 'Salou Djibo', 'Hla Tun', 'Soe Thein', 'Jean Ping', 'Ma Kai', 'Chea Sim', 'Shwe Mann', 'Ne Win', 'Benin', 'Jawed Ludin', 'Babar Awan', 'Hamid Mir', 'Joe Biden', 'Alexandria', 'Paul Martin', 'Sylvia Lim', 'Gilad Erdan', 'Carl Levin', 'Sam Sesay', 'Valdivia', 'Susan Rice', 'Dagestan', 'Macau', 'Attajdid', 'Sinn Féin', 'Kadima', 'Fatah', 'Basij', 'Shas', 'Hamas', 'Qatar', 'Oman', 'Burundi', 'Bayan Muna', 'Palau', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'San Marino', 'Salzburg', 'Sirindhorn', 'Kuwait', 'Naruhito', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Madrid', 'Jamaica', 'Maldives', 'Sung Kim', 'Sukarno', 'Mao Zedong', 'Poland', 'Ron Wyden', 'Japan', 'Somalia', 'Suharto', 'Vanuatu', 'Panama', 'Ramdev', 'Cambodia', 'Sweden', 'Kalyan Singh', 'Aung Min', 'Su Chi']</most> and Terminate[Abdulla Kurd]
------------------------------ Example End ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly. The answer format is: The most similar 70 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
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

motif_ReAct_example_prompt_cn50_cn50 = """
    You are a programmer in a large company, tasked with selecting the most similar entity to a target entity from a candidate list. You will solve the task using a series of interleaving Thought, Action, and Observation steps. Thought can reason about the current situation, and Action can only be one of the following two types:
    
    - Request[entity]: Requests the context information of the entity from external Knowledge Graphs. The context in formation is represented in the code motif format. You can only request one entity in each turn, and it must be from the candidate list or the target entity itself.
    - The most similar 50 entities are: <MOST>[]</MOST> and Terminate[answer]: Returns the answer and finishes the task. This action can only occur when you finish the task! When you decide to use terminate action, you mush put the most similar 50 entities into: "<MOST>[]</MOST>". Please note that if there is a direct match, please use act Terminate[] directly to end the precess.
    
    You must have a 'Thought' and 'Act' each turn, no matter the 'Act' is 'Request[entity]' or 'The most similar 50 entities are: <MOST>[]</MOST> and Terminate[answer]'. The 'Act' can only be two types. During the alignemnt task, you must follow the following rules:
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
    18. The output format should be: "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[entity]."
    19. Avoid selecting entities that shift focus away from the target entity's geographical or contextual relevance.
    20. Adapt the process based on the available information to ensure the accurate alignment of entities.
    21. The action can only be two types: "Request[entity]" and "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[entity]."
    22. Do not generate the observations and wait User to generate.
    23. The output format should be: "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[entity]."
    24. Please pay attention to the full candidate list including the tail of candidate list for candidate entities has high name similarity with the target entity.
    25. If there is same entity with target entity in the candidate list, please select and terminate with it directly.

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
    ** A class represented an entity.
    ** Fuction name: The function name is an abstract of the motif. Each function represent a motif.
    ** Relevant import statements: The import statement is relationship between entities.
    ** Function parameter: The function parameters are the entities in a motif.
    ** Function Implementation: Implement the function by calling the imported relations with the appropriate entities(parameters). Each relation call should correspond to the connections or actions described in the motif information.
    ** Relationship: For simple connections between nodes, use the connected_with relation. For more complex interactions (e.g., meetings, visits), use specific relations like make_a_visit, express_intent_to_meet_or_negotiate, etc.
    ** Return values: Return all the entities involved in the motif as part of the function’s result.
    ** Multiple relationship: Recognize the `+=` relationship as indicative of multiple types of connections between two entities, enriching the motif's complexity.
    ** Demonstrative Execution: Use the `if __name__ == '__main__':` block to showcase the motif's application, offering a practical example of its use.
    ** Triple: A triple in triangle information represent a motif and is expressed as a function in code motif.

    **NOTE:** You must request the most relevant entity information from the candidate list to reduce your uncertainty and finally help you to finish this task correctly. If you request less important entities and fail to handle this task perfectly, you will be immediately fired! Here are two examples to refer:
    
    ------
    ## Example 1:
    
    [USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it directly.
    
    **The target entity is:** 
    'Ne Win'
    
    **The candidate entities list is:**
    ['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia']
    
    NOTE:
    1. You have at most 4 turns to generate the final result. Please answer the task with interleaving Thought, Code, Action, Result turns. 
    2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
    3. The output format should be: "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[entity]."
    
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
    3. The output format should be: "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[entity]."
    
    [YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!
    
    ### Turn 1: (3 turns left to use "Terminate" action to provide final answer.)
    **Thought 1:** I find an entity in the candidate list that is a direct match for "Salauddin." 
    **Act 1:
    **The most similar 50 entities are:<MOST>['Abdulla Kurd', 'Salam Fayyad', 'Sule Lamido', 'Talal Arslan', 'Saad Hariri', 'Salou Djibo', 'Shwe Mann', 'Aung Min', 'Soe Thein', 'Suharto', 'Hla Min', 'Hla Tun', 'Jawed Ludin', 'Sima Samar', 'Samar', 'Sama', 'Shas', 'Fatah', 'Hamas', 'Gilad Erdan', 'Babar Awan', 'Hamid Mir', 'Ramdev', 'Imran Khan', 'Sylvia Lim', 'Kashmir', 'Ānanda', 'Sukarno', 'Sam Nujoma', 'Ne Win', 'Benin', 'Sula Lamido', 'Shwe Mann', 'Su Chi', 'Aung Min', 'Talal Arslan', 'Kashmir', 'Sule Lamido', 'Samar', 'Fatah', 'Hamas', 'Gilad Erdan', 'Babar Awan']</MOST> and Terminate['Abdulla Kurd']
   
    ------
    # New Task:
    [USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it and terminate directly. 
    
    **The target entity is:** 
    {}
    
    **The candidate entities list is:**
    {}
        
    NOTE:
    1. You have at most 4 turns to generate the final result. Please follow my examples above to answer the task with interleaving Thought, Code, Action, Result turns. 
    2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
    3. The output format should be: "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[entity]."
    
    
    [YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment
    
    ### Turn 1: (3 turns left to use "Terminate" action to provide final answer.)
    **Thought 1:**
    
"""

motif_ReAct_example_prompt_cn50_cn50_v0 = """
    You are a programmer in a large company, tasked with selecting the most similar entity to a target entity from a candidate list. You will solve the task using a series of interleaving Thought, Action, and Observation steps. Thought can reason about the current situation, and Action can only be one of the following two types:
    
    - Request[entity]: Requests the context information of the entity from external Knowledge Graphs. You can only request one entity in each turn, and it must be from the candidate list or the target entity itself.
    - Terminate[answer]: Returns the answer and finishes the task. This action can only occur when you finish the task! When you decide to use terminate action, you mush put the most similar 50 entities into: "<MOST>[]</MOST>". Please note that if there is a direct match, please use act Terminate[] directly to end the precess.
    
    You must have an act from above two actions per turn no matter it is request or terminate. The act can only be two types. 
    
    **NOTE:** You must request the most relevant entity information from the candidate list to reduce your uncertainty and finally help you to finish this task correctly. If you request less important entities and fail to handle this task perfectly, you will be immediately fired! Here are two examples to refer:

    ------
    ## Example 1:
    
    [USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it directly.
    
    **The target entity is:** 'Ne Win'
    
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
    
    [USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it directly. 
    
    **The target entity is:** 'Salauddin'
    
    **The candidate entities list is:**
    ['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Fatah', 'Kadima', 'Babar Awan', 'Hamid Mir', 'Gilad Erdan', 'Qatar', 'Basij', 'Alexandria', 'Kuwait', 'Naruhito', 'Jean Ping', 'Oman', 'Susan Rice', 'Naoto Kan', 'Mali', 'Sam Nujoma', 'Joe Biden', 'Ma Kai', 'Burundi', 'Shas', 'Madrid', 'Ne Win', 'Dagestan', 'Paul Martin', 'Bayan Muna', 'Jamaica', 'Maldives', 'Chea Sim', 'Sung Kim', 'Shwe Mann', 'Abdulla Kurd']
    
    NOTE:
    1. You have at most 4 turns to generate the final result. Please answer the task with interleaving Thought, Code, Action, Result turns. 
    2. Please put the entity in the terminate in the first entity of the candidate list reranked!!! 
    
    [YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!
    
    ### Turn 1: (3 turns left to use "Terminate" action to provide final answer.)
    **Thought 1:** I cannot find an entity in the candidate list that is a direct match for "Salauddin." I need more information about "Salauddin" to make an informed decision.
    **Act 1:** Request['Salauddin']
    **Observation 1:**
    ```
    # Importing the necessary relationships for the motifs
    from relations import connected_with, consult, host_a_visit, engage_in_negotiation
    from relations import express_intent_to_meet_or_negotiate, deny_responsibility
    from relations import abduct_hijack_take_hostage, occupy_territory, confiscate_property
    
    class Salauddin:
        def __init__(self, Salauddin, Head_of_Government_Qatar, Pervez_Musharraf, Israel, Bangladesh, Criminal_India, Citizen_India, Police_Bangladesh):
            # Initializing entities involved in the motifs
            self.Salauddin = Salauddin
            self.Head_of_Government_Qatar = Head_of_Government_Qatar
            self.Pervez_Musharraf = Pervez_Musharraf
            self.Israel = Israel
            self.Bangladesh = Bangladesh
            self.Criminal_India = Criminal_India
            self.Citizen_India = Citizen_India
            self.Police_Bangladesh = Police_Bangladesh
        
        def Salauddin_Consult_with_Head_of_Government_Qatar(self):
            # Implementing Motif 1: Salauddin consults with the Head of Government of Qatar
            self.Salauddin = consult(self.Head_of_Government_Qatar)
            self.Salauddin += connected_with(self.Pervez_Musharraf)
            self.Head_of_Government_Qatar = host_a_visit(self.Pervez_Musharraf)
            self.Head_of_Government_Qatar += engage_in_negotiation(self.Pervez_Musharraf)
            
            return self.Salauddin, self.Head_of_Government_Qatar, self.Pervez_Musharraf
        
        def Salauddin_Express_Intent_to_Meet_Israel(self):
            # Implementing Motif 2: Salauddin expresses intent to meet or negotiate with Israel
            self.Salauddin = express_intent_to_meet_or_negotiate(self.Israel)
            self.Salauddin += deny_responsibility(self.Bangladesh)
            self.Israel = connected_with(self.Bangladesh)
            
            return self.Salauddin, self.Israel, self.Bangladesh
        
        def Salauddin_Connected_with_Criminal_India(self):
            # Implementing Motif 3: Salauddin's connection with Criminal (India)
            self.Salauddin = connected_with(self.Criminal_India)
            self.Salauddin += deny_responsibility(self.Bangladesh)
            self.Criminal_India = abduct_hijack_take_hostage(self.Bangladesh)
            self.Criminal_India += occupy_territory(self.Bangladesh)
            
            return self.Salauddin, self.Criminal_India, self.Bangladesh
        
        def Citizen_India_Connected_with_Salauddin(self):
            # Implementing Motif 4: Citizen (India) connected with Salauddin and expressing intent to meet Israel
            self.Citizen_India = connected_with(self.Salauddin)
            self.Citizen_India += express_intent_to_meet_or_negotiate(self.Israel)
            self.Salauddin += express_intent_to_meet_or_negotiate(self.Israel)
            
            return self.Citizen_India, self.Salauddin, self.Israel
        
        def Salauddin_Connected_with_Police_Bangladesh(self):
            # Implementing Motif 5: Salauddin's connection with Police (Bangladesh) and Pervez Musharraf
            self.Salauddin = connected_with(self.Police_Bangladesh)
            self.Salauddin += connected_with(self.Pervez_Musharraf)
            self.Police_Bangladesh = confiscate_property(self.Pervez_Musharraf)
            
            return self.Salauddin, self.Police_Bangladesh, self.Pervez_Musharraf
            
    if name == 'main':
        # Sample nodes representing entities in the motifs
        Salauddin = "Salauddin"
        Head_of_Government_Qatar = "Head_of_Government_Qatar"
        Pervez_Musharraf = "Pervez_Musharraf"
        Israel = "Israel"
        Bangladesh = "Bangladesh"
        Criminal_India = "Criminal_India"
        Citizen_India = "Citizen_India"
        Police_Bangladesh = "Police_Bangladesh"
        
        # Instantiating the class with sample data
        motifs = Salauddin(Salauddin, Head_of_Government_Qatar, Pervez_Musharraf, Israel, Bangladesh, Criminal_India, Citizen_India, Police_Bangladesh)
        
        # Demonstrating the motifs
        print(motifs.Salauddin_Consult_with_Head_of_Government_Qatar())
        print(motifs.Salauddin_Express_Intent_to_Meet_Israel())
        print(motifs.Salauddin_Connected_with_Criminal_India())
        print(motifs.Citizen_India_Connected_with_Salauddin())
        print(motifs.Salauddin_Connected_with_Police_Bangladesh())
    
    ```
    
    ### Turn 2: (2 turns left to use "Terminate" action to provide final answer.)
    **Thought 2:** Based on the observation, 'Salauddin' has connections with Bangladesh, India, and Pervez Musharraf. Considering this information, I should now request information about the most relevant candidate entity.
    **Act 2:** Request['Abdulla Kurd']
    **Observation 2:**
    ```
    # Importing the necessary connection relationship functions
    from connections import connected_with
    
    class Abdulla_Kurd(object):
        
        def __init__(self, Abdulla_Kurd, Turkey, Entity):
            # Initialize the entities involved in the motifs
            self.Abdulla_Kurd = Abdulla_Kurd
            self.Turkey = Turkey
            self.Entity = Entity
    
        def entity_connected_with_Turkey_and_Abdulla_Kurd(self):
            #This motif represents a triangle where the entity is connected with Turkey and Abdulla Kurd,
            #and Turkey is also connected with Abdulla Kurd.
  
            self.Entity = connected_with(self.Turkey)
            self.Entity = connected_with(self.Abdulla_Kurd)
            self.Turkey = connected_with(self.Abdulla_Kurd)
    
            return self.Entity, self.Turkey, self.Abdulla_Kurd
    
    if __name__ == "__main__":
        # Demonstrating the motif's application with sample nodes
        motif = Abdulla_Kurd("Abdulla Kurd", "Turkey", "Entity")
        result = motif.entity_connected_with_Turkey_and_Abdulla_Kurd()
        print(result)
    ```
    
    ### Turn 2: (1 turns left to use "Terminate" action to provide final answer.)
    **Thought 3:** Based on the observation, 'Abdulla Kurd' has connections with Turkey. Since 'Salauddin' has connections with regions including Bangladesh and India, I need to evaluate if there is a stronger match in the candidate list. Given this context, I should now request information about another potentially relevant candidate entity.
    **Act 3:** Request['Salahuddin of Selangor']
    **Observation 3:**
    ```
    # Importing the necessary relationship functions
    from connections import connected_with, contained_in_place, nationality
    
    class Salahuddin_of_Selangor(object):
        
        def __init__(self, Salahuddin_of_Selangor, Kuala_Lumpur, Malaysia):
            # Initialize the entities involved in the motifs
            self.Salahuddin_of_Selangor = Salahuddin_of_Selangor
            self.Kuala_Lumpur = Kuala_Lumpur
            self.Malaysia = Malaysia
    
        def Kuala_Lumpur_connected_with_Salahuddin_of_Selangor(self):
        
            ##This motif represents the connection between Kuala Lumpur and Salahuddin of Selangor,
            ##where Kuala Lumpur is also contained in Malaysia, and Salahuddin of Selangor's nationality is Malaysia.
        
            self.Kuala_Lumpur = connected_with(self.Salahuddin_of_Selangor)
            self.Kuala_Lumpur = contained_in_place(self.Malaysia)
            self.Salahuddin_of_Selangor = nationality(self.Malaysia)
    
            return self.Kuala_Lumpur, self.Salahuddin_of_Selangor, self.Malaysia
    
    if __name__ == "__main__":
        # Demonstrating the motif's application with sample nodes
        motif = Salahuddin_of_Selangor_Motifs("Salahuddin of Selangor", "Kuala Lumpur", "Malaysia")
        result = motif.Kuala_Lumpur_connected_with_Salahuddin_of_Selangor()
        print(result)
        
    ```
    
    ### Turn 4: (NOTE: MUST use "Terminate" action to provide final answer in this turn)
    **Thought 4:** Based on the observation, 'Salahuddin of Selangor' is connected with Kuala Lumpur and Malaysia. This information is not as relevant as the connections 'Salauddin' has with Bangladesh, India, and Pervez Musharraf. The connections of 'Abdulla Kurd' with Turkey seem more aligned with the context of 'Salauddin'.
    **Act 4:
    **The most similar 50 entities are:<MOST>['Abdulla Kurd', 'Salam Fayyad', 'Sule Lamido', 'Talal Arslan', 'Saad Hariri', 'Salou Djibo', 'Shwe Mann', 'Aung Min', 'Soe Thein', 'Suharto', 'Hla Min', 'Hla Tun', 'Jawed Ludin', 'Sima Samar', 'Samar', 'Sama', 'Shas', 'Fatah', 'Hamas', 'Gilad Erdan', 'Babar Awan', 'Hamid Mir', 'Ramdev', 'Imran Khan', 'Sylvia Lim', 'Kashmir', 'Ānanda', 'Sukarno', 'Sam Nujoma', 'Ne Win', 'Benin', 'Sula Lamido', 'Shwe Mann', 'Su Chi', 'Aung Min', 'Talal Arslan', 'Kashmir', 'Sule Lamido', 'Samar', 'Fatah', 'Hamas', 'Gilad Erdan', 'Babar Awan']</MOST> and Terminate['Abdulla Kurd']

    ------
    # New Task:
    [USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it directly. 
    
    **The target entity is:** {}
    
    **The candidate entities list is:**
    {}
    
    NOTE:
    1. You have at most 4 turns to generate the final result. Please follow my examples above to answer the task with interleaving Thought, Code, Action, Result turns. 
    2. Please put the entity in the terminate in the first entity of the candidate list reranked!!!
    3. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'!!!
    4. If you are very sure about the answer, please answer directly. 
    5. If there is the same entity in the candidate list as the target entity, please select it directly and terminate the process. 
    6. You must have an act from above two actions per turn no matter it is request or terminate. The act can only be two types.
    7. Please follow the example format: thought, action, observation steps. Do not generate response by yourself.
    8. If you can find a direct match, please use act "Terminate[]" directly and do no need to confirm another entity.
    9. If you are can not find a direct match, please request and do not terminate.
    10. Please do not generate any observations, generate thought and act.
    11. The output format is "The most similar 50 entities are: <MOST>[]</MOST> and Terminate[answer]".
    12. Request[] action can only request an entity in candidate list or it is itself. 
    
    [YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment
    
    ### Turn 1: (3 turns left to use "Terminate" action to provide final answer.)
    **Thought 1:**
    
"""

motif_ReAct_example_prompt_cn50_cn50_v1 = """
    You are a programmer in a large company, tasked with selecting the most similar entity to a target entity from a candidate list. You will solve the task using a series of interleaving Thought, Action, and Observation steps. Thought can reason about the current situation, and Action can only be one of the following two types:
    
    - Request[entity]: Requests the context information of the entity from external Knowledge Graphs. You can only request one entity in each turn, and it must be from the candidate list or the target entity itself.
    - The most similar 50 entities are: <MOST>[]</MOST> and Terminate[answer]: Returns the answer and finishes the task. This action can only occur when you finish the task! When you decide to use terminate action, you mush put the most similar 50 entities into: "<MOST>[]</MOST>". Please note that if there is a direct match, please use act Terminate[] directly to end the precess.
    
    You must have an act from above two actions per turn no matter it is request or terminate. The act can only be two types. 
    
    **NOTE:** You must request the most relevant entity information from the candidate list to reduce your uncertainty and finally help you to finish this task correctly. If you request less important entities and fail to handle this task perfectly, you will be immediately fired! Here are two examples to refer:
    
    ------
    ## Example 1:
    
    [USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it directly.
    
    **The target entity is:** 'Ne Win'
    
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
    
    [USER (Boss)]: Please rerank the candidate list by the similarity to target entity and select 1 most similar entity from it to terminate. If there is the same entity in the candidate list as the target entity, please select it directly. 
    
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
    {}
    
    **The candidate entities list is:**
    {}
    
    NOTE:
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
    
    [YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment
    
    ### Turn 1: (3 turns left to use "Terminate" action to provide final answer.)
    **Thought 1:**
    
    """

# motif_ReAct_example_prompt_cn50_cn50_llama = motif_ReAct_example_prompt_cn50_cn50
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
{}

The candidate entities list is:
{}

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
{}

The candidate entities list is:
{}

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