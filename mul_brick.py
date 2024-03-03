import pygame
from brick import Brick


class MulBrick(Brick):

    color = (10, 190, 30)  # Green
    multi_number = 2
    
    def __init__(self, position: pygame.Vector2, size: pygame.Vector2):
        super().__init__(position, size, self.color)

