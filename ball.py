import random
import pygame
import math


class Ball:

    def __init__(self, init_position, size: float, color: tuple, velocity: pygame.Vector2 = None):
        """
        Initialize a Ball object.

        :param init_position: Initial position of the ball as a tuple (x, y).
        :param size: Radius of the ball.
        :param color: RGB tuple representing the color of the ball.
        :param velocity: Initial velocity of the ball as a pygame.Vector2. If None, a random velocity is assigned.
        """
        self.position = init_position
        self.velocity = velocity
        self.size = size
        self.color = color
        self.destroy_brick = False
        self.is_dead = False
        self.spawn_time = pygame.time.get_ticks()

        if self.velocity is None:
            self.velocity = pygame.math.Vector2(
                random.uniform(-10, 10), 5
            )

    def __str__(self):
        return f"Position: {self.position}, Velocity: {self.velocity}"

    def __del__(self):
        return f"Delete ball at position: {self.position}"

    def display(self, screen):
        """
        Display the ball on the given screen.

        :param screen: Pygame screen where the ball will be displayed.
        :return: None
        """
        pygame.draw.circle(screen, self.color, self.position, self.size)

    def transform(self, other):
        """
        Transform the ball into new ball by spawning a new ball with the same position and velocity.

        :param other: Object with a spawn_new_ball method.
        :return: None
        """
        other.spawn_new_ball(self.position, self.velocity)

    def update_lifetime(self):
        """
        Update the lifetime of the ball.

        :return: None
        """
        pass

    def restrict_velocity(self):
        """
        Restrict the velocity of the ball within certain bounds.

        :return: None
        """
        if self.velocity.x > 10:
            self.velocity.x = random.randint(5, 10)
        elif self.velocity.y > 10:
            self.velocity.y = random.randint(5, 10)
        elif self.velocity.x < -10:
            self.velocity.x = random.randint(-10, -5)
        elif self.velocity.y < -10:
            self.velocity.y = random.randint(-10, -5)

    def move(self):
        """
        Move the ball based on its velocity.

        :return: None
        """
        self.position += self.velocity

    def bounce_wall(self, bounce_left=False, bounce_right=False, bounce_top=False, bounce_bottom=False,
                    border_left=0, border_right=0, border_top=0, border_bottom=0):
        """
        Bounce the ball off the walls based on specified conditions.

        :param bounce_left: If True, bounce off the left wall.
        :param bounce_right: If True, bounce off the right wall.
        :param bounce_top: If True, bounce off the top wall.
        :param bounce_bottom: If True, bounce off the bottom wall.
        :param border_left: Left boundary for bouncing.
        :param border_right: Right boundary for bouncing.
        :param border_top: Top boundary for bouncing.
        :param border_bottom: Bottom boundary for bouncing.
        :return: None
        """
        if bounce_left and self.position.x - self.size < border_left and self.velocity.x < 0:
            self.velocity.x *= -1

        if bounce_right and self.position.x + self.size > border_right and self.velocity.x > 0:
            self.velocity.x *= -1

        if bounce_top and self.position.y - self.size < border_top and self.velocity.y < 0:
            self.velocity.y *= -1

        if bounce_bottom and self.position.y + self.size > border_bottom and self.velocity.y > 0:
            self.velocity.y *= -1

    def __check_corner(self, corner_a: tuple, corner_b: tuple) -> tuple[pygame.Vector2, float]:
        """
        Calculate and return the nearest corner of the object and its distance.

        :param corner_a: First corner of the polygon.
        :param corner_b: Second corner of the polygon.
        :return: Tuple containing the nearest corner (Vector2) and the distance to that corner (float).
        """
        distance_to_corner_a = math.sqrt(pow(self.position.x - corner_a[0], 2) +
                                         pow(self.position.y - corner_a[1], 2))
        distance_to_corner_b = math.sqrt(pow(self.position.x - corner_b[0], 2) +
                                         pow(self.position.y - corner_b[1], 2))
        # Compare and return value
        if distance_to_corner_a > distance_to_corner_b:
            collision_corner = pygame.math.Vector2(corner_a[0], corner_a[1])
            distance_to_corner = distance_to_corner_a
        else:
            collision_corner = pygame.math.Vector2(corner_b[0], corner_b[1])
            distance_to_corner = distance_to_corner_b

        return collision_corner, distance_to_corner

    def __reflect_on_corner(self, corner_point: pygame.Vector2):
        """
        Calculate and modify velocity of the ball when colliding with the nearest corner of polygon objects.

        :param corner_point: Nearest corner.
        :return: None
        """
        # Reflect ball in corner
        x = self.position.x - corner_point.x
        y = self.position.y - corner_point.y
        tmp = -2 * (self.velocity.x * x + self.velocity.y * y)
        coefficient = tmp / (x * x + y * y)
        self.velocity.x = self.velocity.x + coefficient * x
        self.velocity.y = self.position.y + coefficient * y

    def __reflect_on_edge(self, brick: pygame.Rect):
        """
        Calculate and modify velocity of the ball when colliding with the edge of polygon objects.

        :param brick: Polygon object which is collided with.
        :return: None
        """
        # Check collision if not corner
        if (self.position.y < brick.bottom) and (self.position.y > brick.top):
            if ((self.position.x + self.size > brick.left) and
                    (self.position.x < brick.centerx)):
                self.position.x = brick.left - self.size - 1
                self.velocity.x *= -1
                self.destroy_brick = True
            if ((self.position.x - self.size <= brick.right) and
                    (self.position.x > brick.centerx)):
                self.position.x = brick.right + self.size + 1
                self.velocity.x *= -1
                self.destroy_brick = True
        if (self.position.x > brick.left) and (self.position.x < brick.right):
            if ((self.position.y + self.size > brick.top) and
                    (self.position.y < brick.centery)):
                self.position.y = brick.top - self.size - 1
                self.velocity.y *= -1
                self.destroy_brick = True
            if ((self.position.y - self.size < brick.bottom) and
                    (self.position.y > brick.centery)):
                self.position.y = brick.bottom + self.size + 1
                self.velocity.y *= -1
                self.destroy_brick = True

    def bounce_rect(self, brick):
        """
        Bounce off any rectangle.

        :param brick: Object that ball bounces off.
        :return: None
        """
        self.destroy_brick = False

        # Calculate distance to object
        if self.position.x < brick.centerx:
            collision_corner, distance_to_corner = self.__check_corner(brick.bottomleft, brick.topleft)
        else:
            collision_corner, distance_to_corner = self.__check_corner(brick.bottomleft, brick.topleft)

        # Reflect algorithm
        if distance_to_corner < self.size:
            self.__reflect_on_corner(collision_corner)
            self.destroy_brick = True
        else:
            self.__reflect_on_edge(brick)

        # Breaking other_platform if collided
        if self.destroy_brick:
            brick.is_collided = True

    def collision(self, other_object) -> bool:
        """
        Check collision with 2D square object.

        :param other_object: 2D square object.
        :return: True if collision, False if not.
        """
        try:
            # Calculate the closest point on the rectangle to the center of the ball
            closest_x = max(other_object.left, min(self.position.x, other_object.right))
            closest_y = max(other_object.top, min(self.position.y, other_object.bottom))

            # Check if the closest point is strictly inside the rectangle
            inside_rect = closest_x == self.position.x and closest_y == self.position.y

            # Collision detected only if the closest point is strictly inside the rectangle
            return inside_rect
        except AttributeError:
            print("object is not a Rect class")

    def collision_non_side_geometry(self, other_ball: 'Ball') -> bool:
        """
        Check collision between 2D ball objects by comparing distance between them.

        :param other_ball: Another ball object.
        :return: True if collision, False if not.
        """
        dist_now = math.sqrt(pow(self.position.x - other_ball.position.x, 2) +
                             pow(self.position.y - other_ball.position.y, 2))
        dist_next = math.sqrt(pow(self.position.x + self.velocity.x -
                                  other_ball.position.x - other_ball.velocity.x, 2) +
                              pow(self.position.y + self.velocity.y -
                                  other_ball.position.y - other_ball.velocity.y, 2))
        min_dist = self.size + other_ball.size
        return (dist_now < min_dist) and (dist_next < dist_now)

    def bounce_elastic(self, other_ball: 'Ball') -> None:
        """
        Bounce with circle object only using elastic collision.

        :param other_ball: Another ball object.
        :return: None
        """
        numerator = ((self.velocity.x - other_ball.velocity.x) * (self.position.x - other_ball.position.x) +
                     (self.velocity.y - other_ball.velocity.y) * (self.position.y - other_ball.position.y))
        denominator = (pow(self.position.x - other_ball.position.x, 2) +
                       pow(self.position.y - other_ball.position.y, 2))

        temp1dx = self.velocity.x - numerator / denominator * (self.position.x - other_ball.position.x)
        temp1dy = self.velocity.y - numerator / denominator * (self.position.y - other_ball.position.y)
        temp2dx = other_ball.velocity.x - numerator / denominator * (other_ball.position.x - self.position.x)
        temp2dy = other_ball.velocity.y - numerator / denominator * (other_ball.position.y - self.position.y)

        self.velocity.x = temp1dx
        self.velocity.y = temp1dy
        other_ball.velocity.x = temp2dx
        other_ball.velocity.y = temp2dy
