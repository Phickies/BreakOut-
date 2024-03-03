import pygame
import random
from particle import Particle
from ball_list import BallList


class ParticleList(BallList):

    def __init__(self):
        super().__init__()

    def spawn_particle_of(self, other: BallList):
        for ball in other.ball_list:
            if ball.is_dead:
                for i in range(ball.size*2):
                    velocity = pygame.Vector2(random.uniform(0, ball.velocity.x/2),
                                              random.uniform(0, ball.velocity.y/2))
                    position = pygame.Vector2(random.uniform(ball.position.x-ball.size, ball.position.x+ball.size),
                                              random.uniform(ball.position.y-ball.size, ball.position.y+ball.size))
                    new_particle = Particle(position, ball.color, velocity)
                    self.ball_list.append(new_particle)

    def fade_away(self):
        for this in self.ball_list:
            this.update_lifetime()
            this.fade()
            if this.is_dead:
                self.ball_list.remove(this)
