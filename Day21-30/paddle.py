from turtle import Turtle
UP = 90
DOWN = 270
START_POSITION = [(350, 0), (-350, 0)]


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setpos(position)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
