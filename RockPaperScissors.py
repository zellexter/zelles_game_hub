"""ROCK, PAPER, SCISSORS"""

import random
from termcolor import cprint

class GameBase:
    choices = []
    name = "Base"

    ### Win/Lose
    lose = dict(text='You lose!', color='red')
    win =  dict(text='You win!', color='green')
    tie = dict(text="It's a tie!")

    def play_once(self):
        raise NotImplementedError

    def _print_banner(self):
        print(f'Welcome to {self.name}!')

    def get_user_inputs(self):
        """Player Input"""
        while True:
            player_input = input(f'Please choose from {self.choices}.\n')
            player_input = player_input.lower()
            print(f'You chose {player_input}')
            if player_input not in self.choices:
                print(f'Invalid input {player_input}\nPlease try again')
            else:
                return player_input

    def get_computer_input(self):
        """Computer Input"""
        possible_choices = self.choices
        computer_input = random.choice(possible_choices)
        computer_input = computer_input.lower()
        print(f'Your opponent chose {computer_input}')

        return computer_input


class RockPaperScissors(GameBase):
    choices = ['rock', 'paper', 'scissors']
    name = 'Rock Paper Scissors'

    def play_once(self):
        """GenericRPS game engine:
        Result is based on the order of which choices are.
        Element beats immediately preceding element.
        First element beats last element.
        """

        player_input = self.get_user_inputs()
        computer_input = self.get_computer_input()

        p_idx = self.choices.index(player_input)
        c_idx = self.choices.index(computer_input)
        
        if p_idx - c_idx == 1:
            result = self.win
        elif p_idx - c_idx == -1:
            result = self.lose
        elif p_idx == c_idx:
            result = self.tie
        elif p_idx == 0 and c_idx == (len(self.choices) - 1):
            result = self.win
        elif c_idx == 0 and p_idx == (len(self.choices) - 1):
            result = self.lose
        else:
            result = self.tie

        cprint(**result)  # cprint(text=?, color=?)

    def main(self):
        self._print_banner()
        play_again = 'Y'
        while True:
            if play_again == 'Y':
                # rerun loop
                self.play_once()
            elif play_again == 'N':
                # close game
                break
            else:
                print(f'invalid input {play_again}')

            play_again = input('Play Again? Y or N\n') # can create as function instead of typing every time
            play_again = play_again.upper()

        print('Thank you for playing!')


class TigerStickChicken(RockPaperScissors):
    choices = ['tiger', 'stick', 'chicken']
    name = 'Tiger Stick Chicken'


class GenericRPS(RockPaperScissors):
    choices = ['1','2','3','4'] #win/lose defined by order of choices in choices
    name = 'GenericRPS'
    

if __name__ == '__main__':
    game = RockPaperScissors()
    game.main()
