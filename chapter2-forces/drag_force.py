import pygame
import random


from vector import Mover,Vector

class Ball(Mover):
    def __init__(self,screen,x,y,mass,size):
        super().__init__(x,y)
        self.screen = screen
        self.color = (255,255,255)
        self.size = size
        self.mass = mass
    def draw(self):
        self.rect = pygame.Rect(self.position.x,self.position.y,self.size,self.size)
        pygame.draw.rect(self.screen,self.color,self.rect)


pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Ball")

clock = pygame.time.Clock()
FPS = 60

ball1 = Ball(screen=screen,x=width/1.5,y=0,mass=50,size=100)
ball2 = Ball(screen=screen,x=width/3.5,y=0,mass=10,size=50)
ball3 = Ball(screen=screen,x=width/2,y=0,mass=30,size=75)



running = True

while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("Black")

    ball1.ap_forces = []
    ball2.ap_forces = []
    ball3.ap_forces = []

    water = height/2
    waterrect = pygame.Rect(0,water,width,width)
    pygame.draw.rect(screen,(0,0,255),waterrect)

    drag_force = Vector(0,-0.01)
    if ball1.position.y + ball1.size > water :
        ball1.ap_force(drag_force)

    if ball2.position.y + ball2.size > water :
        ball2.ap_force(drag_force)

    if ball3.position.y + ball3.size > water :
        ball3.ap_force(drag_force)


    if ball1.position.y + ball1.size > height :
        ball1.position.y=height - ball1.size
        ball1.velocity.multi(0)
    if ball2.position.y + ball2.size > height :
        ball2.position.y=height - ball2.size
        ball2.velocity.multi(0)
    if ball3.position.y + ball3.size > height :
        ball3.position.y=height - ball3.size
        ball3.velocity.multi(0)

    gravity = Vector(0,0.001)
    gravity.multi(ball1.mass)
    ball1.ap_force(gravity)

    gravity = Vector(0,0.001)
    gravity.multi(ball2.mass)
    ball2.ap_force(gravity)
    
    gravity = Vector(0,0.001)
    gravity.multi(ball3.mass)
    ball3.ap_force(gravity)


    ball1.cal_acce()
    ball2.cal_acce()
    ball3.cal_acce()



    ball1.draw()
    ball2.draw()
    ball3.draw()

    
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
