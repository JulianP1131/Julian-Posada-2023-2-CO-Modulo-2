import pygame
import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleMannager:
    def __init__(self):
        self.obstacles = []
        self.counter = 0
        self.winged = 0

    def update(self, game):
        if len(self.obstacles) == 0:
            if self.counter % 2 == 0:
                cactus = Cactus(SMALL_CACTUS)
                self.obstacles.append(cactus)
                self.counter += random.randint(0, 7)
            elif self.counter % 5 == 0:
                cactus = Cactus(LARGE_CACTUS)
                self.obstacles.append(cactus)
                self.counter += random.randint(0, 7)
            else:
                bird = Bird(BIRD)
                self.obstacles.append(bird)
                self.counter += random.randint(0, 7)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)