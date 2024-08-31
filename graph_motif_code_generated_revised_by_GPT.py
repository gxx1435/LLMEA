import os.path
import networkx as nx
from itertools import combinations
import numpy as np
from run.utils import get_id_entity_dict, get_ent_id_dict

# tmp1 = Please encapsulate the answer code within <code> </code>.
# tmp2 = 回答请在python代码块中呈现
# Example functions for motif instances based on provided triangle information
# 6.  Please encapsulate the answer code within <code> </code>
"""
    1.  The function name is a relation between the nodes
    2.  Please import relation
    3.  Please note that the inter-calling relationships within the functions should correspond to the given triangle motif relationships. 
    4.  Please note the left-right relationship between function calls and variable names.
    5.  The function name should represent some relations.c
    6.  回答请在python代码块中呈现
"""


"""[(Vladimir Putin, makes a visit, expresses intent to meet or negotiate, and consults with, Yury Nikolayevich Baluyevsky), (Yury Nikolayevich Baluyevsky, holds a visit, with Citizen (Russia)),(Citizen (Russia), is connected with, Vladimir Putin)]

"""
"""[(Vladimir Putin, makes a visit,Yury Nikolayevich Baluyevsky),( Vladimir Putin, expresses intent to meet or negotiate,Yury Nikolayevich Baluyevsky),(Vladimir Putin, and consults with , Yury Nikolayevich Baluyevsky), (Yury Nikolayevich Baluyevsky, holds a visit, with Citizen (Russia)),(Citizen (Russia), is connected with, Vladimir Putin)]
"""

