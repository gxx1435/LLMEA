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
Act 4:The most similar 50 entities are: ['Abdulla Kurd', 'Salam Fayyad', 'Hamid Mir', 'Salou Djibo', 'Soe Thein', 'Sukarno', 'Jean Ping', 'Chea Sim', 'Shwe Mann', 'Aung Min', 'Ne Win', 'Gilad Erdan', 'Ramdev', 'Paul Martin', 'Sam Sesay', 'Ma Kai', 'Fatah', 'Sinn Féin', 'Somalia', 'Mao Zedong', 'Hla Min', 'Hla Tun', 'Panama', 'Hamas', 'Suharto', 'Attajdid', 'Talal Arslan', 'Isa Yuguda', 'Saad Hariri', 'Shaul Mofaz', 'Alexandria', 'Carl Levin', 'Sam Nujoma', 'Dan Burton', 'Ron Wyden', 'Kadima', 'Raila Odinga', 'Sylvia Lim', 'Susan Rice', 'Babar Awan', 'Sima Samar', 'Aung San', 'Jawed Ludin', 'Imran Khan', 'Navarre', 'Poland', 'Wales', 'Soe Aung', 'Malawi', 'Benin', 'Tatarstan']. Terminate['Abdulla Kurd'].
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
