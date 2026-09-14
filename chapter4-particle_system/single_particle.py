import pygame
import random
import math

from cls import Vectorcls,Particle

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Single particle")

clock = pygame.time.Clock()
FPS = 60

singular_particle = Particle(screen=screen,x=540,y=0,mass=1,size=10,lifespan=255)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")
    print(singular_particle.lifespan)
    #singular_particle.ap_forces = []
    singular_particle.velocity = Vectorcls(0,5)
    #singular_particle.cal_acce()
    singular_particle.update()


    singular_particle.draw()
    if singular_particle.position.y>height:
        singular_particle.position.y=0
        singular_particle.lifespan = 255
        singular_particle.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()