# powerups.py

import pygame
import random
from settings import BLOCK_SIZE, RED, WINDOW_SIZE

class PowerUp:
    def __init__(self):
        self.x = round(random.randrange(0, WINDOW_SIZE - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = round(random.randrange(0, WINDOW_SIZE - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    def draw(self, window):
        pygame.draw.rect(window, RED, [self.x, self.y, BLOCK_SIZE, BLOCK_SIZE])

    def respawn(self):
        self.x = round(random.randrange(0, WINDOW_SIZE - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = round(random.randrange(0, WINDOW_SIZE - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
