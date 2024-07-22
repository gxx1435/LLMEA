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
