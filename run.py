# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

"""
The command to import random module for functions
"""


def display_rules():
    rules = ("Hi There, Game rules are: Rock smashes scissors, Paper covers "
             "rock & Scissors cut paper")
    print(rules)


def get_computer_move():
    """
    This function randomly selects a value from this list
    """
    computer_move = random.choice(['rock', 'paper', 'scissors'])
    return computer_move


def get_your_move():
    """
    This function will ask user for an input and validate
    """
    while True:
        your_move = input("Choose between rock, paper or scissors:\n").lower()
        options = ["rock", "paper", "scissors"]

        if not your_move:
            print("No answer given, please give an answer")
        elif your_move not in options:
            print("Invalid answer, please read the game rules again")
        else:
            return your_move


def display_results(computer_move, your_move):
    if your_move == computer_move:
        print("Its a tie")
    elif ((your_move == "rock" and computer_move == "scissors") or
          (your_move == "paper" and computer_move == "rock") or
          (your_move == "scissors" and computer_move == "paper")):
        print(f"Congratulations, you win! {your_move.capitalize()} beats "
              f"{computer_move.capitalize()}")
    else:
        print(f"You lost! {computer_move.capitalize()} beats "
              f"{your_move.capitalize()}")


def game_flow():
    """
    This function executes the game flow and includes helper functions
    """
    display_rules()

    opponent_move = get_computer_move()

    player_move = get_your_move()

    display_results(opponent_move, player_move)

    return opponent_move, player_move


def main():
    """
    This function keeps track of scores
    """

    # Initialisation of scores
    computer_wins = 0
    player_wins = 0
    tie_score = 0

    # Starting game loop
    while True:
        opponent_move, player_move = game_flow()

        # Updating scores
        if opponent_move == player_move:
            tie_score += 1
            print(f"Computer selected {opponent_move.capitalize()}\n")
        elif ((player_move == "rock" and opponent_move == "scissors") or
              (player_move == "paper" and opponent_move == "rock") or
              (player_move == "scissors" and opponent_move == "paper")):
            player_wins += 1
            print(f"Computer selected {opponent_move.capitalize()}\n")
        else:
            computer_wins += 1
            print(f"Computer selected {opponent_move.capitalize()}\n")

        # Displaying results
        print(f"\nScores - Computer: {computer_wins}, Player: {player_wins}, "
              f"Tie: {tie_score}\n")

        # Asking if player wants to play again
        wanna_play_again = input("Enter any key to play another round or press "
                                 "q to quit\n")
        if wanna_play_again == 'q':
            print("Thanks for playing, Goodbye!")
            break


main()
