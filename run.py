import random
from enum import IntEnum


def name():
    """
    Entering a user name and checking its input
    """
    users_name = ""
    while len(users_name.strip()) < 1:
        users_name = input('Please, enter your name: ')
    return users_name


class Action(IntEnum):
    """
    Created a class in which each action is tied to a number,
    to avoid comparison errors.
    """
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


def user_action():
    """
    Accepts a value from the user and
    check it on errors
    """
    while True:
        user_choice = ''
        try:
            user_choice = int(input('Please, make your choice: \n'))
            break
        except ValueError:
            print('Input error pleas select from 0, 1, or 2:\n ')
    return user_choice


def computer_action():
    """
    Function in which computer makes random choice with import randint()
    """
    computer_choice = random.randint(0, len(Action) - 1)
    action = Action(computer_choice)
    return action


def comparison(user_action, computer_action):
    """
    Comparisonof user and computer choices to determine the winner.
    """
    if user_action == computer_action:
        print('Draw')
    elif computer_action == Action.ROCK:
        if user_action == Action.PAPER:
            print('Paper wrap rock. You win!')
        else:
            print('Rock brake scissors. You lose.')
    elif computer_action == Action.PAPER:
        if user_action == Action.ROCK:
            print('Paper wrap rock. You lose.')
        else:
            print('Scissors cut paper. You win!')        
    elif computer_action == Action.SCISSORS:
        if user_action == Action.ROCK:
            print('Rock brake scissors. You win!')
        else:
            print('Scissors cut paper. You lose.')      


def main():
    """
    Run all program functions
    """
    print('     Rock Paper Scissors\n')
    print('--------------------------------\n')
    user_name = name()    
    print(f'Hi, {user_name}, Welcome to our game!\n')
    print('     Remember:\n')
    print('* Rock wins against scissors.\n')
    print('* Scissors win against paper.\n')
    print('* Paper wins against rock.\n')
    print(f'{user_name}, make your choise! Enter only relevant numbers: \n')
    print('ROCK___[0], PAPER___[1], SCISSORS___[2].\n')
    u_choice = user_action()
    print(f'Your choice is {u_choice}')
    c_choice = computer_action()
    comparison(u_choice, c_choice)


main()
