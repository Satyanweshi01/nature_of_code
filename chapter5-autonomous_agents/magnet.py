import pygame
import random
import math

from cls import Vectorcls,Body

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("spiral")

clock = pygame.time.Clock()
FPS = 60

box = Body(screen,540,350,40, 50, 0,0)
magnet = Body(screen, 0,0, 10, 10, 10,10)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")
    box.draw()
    magnet.seek(box.position)

    magnet.draw()


    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()