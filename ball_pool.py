import pygame
from nor_ball_list import NorBallList
from inf_ball_list import InfBallList
from cur_ball_list import CurBallList
from particle_list import ParticleList
from nor_brick import NorBrick
from inf_brick import InfBrick
from mul_brick import MulBrick


class BallPool:
    """
    A class representing a pool of different types of balls in the game.
    Manages the behavior, transformation, and interactions of different ball types.
    """

    def __init__(self):
        self.nor_balls = NorBallList()
        self.inf_balls = InfBallList()
        self.cur_balls = CurBallList()
        self.particles = ParticleList()

    def __str__(self):
        self.nor_balls.__str__()
        self.inf_balls.__str__()
        self.cur_balls.__str__()
        self.particles.__str__()

    def update(self):
        """
         Update the state of the BallPool, including transforming and managing different ball types.
         """
        self.nor_balls.update()
        self.inf_balls.update()
        self.cur_balls.update()
        self.particles.update()
        self.nor_balls.deceased_into(self.particles)
        self.particles.spawn_particle_of(self.inf_balls)
        self.particles.spawn_particle_of(self.cur_balls)
        self.nor_balls.transform_into(self.cur_balls)
        self.inf_balls.transform_into(self.nor_balls)
        self.cur_balls.transform_into(self.inf_balls)
        self.cur_balls.cure(self.inf_balls)
        self.inf_balls.eat(self.nor_balls)
        self.inf_balls.self_destruction()
        self.particles.fade_away()

    def display(self, screen):
        self.particles.display(screen)
        self.nor_balls.display(screen)
        self.inf_balls.display(screen)
        self.cur_balls.display(screen)

    def total_balls(self) -> int:
        sum_nor = len(self.nor_balls.ball_list)
        sum_inf = len(self.inf_balls.ball_list)
        sum_cur = len(self.cur_balls.ball_list)
        return sum_nor + sum_inf + sum_cur

    def spawn_nor_ball(self, position: pygame.Vector2):
        self.nor_balls.spawn_new_ball(position)

    def spawn_inf_ball(self, position: pygame.Vector2):
        self.inf_balls.spawn_new_ball(position)

    def spawn_cur_bal(self, position: pygame.Vector2):
        self.cur_balls.spawn_new_ball(position)

    def avoid_out_of_screen(self, screen):
        self.nor_balls.bounce_wall(True, True, True, True,
                                   0, screen.get_width(), 0, screen.get_height())
        self.inf_balls.bounce_wall(True, True, True, True,
                                   0, screen.get_width(), 0, screen.get_height())
        self.cur_balls.bounce_wall(True, True, True, True,
                                   0, screen.get_width(), 0, screen.get_height())
        self.particles.bounce_wall(True, True, True, True,
                                   0, screen.get_width(), 0, screen.get_height())

    def get_power(self, brick: InfBrick | NorBrick | MulBrick):
        """
        Process the power obtained by the BallPool based on the collided brick type.

        :param brick: The brick that the balls collided with.
        """
        if isinstance(brick, InfBrick) and brick.is_collided:
            self.spawn_inf_ball(pygame.Vector2(brick.centerx, brick.centery))
        elif isinstance(brick, NorBrick) and brick.is_collided:
            pass
        elif isinstance(brick, MulBrick) and brick.is_collided:
            self.spawn_nor_ball(pygame.Vector2(brick.centerx, brick.centery))

    def bounce(self, rect_object_list: list = None, rect_object: pygame.Rect = None, other_list=None):
        """
        Bounce balls upon objects.

        :param rect_object_list: List of rectangle objects to bounce with.
        :param rect_object: Single rectangle object to bounce with.
        :param other_list: List of other non-polygon objects for collision.
        """

        # Collision between one object
        if rect_object is not None:
            self.nor_balls.bounce_rect(rect_object)
            self.inf_balls.bounce_rect(rect_object)
            self.cur_balls.bounce_rect(rect_object)
            self.particles.bounce_rect(rect_object)

        # Collision between list of object
        elif rect_object_list is not None:
            for rect_object in rect_object_list:
                self.nor_balls.bounce_rect(rect_object)
                self.inf_balls.bounce_rect(rect_object)
                self.cur_balls.bounce_rect(rect_object)
                self.particles.bounce_rect(rect_object)

        # Collision between balls
        elif other_list is not None:
            self.nor_balls.bounce_elastic(self.nor_balls)
            self.nor_balls.bounce_elastic(self.cur_balls)
            self.inf_balls.bounce_elastic(self.inf_balls)
            self.cur_balls.bounce_elastic(self.cur_balls)
            self.particles.bounce_elastic(self.particles)
