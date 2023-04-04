import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = random.randint(200, 300)
        self.winged = 0

    def draw(self, screen):
        if self.winged >= 9:
            self.winged = 0

        screen.blit(self.image[self.winged // 5], self.rect)
        self.winged += 1