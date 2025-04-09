import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((255, 255, 255))

colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
current_color = colorBLACK

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5
currX = currY = prevX = prevY = 0

draw_mode = "rectangle"

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def draw_right_triangle(surface, color, x1, y1, x2, y2, width):
    pygame.draw.polygon(surface, color, [(x1, y1), (x2, y2), (x1, y2)], width)

def draw_equilateral_triangle(surface, color, x1, y1, x2, y2, width):
    side = min(abs(x2 - x1), abs(y2 - y1))
    x3 = x1 + side / 2
    y3 = y1 - math.sqrt(3) / 2 * side
    pygame.draw.polygon(surface, color, [(x1, y1), (x1 + side, y1), (x3, y3)], width)

def draw_rhombus(surface, color, x1, y1, x2, y2, width):
    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
    points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
    pygame.draw.polygon(surface, color, points, width)

def draw_square(surface, color, x1, y1, x2, y2, width):
    size = min(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(x1, y1, size, size)
    rect.normalize()
    pygame.draw.rect(surface, color, rect, width)

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
            elif draw_mode == "square":
                draw_square(screen, current_color, prevX, prevY, currX, currY, THICKNESS)
            elif draw_mode == "right_triangle":
                draw_right_triangle(screen, current_color, prevX, prevY, currX, currY, THICKNESS)
            elif draw_mode == "equilateral_triangle":
                draw_equilateral_triangle(screen, current_color, prevX, prevY, currX, currY, THICKNESS)
            elif draw_mode == "rhombus":
                draw_rhombus(screen, current_color, prevX, prevY, currX, currY, THICKNESS)
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
            ############
            elif draw_mode == "square":
                draw_square(base_layer, current_color, prevX, prevY, currX, currY, THICKNESS)
            elif draw_mode == "right_triangle":
                draw_right_triangle(base_layer, current_color, prevX, prevY, currX, currY, THICKNESS)
            elif draw_mode == "equilateral_triangle":
                draw_equilateral_triangle(base_layer, current_color, prevX, prevY, currX, currY, THICKNESS)
            elif draw_mode == "rhombus":
                draw_rhombus(base_layer, current_color, prevX, prevY, currX, currY, THICKNESS)
            ############

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)
            if event.key == pygame.K_r:
                draw_mode = "rectangle"
            if event.key == pygame.K_c:
                draw_mode = "circle"
            if event.key == pygame.K_e:
                draw_mode = "eraser"
            if event.key == pygame.K_f:
                draw_mode = "free_draw"
            ######
            if event.key == pygame.K_s:
                draw_mode = "square"   
            if event.key == pygame.K_t:
                draw_mode = "right_triangle"
            if event.key == pygame.K_q:
                draw_mode = "equilateral_triangle"
            if event.key == pygame.K_h:
                draw_mode = "rhombus"
            #####
            if event.key == pygame.K_1:
                current_color = colorBLACK
            if event.key == pygame.K_2:
                current_color = colorRED
            if event.key == pygame.K_3:
                current_color = colorBLUE

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
