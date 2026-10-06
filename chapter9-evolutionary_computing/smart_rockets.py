import pygame
import random
import math

from cls import Body

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Smart Rockets")

clock = pygame.time.Clock()
FPS = 60

targeting_block = Body(screen,540,320,100,100,0)
rocket = Body(screen, 0, 0,10,10,targeting_block) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()