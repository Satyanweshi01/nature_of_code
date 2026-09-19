import pygame
import random
import math

from cls import Vectorcls,Body

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("wanderer vehicle")

clock = pygame.time.Clock()
FPS = 60

box = Body(screen,540,350,40, 50, 0,0)

magnet = Body(screen, 0,0, 10, 100, 10,7)


running = True
radius = 200
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos_x = pos[0]
                pos_y = pos[1]
                box.position.x = pos_x
                box.position.y = pos_y
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")
    magnet.ap_forces = []#to avoid force accumulation 

    print(magnet.position.x,magnet.position.y) 
    magnet.wander()

    magnet.draw2()


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()