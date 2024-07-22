motif_ReAct_example_prompt = """
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
