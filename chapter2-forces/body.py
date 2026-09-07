import pygame
import random

from newvector import Vectorcls,Mover

class Body(Mover):
    def __init__(self,screen,x,y,mass,size):
        super().__init__(x,y,mass)
        self.screen = screen
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.size = size
    def draw(self):
        self.rect = pygame.Rect(self.position.x,self.position.y,self.size,self.size)
        pygame.draw.rect(self.screen,self.color,self.rect)

class Attractor(Body):
    def __init__(self,screen,x,y,mass,size):
        super().__init__(screen,x,y,mass,size)
        self.color= (0,255,255)
    def attract(self,body:Body):
        direction = Vectorcls.sub(self.position,body.position)
        dist = max(direction.mag(),10)
        normalized = direction.normalize()
        force = (10 * self.mass * body.mass)/(dist*dist)
        force_vector = Vectorcls.multi(normalized,force)
        body.ap_force(force_vector)


pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("n body")

clock = pygame.time.Clock()
FPS = 60


body1 = Attractor(screen=screen,x=width/2,y=height/2,mass=80,size=100)
body2 = Body(screen=screen,x=0,y=0,mass=10,size=20)
body3 = Body(screen=screen,x=0,y=height,mass=20,size=40)
body4 = Body(screen=screen,x=width,y=0,mass=40,size=60)




running = True

while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")

    body2.ap_forces = []
    body3.ap_forces = []
    body4.ap_forces = []


    body1.attract(body2)
    body1.attract(body3)
    body1.attract(body4)



    body2.cal_acce()
    body3.cal_acce()
    body4.cal_acce()

    print(body2.acceleration.x,body2.velocity.x,body2.position.x)

    body1.draw()
    body2.draw()
    body3.draw()
    body4.draw()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()