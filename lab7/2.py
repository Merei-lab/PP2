import pygame

pygame.init()
pygame.mixer.init()

songs = ["mp3_1.mp3", "mp3_2.mp3", "mp3_3.mp3"]
index = 0

pygame.mixer.music.load(songs[index])
pygame.mixer.music.play()

screen = pygame.display.set_mode((400, 300))
running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                paused = not paused
            elif event.key == pygame.K_n:
                index = (index + 1) % len(songs)
                pygame.mixer.music.load(songs[index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_p:
                index = (index - 1) % len(songs)
                pygame.mixer.music.load(songs[index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()

pygame.quit()

