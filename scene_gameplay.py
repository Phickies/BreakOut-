import pygame
from game_manager import GameManager


class SceneGameplay:

    size = pygame.FULLSCREEN
    player_a_speed = 5
    player_b_mxbrick = 70

    def __init__(self):
        self.game = GameManager(self.size, self.player_a_speed, self.player_b_mxbrick)

    def run(self):
        self.game.run_loop()
