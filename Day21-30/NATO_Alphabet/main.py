# Day 26 - NATO Alphabet Translator

import pandas as pd

nato_df = pd.read_csv('Day21-30/NATO_Alphabet/nato_phonetic_alphabet.csv')
nato_dict = {row['letter']: row['code'] for (index, row) in nato_df.iterrows()}
valid = True

while valid:
    word = input('Enter a word: ').upper()
    try:
        nato_word = [nato_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
    else:
        print(nato_word)
        valid = False
