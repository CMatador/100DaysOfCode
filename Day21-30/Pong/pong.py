# Day 22 - Pong
from turtle import Screen, Turtle
from paddle import Paddle, START_POSITION
from ball import Ball
from pong_score import Scoreboard
import time

# Build the playing field
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# Dash lines down the middle
dash = Turtle()
dash.sety(300)
dash.hideturtle()
dash.color('white')
dash.setheading(270)
dash.speed(0)
dash.pensize(3)
for i in range(15):
    dash.forward(20)
    dash.penup()
    dash.forward(20)
    dash.pendown()

# Paddles - controllable turtles on the sides
r_paddle = Paddle(START_POSITION[0])
l_paddle = Paddle(START_POSITION[1])
screen.listen()
screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')
screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')

# Ball
ball = Ball()
ball_speed = 0.10

# Scoreboard
left_score = Scoreboard((-130, 250))
right_score = Scoreboard((100, 250))

game_on = True
while game_on:
    screen.update()
    time.sleep(ball_speed)
    ball.move(ball.xdir, ball.ydir)
    # Wall collision detection
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.ydir *= -1
    # Paddle collision detection
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 \
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.xdir *= -1
        ball_speed *= 0.90
    # Detect when paddles miss
    if ball.xcor() > 370:
        left_score.increase_score()
        ball.home()
        ball_speed = 0.10
        ball.xdir = -1
    if ball.xcor() < -370:
        right_score.increase_score()
        ball.home()
        ball_speed = 0.10
        ball.xdir = 1

    # Game end
    if left_score.score == 3 or right_score.score == 3:
        game_on = False

screen.exitonclick()
