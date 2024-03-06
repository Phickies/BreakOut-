import sys
import pygame
from score import Score
from limit_line import LimitLine
from ball_pool import BallPool
from shooter import Shooter
from builder import Builder


class GameManager:
    """
    Class representing the game manager for controlling game flow.

    Attributes:
    - canvas_size (pygame.math.Vector2): Size of the game canvas.
    - player_a_speed (float): Speed of player A (shooter).
    - player_b_max_brick (int): Maximum number of bricks for player B.

    Methods:
    - __init__: Initializes an instance of GameManager.
    - key_clicked_events: Handles key clicked events
    - mouse_pressed_events: Handles mouse pressed events.
    - key_pressed_events: Handles key pressed events.
    - handle_collisions: Updates game entities based on collisions.
    - handle_events: Handles various game events.
    - display: Clears the screen and displays game entities.
    - update: Updates game entities and checks for screen boundaries.
    - run_loop: Main game loop.
    """

    FPS = 60  # Set frame per second

    def __init__(self, canvas_size: pygame.math.Vector2 | int,
                 player_a_speed: float,
                 player_b_max_brick: int):
        """
        Initialize a GameManager instance.

        :param canvas_size: Size of the game canvas.
        :param player_a_speed: Speed of player A (shooter).
        :param player_b_max_brick: Maximum number of bricks for player B.
        :return: None
        """
        self.size = canvas_size
        self.screen = pygame.display.set_mode((0, 0), self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()

        self.balls = BallPool()
        self.score = Score()
        self.shooter = Shooter(init_position=pygame.math.Vector2(self.screen.get_width() / 2 - 50, self.screen.get_height() - 30),
                               size=pygame.math.Vector2(100, 18), speed=player_a_speed)
        self.builder = Builder(brick_size=pygame.math.Vector2(50, 18), max_brick=player_b_max_brick)
        self.balls.spawn_nor_ball(position=pygame.Vector2(self.screen.get_width()/2, self.screen.get_height()/2))
        self.limit_line = LimitLine(self.screen, (50, 50, 50))

    def clicked_event(self):
        """
        Handle key click events and exit game condition

        :return: None
        """
        for event in pygame.event.get():
            # Exit condition
            if (event.type == pygame.QUIT or
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
                self.shooter.rotate()
                for brick in self.builder.bricks:
                    if self.shooter.colliderect(brick):
                        self.shooter.rotate()

    def mouse_pressed_events(self):
        """
        Handle mouse pressed events.

        :return: None
        """
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            m_pos = pygame.mouse.get_pos()
            if ((m_pos[0] > 0) and (m_pos[0] < self.screen.get_width()) and
                    (m_pos[1] > 0 and m_pos[1]) < (self.screen.get_height())):
                self.builder.spawn_brick(pygame.mouse.get_pos())
            else:
                print("Outside of scope")

    def key_pressed_events(self):
        """
        Handle key pressed events.

        :return: None
        """
        keys = pygame.key.get_pressed()
        move_direction = pygame.math.Vector2(keys[pygame.K_d] - keys[pygame.K_a], keys[pygame.K_s] - keys[pygame.K_w])
        self.shooter.pre_position = self.shooter.x, self.shooter.y
        self.shooter.translate(self.screen, move_direction)

    def handle_collisions(self):
        """
        Update game entities based on collisions.

        :return: None
        """
        # Update bouncing
        self.balls.bounce(rect_object=self.shooter)
        self.balls.bounce(rect_object_list=self.builder.bricks)
        self.balls.bounce(other_list=self.balls)

        # Update collision between brick
        for brick in self.builder.bricks:
            self.shooter.collideplatform(brick)
            self.balls.get_power(brick)
            for other_brick in self.builder.bricks:
                if brick is not other_brick:
                    brick.collideplatform(other_brick)

    def handle_events(self):
        self.clicked_event()
        self.mouse_pressed_events()
        self.key_pressed_events()

    def display(self):
        self.screen.fill((0, 0, 0))
        self.limit_line.display(self.screen)
        self.shooter.display(self.screen)
        self.builder.display(self.screen)
        self.balls.display(self.screen)
        self.score.display(self.screen, self.balls)

    def update(self):
        self.handle_collisions()
        self.score.update(self.builder.bricks)
        self.balls.update()
        self.builder.update()

        self.balls.avoid_out_of_screen(self.screen)
        self.shooter.avoid_out_of_screen(self.screen)
        self.builder.avoid_out_of_screen(self.screen)

        pygame.display.flip()
        self.clock.tick(self.FPS)

    def run_loop(self):
        self.handle_events()
        self.update()
        self.display()
