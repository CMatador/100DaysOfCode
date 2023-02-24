# Day 19 - Etch a Sketch

from turtle import Turtle, Screen


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def reset():
    tim.reset()


tim = Turtle()
screen = Screen()
screen.listen()

screen.onkeypress(key='w', fun=forward)
screen.onkeypress(key='s', fun=backward)
screen.onkeypress(key='a', fun=turn_left)
screen.onkeypress(key='d', fun=turn_right)
screen.onkeypress(key='c', fun=reset)

screen.exitonclick()
