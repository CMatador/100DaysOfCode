# Day 14 - Higher Lower Game

import random
from replit import clear
from higher_lower_art import logo, vs
from higher_lower_data import data


def select_choices(a, b):
    '''Moves choice B into choice A, picks a random choice B while checking to
    make sure they are not equal.'''
    a = b
    b = data[random.randint(0, len(data) - 1)]
    while a == b:
        b = data[random.randint(0, len(data) - 1)]
    return a, b


def compare_display():
    '''Displays the choices to pick from and current score'''
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from \
          {choice_a['country']}.")
    print(vs)
    print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from \
          {choice_b['country']}.")


def compare_followers(player_choice, score):
    '''Game logic for determining if player choice is higher or lower than the
    other option'''
    if player_choice == 'a':
        if choice_a['follower_count'] > choice_b['follower_count']:
            score += 1
            game_over = False
            return game_over, score
        else:
            game_over = True
            return game_over, score
    elif player_choice == 'b':
        if choice_b['follower_count'] > choice_a['follower_count']:
            score += 1
            game_over = False
            return game_over, score
        else:
            game_over = True
            return game_over, score
    else:
        game_over = True
        return game_over, score


# Initial variables
score = 0
game_over = False
choice_a = {}
choice_b = data[random.randint(0, len(data) - 1)]

# Gameplay loop while player guesses correctly
while not game_over:
    clear()
    choice_a, choice_b = select_choices(choice_a, choice_b)
    compare_display()
    player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    game_over, score = compare_followers(player_choice, score)

# Game End
clear()
print(logo)
print(f"Sorry, that's wrong. Final Score: {score}")
