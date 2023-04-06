import pygame
import random

from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE, DEFAULT_TYPE
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpMannager:
    def __init__(self):
        self.power_ups = []

        self.duration = random.randint(3, 5)
        self.when_appears = random.randint(50, 70)
        self.counter = random.randint(0,1)

    def update(self, game):
        if len(self.power_ups) == 0 and self.when_appears == game.score.count:
            self.generate_power_up(game)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                if self.counter == 0:
                    self.power_ups.remove(power_up)
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.has_power_up = True
                    game.player.type = SHIELD_TYPE
                    game.player.power_up_time = power_up.start_time + (self.duration * 1000)
                elif self.counter == 1:
                    self.power_ups.remove(power_up)
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.has_power_up = True
                    game.player.type = HAMMER_TYPE
                    game.player.power_up_time = power_up.start_time + (self.duration * 1000)
                self.counter = random.randint(0,1)    

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
            

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(50, 70)
        self.counter = random.randint(0,1)

    def generate_power_up(self, game):
        self.when_appears = random.randint(200 + game.score.count, game.score.count + 300)
        if self.counter == 0:
            power_up = Shield()
            self.power_ups.append(power_up)
        elif self.counter == 1:
            power_up = Hammer()
            self.power_ups.append(power_up)

        