# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random 
"""
The command to import random module for functions
"""

def display_rules():
    rules = """

    Hi There! 

    Game rules are :
    
    - Rock smashes scissors 
    - Paper covers rock
    - Scissors cut paper.

    """
    

def get_computer_move():
    """
    This function randomly selects a value from this list
    """
    computer_move = random.choice(['rock','paper','scissors '])    
    return computer_move


