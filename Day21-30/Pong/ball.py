from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.xdir = 1
        self.ydir = 1

    def move(self, xdir, ydir):
        new_x = self.xcor() + 10 * xdir
        new_y = self.ycor() + 10 * ydir
        self.goto(new_x, new_y)
