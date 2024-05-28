import time
from turtle import Screen, Turtle

import ball
import paddle
import parameters
import scoreboard

# Create screen
screen = Screen()
screen.setup(width=parameters.WIDTH, height=parameters.HEIGHT)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# Create centre line
centre_line = Turtle()
centre_line.pensize(5)
centre_line.hideturtle()
centre_line.color('white')
centre_line.penup()
centre_line.teleport(0, parameters.BOTTOM_BOUNDARY)
centre_line.setheading(90)

# Print centre line
for _ in range(int(parameters.HEIGHT / 20)):
    centre_line.forward(10)
    centre_line.penup()
    centre_line.forward(10)
    centre_line.pendown()

# Create paddles
left_paddle = paddle.Paddle('left')
right_paddle = paddle.Paddle('right')

# Create key bindings for paddles
screen.listen()
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')

# Create ball
ball = ball.Ball()

# Create scoreboard
left_paddle_scoreboard = scoreboard.Scoreboard('left')
right_paddle_scoreboard = scoreboard.Scoreboard('right')

# Simulate game
while True:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision between ball and wall
    if ball.ycor() > parameters.TOP_BOUNDARY - parameters.BALL_SIZE or ball.ycor() < parameters.BOTTOM_BOUNDARY + parameters.BALL_SIZE:
        ball.bounce_y()

    # Detect collision between ball and right paddle's side
    if ball.distance(
        right_paddle) <= parameters.BALL_SIZE * (parameters.PADDLE_SIZE - 1) and abs(
            ball.xcor() - right_paddle.xcor()) == parameters.BALL_SIZE and ball.xcor() < right_paddle.xcor():
        ball.bounce_x()

    # Detect collision between ball and right paddle's top
    if ball.xcor() == right_paddle.xcor() and ball.ycor() == right_paddle.ycor() + parameters.BALL_SIZE * (
            round(parameters.PADDLE_SIZE / 2) + 1) and ball.y_move < 0:
        ball.bounce_y()

    # Detect collision between ball and right paddle's bottom
    if ball.xcor() == right_paddle.xcor() and ball.ycor() == right_paddle.ycor() - parameters.BALL_SIZE * (
            round(parameters.PADDLE_SIZE / 2) + 1) and ball.y_move > 0:
        ball.bounce_y()

    # Detect collision between ball and left paddle's side
    if ball.distance(
        left_paddle) <= parameters.BALL_SIZE * (parameters.PADDLE_SIZE - 1) and abs(
            ball.xcor() - left_paddle.xcor()) == parameters.BALL_SIZE and ball.xcor() > left_paddle.xcor():
        ball.bounce_x()

    # Detect collision between ball and left paddle's top
    if ball.xcor() == left_paddle.xcor() and ball.ycor() == left_paddle.ycor() + parameters.BALL_SIZE * (
            round(parameters.PADDLE_SIZE / 2) + 1) and ball.y_move < 0:
        ball.bounce_y()

    # Detect collision between ball and left paddle's bottom
    if ball.xcor() == left_paddle.xcor() and ball.ycor() == left_paddle.ycor() - parameters.BALL_SIZE * (
            round(parameters.PADDLE_SIZE / 2) + 1) and ball.y_move > 0:
        ball.bounce_y()

    # Detect miss by right paddle
    if ball.xcor() > parameters.RIGHT_BOUNDARY:
        left_paddle_scoreboard.increase_score()
        ball.restart()

    # Detect miss by left paddle
    if ball.xcor() < parameters.LEFT_BOUNDARY:
        right_paddle_scoreboard.increase_score()
        ball.restart()

screen.exitonclick()
