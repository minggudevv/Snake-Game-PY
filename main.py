# main.py

import pygame
from settings import WINDOW_SIZE, BLOCK_SIZE, BLACK, RED, WHITE
from snake import Snake
from food import Food
from score import display_score, load_high_score, save_high_score
from powerups import PowerUp
from obstacles import Obstacle

def game_loop():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()
    power_up = PowerUp()
    obstacle = Obstacle()

    high_score = load_high_score()
    score = 0

    x_change = 0
    y_change = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0

        if x_change == 0 and y_change == 0:
            continue  # Tunggu sampai pengguna menekan tombol

        snake.move(x_change, y_change)

        if snake.check_collision() or snake.snake_list[-1][0] >= WINDOW_SIZE or snake.snake_list[-1][0] < 0 or snake.snake_list[-1][1] >= WINDOW_SIZE or snake.snake_list[-1][1] < 0:
            game_over = True

        if snake.snake_list[-1][0] == food.x and snake.snake_list[-1][1] == food.y:
            food.respawn()
            snake.length += 1
            score += 1

        if snake.snake_list[-1][0] == power_up.x and snake.snake_list[-1][1] == power_up.y:
            power_up.respawn()
            score += 5  # Contoh efek power-up

        if snake.snake_list[-1][0] == obstacle.x and snake.snake_list[-1][1] == obstacle.y:
            game_over = True

        window.fill(BLACK)
        snake.draw(window)
        food.draw(window)
        power_up.draw(window)
        obstacle.draw(window)
        display_score(window, score, high_score)
        pygame.display.update()
        clock.tick(10)  # Atur kecepatan ular menjadi lebih lambat pada awalnya

    if score > high_score:
        save_high_score(score)

    # Tampilkan layar "Game Over"
    game_over_screen(window, score, high_score)

    pygame.quit()

def game_over_screen(window, score, high_score):
    font = pygame.font.SysFont(None, 50)
    small_font = pygame.font.SysFont(None, 35)

    while True:
        window.fill(BLACK)
        msg = font.render("Game Over", True, RED)
        score_msg = small_font.render(f"Score: {score}", True, WHITE)
        high_score_msg = small_font.render(f"High Score: {high_score}", True, WHITE)
        retry_msg = small_font.render("Press C to Play Again or Q to Quit", True, WHITE)
        
        window.blit(msg, [WINDOW_SIZE // 3, WINDOW_SIZE // 4])
        window.blit(score_msg, [WINDOW_SIZE // 3, WINDOW_SIZE // 2])
        window.blit(high_score_msg, [WINDOW_SIZE // 3, WINDOW_SIZE // 2 + 40])
        window.blit(retry_msg, [WINDOW_SIZE // 6, WINDOW_SIZE // 2 + 80])
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    game_loop()

if __name__ == "__main__":
    game_loop()
