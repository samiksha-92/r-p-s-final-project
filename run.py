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


def get_your_move():
    """
    This function will ask user for an input and validate if the input is valid.
    """
    while True:
        your_move = input("Choose between rock, paper or scissors")
        list = ["rock","paper","scissors"]

        if not your_move:
            print("Invalid answer, please give an answer")
        elif your_move not in list:
            print("Invalid answer, please read the game rules again")
        else:
            return your_move    

def validate_moves (your_move,computer_move):
    """
    This function validates moves fo both computer and user.
    """
    list_1 = ["rock","paper","scissors"]
    if your_move not in list_1 or computer_move not in list_1:
        raise ValueError('Invalid input')

def display_results(your_move,computer_move):
    result = ""
    
    if your_move ==computer_move:
        print("It's a tie")
    elif (your_move == "rock" and computer_move == "scissors") or (your_move == "paper" and computer_move == "rock") or  elif(your_move == "scissors" and computer_move == "paper"):
        result = f"Congratulations, you win! {your_move.capitalize()} beats {computer_move.capitalize()}"
    else:
        result = f"Oops,You lost! {computer_move.capitalize()} beats {your_move.capitalize()}"

    return result
    print(result)


def game_flow():
    """
    This function executes the game flow and includes helper functions declared above
    """

    display_rules()

    Opponent_move = get_computer_move()

    player_move = get_your_move()

    validate_moves(Opponent_move,player_move)

    display_results(Opponent_move,player_move)

    return Opponent_move, player_move


def main():
    """
    This function keeps track of scores
    """

    #Initialisation of scores

    computer_wins = 0
    player_wins = 0
    tie_score = 0    


    



    




