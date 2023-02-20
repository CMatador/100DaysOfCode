# Day 15 - Coffee Machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")


def check_resources(drink, resources):
    '''Checks if there enough resources to make selected drink and returns
    true or false.'''
    for ingredient in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][f"{ingredient}"] \
                > resources[f"{ingredient}"]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        else:
            return True


def check_money(drink, coins, money):
    '''Checks if enough money was inserted for the drink, returns error
    for too little, and returns change for too much.'''
    if coins < MENU[drink]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False, money
    else:
        money += MENU[drink]['cost']
        coins -= MENU[drink]['cost']
        if coins > 0:
            print(f"Here is ${coins:.2f} in change.")
        return True, money


def make_coffee(drink, resources):
    '''Deducts resources for chosen drink from machine resources.'''
    for ingredient in MENU[drink]['ingredients']:
        resources[ingredient] -= MENU[drink]['ingredients'][f"{ingredient}"]
    print(f'Here is your {drink} ☕. Enjoy!')
    return resources


machine_on = True
money = 0

while machine_on:
    drink_choice = input('\nWhat would you like? \
(espresso/latte/cappuccino): ')
    if drink_choice in ('espresso', 'latte', 'cappuccino'):
        enough_resources = check_resources(drink_choice, resources)
        if enough_resources:
            print('Please insert coins.')
            quarters = int(input('How many quarters?: '))
            dimes = int(input('How many dimes?: '))
            nickels = int(input('How many nickels?: '))
            pennies = int(input('How many pennies?: '))
            coin_in = (0.25 * quarters) + (0.10 * dimes) \
                + (0.05 * nickels) + (0.01 * pennies)
            enough_money, money = check_money(drink_choice, coin_in, money)
            if enough_money:
                resources = make_coffee(drink_choice, resources)
    elif drink_choice == 'report':
        print_report(resources)
    elif drink_choice == 'off':
        machine_on = False
    else:
        print('Invalid input.')
