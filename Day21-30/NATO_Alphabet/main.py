# Day 26 - NATO Alphabet Translator

import pandas as pd

nato_df = pd.read_csv('Day21-30/NATO_Alphabet/nato_phonetic_alphabet.csv')

nato_dict = {row['letter']: row['code'] for (index, row) in nato_df.iterrows()}

word = input('Enter a word: ').upper()
nato_word = [nato_dict[letter] for letter in word]
print(nato_word)
