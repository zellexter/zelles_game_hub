"""My great game"""

# TODO delay a little bit initial welcome to game msg >>> time.sleep(0.1)
# TODO delay dealing msg, add 'dealing...'
# TODO add print message to specify who busted if so in do_game_result()
# TODO SUBMIT TO GITHUB
# TODO add docstring for major functions
# TODO differentiate private vs public functions
# TODO modulize the code into Class

import random
from termcolor import cprint

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

dealer_choices = None  # set(playing_cards.keys())
player_choices = ['hit','stay']

player_hand = None
bot_hand = None

def reset_deck():
    global dealer_choices, player_hand, bot_hand
    dealer_choices = set(playing_cards.keys())
    player_hand = []
    bot_hand = []
    # dealer_choices without referencing global is just assigning a variable, need to state global


def deal_to_player(): 
    card_delt_to_player = random.choice(list(dealer_choices))
    dealer_choices.remove(card_delt_to_player)
    card_value = playing_cards[card_delt_to_player]
    player_hand.append(card_value)
    print(f'You have been delt {card_delt_to_player}. Your hand is {player_hand}, and you are at {sum(player_hand)}')


def deal_to_bot():
    card_delt_to_bot = random.choice(list(dealer_choices))
    dealer_choices.remove(card_delt_to_bot)
    print("Your opponent's card has been delt.")
    card_value = playing_cards[card_delt_to_bot]
    bot_hand.append(card_value)


def get_user_inputs():
    while True:
        player_input = input('Hit or Stay?\n')
        player_input = player_input.lower()
        print(f'You chose to {player_input}.')
        if player_input not in player_choices:
            print(f'Invalid input {player_input}\n Please try again.')
        else:
            return player_input


def get_bot_input():
    while True:
        if sum(bot_hand) <= 15:
            bot_input = 'hit'
        else:
            bot_input = 'stay'
        print(f'Your opponent chose to {bot_input}.')
        return bot_input
        

# player_input = get_user_inputs()
# bot_input = get_bot_input()

     
def busted():
    return sum(player_hand) > 21 and sum(bot_hand) > 21
    

def both_stay(player_input, bot_input):
    if player_input == 'stay' and bot_input == 'stay':
        return True
    else:
        return False
        

def game_ended(player_input, bot_input):
    if busted() or both_stay(player_input, bot_input):
        do_game_result()
        return True
    return False


def do_game_result():
    player_sum = sum(player_hand)
    bot_sum = sum(bot_hand)

    print(f'You have {sum(player_hand)} ({player_hand}). Your opponent has {sum(bot_hand)} ({bot_hand})')

    if player_sum > 21 and bot_sum > 21:
        winner = 'tie'
    elif player_sum > 21:
        winner = 'bot'
    elif bot_sum > 21:
        winner = 'player'
    elif player_sum == bot_sum:
        winner = 'tie'
    elif player_sum > bot_sum:
        winner = 'player'
    else:
        winner = 'bot'

    if winner == 'player':
        cprint('Congratulations! You won!', 'green')
    elif winner == 'bot':
        cprint('Sorry, you lost! Try again next time.', 'red')
    elif player_sum > 21 and bot_sum > 21:
        print('All players busted. No winner, try again next time.')
    elif player_sum == bot_sum:
        print('You have tied!')



def play_one_game():
    """"""
    reset_deck()
    player_input = bot_input = 'hit'
    deal_to_player()
    deal_to_bot() 
    while not game_ended(player_input, bot_input):
        player_input = get_user_inputs()
        if player_input == 'hit':
            deal_to_player()
        bot_input = get_bot_input()
        if bot_input == 'hit':
            deal_to_bot()

def _print_banner():
    print('Welcome to Blackjack!')

### Creating Player Class
# players = [Player(bot=False), Player(bot=True), Player(bot=False)]
# for player in players:
#     player.input()
        
# Source Control 
# git, github, gitlab
# put source code into a git repo
# git checkin, git checkout, git pull
    

def main():
    """"""
    # banner
    # play_one_game:
    #   reset deck
    #   delt to person player
    #   delt to bot
    #   player choose hit or stay
    #       player choice: hit >> deal to person player
    #       player choice: stay >> move to bot choice
    #   bot chooses to hit or stay << build computer logic function
    #       bot choice: hit >> deal to bot
    #       bot choice: stay >> move to player choice
    #   continue game until a) one player busts or b) both players choose to stay
    #       a) one player busts, other player wins
    #       b) both players stay, player with closest to 21 wins
    #               both players have same value = tie
    # choose to play again?
    #       reset set
    _print_banner()
    var_play_again = 'Y'
    while play_again(var_play_again):
        play_one_game()
        var_play_again = None
    print('Thank you for playing!')

def play_again(var_play_again):
    if var_play_again is None:
        var_play_again = input('Play Again? Y or N\n') 
    return var_play_again.upper() == 'Y'


if __name__ == '__main__':
    main()

