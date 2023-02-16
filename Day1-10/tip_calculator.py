# Day 2 - Tip Calculator
print('Welcome to the tip calculator.')
bill = input('What was the total bill? $')
tip = int(input('What percentage tip would you like to give? ')) / 100
people = input('How many people to split the bill? ')

bill = float(bill)
total = bill * (1 + tip)
amount_per_person = round(total / int(people), 2)

print(f'Each person should pay: ${amount_per_person}')