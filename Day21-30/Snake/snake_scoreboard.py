from turtle import Turtle

FONT = ('Arial', 18, 'normal')
ALIGNMENT = 'center'
HIGHSCORE_PATH = 'Day21-30/Snake/data.txt'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.sety(270)
        self.color('white')
        self.speed('fastest')
        self.score = 0
        with open(HIGHSCORE_PATH) as file:
            self.high_score = int(file.read())
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(
            f'Score: {self.score} High Score: {self.high_score}',
            align=ALIGNMENT,
            font=FONT
            )

    def increase_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.home()
        self.write(
            'Game Over.',
            align=ALIGNMENT,
            font=FONT
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(HIGHSCORE_PATH, mode='w') as file:
                file.write(str(self.high_score))
                print('New high score!')
        self.score = 0
        self.display_score()
