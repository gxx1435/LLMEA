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

As a good Computer Science student good at coding, your task is to describe the graph structure in Python code format. Each Motif instance will be viewed as a function with specialized name and node involved in the Motif instance will be the parameters in the function. 
<RULE>
  1. Function Name: Use a descriptive name for the function that represents the relationship between the nodes. The function name should indicate the type of relationship or action involving the nodes.
  2. Import Statements: Import the necessary relations or actions. Use descriptive names that match the relationships in the motif information.
  3. Function Parameters: Include all nodes involved in the motif as parameters to the function.
  4. Function Implementation: Implement the function by calling the imported relations with the appropriate parameters. Each relation call should correspond to the connections or actions described in the motif information.
  5. Connection Relationships: For simple connections between nodes, use the connected_with relation.
  6. Complex Relationships: For more complex interactions (e.g., meetings, visits), use specific relations like make_a_visit, express_intent_to_meet_or_negotiate, etc.
  7. Return Values: Return all the nodes involved in the motif as part of the function’s result. Ensure that the function returns the state or outcome after applying the relationships.
  8. Execution: In the if __name__ == '__main__': block, call the defined functions with sample nodes to demonstrate how the motif relationships are applied.
  
</RULE>
Please refer to the example below and handle new tasks! 

=== Example Starts: ===
Given triangle information, generate its Code description.
Triangle information:
6023 ,  Vladimir Putin, Motif 1:
Vladimir Putin is connected with Georgia
Georgia is connected with Yury Nikolayevich Baluyevsky
Yury Nikolayevich Baluyevsky is connected with Vladimir Putin
6023 ,  Vladimir Putin, Motif 2:
Vladimir Putin is connected with Georgia
Georgia is connected with Bronislaw Geremek
Bronislaw Geremek is connected with Vladimir Putin)
6023 ,  Vladimir Putin, Motif 3:
Vladimir Putin make a visit, Express intent to meet or negotiate, Consult Yury Nikolayevich Baluyevsky
Yury Nikolayevich Baluyevsky hold a visit Citizen_(Russia)
Citizen (Russia) is connected with Vladimir Putin 

<CODE>
import is_connected_with, make_a_visit, hold_a_visit

def Vladimir_Putin_connected_with(Vladimir_Putin, Georgia, Yury_Nikolayevich_Baluyevsky):
        Vladimir_Putin = is_connected_with(Georgia)
        Georgia = is_connected_with(Yury_Nikolayevich_Baluyevsky)
        Yury_Nikolayevich_Baluyevsky = is_connected_with(Vladimir_Putin)
        return Vladimir_Putin, Georgia, Yury_Nikolayevich_Baluyevsky


def Georgia_connected_with(Vladimir_Putin, Georgia, Bronislaw_Geremek):
        Vladimir_Putin = is_connected_with(Georgia)
        Georgia = is_connected_with(Bronislaw_Geremek)
        Bronislaw_Geremek = is_connected_with(Vladimir_Putin)
        return Vladimir_Putin, Georgia, Bronislaw_Geremek


def Vladimir_Putin_Make_a_visit(Vladimir_Putin, Yury_Nikolayevich_Baluyevsky, Citizen_Russia):
        Vladimir_Putin = make_a_visit(Yury_Nikolayevich_Baluyevsky)
        Vladimir_Putin += Express_intent_to_meet_or_negotiate(Yury_Nikolayevich_Baluyevsky)
        Vladimir_Putin += Consult(Yury_Nikolayevich_Baluyevsky)
        Yury_Nikolayevich_Baluyevsky = hold_a_visit(Citizen_(Russia))
        Citizen_Russia = is_connected_with(Vladimir_Putin)
        return Vladimir_Putin, Yury_Nikolayevich_Baluyevsky, Citizen_Russia

if __name__ == '__main__':
    Vladimir_Putin, Yury_Nikolayevich_Baluyevsky, Citizen_Russia = Vladimir_Putin_Make_a_visit('Vladimir_Putin', 'Yury_Nikolayevich_Baluyevsky', 'Citizen_Russia')
    Vladimir_Putin_connected_with(Vladimir_Putin, 'Georgia', Yury_Nikolayevich_Baluyevsky)

</CODE>
=== Example Ends ===

=== New Task Starts: ===
Given Graph, please generate its code description language.
Given Entity, The triangle motif information is
{}
""".format("""
9483 , Organization for Economic Cooperation and Development , Motif 1:
Austria Express intent to engage in diplomatic cooperation (such as policy support),Express intent to meet or negotiate,Engage in negotiation,Engage in diplomatic cooperation,Meet at a 'third' location Slovenia
Austria connected with Organization for Economic Cooperation and Development
Slovenia Express intent to meet or negotiate Organization for Economic Cooperation and Development
9483 , Organization for Economic Cooperation and Development , Motif 2:
Arab League connected with Vietnam
Arab League Rally opposition against Organization for Economic Cooperation and Development
Vietnam connected with Organization for Economic Cooperation and Development
9483 , Organization for Economic Cooperation and Development , Motif 3:
Lee Myung Bak Make an appeal or request,Express intent to meet or negotiate,Make a visit Canada
Lee Myung Bak Make an appeal or request Organization for Economic Cooperation and Development
Canada connected with Organization for Economic Cooperation and Development
9483 , Organization for Economic Cooperation and Development , Motif 4:
Ethiopia Engage in diplomatic cooperation,Consult,Sign formal agreement,Make a visit,Praise or endorse Canada
Ethiopia connected with Organization for Economic Cooperation and Development
Canada connected with Organization for Economic Cooperation and Development
9483 , Organization for Economic Cooperation and Development , Motif 5:
Ukraine Declare truce, ceasefire,Engage in negotiation,Praise or endorse,Engage in diplomatic cooperation,Consult Lithuania
Ukraine Engage in diplomatic cooperation Organization for Economic Cooperation and Development
Lithuania Engage in negotiation,Engage in diplomatic cooperation,Host a visit Organization for Economic Cooperation and Development
""")
