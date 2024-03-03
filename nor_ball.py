import pygame
from ball import Ball


class NorBall(Ball):
    """
    Class representing a normal ball, a subtype of the Ball class.

    Attributes:
    - color (tuple): RGB color tuple representing the ball's color.
    - size (float): Size of the ball.
    - lifetime (int): Time limit for the ball's existence in milliseconds.

    Methods:
    - __init__: Initializes an instance of NorBall.
    - update_lifetime: Updates the ball's lifetime and marks it as transformed if the lifetime has expired.
    """

    color = (250, 255, 250)
    size = 10
    lifetime = 10000  # Time duration in milliseconds

    def __init__(self, init_position, velocity=None):
        """
        Initialize a NorBall instance.

        :param init_position: Initial position of the ball.
        :param velocity: Initial velocity of the ball.
        :return: None
        """
        super().__init__(init_position, self.size, self.color, velocity)
        self.is_transformed = False

    def update_lifetime(self):
        """
         Update the lifetime of the normal ball and mark it as transformed if the lifetime has expired.
         :return: None
         """
        current_time = pygame.time.get_ticks()
        time_since_spawn = current_time - self.spawn_time

        # Check if the ball's lifetime has expired
        if time_since_spawn >= self.lifetime:
            self.is_transformed = True
