import pygame
import random
import math

from cls import Vectorcls,Body

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Baton-like object")

clock = pygame.time.Clock()
FPS = 60

body1 = Body(screen,540,250,20,30)
body2 = Body(screen,540,450,20,30)

running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")
    
    
    radius =200
    hori_offset = radius*math.cos(angle)
    vertical_offset = radius*math.sin(angle)

    hori_offset_b2 = radius*math.cos(-angle)
    vertical_offset_b2 = radius*math.sin(-angle)

    centerx, centery = 540, 350

    body1.position.x = centerx + hori_offset
    body1.position.y = centery + vertical_offset


    body2.position.x = centerx + hori_offset_b2
    body2.position.y = centery + vertical_offset_b2

    body1.draw()
    body2.draw()

    angle += 0.1
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()