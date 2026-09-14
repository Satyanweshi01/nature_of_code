import pygame
import random
import math
import noise

from cls import Vectorcls,Particle,Emitter

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Single particle")

clock = pygame.time.Clock()
FPS = 60


emitter = Emitter(screen,540, 350, 40, 50)
time = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")

    emitter.addParticle(None,time)
    emitter.effectParticles(Vectorcls(0,1))


    emitter.draw()    
    emitter.drawParticles()


    time += 0.01
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()