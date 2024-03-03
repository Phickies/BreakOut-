import pygame
from nor_brick import NorBrick


class Score:

    color = (255, 255, 255)

    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 30)

    def update(self, other_list: list):
        for brick in other_list:
            if isinstance(brick, NorBrick) and brick.is_collided:
                self.score += brick.score_value

    def display(self, screen, balls):
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        ball_text = self.font.render(f"Number of balls: {balls.total_balls()}", True, self.color)
        screen.blit(score_text, (20, 35))
        screen.blit(ball_text, (20, 85))

    def increase_score(self, number):
        self.score += number
