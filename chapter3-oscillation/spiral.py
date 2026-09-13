import pygame
import random
import math

from cls import Vectorcls,Body

#one of the beautiful creation of mine

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("spiral")

clock = pygame.time.Clock()
FPS = 60

body1 = Body(screen,540,250,20,10)


running = True
angle = 0
speed = 0.05
radius = 1
while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed+=0.05
            if event.key == pygame.K_DOWN:
                speed-=0.05
        if event.type == pygame.QUIT:
            running = False



    hori_offset = radius*math.cos(angle)
    vertical_offset = radius*math.sin(angle)

    centerx, centery = 540, 350

    body1.position.x = centerx + hori_offset
    body1.position.y = centery + vertical_offset


    body1.draw()


    radius += speed*3
    angle += speed

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()