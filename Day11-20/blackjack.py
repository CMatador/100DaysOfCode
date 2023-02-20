# Day 11 - Blackjack (Expert)

import random
from blackjack_art import logo
from replit import clear

# ############## Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# ############## Our Blackjack House Rules #####################

# # The deck is unlimited in size.
# # There are no jokers.
# # The Jack/Queen/King all count as 10.
# # The the Ace can count as 11 or 1.
# # Use the following list as the deck of cards:
# # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# # The cards in the list have equal probability of being drawn.
# # Cards are not removed from the deck as they are drawn.
# # The computer is the dealer.

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_hand():
    '''Asks user for input to determine whether to start a new hand.'''
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'y':
        play_game = True
        return play_game
    else:
        play_game = False
        return play_game


def deal_card(hand):
    '''Selects a random card and adds it to the specified player's hand.'''
    card = random.choice(cards)
    # Logic for whether an Ace should be 11 or 1
    if card == 11:
        if sum(hand) > 10:
            card = 1
    hand.append(card)
    return hand


def display_hand():
    '''Displays current player hand, score and exposed first card of dealer.'''
    print(f'    Your cards: {player_hand}, current score: {sum(player_hand)}')
    print(f'    Dealer\'s first card: {dealer_hand[0]}')


def final_reveal():
    '''Displays all cards and scores'''
    print(f'    Your final hand: {player_hand}, final score:\
         {sum(player_hand)}')
    print(f'    Dealer\'s first hand: {dealer_hand}, final score:\
          {sum(dealer_hand)}')


play_game = play_hand()

while play_game:
    clear()
    print(logo)
    player_hand = []
    dealer_hand = []
    player_hand = deal_card(player_hand)
    player_hand = deal_card(player_hand)
    dealer_hand = deal_card(dealer_hand)
    dealer_hand = deal_card(dealer_hand)
    dealer_turn = True
    player_turn = True

    if sum(player_hand) == 21 and sum(dealer_hand) == 21:
        final_reveal()
        print('It is a draw.')
        play_game = play_hand()
    elif sum(player_hand) == 21:
        final_reveal()
        print('Blackjack! You win.')
        play_game = play_hand()
    elif sum(dealer_hand) == 21:
        final_reveal()
        print('Dealer Blackjack. You lose.')
        play_game = play_hand()
    else:
        display_hand()
        while player_turn:
            add_card = input("Type 'y' to get another card, type 'n' to pass:")
            if add_card == 'y':
                deal_card(player_hand)
                display_hand()
                if 11 in player_hand and sum(player_hand) > 21:
                    player_hand[player_hand.index(11)] = 1
                if sum(player_hand) > 21:
                    final_reveal()
                    print('You went over. You lose :\'(')
                    player_turn = False
                    play_game = play_hand()
            else:
                player_turn = False

        while dealer_turn:
            if sum(dealer_hand) < 17:
                deal_card(dealer_hand)
                if sum(dealer_hand) > 21 and sum(player_hand) <= 21:
                    final_reveal()
                    print('Dealer went over. You win :)')
                    dealer_turn = False
                    play_game = play_hand()
            else:
                dealer_turn = False

        if sum(player_hand) < 22 and sum(dealer_hand) < 22:
            final_reveal()
            if sum(player_hand) > sum(dealer_hand):
                print('You win')
            elif sum(dealer_hand) > sum(player_hand):
                print('You lose')
            else:
                print('It is a draw.')
            play_game = play_hand()
