import random

from pygame.sprite import Sprite
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_FLY_TYPE
from dino_runner.utils.constants import SCREEN_WIDTH

class HammerThrow(Sprite):
    Y_POS = 350
    X_POS = 100
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_FLY_TYPE
        self.hammer_rect = self.image.get_rect()
        self.hammer_rect.x = SCREEN_WIDTH
        self.hammer_rect.y = self.Y_POS

    def update(self, game_speed, power_ups):
        self.hammer_rect.x == game_speed
        if self.hammer_rect.x < -self.hammer_rect.width:
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.hammer_rect)