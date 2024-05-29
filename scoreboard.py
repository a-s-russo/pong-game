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
            self.goto(0 - parameters.BALL_SIZE * 5,
                      parameters.TOP_BOUNDARY - parameters.BALL_SIZE * 6)
        else:
            self.goto(0 + parameters.BALL_SIZE * 5,
                      parameters.TOP_BOUNDARY - parameters.BALL_SIZE * 6)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'{self.score}', align=parameters.ALIGNMENT,
                   font=parameters.SCORE_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def win_game(self):
        if self.side == 'left':
            x_cor = 0 - (parameters.WIDTH / 4)
        if self.side == 'right':
            x_cor = 0 + (parameters.WIDTH / 4)
        self.goto(x_cor, 0)
        self.write(f'{self.side.title()}\nwins!',
                   align=parameters.ALIGNMENT, font=parameters.WINNER_FONT)
