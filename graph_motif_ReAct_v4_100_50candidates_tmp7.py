motif_ReAct_example_prompt = """
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
