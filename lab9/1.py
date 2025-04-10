import pygame
import random
import time

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

image_background = pygame.image.load('AnimatedStreet.png')
image_player = pygame.image.load('Player.png')
image_enemy = pygame.image.load('Enemy.png')
coin_image = pygame.image.load('coin.png')
mincoin = pygame.image.load('mincoin.png')
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

sound_crash = pygame.mixer.Sound('crash.wav')

font = pygame.font.SysFont("Verdana", 60)
image_game_over = font.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 5
        self.generate_random_rect()

    def generate_random_rect(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()

# Coin with random weight
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.weight = random.choice([1, 2, 3])  # 1, 2 или 3 очка
        self.random_coin()

    def random_coin(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = random.randint(-100, -40)
        self.weight = random.choice([1, 2, 3])  # Coin weight changes on respawn

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > HEIGHT:
            self.random_coin()

    def respawn(self):
        self.random_coin()

running = True
clock = pygame.time.Clock()
FPS = 60

player = Player()
enemy = Enemy()

coins = [Coin() for _ in range(3)]  # Несколько монет

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

all_sprites.add(player, enemy)
enemy_sprites.add(enemy)
for coin in coins:
    all_sprites.add(coin)
    coin_group.add(coin)

score = 0
next_speedup_score = 5  # Увеличивать скорость врага каждые 5 очков

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move()
    screen.blit(image_background, (0, 0))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(1)
        running = False
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()
        time.sleep(3)

    # Подбор монеты с учётом её веса
    for coin in coins:
        if pygame.sprite.collide_rect(player, coin):
            score += coin.weight  # Coin with different weights
            coin.respawn()

            # Увеличение скорости врага
            if score >= next_speedup_score:
                enemy.speed += 1  # Increase enemy speed
                next_speedup_score += 5

    t = pygame.font.Font(None, 50)
    tt = t.render(str(score), True, (255, 255, 255))
    screen.blit(tt, (WIDTH - 40, 8))
    screen.blit(mincoin, (WIDTH - 70, 8))

    pygame.display.flip()
    clock.tick(FPS)
