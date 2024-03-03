import pygame
from platform import Platform


class Shooter(Platform):
    """
    Class representing a shooter platform, a subtype of the Platform class.

    Attributes:
    - init_position (pygame.math.Vector2): Initial position of the shooter.
    - size (pygame.math.Vector2): Size of the shooter.
    - speed (float): Speed of the shooter's movement.
    - color (tuple): RGB color tuple representing the shooter's color.

    Methods:
    - __init__: Initializes an instance of Shooter.
    - __del__: Destructor method.
    - translate: Moves the shooter with a given velocity.
    - power_up: Placeholder method for powering up the shooter.

    """

    color = (255, 200, 0)  # Default color

    def __init__(self, init_position: pygame.math.Vector2,
                 size: pygame.math.Vector2, speed: float):
        """
         Initialize a Shooter instance.

         :param init_position: Initial position of the shooter.
         :param size: Size of the shooter.
         :param speed: Speed of the shooter's movement.
         :return: None
         """
        super().__init__(position=init_position,
                         size=size,
                         color=self.color)
        self.speed = speed
        self.rotation_angle = 0  # Initialize rotation angle
        self.rotation_direction = 1  # 1 for clockwise, -1 for counterclockwise

    def __del__(self):
        pass

    def translate(self, screen, velocity: pygame.math.Vector2):
        """
        Move the shooter with velocity.

        :param screen: Screen display object.
        :param velocity: Velocity for translation.
        :return: None
        """
        velocity *= self.speed
        super().move_ip(velocity.x, velocity.y)

    def rotate(self):
        """
        Rotate the shooter between horizontal and vertical position
        """
        pivot = [self.centerx, self.centery]
        self.width, self.height = self.height, self.width
        self.centerx = pivot[0]
        self.centery = pivot[1]

    def power_up(self):
        pass
