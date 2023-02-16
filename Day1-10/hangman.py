# Day 7 - Hangman

import random
from hangman_art import stages, logo
from hangman_words import word_list

# Game setup
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
guesses = []
print(logo)

# Initial display
display = []
for i in range(word_length):
    display.append('_')
print(display)
print(stages[lives])

# Gameplay loop
while '_' in display and lives > 0:
    guess = input('Guess a letter: ').lower()

    if guess in guesses:
        print(f'You\'ve already guessed {guess}, Try again.')
    elif guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        print(f'Sorry, {guess} is not in the word.')
        lives -= 1
        
    print(display)
    print(stages[lives])
    guesses.append(guess)

# Game end
if lives > 0:
    print('You win.')
else:
    print('You lose.')