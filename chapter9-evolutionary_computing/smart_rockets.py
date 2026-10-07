import pygame
import random
import math

from cls import GA,DNA,Body,text

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Smart Rockets")

clock = pygame.time.Clock()
FPS = 60

targeting_block = Body(screen,0,0,100,100,0,DNA(0))
ga = GA(target=targeting_block,populationSize=50,mulationRate=0.2,lifespan=200,screen=screen)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            targeting_block.position.x = pos[0]
            targeting_block.position.y = pos[1]
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")
    text(f"Population Size: {ga.populationSize}",screen,(255,255,255),600,20)
    text(f"Mulation Rate: {ga.mulationRate}",screen,(255,255,255),600,60)
    text(f"Generation: {ga.gen}",screen,(255,255,255),600,100)
    text(f"Average Fitness(pgen): {ga.avg_fitness}",screen,(255,255,255),600,140)
    targeting_block.draw()
    ga.live()



    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()