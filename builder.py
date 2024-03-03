import random
import pygame
from nor_brick import NorBrick
from inf_brick import InfBrick
from mul_brick import MulBrick


class Builder:
    """
    A class responsible for managing the creation, display, and update of bricks in the game.
    """

    def __init__(self, brick_size: pygame.math.Vector2, max_brick: int):
        """
        Initialize the Builder with brick size and maximum allowed bricks.

        :param brick_size: The size of each brick as a pygame.math.Vector2.
        :param max_brick: The maximum number of bricks allowed.
        """
        self.brick_size = brick_size
        self.max_brick = max_brick
        self.bricks = []

    def __str__(self):
        return (f"Max_brick: {self.max_brick}, "
                f"Number_of_brick_left: {self.max_brick - len(self.bricks)}",
                f"Current num_brick: {len(self.bricks)}")

    def __del__(self):
        pass

    def display(self, screen):
        """
        Display all bricks on the given screen.

        :param screen: The screen to display the bricks on.
        """
        for i in self.bricks:
            i.display(screen)

    def update(self):
        """
        Update the state of each brick in the builder.

        Removes bricks that have been marked as collided.
        """
        for brick in self.bricks:
            if brick.is_collided is True:
                brick.break_animation()
                self.bricks.remove(brick)

    def avoid_out_of_screen(self, screen):
        """
        Adjust the position of bricks to avoid them going out of the screen.

        :param screen: The screen boundaries.
        """
        for brick in self.bricks:
            brick.avoid_out_of_screen(screen)

    def spawn_brick(self, position: tuple):
        """
        Spawn a new brick at the given position if the maximum number of bricks is not reached
        and there is no overlay with existing bricks.

        :param position: The position to spawn the new brick.
        """
        spawn_new_brick = True
        new_pos = pygame.math.Vector2(position[0]-self.brick_size.x/2,
                                      position[1]-self.brick_size.y/2)

        # Create a temp_brick to compare if overlay
        temp_brick = NorBrick(new_pos, self.brick_size)
        for other_brick in self.bricks:
            if temp_brick.colliderect(other_brick):
                spawn_new_brick = False

        temp_brick.__del__()
        if spawn_new_brick:
            if len(self.bricks) < self.max_brick:
                new_brick = self.__random_brick_generated(position, self.brick_size)
                self.bricks.append(new_brick)
            else:
                print("You are out of bricks")
    
    @staticmethod
    def __random_brick_generated(position, brick_size) -> NorBrick | InfBrick | MulBrick:
        """
        Generate a random type of brick based on a probability distribution.

        :param position: The position of the new brick.
        :param brick_size: The size of the new brick.
        :return: An instance of NorBrick, InfBrick, or MulBrick.
        """
        probability = random.randint(1, 10) % 10 * 10
        if probability <= 5:
            new_brick = InfBrick(position, brick_size)
        elif probability <= 15:
            new_brick = MulBrick(position, brick_size)
        else:
            new_brick = NorBrick(position, brick_size)
        return new_brick
