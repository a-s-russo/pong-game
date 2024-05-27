import random
from turtle import Turtle

import parameters


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('green')
        self.penup()
        self.x_move = random.choice([-parameters.MOVEMENT, parameters.MOVEMENT])
        self.y_move = random.choice([-parameters.MOVEMENT, parameters.MOVEMENT])

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def rebound(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1

    def restart(self):
        self.goto(0,0)
        self.hit()
        self.y_move = random.choice([-parameters.MOVEMENT, parameters.MOVEMENT])