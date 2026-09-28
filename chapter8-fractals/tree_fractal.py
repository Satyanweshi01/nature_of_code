from cls import Vectorcls
import pygame
import math
import random

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("The Tree fractal")

clock = pygame.time.Clock()
FPS = 60
running = True

r= 0.67
deltaangle= math.pi/6

def line(screen, x, y, length, angle):
    if (length <= 10):
        return
    x2 = x - length*math.sin(angle)
    y2 = y - length*math.cos(angle)
    pygame.draw.line(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(x,y),(x2,y2))
    line(screen, x2, y2, length*r, angle+deltaangle)
    line(screen, x2, y2, length*r, angle-deltaangle)
    
mouse_pos_y=math.pi*2
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_x = (mouse_pos[1]/width)*150

    line(screen, width/2, height, mouse_pos_x, mouse_pos_y)
    
    r = (mouse_pos[0]/500)*0.4


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()