code_motif_prompts_generate = """
    As a good Computer Science student good at coding, your task is to describe the graph structure in Python code format. Motifs are recurrent and statistically significant subgraphs or patterns of a larger graph. Each Motif instance will be viewed as a function with specialized name and node involved in the Motif instance will be the parameters in the function. 
    During the code motif generation task, you should follow the below rules:
    **Rules for generating Code Description**
    ** Class: A class represented an entity.
    ** If triangle motif information is '', its code description is ''.
    ** There is no need for you to generate code description for empty triangle motif information.
    ** Descriptive Function Names: Ensure the function name clearly represents the abstract of the motif. This aids in understanding the motif's purpose at a glance.
    ** Relevant import statements: The import statement is relationship between entities.
    ** Function parameter: The function parameters are all the entities of a motif.
    ** Function Implementation: Implement the function by calling the imported relations with the appropriate entities(parameters). Each relation call should correspond to the connections or actions described in the motif information.
    ** Relationship: For simple connections between nodes, use the connected_with relation. For more complex interactions (e.g., meetings, visits), use specific relations like make_a_visit, express_intent_to_meet_or_negotiate, etc.
    ** Return values: Return all the entities involved in the motif as part of the function’s result.
    ** Multiple relationship: Recognize the `+=` relationship as indicative of multiple types of connections between two entities, enriching the motif's complexity.
    ** Demonstrative Execution: Use the `if __name__ == '__main__':` block to showcase the motif's application, offering a practical example of its use.
    ** Triple: A triple in triangle information represent a motif and is expressed as a function in code motif, like:
    1. Accurately represent all entities and their relationships within the knowledge graph in the code.
    2. Use clear, descriptive variable names that reflect the entity or relationship they represent.
    3. Model the interactions or behaviors between entities through functions.
    4. Include comments to explain the purpose of functions and the significance of variables.
    5. Reflect the hierarchical or networked nature of the knowledge graph in the code structure.
    6. Apply object-oriented programming principles to model entities as objects and relationships as methods.
    7. Ensure modularity for easy updates or expansions.
    8. Incorporate error handling for incomplete or incorrect data.
    9. Use consistent naming conventions for functions, variables, and classes.
    10. Implement testing routines for code accuracy verification.
    11. Prioritize code efficiency for handling large or complex knowledge graphs.
    12. Include documentation detailing the code's purpose, its modeling of the knowledge graph, and usage instructions.
    13. Ensure flexibility to handle different types of entities and relationships.
    14. Use appropriate data structures for efficient entity and relationship storage and access.
    15. Implement search and query functions for information retrieval.
    16. Accurately reflect the statistical significance of motifs within the knowledge graph.
    17. Incorporate feedback mechanisms for code accuracy refinement.
    18. Design the code for scalability to accommodate knowledge graph growth.
    19. Use version control for change management.
    20. Align the code with software development best practices, including security, maintainability, and scalability.
   
    Note: Please refer to the example below and handle a new task! 
    
    ## Example Starts: 
    Given triangle Motif information, generate its Code description.
    
    **Triangle Motif information:**
    - Target entity: Vladimir Putin; Motif 1: [(Vladimir Putin, is connected with, Georgia),(Georgia, is connected with, Yury Nikolayevich Baluyevsky),(Yury Nikolayevich Baluyevsky, is connected with, Vladimir Putin)]
    - Target entity: Vladimir Putin; Motif 2：[(Vladimir Putin, is connected with, Georgia),(Georgia, is connected with, Bronislaw Geremek),(Bronislaw Geremek, is connected with, Vladimir Putin)]
    - Target entity: Vladimir Putin; Motif 3: [(Vladimir Putin, makes a visit, expresses intent to meet or negotiate, and consults with, Yury Nikolayevich Baluyevsky), (Yury Nikolayevich Baluyevsky, holds a visit, with Citizen (Russia)),(Citizen (Russia), is connected with, Vladimir Putin)]
        
        
    **Code description:**
    <CODE>
    ```     
    import is_connected_with, make_a_visit, hold_a_visit，Express_intent_to_meet_or_negotiate，Consult
    
    class Vladimir_Putin(object):
    
        def __init__(self, Vladimir_Putin, Georgia, Yury_Nikolayevich_Baluyevsky, Bronislaw_Geremek, Citizen_Russia):
            ## This is initial funciton
            self.Vladimir_Putin = Vladimir_Putin
            self.Georgia = Georgia
            self.Yury_Nikolayevich_Baluyevsky = Yury_Nikolayevich_Baluyevsky
            self.Bronislaw_Geremek =  Bronislaw_Geremek
            self.Citizen_Russia = Citizen_Russia
           
        
        def Vladimir_Putin_connected_with(self):
            self.Vladimir_Putin = is_connected_with(self.Georgia)
            self.Georgia = is_connected_with(self.Yury_Nikolayevich_Baluyevsky)
            self.Yury_Nikolayevich_Baluyevsky = is_connected_with(self.Vladimir_Putin)
            
            return self.Vladimir_Putin, self.Georgia, self.Yury_Nikolayevich_Baluyevsky
    
    
        def Georgia_connected_with(self):
            self.Vladimir_Putin = is_connected_with(self.Georgia)
            self.Georgia = is_connected_with(self.Bronislaw_Geremek)
            self.Bronislaw_Geremek = is_connected_with(self.Vladimir_Putin)
            
            return self.Vladimir_Putin, self.Georgia, self.Bronislaw_Geremek
    
    
        def Vladimir_Putin_Make_a_visit(self):
            self.Vladimir_Putin = make_a_visit(self.Yury_Nikolayevich_Baluyevsky)
            self.Vladimir_Putin += Express_intent_to_meet_or_negotiate(self.Yury_Nikolayevich_Baluyevsky)
            self.Vladimir_Putin += Consult(self.Yury_Nikolayevich_Baluyevsky)
            self.Yury_Nikolayevich_Baluyevsky = hold_a_visit(self.Citizen_(Russia))
            self.Citizen_Russia = is_connected_with(self.Vladimir_Putin)
    
            return self.Vladimir_Putin, self.Yury_Nikolayevich_Baluyevsky, self.Citizen_Russia
    ```     
    </CODE>
    
    
    ## New Task Starts:
    Given triangle Motif information, generate its Code description.
    
    **Triangle Motif information:**
    {}
    
    Note: There is no need for you to generate code description for empty triangle motif information.
   
""".format(
    """
    - Target entity: Carlos Johnny Méndez; Motif 1: [(Carlos Johnny Méndez, has Occupation ,Politician),(Carlos Johnny Méndez, nationality ,United States),(Carlos Johnny Méndez, given Name ,Carlos (given name)),(Carlos Johnny Méndez, member Of ,New Progressive Party (Puerto Rico)),(Carlos Johnny Méndez, alumni Of ,University of Puerto Rico),(Politician, connected with ,Carlos Johnny Méndez),(United States, connected with ,Carlos Johnny Méndez),(Carlos (given name), connected with ,Carlos Johnny Méndez),(New Progressive Party (Puerto Rico), connected with ,Carlos Johnny Méndez),(University of Puerto Rico, connected with ,Carlos Johnny Méndez)]
    """
)

code_motif_rules = """
        ** Class: A class represented an entity.
        ** If triangle motif information is '', its code description is ''.
        ** There is no need for you to generate code description for empty triangle motif information.
        ** Descriptive Function Names: Ensure the function name clearly represents the abstract of the motif. This aids in understanding the motif's purpose at a glance.
        ** Relevant import statements: The import statement is relationship between entities.
        ** Function parameter: The function parameters are all the entities of a motif.
        ** Function Implementation: Implement the function by calling the imported relations with the appropriate entities(parameters). Each relation call should correspond to the connections or actions described in the motif information.
        ** Relationship: For simple connections between nodes, use the connected_with relation. For more complex interactions (e.g., meetings, visits), use specific relations like make_a_visit, express_intent_to_meet_or_negotiate, etc.
        ** Return values: Return all the entities involved in the motif as part of the function’s result.
        ** Multiple relationship: Recognize the `+=` relationship as indicative of multiple types of connections between two entities, enriching the motif's complexity.
        ** Demonstrative Execution: Use the `if __name__ == '__main__':` block to showcase the motif's application, offering a practical example of its use.
        ** Triple: A triple in triangle information represent a motif and is expressed as a function in code motif, like:
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
 """