# Day 8 - Caesar Cipher

from cipher_art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end_program = False

def caesar(text, shift, direction):
    output_text = ''
    if direction == 'decode':
        shift *= -1
    for char in text:
        if char not in alphabet:
            output_text += char
        else:
            index = alphabet.index(char)
            shift_index = index + shift
            if shift_index >= 26:
                shift_index -= 26
            output_text += alphabet[shift_index]
    print(f'The {direction}d text is {output_text}')

while end_program == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caesar(text, shift, direction)
    choice = input('Type "yes" if you want to go again. Otherwise type "no".\n')
    if choice != 'yes':
        end_program = True