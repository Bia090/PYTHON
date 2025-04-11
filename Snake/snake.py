import pygame
import random
import sys
import os

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont("Arial", 30)
big_font = pygame.font.SysFont("Arial", 50)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
COLORS = [GREEN, RED, YELLOW, BLUE, PURPLE]

HIGHSCORE_FILE = "highscore.txt"

def load_highscore():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as f:
            return int(f.read())
    return 0

def save_highscore(score):
    with open(HIGHSCORE_FILE, "w") as f:
        f.write(str(score))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def button(surface, text, x, y, w, h, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(surface, active_color, (x, y, w, h))
        if click[0] == 1 and action:
            action()
    else:
        pygame.draw.rect(surface, inactive_color, (x, y, w, h))

    draw_text(text, font, BLACK, surface, x + w / 2, y + h / 2)

def quit_game():
    pygame.quit()
    sys.exit()

def show_menu():
    while True:
        screen.fill(BLACK)
        draw_text("SNAKE GAME", big_font, GREEN, screen, WIDTH / 2, HEIGHT / 3)
        button(screen, "Start", WIDTH / 2 - 50, HEIGHT / 2, 100, 50, GREEN, YELLOW, game_loop)
        button(screen, "Quit", WIDTH / 2 - 50, HEIGHT / 2 + 70, 100, 50, RED, YELLOW, quit_game)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

def game_loop():
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = CELL_SIZE, 0

    snake = []
    snake_length = 1

    food_x = random.randrange(0, WIDTH - CELL_SIZE, CELL_SIZE)
    food_y = random.randrange(0, HEIGHT - CELL_SIZE, CELL_SIZE)

    food_color = random.choice(COLORS)
    snake_color = random.choice(COLORS)

    score = 0
    speed = 5
    highscore = load_highscore()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -CELL_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = CELL_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -CELL_SIZE
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = CELL_SIZE
                    dx = 0

        x += dx
        y += dy

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or [x, y] in snake:
            if score > highscore:
                save_highscore(score)
            show_menu()

        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - CELL_SIZE, CELL_SIZE)
            food_y = random.randrange(0, HEIGHT - CELL_SIZE, CELL_SIZE)
            food_color = random.choice(COLORS)
            snake_length += 1
            score += 1
            speed += 0.1

        snake.append([x, y])
        if len(snake) > snake_length:
            del snake[0]

        screen.fill(BLACK)
        pygame.draw.rect(screen, food_color, [food_x, food_y, CELL_SIZE, CELL_SIZE])

        # Desenăm șarpele
        for i, part in enumerate(snake):
            if i == len(snake) - 1:
                # Capul șarpelui
                pygame.draw.rect(screen, (0, 150, 0), [part[0], part[1], CELL_SIZE, CELL_SIZE])
                # Ochi pentru cap
                eye_size = 4
                pygame.draw.circle(screen, WHITE, (part[0] + 5, part[1] + 5), eye_size)
                pygame.draw.circle(screen, WHITE, (part[0] + CELL_SIZE - 5, part[1] + 5), eye_size)
            else:
                # Corpul șarpelui
                pygame.draw.rect(screen, (0, 100, 0), [part[0], part[1], CELL_SIZE, CELL_SIZE])

        draw_text(f"Score: {score}  Highscore: {highscore}", font, WHITE, screen, WIDTH / 2, 20)

        pygame.display.update()
        clock.tick(speed)

show_menu()
