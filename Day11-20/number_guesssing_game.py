# Day 12 - Number Guessing Game

from number_guessing_art import logo
import random

correct = False
number = random.randint(1, 100)

print(logo)
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number betweeen 1 and 100.")

# Select difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    attempts = 0

# Gameplay loop
while not correct and attempts > 0:
    print(f'You have {attempts} attempts remaining to guess the number.')
    guess = int(input('Make a guess: '))

    # Checking guess against number
    if guess == number:
        print(f'You got it! The answer was {number}')
        correct = True
    elif guess > number:
        print('Too high.')
        attempts -= 1
    else:
        print('Too low.')
        attempts -= 1

    if correct == False and attempts > 0:
        print('Guess again.')

# Game end running out of attempts
if attempts == 0:
    print("You've run out of guesses, you lose.")