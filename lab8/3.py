import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((255, 255, 255))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
current_color = colorBLACK

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

currX = 0
currY = 0
prevX = 0
prevY = 0

draw_mode = "rectangle"  

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

running = True

while running:
    screen.blit(base_layer, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX, prevY = event.pos
        if event.type == pygame.MOUSEMOTION and LMBpressed:
            currX, currY = event.pos
            screen.blit(base_layer, (0, 0))
            if draw_mode == "rectangle":
                pygame.draw.rect(screen, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            elif draw_mode == "circle":
                radius = max(abs(currX - prevX), abs(currY - prevY)) // 2
                pygame.draw.circle(screen, current_color, (prevX, prevY), radius, THICKNESS)
            elif draw_mode == "free_draw":
                pygame.draw.line(base_layer, current_color, (prevX, prevY), (currX, currY), THICKNESS)
                prevX, prevY = currX, currY
            elif draw_mode == "eraser":
                pygame.draw.line(base_layer, colorWHITE, (prevX, prevY), (currX, currY), THICKNESS * 2)
                prevX, prevY = currX, currY
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX, currY = event.pos
            if draw_mode == "rectangle":
                pygame.draw.rect(base_layer, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            elif draw_mode == "circle":
                radius = max(abs(currX - prevX), abs(currY - prevY)) // 2
                pygame.draw.circle(base_layer, current_color, (prevX, prevY), radius, THICKNESS)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)
            if event.key == pygame.K_r:
                draw_mode = "rectangle"
            if event.key == pygame.K_c:
                draw_mode = "circle"
            if event.key == pygame.K_f:
                draw_mode = "free_draw"
            if event.key == pygame.K_e:
                draw_mode = "eraser"
            if event.key == pygame.K_1:
                current_color = colorBLACK
            if event.key == pygame.K_2:
                current_color = colorRED
            if event.key == pygame.K_3:
                current_color = colorBLUE
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
