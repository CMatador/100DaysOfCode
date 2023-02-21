# Day 16 - OOP Coffee Machine

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while machine_on:
    drink_choice = input(f'\nWhat would you like? ({menu.get_items()}): ')
    if drink_choice == 'off':
        machine_on = False
    elif drink_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(drink_choice)
        if coffee_maker.is_resource_sufficient(drink) \
                and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
