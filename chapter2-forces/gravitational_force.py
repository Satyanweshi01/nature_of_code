import pygame
import random

from vector import Mover,Vector

class Ball(Mover):
    def __init__(self,screen,x,y,mass,size):
        super().__init__(x,y)
        self.x = x
        self.y = y
        self.screen = screen
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.size = size
        self.mass = mass
    def draw(self):
        self.rect = pygame.Rect(self.position.x,self.position.y,self.size,self.size)
        pygame.draw.rect(self.screen,self.color,self.rect)

class Attractor(Ball):
    def __init__(self,screen,x,y,mass,size):
        super().__init__(screen,x,y,mass,size)
        self.color= (0,255,255)
        self.mass = mass
    def attract(self,ball:Ball):
        vecx = self.x - ball.position.x
        vecy = self.y - ball.position.y
        direction = Vector(vecx,vecy)
        dist = max(direction.mag,10)
        direction.normalize()
        force = (0.001 * self.mass * ball.mass)/(dist*dist)
        force_vector = direction.multi(force)
        ball.ap_force(direction)

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Ball")

clock = pygame.time.Clock()
FPS = 60

ball1 = Attractor(screen=screen,x=width/2,y=height/2,mass=100,size=100)
ball2 = Ball(screen=screen,x=0,y=0,mass=10,size=20)
ball3 = Ball(screen=screen,x=0,y=height,mass=30,size=40)
ball4 = Ball(screen=screen,x=width,y=0,mass=50,size=60)


running = True

while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("Black")


    ball2.ap_forces = []
    ball3.ap_forces = []
    ball4.ap_forces = []

    ball1.attract(ball2)
    ball1.attract(ball3)
    ball1.attract(ball4)



    ball2.cal_acce()
    ball3.cal_acce()
    ball4.cal_acce()



    ball1.draw()
    ball2.draw()
    ball3.draw()
    ball4.draw()

    
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
