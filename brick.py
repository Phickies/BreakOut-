import pygame
from platform import Platform


class Brick(Platform):

    def __init__(self, position: pygame.Vector2, size: pygame.Vector2, color: tuple):
        super().__init__(position, size, color)
        self.is_collided = False

    def __str__(self):
        super().__str__()
        return f"is_collided: {self.is_collided}"

    def __del__(self):
        pass

    def collideplatform(self, other_platform):
        """
        Prevent go through brick

        :param other_platform:
        :return: None
        """
        if self.colliderect(other_platform):
            if (self.right >= other_platform.left - 2) and (self.right < other_platform.right):
                self.x = other_platform.left - self.width - 2
            elif (self.x <= other_platform.right + 2) and (self.x > other_platform.left):
                self.x = other_platform.right + 2
            elif (self.bottom >= other_platform.top - 2) and (self.bottom < other_platform.bottom):
                self.y = other_platform.top - self.height - 2
            elif (self.y <= other_platform.bottom + 2) and (self.y > other_platform.top):
                self.y = other_platform.bottom + 2

    def release_power(self):
        pass

    def break_animation(self):
        pass
