import random
from enum import IntEnum


def name():
    """
    Entering a user name and checking its input
    """
    users_name = ""
    while len(users_name.strip()) < 1:
        users_name = input('Please, enter your name:\n')
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
            user_choice = int(input('Please, make your choice:\n'))
            if user_choice not in (range(len(Sample))):
                raise ValueError
            break
        except ValueError:
            print('Input error pleas select from 0, 1, or 2: ')
    return user_choice


def computer_action():
    """
    Function in which computer makes random choice with import randint()
    """
    computer_choice = random.randint(0, len(Sample) - 1)
    return computer_choice


def images(required_choice):  # "hands pictures" from https://hackernoon.com/
    """
    Displaing a picture of a hand after selecting a user and a computer
    """
    if required_choice == 0:
        choice_text = '''ROCK\n
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.(___)
                '''
    if required_choice == 1:
        choice_text = '''PAPER\n
            ______
        ---'  ____)____
                 ______)
                 _______)
                _______)
        ---.__________)'''
    if required_choice == 2:
        choice_text = '''SCISSORS\n
        ______
    ---'  ____)____
             ______)
           _________)
          (____)
    ---.__(___) '''
    return choice_text


def comparison(user_input, computer_input):
    """
    Comparisonof user and computer choices to determine the winner.
    """
    if user_input == computer_input:
        print('It is Draw!')
    elif computer_input == Sample.ROCK:
        if user_input == Sample.PAPER:
            print('Paper wrap rock. You win!')
            user_action_list.append('win')
        else:
            print('Rock brake scissors. Sorry, You lost this round.')
            comp_action_list.append('lose')
    elif computer_input == Sample.PAPER:
        if user_input == Sample.ROCK:
            print('Paper wrap rock. Sorry, You lost this round.')
            comp_action_list.append('lose')
        else:
            print('Scissors cut paper. You win!')
            user_action_list.append('win')
    elif computer_input == Sample.SCISSORS:
        if user_input == Sample.ROCK:
            print('Rock brake scissors. You win!')
            user_action_list.append('win')
        else:
            print('Scissors cut paper. Sorry, You lost this round.')
            comp_action_list.append('lose')


def winner_definition():
    """
    Determination of the winner by comparing lists of elections
    as a result of three games
    """
    text1 = '###############################'
    if len(user_action_list) > len(comp_action_list):        
        text2 = 'Congratulation! You are the winner!'
        text3 = text2.upper()
        print(text1)
        print(text3)
        print(text1)
    elif len(user_action_list) < len(comp_action_list):
        print(text1)
        print('So sorry, at this time luck is not on your side.')
        print(text1)
    elif len(user_action_list) == len(comp_action_list):
        print(text1)
        print('It is Draw!')
        print(text1)


def question():
    """
    Determining whether user wants to continue or end the game
    if continue, start game from the begining.
    """
    play_again = input('Do you want to play again? y/n:\n')
    if play_again.lower() != 'y':
        print('By! Come back when you want to play again!')
    else:
        main()


def main():
    """
    Run all program functions
    """
    print('     ROCK ** PAPER ** SCISSORS\n')
    print('--------------------------------\n')
    user_name = name()
    print(f'Hi, {user_name}, Welcome to our game!\n')
    print('     Remember:\n')
    print('* Rock beats Scissors, loses to paper and ties with rock.\n')
    print('* Paper beats Rock, loses to scissors and ties with paper.\n')
    print('* Scissors beats Paper, loses to rock and ties with scissors.\n')
    for i in range(3):  # [for i in range(3)] code from "cyberforum.ru"
        print(f'{user_name}, make your choice! Enter only relevant number: \n')
        print('    Enter {0}, if your choice is ROCK.\n')
        print('    Enter {1}, if your choice is PAPER.\n')
        print('    Enter {2}, if your choice is SCISSORS.\n')
        u_choice = user_action()
        result = images(u_choice)
        print(f'Your choice is {result}')
        c_choice = computer_action()
        c_result = images(c_choice)
        print(f'Computer choice is {c_result}')
        comparison(u_choice, c_choice)
    winner_definition()
    question()


main()
