import colorgram
import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)


def draw_circle(turtle):
    turtle.color(random.choice(rgb_colors))
    turtle.dot(20)


rgb_colors = []
colors = colorgram.extract('Day11-20/image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

color_list = rgb_colors[4:]

timmy = Turtle(shape='turtle')
timmy.speed('fastest')
timmy.penup()
timmy.hideturtle()

for y in range(10):
    timmy.setpos(x=-250, y=-250 + (y * 50))
    for x in range(10):
        draw_circle(timmy)
        timmy.forward(50)

screen.exitonclick()
