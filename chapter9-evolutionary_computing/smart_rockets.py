import pygame
import random
import math

from cls import GA,DNA,Body

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Smart Rockets")

clock = pygame.time.Clock()
FPS = 60

targeting_block = Body(screen,0,0,100,100,0,DNA(0))
ga = GA(targeting_block,10,50,100,screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")
    targeting_block.draw()
    ga.fitness_cal()
    ga.fitness_normalize()
    ga.selection()
    ga.live()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()