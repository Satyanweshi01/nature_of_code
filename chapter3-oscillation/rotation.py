import pygame
import random
import math

from cls import Vectorcls,Body

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("rotation")

clock = pygame.time.Clock()
FPS = 60
running = True



box = Body(screen, 100, 200, 20, 100)
speed = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed=-0.5
            if event.key == pygame.K_DOWN:
                speed=0.5
        if event.type == pygame.QUIT:
            running = False
    screen.fill("Black")
    
    if box.position.x > width:
        box.position.x = 0
    box.velocity = Vectorcls(3,speed)
    box.ap_forces = []
    box.cal_acce()

    #box.draw()
    box.draw2()


    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()