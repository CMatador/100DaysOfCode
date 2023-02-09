# Day 4 - Rock, Paper, Scissors Game

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____0
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

# Gathers players choice by input and computer's choice by random
player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n'))
computer_choice = random.randint(0,2)

# Game Logic
if player_choice == 0:
    print(rock + '\n')
    print('Computer chose:')
    if computer_choice == 0:
        print(rock + '\nRock ties Rock.')
    elif computer_choice == 1:
        print(paper + '\nPaper beats Rock. You Lose.')
    else:
        print(scissors + '\nRock beats Scissors. You Win.')
elif player_choice == 1:
    print(paper + '\n')
    print('Computer chose:')
    if computer_choice == 0:
        print(rock + '\nPaper beats Rock. You Win.')
    elif computer_choice == 1:
        print(paper + '\nPaper ties Paper.')
    else:
        print(scissors + '\nScissors beat Paper. You Lose.')
elif player_choice == 2:
    print(scissors + '\n')
    print('Computer chose:')
    if computer_choice == 0:
        print(rock + '\nRock beats Scissors. You Lose.')
    elif computer_choice == 1:
        print(paper + '\nScissors beats Paper. You Win.')
    else:
        print(scissors + '\nScissors ties Scissors.')
else:
    print('Invalid selection, please try again.')