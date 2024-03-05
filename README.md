# Rock Paper Scissors Game (R-P-S)

## Overview

This is a console based game of rock,  paper, scissors implemented in python. 
The game allows the player to play against the computer by selecting the following options : rock/paper/scissors

## How to Play

1. Run the "run.py" file
2. Follow the instructions to choose your move (rock, paper, or scissors).
3. The computer will randomly select its move.
4. The game will display the result (win, lose, or tie) and update the scores.
5. You can choose to play another round or quit.

### Game Rules 

- Rock smashes Paper
- Paper covers Rock
- Scissors cut Paper


### Helper Functions

In the game logic, the following helper functions are called. 

1. display_rules(): This function displays the rules of the game to the user.

2. get_computer_move(): This function randomly selects a move for the computer player from the list of available moves: rock, paper, or scissors.

3. get_your_move(): This function prompts the user to input their move (rock, paper, or scissors) and validates the input to ensure it is one of the valid options.

4. display_results(computer_move, your_move): This function compares the moves of the computer player and the user player and prints the result of the game: whether it's a tie, the user wins, or the computer wins.

These functions encapsulate specific tasks within the game and help to organize the code by breaking it down into smaller, more manageable parts.

### Edge Cases

1. **Empty Input**: If the player enters nothing when prompted for their move, they will be asked to provide an answer.
2. **Invalid Input**: If the player enters an invalid move (anything other than rock, paper, or scissors), they will be prompted to read the game rules again.
3. **Tie**: If both the player and the computer select the same move, the game will declare a tie.
4. **Case Sensitivity**: Input is case-sensitive. "rock", "Rock", and "ROCK" are considered different inputs.
5. **Quitting**: During the game, if the player enters 'q' when asked if they want to play another round, the game will terminate.
