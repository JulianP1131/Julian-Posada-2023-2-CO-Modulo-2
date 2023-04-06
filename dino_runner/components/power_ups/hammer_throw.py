from pygame.sprite import Sprite
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE

class HammerThrow(Sprite):
    X_POS = 140
    Y_POS = 325

    def __init__(self):
        """ super().__init__(HAMMER, HAMMER_TYPE) """
        self.hammer_rect = self.image.get_rect()
        self.hammer_rect.x = self.X_POS
        self.hammer_rect.y = self.Y_POS
    
    def update(self, game_speed, power_ups):
        self.rect.x += game_speed
        if self.rect.x > self.rect.width:
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.hammer_rect)