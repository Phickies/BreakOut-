import pygame
from ball import Ball


class InfBall(Ball):
    """
    Class representing an infected ball, a subtype of the Ball class.

    Attributes:
    - color (tuple): RGB color tuple representing the ball's color.
    - size (float): Size of the ball.
    - lifetime (int): Time limit for the ball's existence in milliseconds.

    Methods:
    - __init__: Initializes an instance of InfBall.
    - increase_strength: Increases the strength (color, size, lifetime) of the ball.
    - consume: Consumes another ball, increasing its own strength and removing the consumed ball.
    - update_lifetime: Updates the ball's lifetime and marks it as dead if the lifetime has expired.
    """

    color = (180, 50, 20)
    size = 10
    lifetime = 10000  # Time limit in milliseconds

    def __init__(self, init_position, velocity=None):
        """
        Initialize an InfBall instance.

        :param init_position: Initial position of the ball.
        :param velocity: Initial velocity of the ball.
        :return: None
        """
        super().__init__(init_position, self.size, self.color, velocity)
        self.is_cured = False

    def increase_strength(self):
        """
        Increase the strength of the infected ball by modifying its color, size, and lifetime.
        :return: None
        """
        try:
            self.color = (self.color[0] + 1, self.color[1], self.color[2] - 1)
        except ():
            pass
        self.size += 1
        self.lifetime += 5000

    def consume(self, other: Ball):
        """
        Consume another ball, increasing the strength of the infected ball and removing the consumed ball.

        :param other: Ball to be consumed.
        :return: None
        """
        if self.collision_non_side_geometry(other):
            self.increase_strength()
            other.is_dead = True

    def update_lifetime(self):
        """
        Update the lifetime of the infected ball and mark it as dead if the lifetime has expired.
        :return: None
        """
        current_time = pygame.time.get_ticks()
        time_since_spawn = current_time - self.spawn_time

        # Check if the ball's lifetime has expired
        if time_since_spawn >= self.lifetime:
            self.is_dead = True

    def bounce_rect(self, brick):
        super().bounce_rect(brick)
        if self.destroy_brick and hasattr(brick, 'score_value'):
            brick.score_value = 2
