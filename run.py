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


class Sample(IntEnum):
    """
    Created a class in which each action is tied to a number,
    to avoid comparison errors.
    """
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


user_action_list = []
comp_action_list = []


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
    computer_choice = random.randint(0, len(Sample) - 1)
    return computer_choice


def comparison(user_action, computer_action):
    """
    Comparisonof user and computer choices to determine the winner.
    """
    if user_action == computer_action:
        print('It is Draw!')
    elif computer_action == Sample.ROCK:
        if user_action == Sample.PAPER:
            print('Paper wrap rock. You win!')
            user_action_list.append('win')
        else:
            print('Rock brake scissors. You lose.')
            comp_action_list.append('lose')
    elif computer_action == Sample.PAPER:
        if user_action == Sample.ROCK:
            print('Paper wrap rock. You lose.')
            comp_action_list.append('lose')
        else:
            print('Scissors cut paper. You win!')
            user_action_list.append('win')
    elif computer_action == Sample.SCISSORS:
        if user_action == Sample.ROCK:
            print('Rock brake scissors. You win!')
            user_action_list.append('win')
        else:
            print('Scissors cut paper. You lose.')
            comp_action_list.append('lose')


def winner_definition():
    """
    Determination of the winner by comparing lists of elections
    as a result of three games
    """
    if len(user_action_list) > len(comp_action_list):
        print('Congratilation! You are WINNER!')
    elif len(user_action_list) < len(comp_action_list):
        print('So sorry, this time luck is not on your side.')
    elif len(user_action_list) == len(comp_action_list):
        print('It is Draw!')


def question():
    """
    Determining whether user wants to continue or end the game
    if continue, start game from the begining.
    """
    play_again = input('Do you want to play again? y/n: ')
    if play_again.lower() != 'y':
        print('By! Come back when you want to play again!')
    else:
        main()


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
    for i in range(3):  # [for i in range(3)] code from "cyberforum.ru"
        print(f'{user_name}, make your choise! Enter only relevant numbers: ')
        print('ROCK___[0], PAPER___[1], SCISSORS___[2].\n')
        u_choice = user_action()
        print(f'Your choice is {u_choice}')
        c_choice = computer_action()
        comparison(u_choice, c_choice)
        print(comp_action_list)  # del
        print(user_action_list)  # del
    winner_definition()
    question()


main()
