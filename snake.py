# snake.py

import pygame
from settings import BLOCK_SIZE, WHITE, WINDOW_SIZE

class Snake:
    def __init__(self):
        self.snake_list = [[WINDOW_SIZE // 2, WINDOW_SIZE // 2]]  # Posisi awal ular di tengah
        self.length = 1

    def draw(self, window):
        for block in self.snake_list:
            pygame.draw.rect(window, WHITE, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

    def move(self, x_change, y_change):
        snake_head = [self.snake_list[-1][0] + x_change, self.snake_list[-1][1] + y_change]
        self.snake_list.append(snake_head)
        if len(self.snake_list) > self.length:
            del self.snake_list[0]

    def check_collision(self):
        head = self.snake_list[-1]
        for block in self.snake_list[:-1]:
            if block == head:
                return True
        return False
