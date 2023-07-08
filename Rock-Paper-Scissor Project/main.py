# Import Random Module To make random index for pc choice
import random

# The starting title of the game
title = "\t\t\tWelcome in R_P_S Game\t\t\t\n\n"

# user input words
showing_words = """
Choose : (r)Rock - (p)Paper - (s)Scissor\n
Enter Your choice : 
"""

score_of_end = "Enter the score that you need to end the game on it :"

# the game choices ==> r --> rock, p --> paper, s --> scissor
game_list = ["r", "p", "s"]

# the scores of game
# score1 --> user score , score2 --> pc score
score1 = 0
score2 = 0

# to make random choice for the pc
def make_random_pc_choice():
    pc_random_choice = random.randint(0, 2)
    return game_list[pc_random_choice]


# take the input from user and validate it
def take_input():
    while True:
        user_choice = input(showing_words)
        if user_choice not in game_list:
            print("Invalid Choice, NOTE : the Valid Choices is [r, p, s]")
        else:
            return user_choice


# check the winner in the round to increase the score, and have the rules of the game
def check_round_winner(user_choice, pc_choice):
    if user_choice == pc_choice:
        return 0
    elif user_choice == "r" and pc_choice == "p":
        return 2
    elif user_choice == "r" and pc_choice == "s":
        return 1
    elif user_choice == "p" and pc_choice == "r":
        return 1
    elif user_choice == "p" and pc_choice == "s":
        return 2
    elif user_choice == "s" and pc_choice == "r":
        return 2
    elif user_choice == "s" and pc_choice == "p":
        return 1


# calculate the score of the game based on game score that take from user in start of game
def calc_score(user_score, pc_score, game_score):
    if user_score > pc_score and user_score == game_score:
        return 1
    elif pc_score > user_score and pc_score == game_score:
        return 2
    elif user_score > pc_score and user_score < game_score:
        return 0
    elif pc_score > user_score and pc_score < game_score:
        return 0


# it show the current state of game
def view_state(score):
    if score == 1:
        return "User Win"
    elif score == 2:
        return "PC Win"
    else:
        return "Still Playing"


# this is to run the file directly
if __name__ == "__main__":
    # Show the title
    print(title)

    # take score of game from user
    game_score = int(input(score_of_end))

    # make it while true to still going on until end of game
    while True:

        # take user choice
        user_input = take_input()

        # make random choice for pc to be fair enough
        pc_input = make_random_pc_choice()

        # check who win the round or tie between them
        check = check_round_winner(user_input, pc_input)

        # print the choices of user and pc to check the game current state
        print(f"You Played : {user_input}")
        print(f"Pc Played : {pc_input}")

        # increase the score of user or pc
        if check == 1:
            score1 += 1
        elif check == 2:
            score2 += 1

        # print the score on screen
        print(f"User Score = {score1}\t\tPc Score = {score2}")

        # calculate if any one win the whole game
        score = calc_score(score1, score2, game_score)

        # to check the state of game
        state = view_state(score)

        # End or Still going the game
        if state == "User Win":
            print("User Win")
            break
        elif state == "PC Win":
            print("PC Win")
            break
        else:
            print("Still Tie")
            continue
