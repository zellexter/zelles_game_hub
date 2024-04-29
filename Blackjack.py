"""BLACKJACK"""

# TODO modulize the code into Class
# TODO ERROR LINE 158: function takes 1 positioanl argument but 2 were given
# DONE GET_USER_INPUTS() : when player input was previously stay, else should not run again. the assumed player_input should be 'stay'. cant make an if statement with player_input as a condition (scope)
# DONE delay a little bit initial welcome to game msg >>> time.sleep(0.1)
# DONE delay dealing msg, add 'dealing...'
# DONE add print message to specify who busted if so in do_game_result()
# DONE SUBMIT TO GITHUB
# DONE add docstring for major functions
# DONE differentiate private vs public functions

### Creating Player Class
# players = [Player(bot=False), Player(bot=True), Player(bot=False)]
# for player in players:
#     player.input()
# TODO create for loop for player turns? only if multiple user players

import random
from termcolor import cprint
import time

class GameBase:
    player_choices = []
    name = 'Base'

    player_hand = None
    bot_hand = None
    dealer_choices = None  # set(playing_cards.keys())

    target_sum = None

    ### Deck of Cards
    playing_cards = { # {Card:Value}
        'A of Spades':1, 
        '2 of Spades':2,
        '3 of Spades':3,
        '4 of Spades':4,
        '5 of Spades':5,
        '6 of Spades':6,
        '7 of Spades':7,
        '8 of Spades':8,
        '9 of Spades':9,
        '10 of Spades':10,
        'J of Spades':10,
        'Q of Spades':10,
        'K of Spades':10,
        
        'A of Clubs':1, 
        '2 of Clubs':2,
        '3 of Clubs':3,
        '4 of Clubs':4,
        '5 of Clubs':5,
        '6 of Clubs':6,
        '7 of Clubs':7,
        '8 of Clubs':8,
        '9 of Clubs':9,
        '10 of Clubs':10,
        'J of Clubs':10,
        'Q of Clubs':10,
        'K of Clubs':10,
        
        'A of Diamonds':1, 
        '2 of Diamonds':2,
        '3 of Diamonds':3,
        '4 of Diamonds':4,
        '5 of Diamonds':5,
        '6 of Diamonds':6,
        '7 of Diamonds':7,
        '8 of Diamonds':8,
        '9 of Diamonds':9,
        '10 of Diamonds':10,
        'J of Diamonds':10,
        'Q of Diamonds':10,
        'K of Diamonds':10,
        
        'A of Hearts':1, 
        '2 of Hearts':2,
        '3 of Hearts':3,
        '4 of Hearts':4,
        '5 of Hearts':5,
        '6 of Hearts':6,
        '7 of Hearts':7,
        '8 of Hearts':8,
        '9 of Hearts':9,
        '10 of Hearts':10,
        'J of Hearts':10,
        'Q of Hearts':10,
        'K of Hearts':10,
    }

    def _stagger_msg(message):
        cprint(message, 'dark_grey', end='')
        for _i in range(5):
            cprint('.', 'dark_grey', end='', flush=True)
            time.sleep(0.5)
        print()

    def _print_banner(self):
        print(f'Welcome to {self.name}!')

    def reset_deck(self):
        """Resets dealer_choices to a set containing all cards from deck.
        Resets all players' hands to empty.
        """
        global dealer_choices, player_hand, bot_hand
        dealer_choices = set(GameBase.playing_cards.keys())
        player_hand = []
        bot_hand = []
        # dealer_choices without referencing global is just assigning a variable, need to state global


