from turtle import Turtle

import parameters


class Scoreboard(Turtle):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        if self.side == 'left':
            self.goto(0 - parameters.SIZE * 5, parameters.TOP_BOUNDARY - parameters.SIZE * 6)
        else:
            self.goto(0 + parameters.SIZE * 5, parameters.TOP_BOUNDARY - parameters.SIZE * 6)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'{self.score}', align=parameters.ALIGNMENT, font=parameters.FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
