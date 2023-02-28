import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def generate_car(self):
        new_car = Car()
        self.cars.append(new_car)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.turtlesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(x=280, y=random.randint(-250, 250))
        self.setheading(180)

    def move(self, level):
        self.forward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (level - 1)))
