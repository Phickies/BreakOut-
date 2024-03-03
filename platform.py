import pygame
from pygame import Rect


class Platform(Rect):
    """
    Class representing a platform, a subtype of the Rect class.

    Attributes:
    - position (pygame.math.Vector2): Initial position of the platform.
    - size (pygame.math.Vector2): Size of the platform.
    - color (tuple): RGB color tuple representing the platform's color.

    Methods:
    - __init__: Initializes an instance of Platform.
    - __str__: Returns a string representation of the platform.
    - display: Draws the platform on the screen.
    - avoid_out_of_screen: Adjusts the platform's position to stay within the screen boundaries.
    - collideplatform: Prevents the platform from going through another platform.

    """

    def __init__(self,
                 position: pygame.math.Vector2,
                 size: pygame.math.Vector2,
                 color: tuple):
        """
        Initialize a Platform instance.

        :param position: Initial position of the platform.
        :param size: Size of the platform.
        :param color: RGB color tuple representing the platform's color.
        :return: None
        """
        super().__init__(position, size)
        self.color = color

    def __str__(self):
        super().__str__()
        return f"Color: {self.color}"

    def display(self, screen):
        """
        Draws the platform on the screen.

        :param screen: Pygame screen to draw on.
        :return: None
        """
        pygame.draw.rect(screen, self.color, self)

    def avoid_out_of_screen(self, screen):
        """
        Adjusts the platform's position to stay within the screen boundaries.

        :param screen: Screen to set the boundary of.
        :return: None
        """
        if self.x > screen.get_width() - self.width:
            self.x = screen.get_width() - self.width - 1
        if self.x < 0:
            self.x = 1
        if self.y > screen.get_height() - self.height:
            self.y = screen.get_height() - self.height - 1
        if self.y < 0:
            self.y = 1

    def collideplatform(self, other_platform):
        """
        Prevents the platform from going through another platform.

        :param other_platform: Other platform to avoid collision with.
        :return: None
        """
        off_set_brick = other_platform.width / 2 + other_platform.width / 5
        if self.colliderect(other_platform):
            if (self.right >= other_platform.left - 1) and (self.right + off_set_brick < other_platform.right):
                self.x = other_platform.left - self.width - 2
            elif (self.x <= other_platform.right + 1) and (self.x - off_set_brick > other_platform.left):
                self.x = other_platform.right + 2
            elif (self.bottom >= other_platform.top - 1) and (self.bottom < other_platform.bottom):
                self.y = other_platform.top - self.height - 2
            elif (self.y <= other_platform.bottom + 1) and (self.y > other_platform.top):
                self.y = other_platform.bottom + 2
