"""GAME MENU"""

#DONE at the end of the game, if they chose not to play again, return to game menu
#TODO add time buffer and 'game loading...' to after game is chosen
#TODO print f string you have chosen X game

from RockPaperScissors import main as rps_main
from Blackjack import main as bj_main

menu_options = [
    'Exit',
    'Rock, Paper, Scissors',
    'Blackjack',
]

def _print_banner():
    """opening statements"""
    print("Welcome to Zelle's GameHub, a collection of games that Zelle coded as her introduction project to Python.\n"
          "The following games are available to play:\n")
    for idx, option in enumerate(menu_options):
        print(f'({idx}) {option}')

def main():
    """MAIN FUNCTION:
        prints welcoming banner and prompts user to choose a game"""
    while True:
        _print_banner()
        game = choice_of_game()
        if game is None:
            return
        game()


def choice_of_game():
    """User input of which game they want to play"""
    game_choice = input('\nPlease type the number that corresponds to the game you want to play.\n')
    if game_choice == '0':
        return None
    idx = int(game_choice)
    game_choice = menu_options[idx]

    if game_choice == 'Rock, Paper, Scissors': 
        # print(f'You have chosen {}')
        return rps_main
    elif game_choice == 'Blackjack':
        return bj_main
    

if __name__ == '__main__':
    main()
