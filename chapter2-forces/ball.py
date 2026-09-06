import pygame
import random
import noise

from vector import Mover,Vector

class Ball(Mover):
    def __init__(self,screen,x,y,mass,cof,size):
        super().__init__(x,y)
        self.screen = screen
        self.color = (255,255,255)
        self.size = size
        self.mass = mass
        self.cof = cof
        self.dragging = False
    def draw(self):
        self.rect = pygame.Rect(self.position.x,self.position.y,self.size,self.size)
        pygame.draw.rect(self.screen,self.color,self.rect)


pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Ball")

clock = pygame.time.Clock()
FPS = 60

ball1 = Ball(screen=screen,x=width/2.5,y=height/2,mass=50,cof=0.4,size=100)
ball2 = Ball(screen=screen,x=width/1.5,y=height/2,mass=10,cof=0.8,size =50)



running = True

while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if ball1.rect.collidepoint(mouse_pos):
                    ball1.dragging = True
                if ball2.rect.collidepoint(mouse_pos):
                    ball2.dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            ball1.dragging = False
            ball2.dragging = False
        if event.type == pygame.QUIT:
            running = False
    screen.fill("Black")
    if ball1.dragging:
        ball1.position.x = mouse_pos[0]
        ball1.position.y = mouse_pos[1]
    
    elif ball2.dragging:
        ball2.position.x = mouse_pos[0]
        ball2.position.y = mouse_pos[1]
    else:
        ball1.ap_forces = []
        ball2.ap_forces = []


        gravity = Vector(0,0.3)
        gravity.multi(ball1.mass)
        ball1.ap_force(gravity)

        gravity = Vector(0,0.3)
        gravity.multi(ball2.mass)
        ball2.ap_force(gravity)



        ball1.cal_acce()
        ball2.cal_acce()

        if ball1.position.y + ball1.size > height :
            ball1.position.y=height - ball1.size
            ball1.velocity.y *= -ball1.cof
        if ball2.position.y + ball2.size > height :
            ball2.position.y=height - ball2.size
            ball2.velocity.y *= -ball2.cof


    ball1.draw()
    ball2.draw()

    
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
