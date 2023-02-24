# Day 19 - Turtle Race

from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet',
                            prompt='Which turtle will win the race?\
 Enter a color: ')

color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_coords = [-75, -45, -15, 15, 45, 75]
turtles = []

for i in range(len(color_list)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color_list[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coords[i])
    turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:

    for turtle in turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() >= 230:
            winner = turtle
            race_on = False
            if user_bet == winner.pencolor():
                print(f"You've won! The {winner.pencolor()} \
turtle is the winner!")
            else:
                print(f"You've lost! The {winner.pencolor()} \
turtle is the winner!")

screen.exitonclick()
