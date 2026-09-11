import pygame
import random
import math

from cls import Vectorcls,Body

class Canon(Body):
    def __init__(self,screen,x,y,mass,size):
        super().__init__(screen,x,y,mass,size)
    
    def create_ball(self)->Body:
        ball = Body(self.screen,self.x,self.y,self.mass,self.size)
        return ball


pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Canon")

clock = pygame.time.Clock()
FPS = 60

canon = Canon(screen,1,400,20,50)

running = True
balls=[]
while running:
    pos=0

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos_x = pos[0]
                pos_y = pos[1]
                ball = canon.create_ball()
                new_x = pos_x-ball.x
                new_y = pos_y-ball.y

                sudden_force = Vectorcls(new_x/100,new_y/100)
                ball.ap_force(sudden_force)
                if ball not in balls:
                    balls.append(ball)

        if event.type == pygame.QUIT:
            running = False
    

    screen.fill("Black")

    for i in balls:
        gravity = Vectorcls(0,0.098)
        i.ap_force(
            gravity
        )
        i.cal_acce()
        i.draw()
        if i.x > 720:
            i.x = 710
            i.acceleration = 0
            i.velocity = 0

        if i.y > 1080:
            i.y = 1070
            i.acceleration = 0
            i.velocity = 0
    canon.draw()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()