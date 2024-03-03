import pygame
from start_menu import StartMenu


class SceneStartMenu:

    size = pygame.Vector2(500, 500)
    is_running = True

    def __init__(self):
        self.menu = StartMenu(self.size)

    def run(self):
        self.menu.run_loop()

    def end(self):
        if self.menu.is_closed:
            self.is_running = False
            print("world")
