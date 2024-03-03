import pygame


class LimitLine(pygame.Rect):

    def __init__(self, screen, color: tuple):
        super().__init__(0, screen.get_height() - 150, screen.get_width(), 3)
        self.color = color

    def display(self, screen):
        pygame.draw.rect(screen, self.color, self)