from turtle import Turtle

FONT = ('Arial', 18, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.sety(270)
        self.color('white')
        self.speed('fastest')
        self.score = 0
        self.display_score()

    def display_score(self):
        self.write(
            f'Score: {self.score}',
            align=ALIGNMENT,
            font=FONT
            )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.home()
        self.write(
            'Game Over.',
            align=ALIGNMENT,
            font=FONT
        )
