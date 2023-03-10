# Day 10 - Calculator

from calculator_art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    finished = False
    print(logo)
    num1 = float(input('What\'s the first number?: '))
    for symbol in operations:
        print(symbol)

    while not finished:
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('What\'s the next number?: '))
        answer = operations[operation_symbol](num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')
        calc_more = input(f"Type 'y' to continue calculating with {answer} or \
                          type 'n' to start a new calculation.: ")
        if calc_more == 'n':
            finished = True
            calculator()
        else:
            num1 = answer


calculator()
