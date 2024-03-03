import pygame
from brick import Brick


class NorBrick(Brick):

    color = (10, 100, 250)  # Blue

    def __init__(self, position: pygame.Vector2, size: pygame.Vector2):
        super().__init__(position, size, self.color)
        self.score_value = 1
