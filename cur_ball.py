import pygame
from ball import Ball


class CurBall(Ball):
    """
    A class representing a curable ball in the game.
    Inherits from the Ball class with additional curing functionality.
    """

    color = (10, 200, 200)
    size = 10
    number_of_curing = 1
    lifetime = 20000  # Time limit in milliseconds

    def __init__(self, init_position, velocity):
        """
        Initialize a CurBall with a specific position, velocity, size, and color.

        :param init_position: The initial position of the ball.
        :param velocity: The initial velocity of the ball.
        """
        super().__init__(init_position, self.size, self.color, velocity)
        self.done_curing = False

    def to_cure(self, other: Ball):
        """
        Attempt to cure another ball by checking for collision.

        :param other: The ball to be cured.
        """
        if self.collision_non_side_geometry(other):
            other.is_cured = True
            self.number_of_curing -= 1
            if self.number_of_curing <= 0:
                self.done_curing = True

    def update_lifetime(self):
        """
        Update the lifetime of the CurBall and mark it as dead if the lifetime has expired.
        """
        current_time = pygame.time.get_ticks()
        time_since_spawn = current_time - self.spawn_time

        # Check if the ball's lifetime has expired
        if time_since_spawn >= self.lifetime:
            self.is_dead = True
