from nor_ball import NorBall
from ball_list import BallList


class NorBallList(BallList):

    def __init__(self):
        super().__init__()

    def spawn_new_ball(self, position, velocity=None):
        new_ball = NorBall(position, velocity)
        self.ball_list.append(new_ball)

    def transform_into(self, other: BallList):
        for this in self.ball_list:
            if this.is_transformed:
                this.transform(other)
                self.ball_list.remove(this)
                this.__del__()

    def deceased_into(self, particle_list):
        for this in self.ball_list:
            if this.is_dead:
                particle_list.spawn_particle_of(self)
                self.ball_list.remove(this)
                this.__del__()