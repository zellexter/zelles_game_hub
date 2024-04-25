"""ROCK, PAPER, SCISSORS"""

import random
from termcolor import cprint


choices = ['rock', 'paper', 'scissors']


def get_user_inputs():
    """Player Input"""
    while True:
        player_input = input('Please type rock, paper, or scissors:\n')
        player_input = player_input.lower()
        print(f'You chose {player_input}')
        if player_input not in choices:
            print(f'Invalid input {player_input}\nPlease try again')
        else:
            return player_input

def get_computer_input():
    """Computer Input"""
    possible_choices = choices
    computer_input = random.choice(possible_choices)
    computer_input = computer_input.lower()
    print(f'Your opponent chose {computer_input}')

    return computer_input


### Win/Lose
lose = dict(text='You lose!', color='red')
win =  dict(text='You win!', color='green')
tie = dict(text="It's a tie!")

### Dictionary of Rules
rule_map = {
    ('rock', 'rock'): tie,
    ('rock', 'scissors'): win,
    ('rock', 'paper'): lose,
    ('scissors', 'rock'): lose,
    ('scissors', 'scissors'): tie,
    ('scissors', 'paper'): win,
    ('paper', 'rock'): win,
    ('paper', 'scissors'): lose,
    ('paper', 'paper'): tie
    }

### Rules                 

def play_once_v2():
    """RPS game engine V2"""
    player_input = get_user_inputs()
    computer_input = get_computer_input()
    result = rule_map.get((player_input, computer_input))
    cprint(**result)


def play_once():
    """RPS game engine"""
    player_input = get_user_inputs()
    computer_input = get_computer_input() # scope, need to assign variables again because they are unique to each function and do not exist outside of their respective functions

    if computer_input == player_input:
        cprint(**tie)
    elif computer_input == 'rock' and player_input == 'scissors':
        cprint(**lose)  # * expand tuple, ** expand dict
    elif computer_input == 'rock' and player_input == 'paper':
        cprint(**win)
    elif computer_input == 'scissors' and player_input == 'rock':
        cprint(**win)
    elif computer_input == 'scissors' and player_input == 'paper':
        cprint(**lose)
    elif computer_input == 'paper' and player_input == 'rock':
        cprint(**lose)
    elif computer_input == 'paper' and player_input == 'scissors':
        cprint(**win)
    else:
        print('Please try again. Fully spell your option')


def _print_banner():
    print('Welcome to Rock Paper Scissors!')


def main():
    _print_banner()
    play_again = 'Y'
    while True:
        if play_again == 'Y':
            # rerun loop
            play_once_v2()
        elif play_again == 'N':
            # close game
            break
        else:
            print(f'invalid input {play_again}')

        play_again = input('Play Again? Y or N\n') # can create as function instead of typing every time
        play_again = play_again.upper()

    print('Thank you for playing!')


if __name__ == '__main__':
    main()
