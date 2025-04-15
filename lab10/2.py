import pygame
import random
import time
import psycopg2

# === DATABASE SETUP ===
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_user",
    password="your_password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS user_scores (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    score INTEGER,
    level INTEGER
);
""")
conn.commit()

# === USER SETUP ===
username = input("Enter your username: ")
cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cursor.fetchone()

if not user:
    cursor.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cursor.fetchone()[0]
    conn.commit()
else:
    user_id = user[0]

cursor.execute("SELECT score, level FROM user_scores WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
last_state = cursor.fetchone()

# === GAME INIT ===
pygame.init()
WIDTH, HEIGHT, CELL = 600, 600, 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 20)

WHITE, YELLOW, RED, GREEN, BLACK = (255,255,255), (255,255,0), (255,0,0), (0,255,0), (0,0,0)

class Point:
    def __init__(self, x, y): self.x, self.y = x, y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0
        self.score = last_state[0] if last_state else 0
        self.level = last_state[1] if last_state else 1

    def move(self):
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
        if new_head.x < 0 or new_head.x >= WIDTH // CELL or new_head.y < 0 or new_head.y >= HEIGHT // CELL:
            return False
        if any(segment.x == new_head.x and segment.y == new_head.y for segment in self.body):
            return False
        self.body.insert(0, new_head)
        return True

    def check_collision(self, food):
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
            self.score += food.weight
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
        self.pos = Point(0, 0)
        self.weight = 1
        self.spawn_time = time.time()
        self.generate_random_pos(None)

    def generate_random_pos(self, snake):
        while True:
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)
            if not snake or not any(segment.x == self.pos.x and segment.y == self.pos.y for segment in snake.body):
                break
        self.weight = random.choice([1, 2, 3])
        self.spawn_time = time.time()

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def is_expired(self):
        return time.time() - self.spawn_time > 5

snake = Snake()
food = Food()
food.generate_random_pos(snake)
running = True
paused = False

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
            elif event.key == pygame.K_p:
                paused = not paused
                if paused:
                    cursor.execute(
                        "INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)",
                        (user_id, snake.score, snake.level)
                    )
                    conn.commit()

    if not paused:
        if not snake.move():
            running = False

        if food.is_expired():
            food.generate_random_pos(snake)

        if snake.check_collision(food):
            food.generate_random_pos(snake)

    snake.draw()
    food.draw()

    screen.blit(font.render(f"Score: {snake.score}", True, WHITE), (10, 10))
    screen.blit(font.render(f"Level: {snake.level}", True, WHITE), (10, 40))
    screen.blit(font.render(f"Food weight: {food.weight}", True, WHITE), (10, 70))

    pygame.display.flip()
    clock.tick(5 + snake.level)

pygame.quit()
conn.close()