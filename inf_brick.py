import pygame
from brick import Brick


class InfBrick(Brick):

    color = (180, 10, 20)  # Red

    def __init__(self, position: pygame.Vector2, size: pygame.Vector2):
        super().__init__(position, size, self.color)
