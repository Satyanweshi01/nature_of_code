import pygame
import random
import noise

from vector import Mover,Vector

class Ball(Mover):
    def __init__(self,screen,x,y,mass,cof):
        super().__init__(x,y)
        self.screen = screen
        self.color = (255,255,255)
        self.size = 50
        self.mass = mass
        self.cof = cof
    def draw(self):
        self.rect = pygame.Rect(self.position.x,self.position.y,self.size,self.size)
        pygame.draw.rect(self.screen,self.color,self.rect)


pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Ball")

clock = pygame.time.Clock()
FPS = 60

ball1 = Ball(screen=screen,x=width/2.5,y=height/2,mass=10,cof=0.1)
ball2 = Ball(screen=screen,x=width/1.5,y=height/2,mass=20,cof=0.3)



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("Black")
    ball1.ap_forces = []

    if ball1.position.y > height :
        ball1.position.y=height
        ball1.velocity.y*=ball1.cof
        ball1.velocity.multi(-1)
        


    gravity = Vector(0,0.02)
    ball1.ap_force(gravity)



    ball1.cal_acce()

    ball1.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
