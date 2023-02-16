

def name():
    """
    Entering a user name and checking its input
    """

    users_name = ""
    while len(users_name.strip()) < 1:
        users_name = input('Please, enter your name: ')
    return users_name


def main():
    """
    Run all program functions  
    """
    print('     Rock Paper Scissors\n')
    print('--------------------------------\n')
    user_name = name()    
    print(f'Hi, {user_name}, Welcome to our game!\n')
    print('You need to make your choice - Rock, paper, or scissors.\n')
    print('     Remember:\n')
    print('* Rock wins against scissors.\n')
    print('* Scissors win against paper.\n')
    print('* Paper wins against rock.\n')
    print('Lets play!\n')


main()