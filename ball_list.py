import pygame


class BallList:
    """
    A class representing a list of balls in a 2D space.
    """

    def __init__(self):
        self.ball_list = []

    def __str__(self):
        for i in self.ball_list:
            i.__str__()

    def update(self):
        """
        Update each ball in the list by restricting velocity, moving, and updating their lifetime.
        """
        for i in self.ball_list:
            i.restrict_velocity()
            i.move()
            i.update_lifetime()

    def display(self, screen):
        """
        Display each ball in the list on the given screen.

        :param screen: The screen to display balls on.
        """
        for i in self.ball_list:
            i.display(screen)

    def spawn_new_ball(self, position: pygame.Vector2, velocity: pygame.Vector2 = None):
        """
        Spawn a new ball at the specified position with optional initial velocity.

        :param position: The initial position of the new ball.
        :param velocity: Optional initial velocity of the new ball.
        """
        pass

    def bounce_wall(self, bounce_left=False, bounce_right=False, bounce_top=False, bounce_bottom=False,
                    border_left=0, border_right=0, border_top=0, border_bottom=0):
        """
        Bounce each ball in the list off the walls of the specified borders.

        :param bounce_left: If True, bounce off the left border.
        :param bounce_right: If True, bounce off the right border.
        :param bounce_top: If True, bounce off the top border.
        :param bounce_bottom: If True, bounce off the bottom border.
        :param border_left: Left border position.
        :param border_right: Right border position.
        :param border_top: Top border position.
        :param border_bottom: Bottom border position.
        """
        for i in self.ball_list:
            i.bounce_wall(bounce_left, bounce_right, bounce_top, bounce_bottom,
                          border_left, border_right, border_top, border_bottom)

    def bounce_rect(self, other: pygame.Rect):
        """
        Bounce each ball in the list off the specified rectangle.

        :param other: The rectangle to bounce balls off.
        """
        for i in self.ball_list:
            i.bounce_rect(other)

    def bounce_elastic(self, other: 'BallList'):
        """
        Bounce each ball in the list elastically off other balls in the given list.

        :param other: The other BallList to check for elastic collisions.
        """
        for i in self.ball_list:
            for j in other.ball_list:
                if i is not j:
                    if i.collision_non_side_geometry(j):
                        i.bounce_elastic(j)

    def transform_into(self, other: 'BallList'):
        """
        Transform each ball in the list into a different type based on the provided BallList.

        :param other: The BallList that defines the transformation.
        """
        pass
