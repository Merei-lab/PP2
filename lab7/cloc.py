import pygame
import sys
import datetime

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("MyGame")

clock_surf=pygame.image.load('clock.png')
minu_surf=pygame.image.load('min_hand.png')
sec_surf=pygame.image.load('sec_hand.png')

clock_rect=clock_surf.get_rect(center=(400,300))

clock=pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    now=datetime.datetime.now()
    sec_angle = -now.second * 6 + 90
    min_angle = -now.minute * 6 - now.second * 0.1 
    

    rotate_min=pygame.transform.rotate(minu_surf,min_angle)
    rotate_sec=pygame.transform.rotate(sec_surf,sec_angle)

    min_rect=rotate_min.get_rect(center=clock_rect.center)
    sec_rect=rotate_sec.get_rect(center=clock_rect.center)
    screen.fill((255,255,255))
    screen.blit(clock_surf,clock_rect)
    screen.blit(rotate_min,min_rect)
    screen.blit(rotate_sec,sec_rect)

    pygame.display.update()
    clock.tick(60)