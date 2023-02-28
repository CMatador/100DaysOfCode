from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.level = 1
        self.display()

    def display(self):
        self.write(
            f'Level: {self.level}',
            font=FONT
        )

    def increase_level(self):
        self.clear()
        self.level += 1
        self.display()

    def game_over(self):
        self.home()
        self.write(
            'Game Over',
            align='center',
            font=FONT
        )
