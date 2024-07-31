
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

motif_ReAct_example_prompt_cn50_cn50 = """
You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity]. It requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 50 entities are: <most>[]</most> and Terminate[answer]. It returns the answer and finishes the task. It can only occur once!
Here are two examples.
Compare the background information of entities carefully to see if they are similar. 
------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly. The answer format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Ne Win'

The Candidate entities list is: 
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Ukraine', 'Zambia']

NOTE: 
1. You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.
2. The entity in terminate must be in the first entity in the candidate list returned!

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select 50 most similar answer and 1 most similar entity from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: The most similar 50 entities are: <most>['Ne Win', 'Hla Min', 'Soe Thein', 'Chea Sim', 'Aung Min', 'Hla Tun', 'Su Chi', 'Tea Banh', 'Shwe Mann', 'Tin Oo', 'Aye Maung', 'Benin', 'Yen Ming', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Serbia', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Temelín', 'Basij', 'Joe Biden', 'Wu Sike', 'Fiji', 'Kuwait', 'Le Monde', 'Belize', 'Oman', 'Bahrain', 'NATO', 'New Vision', 'NASA', 'Mechel', 'Cemex', 'Telcel', 'Xerox', 'Niger', 'Mali', 'Gabon', 'Aung San', 'Sung Kim', 'Latvia', 'Naoto Kan', 'Haiti', 'Ukraine', 'Zambia']</most> ans Terminate['Ne Win'].
------------------------------ Example End ------------------------------ 

------------------------------ Example Start ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly. The answer format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
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
Act 1: The most similar 50 entities are: <most>['Abdulla Kurd', 'Salam Fayyad', 'Sule Lamido', 'Talal Arslan', 'Saad Hariri', 'Salou Djibo', 'Shwe Mann', 'Aung Min', 'Soe Thein', 'Suharto', 'Hla Min', 'Hla Tun', 'Jawed Ludin', 'Sima Samar', 'Samar', 'Sama', 'Shas', 'Fatah', 'Hamas', 'Gilad Erdan', 'Babar Awan', 'Hamid Mir', 'Ramdev', 'Imran Khan', 'Sylvia Lim', 'Kashmir', 'Ānanda', 'Sukarno', 'Sam Nujoma', 'Ne Win', 'Benin', 'Sula Lamido', 'Shwe Mann', 'Su Chi', 'Aung Min', 'Talal Arslan', 'Kashmir', 'Sule Lamido', 'Samar', 'Fatah', 'Hamas', 'Gilad Erdan', 'Babar Awan']</most> and Terminate[Abdulla Kurd]
------------------------------ Example End ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly. The answer format is: The most similar 50 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
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

motif_ReAct_example_prompt_cn20_cn20 = """
You are an programmer. You can request useful entity from candidate list but you can not request irrelevant entities. Otherwise, you will be fired. 
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action only can be two types: 
(1) Request[entity], which requests the entity context information from Knowledge Graphs. The context information may be given in code description. You can only request once per time and each time an entity in candidate list.
(2) The most similar 20 entities after sort are: <most>[]</most> and Terminate[answer], which returns the answer and finishes the task.
Here are two examples.
Compare the background information of entities carefully to see if they are similar. 
------------------------------# Example1 Start ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly. The answer format is: The most similar 20 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Ne Win'

The Candidate entities list is: 
['Ne Win', 'Benin', 'Hla Min', 'Femen', 'Yen Ming', 'Nokia', 'Chea Sim', 'Soe Thein', 'Jean Ping', 'Hun Sen', 'Ma Kai', 'Aung Min', 'Serbia', 'Hla Tun', 'Bev Oda', 'Meretz', 'Spain', 'Ta Nea', 'Su Chi', 'Tea Banh']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select 20 most similar answer from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find the aligned entity directly from the candidate list because there is a direct match. 
Act 1: The most similar 20 entities are: <most>['Ne Win', 'Hla Min', 'Soe Thein', 'Aung Min', 'Hla Tun', 'Chea Sim', 'Hun Sen', 'Yen Ming', 'Bev Oda', 'Jean Ping', 'Ma Kai', 'Su Chi', 'Ta Nea', 'Meretz', 'Femen', 'Nokia', 'Spain', 'Benin', 'Serbia', 'Tea Banh']</most> and Terminate['Ne Win']
------------------------------# Example1 End ------------------------------ 

------------------------------ Example2 Start ------------------------------ 

[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly. The answer format is: The most similar 20 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
'Salauddin'

The Candidate entities list is: 
['Palau', 'Hla Min', 'Salou Djibo', 'Attajdid', 'Malawi', 'Bahrain', 'Malaysia', 'Raila Odinga', 'Spain', 'Valdivia', 'San Marino', 'Hla Tun', 'Carl Levin', 'Tatarstan', 'Soe Thein', 'Salzburg', 'Sinn Féin', 'Macau', 'Sirindhorn', 'Jawed Ludin', 'Abdulla Kurd']

NOTE: You have at most 4 turns to generate final results, which means you have to provide the answer at or earlier than Thought 4.  If you are very sure about the answer, please answer directly.

[YOU (Programmer)]: Let's break down the code generation and solve the Entity Alignment task turn by turn!  
################### Your Answer Starts Here: ################### 
Turn 1:
# 4 turns left to provide final answer. Please select one answer from the candidates list. If you are very sure about the answer, please answer directly. Otherwise, you can request the entity you are not sure to increase your confidency. Please do not request entity randomly, otherwise, you will be punished! You can only request one entity per time.
Thought 1: I can find an entity in the candidate list that is a direct match for "Salauddin." 
Act 1:The most similar 20 entities are: <most>['Abdulla Kurd', 'Salou Djibo', 'Attajdid', 'Hla Min', 'Hla Tun', 'Bahrain', 'Malaysia', 'Palau', 'San Marino', 'Soe Thein', 'Spain', 'Valdivia', 'Malawi', 'Sinn Féin', 'Carl Levin', 'Tatarstan', 'Salzburg', 'Macau', 'Sirindhorn', 'Jawed Ludin']</most> and Terminate['Abdulla Kurd']

------------------------------ Example2 End ------------------------------ 


[USER (Boss)]: Please sort the candidate list according to similarity to target entity and select the most aligned entity of the target entity. You have at most 4 turns to finish the task. If there is same entity in candidate list for target entity, please select directly. The answer format is: The most similar 20 entities are: <most>[]</most> and Terminate[answer]. The target entity is:
{}

The Candidate entities list is: 
{}

NOTE: Please follow my example between "Example i Start" and "Example i End" above to answer task with interleaving Thought, Code, Action, Result turns. Each turn contains one segment of the target code to solve the problem. 

[YOU (Programmer)]: Let's break down the code generation into several turns and solve the Entity Alignment task turn by turn! 
################### Your Answer Starts Here: ################### 

Turn 1:
# [Important!] 4 turns left to provide final answer. If you are very sure about the answer, please answer directly. Please only genenrate 'Thought' and 'Act' and wait the User to generate 'Observation'. Your answer must be in candidate list, otherwise, you will got fired. 
Thought 1:

"""