# score.py

import pygame
from settings import WHITE

def display_score(window, score, high_score):
    font = pygame.font.SysFont(None, 35)
    score_text = font.render("Score: " + str(score), True, WHITE)
    high_score_text = font.render("High Score: " + str(high_score), True, WHITE)
    window.blit(score_text, [0, 0])
    window.blit(high_score_text, [0, 30])

def load_high_score():
    try:
        with open('high_score.txt', 'r') as file:
            return int(file.read())
    except:
        return 0

def save_high_score(high_score):
    with open('high_score.txt', 'w') as file:
        file.write(str(high_score))
