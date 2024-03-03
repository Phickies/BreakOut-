import pygame
from ball import Ball


class Particle(Ball):

    size = 2
    lifetime = 2000

    def __init__(self, position, color, velocity):
        self.color = (color[0]-10, color[1]-10, color[2]-10)
        super().__init__(position, self.size, self.color, velocity)
        self.is_dead = False

    def fade(self):
        self.color = (self.color[0]-1, self.color[1]-1, self.color[2]-1)
        if self.color[0] < 0:
            self.color = (0, self.color[1], self.color[2])
        if self.color[1] < 0:
            self.color = (self.color[0], 0, self.color[2])
        if self.color[2] < 0:
            self.color = (self.color[0], self.color[1], 0)

    def update_lifetime(self):
        current_time = pygame.time.get_ticks()
        time_since_spawn = current_time - self.spawn_time

        # Check if the ball's lifetime has expired
        if time_since_spawn >= self.lifetime:
            self.is_dead = True
