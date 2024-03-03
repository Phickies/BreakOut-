import pygame
import sys


class StartMenu:

    FPS = 30

    def __init__(self, size):
        pygame.init()
        self.size = size
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

        self.main_font = pygame.font.SysFont(pygame.font.get_default_font(), 50)
        self.sub_font = pygame.font.SysFont(pygame.font.get_default_font(), 20)
        self.is_closed = False

    def handle_event(self):
        for event in pygame.event.get():
            # Exit condition
            if (event.type == pygame.QUIT or
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_e):
                self.is_closed = True

    def display(self):
        self.screen.fill((20, 20, 50))
        title_text = self.main_font.render(f"BREAK OUT?", True, (250, 250, 250))
        self.screen.blit(title_text, (self.size.x/2 - self.size.x/5, self.size.y/2-100))
        sub_text = self.sub_font.render(f"Press E to start the game?", True, (20, 100, 180))
        self.screen.blit(sub_text, (self.size.x / 2 - self.size.x/6, self.size.y / 2 + 100))

    def update(self):
        pygame.display.flip()
        self.clock.tick(self.FPS)

    def run_loop(self):
        self.handle_event()
        self.update()
        self.display()
