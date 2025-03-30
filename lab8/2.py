import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Verdana", 20)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.score = 0
        self.level = 1

    def move(self):
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)

        if new_head.x < 0 or new_head.x >= WIDTH // CELL or new_head.y < 0 or new_head.y >= HEIGHT // CELL:
            return False  # Столкновение со стеной

        for segment in self.body:
            if new_head.x == segment.x and new_head.y == segment.y:
                return False  # Столкновение с самим собой

        self.body.insert(0, new_head)
        return True

    def check_collision(self, food):
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
            self.score += 1
            if self.score % 4 == 0:
                self.level += 1
            return True
        self.body.pop()
        return False

    def draw(self):
        pygame.draw.rect(screen, RED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, YELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def generate_random_pos(self, snake):
        while True:
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)
            if not any(segment.x == self.pos.x and segment.y == self.pos.y for segment in snake.body):
                break

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

FPS = 5
clock = pygame.time.Clock()

snake = Snake()
food = Food()
food.generate_random_pos(snake)

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1

    if not snake.move():
        running = False  # Останавливаем игру при столкновении

    if snake.check_collision(food):
        food.generate_random_pos(snake)

    snake.draw()
    food.draw()

    score_text = font.render(f"Score: {snake.score}", True, WHITE)
    level_text = font.render(f"Level: {snake.level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(FPS + snake.level)

pygame.quit()
