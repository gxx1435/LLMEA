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
5.  The function name should represent some relations.
6.  回答请在python代码块中呈现
"""


triagles_infomation = """
10791 , Ne Win , Motif 1:
Ne Win Threaten,Express intent to meet or negotiate Military (Myanmar)
Ne Win Make a visit Indonesia
Military (Myanmar) Make a visit Indonesia
10791 , Ne Win , Motif 2:
Than Shwe Engage in symbolic act Ne Win
Than Shwe Express intent to engage in diplomatic cooperation (such as policy support),Express intent to meet or negotiate,Threaten,Demonstrate or rally Military (Myanmar)
Ne Win Threaten,Express intent to meet or negotiate Military (Myanmar)
10791 , Ne Win , Motif 3:
Ne Win connected with Kyaw Win
Ne Win Threaten,Express intent to meet or negotiate Military (Myanmar)
Kyaw Win Express intent to meet or negotiate,fight with artillery and tanks Military (Myanmar)
"""

code_motif_prompts_generate = """
As a good Computer Science student good at coding, your task is to describe the graph structure in Python code format. Motifs are recurrent and statistically significant subgraphs or patterns of a larger graph. Each Motif instance will be viewed as a function with specialized name and node involved in the Motif instance will be the parameters in the function. 

**Rules for generating code format Motif**
  1. Function Name: Use a descriptive name for the function that is an abstract of the motif. The function name should indicate the type of relationship or action involving the nodes.
  2. Import Statements: Import the necessary relations or actions. Use descriptive names that match the relationships in the motif information.
  3. Function Parameters: Include all nodes involved in the motif as parameters to the function.
  4. Function Implementation: Implement the function by calling the imported relations with the appropriate parameters. Each relation call should correspond to the connections or actions described in the motif information.
  5. Connection Relationships: For simple connections between nodes, use the connected_with relation.
  6. Complex Relationships: For more complex interactions (e.g., meetings, visits), use specific relations like make_a_visit, express_intent_to_meet_or_negotiate, etc.
  7. Return Values: Return all the nodes involved in the motif as part of the function’s result. Ensure that the function returns the state or outcome after applying the relationships.
  8. Please note the += relationship which represents multiple relationship between two nodes. It means two nodes have more than 1 type of relationship.
  9. A definition function represents a motif.
  10. The code should fully represent the structural information between nodes.

  
Please refer to the example below and handle a new task! 

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
"""