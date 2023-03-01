# Day 24 - Mail Merge Challenge

starting_letter_path = \
    'Day21-30/Mail Merge Project Start/Input/Letters/starting_letter.txt'
invited_names_path = \
    'Day21-30/Mail Merge Project Start/Input/Names/invited_names.txt'
ready_to_send_path = \
    'Day21-30/Mail Merge Project Start/Output/ReadyToSend'


with open(invited_names_path) as invites:
    invite_list = invites.readlines()
    for i in range(len(invite_list)):
        invite_list[i] = invite_list[i].replace('\n', '')

with open(starting_letter_path) as file:
    letter = file.read()

for i in range(len(invite_list)):
    with open(
        f'{ready_to_send_path}/letter_for_{invite_list[i]}.txt',
        mode='w'
    ) as output:
        output.write(
            letter.replace('[name]', invite_list[i])
            )
