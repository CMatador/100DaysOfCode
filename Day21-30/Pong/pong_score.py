from turtle import Turtle

FONT = ('Courier New', 36, 'bold')


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.goto(position)
        self.score = 0
        self.display_score()

    def display_score(self):
        self.write(
            self.score,
            font=FONT
            )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()
