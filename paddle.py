from turtle import Turtle
import parameters


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        if self.side == 'left':
            self.goto(parameters.LEFT_BOUNDARY + parameters.SIZE, 0)
        else:
            self.goto(parameters.RIGHT_BOUNDARY - parameters.SIZE, 0)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