class Blackjack(GameBase):
    player_choices = ['hit','stay']
    name = 'Blackjack'

    target_sum = 21

    def play_one_game(self):
        """Playthrough of one game, resets the deck and sets both player and bot input to hit for initial input.
        Deals to player and bot so long as the game has not ended (either by bust or stay decision)
        """
        self._stagger_msg('Shuffling the deck')
        self.reset_deck()
        player_input = bot_input = 'hit'
        Dealer.deal_to_player()
        Dealer.deal_to_bot() 
        while not self.game_ended(player_input, bot_input):
            if player_input != 'stay':
                player_input = Player.get_user_inputs()
                if player_input == 'hit':
                    Dealer.deal_to_player()
            bot_input = Player.get_bot_input()
            if bot_input == 'hit':
                Dealer.deal_to_bot()

    def main(self):
        """MAIN FUNCTION:
            _print_banner(): welcomes players to game
            var_play_again is set to Y as default
            while play_again is True, we run play_one_game
            play_one_game:
                reset_deck(): reset the deck
                deal_to_player(): deal to person player
                deal_to_bot(): deal to bot
                get_user_inputs(): player input (hit or stay)
                    player choice: hit >> deal to person player
                    player choice: stay >> move to bot choice
                get_bot_input(): bot chooses to hit or stay << build computer logic function
                    bot choice: hit >> deal to bot
                    bot choice: stay >> move to player choice
                continue game until game_ended():
                    a) busted(): one player busts >> other player wins
                    b) both_stay(): both players stay >> player with closest to 21 wins OR both players have same value = tie
            play_again(): choose to play again?
        """
        self._print_banner()
        var_play_again = 'Y'
        while self.play_again(var_play_again): #TODO ERROR: function takes 1 positioanl argument but 2 were given
            self.play_one_game()
            self.var_play_again = None
        print('Thank you for playing!')

    def play_again(var_play_again):
        """At the end of the game, player can choose to continue the game or stop.
        The function's input is defaulted to Y at the beginning of main().
        In main() after a playthrough happens, var_play_again is set to None.
        play_again() will run when the player's input is Y.
        """
        if var_play_again is None:
            var_play_again = input('Play Again? Y or N\n') 
        return var_play_again.upper() == 'Y'

    def do_game_result(self):
        """Reveals all players hands and reveals game result (winner/loser)
        by running result through parameters for win/lose
        """
        player_sum = sum(player_hand)
        bot_sum = sum(bot_hand)

        print(f'You had {sum(player_hand)} {player_hand}. Your opponent had {sum(bot_hand)} {bot_hand}')

        if player_sum > self.target_sum and bot_sum > self.target_sum:
            result = 'tie'
            print(f'All players busted and the result is a {result}. No winner, try again next time.')
        elif player_sum > self.target_sum:
            result = 'Bot'
            cprint(f'Sorry, you busted at {player_sum}! {result} wins! Try again next time.', 'red')
        elif bot_sum > self.target_sum:
            result = 'Player'
            cprint(f'Congratulations! Your opponent busted at {bot_sum}. {result} won!', 'green')
        elif player_sum == bot_sum:
            result = 'tie'
            print(f'The result is a {result}. You have tied {player_sum} to {bot_sum}')
        elif player_sum > bot_sum:
            result = 'Player'
            cprint(f'Congratulations! {result} won with {player_sum}!', 'green')
        else:
            result = 'Bot'
            cprint(f'Sorry, you lost! The winner is {result}, try again next time.', 'red')

    def busted(self):
        """Determines if all players have bust"""
        return sum(player_hand) > self.target_sum and sum(bot_hand) > self.target_sum

    def both_stay(player_input, bot_input):
        """Determines if all players input is stay"""
        if player_input == 'stay' and bot_input == 'stay':
            return True
        else:
            return False
        
    def game_ended(player_input, bot_input):
        """Game ended when both players bust or all players stay"""
        if Blackjack.busted() or Blackjack.both_stay(player_input, bot_input):
            Blackjack.do_game_result()
            return True
        return False

class Dealer:
    # GameBase._stagger_msg(f'Dealing to {}') #variable for player in current turn

    def deal_to_player(self): 
        """Dealing to Player"""
        GameBase._stagger_msg('Dealing to player')
        card_delt_to_player = random.choice(list(dealer_choices))
        dealer_choices.remove(card_delt_to_player)
        card_value = GameBase.playing_cards[card_delt_to_player]
        player_hand.append(card_value)
        print(f'You have been delt {card_delt_to_player}. Your hand is {player_hand}, and you are at {sum(player_hand)}')
        if sum(player_hand) > self.target_sum:
            cprint(f'You have busted ({sum(player_hand)})', 'red')

    def deal_to_bot(self):
        """Dealing to Bot"""
        GameBase._stagger_msg('Dealing to bot')
        card_delt_to_bot = random.choice(list(dealer_choices))
        dealer_choices.remove(card_delt_to_bot)
        print("Your opponent's card has been delt.")
        card_value = GameBase.playing_cards[card_delt_to_bot]
        bot_hand.append(card_value)
        
class Player:
    def get_user_inputs(self):
        """Player Input from terminal"""
        while True:
            if sum(player_hand) > self.target_sum: #check if player hand is bust
                player_input = 'stay'
                return player_input
            else:
                player_input = input('Hit or Stay?\n')
                player_input = player_input.lower()
                cprint(f'You chose to {player_input}.', 'dark_grey')
                if player_input not in Blackjack.player_choices:
                    print(f'Invalid input {player_input}\n Please try again.')
                else:
                    return player_input

    def get_bot_input(self):
        """Bot Input, created simple logic for computing decision to stay or hit"""
        while True:
            if sum(bot_hand) <= (self.target_sum - 5):
                bot_input = 'hit'
            else:
                bot_input = 'stay'
            cprint(f'Your opponent chose to {bot_input}.', 'dark_grey')
            return bot_input
        
     


if __name__ == '__main__':
    game = Blackjack()
    game.main()

