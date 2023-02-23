from turtle import Turtle, Screen
import random
# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
# table.add_column('Type', ['Electric', 'Water', 'Fire'])
# table.align = 'l'

screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timmy = Turtle()
timmy.shape('turtle')
timmy.speed(0)
for i in range(36):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.left(10)

screen.exitonclick()
