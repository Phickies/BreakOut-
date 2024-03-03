from inf_ball import InfBall
from ball_list import BallList


class InfBallList(BallList):

    def __init__(self):
        super().__init__()

    def eat(self, other: BallList):
        for this in self.ball_list:
            for that in other.ball_list:
                this.consume(that)

    def spawn_new_ball(self, position, velocity=None):
        new_ball = InfBall(position, velocity)
        self.ball_list.append(new_ball)

    def self_destruction(self):
        for ball in self.ball_list:
            if ball.is_dead:
                self.ball_list.remove(ball)
                ball.__del__()

    def transform_into(self, other: BallList):
        for this in self.ball_list:
            if this.is_cured:
                this.transform(other)
                self.ball_list.remove(this)
                this.__del__()
