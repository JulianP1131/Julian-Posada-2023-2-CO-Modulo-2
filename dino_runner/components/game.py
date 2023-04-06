import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, HAMMER, HAMMER_FLY_TYPE
from dino_runner.components.counter import Counter
from dino_runner.components.menu import Menu
from dino_runner.components.obstacles.obstacle_manager import ObstacleMannager
from dino_runner.components.power_ups.power_up_mannager import PowerUpMannager
from dino_runner.components.dinosaur import Dinosour
from dino_runner.components.power_ups.hammer_throw import HammerThrow



class Game:
    GAME_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON[0])
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosour()
        self.obstacle_manager = ObstacleMannager()
        self.menu = Menu(self.screen)
        self.running = False
        self.score = Counter()
        self.death_count = Counter()
        self.highest_score = Counter()
        self.hammer_throw = HammerThrow()
        self.power_up_mannager = PowerUpMannager()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def execute(self):
        self.running = True
        # mientras la aplicacion corra
        while self.running:
            # y si no estoy jugando
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.hammer_throw.update(self.update_score, self.power_up)
        self.power_up_mannager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_mannager.draw(self.screen)
        self.power_up()
        self.hammer_throw.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        self.screen.blit(ICON[0], (half_screen_width - 50, half_screen_height - 140))
        if self.death_count.count == 0:
            self.menu.draw(self.screen, 'Press any key to start')
        else:
            self.update_highest_score()
            self.screen.blit(ICON[1], (half_screen_width - 50, half_screen_height - 140))
            self.screen.blit(ICON[2], (half_screen_width - 200, half_screen_height - 20))
            self.menu.score_message(self.screen, f'Score: {self.score.count}', half_screen_width, 350)
            self.menu.deth_message(self.screen, f'Deaths: {self.death_count.count}', half_screen_width, 400)
            self.menu.high_score_message(self.screen, f'Highest Score: {self.highest_score.count}', half_screen_width, 500)
            self.menu.score_message(self.screen, f'Press any key to start...', half_screen_width, 100)
        self.menu.update(self)

    def update_score(self):
        self.score.update()
        if self.score.count % 100 == 0 and self.game_speed < 40:
            self.game_speed += 2

        if self.score.count == 1500:
            self.game_speed = 45
        elif self.score == 3000:
            self.game_speed = 50
        elif self.score.count == 5000:
            self.game_speed = 55

    def update_highest_score(self):
        if self.score.count > self.highest_score.count:
            self.highest_score.set_count(self.score.count)

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.score.reset()
        self.game_speed = self.GAME_SPEED
        self.player.reset()
        self.power_up_mannager.reset_power_ups()
        
    def power_up(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.menu.power_up_message(self.screen, f'{self.player.type.capitalize()} enabled for {time_to_show} seconds', 500, 50)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE