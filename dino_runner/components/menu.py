import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT


class Menu:
    half_screen_width = SCREEN_WIDTH // 2
    half_screen_height = SCREEN_HEIGHT // 2

    def __init__(self, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)

    def update(self, game):
        self.handle_events_on_menu(game)
        pygame.display.update()

    def draw(self, screen, message, x=half_screen_width, y=half_screen_height):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x, y)
        screen.blit(self.text, self.text_rect)

    def deth_message(self, screen, message, x = half_screen_width, y = half_screen_height):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x, y)
        screen.blit(self.text, self.text_rect)
    
    def score_message(self, screen, message, x = half_screen_width, y = half_screen_height):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x, y)
        screen.blit(self.text, self.text_rect)
    
    def high_score_message(self, screen, message, x = half_screen_width, y = half_screen_height):
        self.text = self.font.render(message, True, (0, 255, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x, y)
        screen.blit(self.text, self.text_rect)

    def power_up_message(self, screen, message, x=half_screen_width, y=half_screen_height):
        self.text = self.font.render(message, True, (241, 241, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x, y)
        screen.blit(self.text, self.text_rect)
    
    def power_up_message_2(self, screen, message, x=half_screen_width, y=half_screen_height):
        self.text = self.font.render(message, True, (255, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x, y)
        screen.blit(self.text, self.text_rect)

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            elif event.type == pygame.KEYDOWN:
                game.run()
