# Day 23 - Turtle Crossing

import time
import random
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from crossing_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    rng = random.randint(1, 6)
    if rng == 6:
        car_manager.generate_car()
    for car in car_manager.cars:
        car.move(score.level)
        if car.distance(player) < 20:
            game_is_on = False
    if player.ycor() >= FINISH_LINE_Y:
        player.reset_pos()
        score.increase_level()

score.game_over()
screen.exitonclick()
