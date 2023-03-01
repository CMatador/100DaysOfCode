# Day 21 - Snake (Part 2)

from turtle import Screen
from snake import Snake
from food import Food
from snake_scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
board = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()

    if board.score <= 4:
        time.sleep(0.15)
    elif board.score <= 9:
        time.sleep(0.10)
    elif board.score <= 14:
        time.sleep(0.08)
    elif board.score <= 19:
        time.sleep(0.06)
    else:
        time.sleep(0.04)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        board.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 \
            or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        board.reset()
        snake.reset()

    # Detect collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            board.reset()
            snake.reset()


screen.exitonclick()
