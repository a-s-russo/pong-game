from random import choice
from turtle import Turtle

import parameters


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('green')
        self.penup()
        self.sleep_time = parameters.BALL_START_SPEED
        self.x_move = choice(
            [-parameters.BALL_MOVEMENT_SIZE, parameters.BALL_MOVEMENT_SIZE])
        self.y_move = choice(
            [-parameters.BALL_MOVEMENT_SIZE, parameters.BALL_MOVEMENT_SIZE])

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.sleep_time *= parameters.BALL_INCREASE_SPEED

    def restart(self):
        self.goto(0, 0)
        self.sleep_time = parameters.BALL_START_SPEED
        self.bounce_x()
        self.y_move = choice(
            [-parameters.BALL_MOVEMENT_SIZE, parameters.BALL_MOVEMENT_SIZE])
