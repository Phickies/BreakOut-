from cur_ball import CurBall
from ball_list import BallList


class CurBallList(BallList):
    """
    A class representing a list of curable balls in the game.
    Inherits from the BallList class with additional curing functionality.
    """
    
    def __init__(self):
        super().__init__()

    def spawn_new_ball(self, position, velocity=None):
        new_ball = CurBall(position, velocity)
        self.ball_list.append(new_ball)

    def cure(self, other: BallList):
        """
        Attempt to cure balls in another BallList by checking for collisions.

        :param other: The BallList containing balls to be cured.
        """
        for this in self.ball_list:
            for that in other.ball_list:
                if not this.done_curing:
                    this.to_cure(that)
                else:
                    self.ball_list.remove(this)
                    break

    def transform_into(self, other: 'BallList'):
        """
        Transform dead CurBalls into other balls in the specified BallList.

        :param other: The BallList to transform into.
        """
        for this in self.ball_list:
            if this.is_dead:
                this.transform(other)
                self.ball_list.remove(this)
                this.__del__()
