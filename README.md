# ROCK PAPER SCISSORS

Rock, Paper, Scissors is an old game known all over the world, which is implemented as a Python terminal game.

User can try their luck in the game with the computer. The player has three rounds in which he chooses his item without knowing what the computer will choose. In the end, the program determines the winner.

Below is an image, of how the game looks on different screens:

![Screen photo](/Images/laptop-frame-gray_!.png)

## Gaming  rules

More detailed rules of the game, the user can learn on [Wikipedia](https://en.wikipedia.org/wiki/Rock_paper_scissors) or [wrpsa.com](https://wrpsa.com/the-official-rules-of-rock-paper-scissors/).

This online game has three rounds, where the user has to choose one of three items: rock, paper or scissors.

* Rock breaks scissors;
* Scissors cut paper;
* Paper wraps rock.

Then the computer makes a random selection and displays the user's and its own selections.

Rock:

```
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.(___)
                 
```

Paper:

```
            ______
        ---'  ____)____
                 ______)
                 _______)
                _______)
        ---.__________)
```

Scissors:

```
        ______
    ---'  ____)____
             ______)
           _________)
          (____)
    ---.__(___)
```                                                                                                      

The program compares its own choice, the user's choice, and determines the winner of one round.
After the third cycle, it is determined the winner of the game. It can also be a draw.

The screen prompts whether the user again wants to play in this game or exit it.
## Features

### Existing Features

1. The game starts with a username request.

    * the player must enter at least one character otherwise the request will be repeated.

![1](/Images/photoRM1.jpg)

2. After describing the gaming rules, the program prompts the user for his choice: rock, paper, or scissors. Gamer cannot see the computer's selection in advance.

I have decided to use IntEnum class, where I tied a number to each action. It helped to avoid Validation Errors when entering the word(choice) incorrectly (otherwise, the user would need to enter the exact correct text, without grammatical errors, in small or capital letters).
Now the user can enter a number corresponding to the value of his choice.

![2](/Images/photoRM2.jpg)

3. Program check input validation:
    * User cannot enter numbers outside the indicated range;
    * User must enter only numbers, but not string.

![3](/Images/photoRM3.jpg)

![4](/Images/photoRM4.jpg)

4. There are three cycles in the game. After each of them, an image of the user's choice and the choice of the computer that it makes using the ```random``` function is displayed on the screen. 

![5](/Images/photoRM6.jpg)

5. After the third gaming cycle program defines the winner and gives a request to continue the game or exit from it.

![6](/Images/photoRM7.jpg)

### Future Features

In the future, I plan to add more items to choose from.

## Testing

* As a result of checking the code in PEP8 linter, no errors were returned.
* Checking in manual mode by entering an incorrect data format:
    - a string when you need to enter numbers;
    - a value in an unspecified range.
* Throughout the creation of the game, I constantly used the ```print``` function to check the correctness of the code.
* Tested in my local terminal and the Code Institute Heroku terminal.
* Tested by independant user to look for any gaps found by self testing unintentional bias.

## Bugs

There was a warning in my ```comparison``` function: " ``` redefining name 'user_action, computer_action' from outer scope``` "because I assigned the names of other functions as an argument, which could lead to an error when using the program in the future. It has been fixed by giving other completely new names to the function's arguments.

## Deployment

I deployed the "Rock, Paper, Scissors" project using Code Institute's mock terminal for Heroku.

- Create a new Heroku app;
- Put project name and choose Europe as my region;
- Set the build-backs to 'Python' and 'Node JS' in that order;
- Link the Heroku app to the required repository;
- Click on 'Deploy'.

## Credits

1. Code Institute for the deployment terminal
2. Wikipedia and wrpsa.com for the gaming rules
3. [hackernoon.com](https://hackernoon.com/) and [cyberforum.ru](https://cyberforum.ru/) for Python code
4. [lucid.app](https://lucid.app/) to create a program flow chart

