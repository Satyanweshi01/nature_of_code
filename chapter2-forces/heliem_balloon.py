import pygame
import random
import noise

from vector import Mover,Vector

class Balloon(Mover):
    def __init__(self,screen,x,y):
        super().__init__(x,y)
        self.screen = screen
        self.color = (255,255,255)
        self.size = 100
    def draw(self):
        self.rect = pygame.Rect(self.position.x,self.position.y,self.size,self.size)
        pygame.draw.rect(self.screen,self.color,self.rect)


pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Heliem Balloon")

clock = pygame.time.Clock()
FPS = 60

balloon = Balloon(screen=screen,x=width/2,y=height/2)



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("Black")
    balloon.ap_forces = []
    time = pygame.time.get_ticks()/100000

    if balloon.position.x < 0 :
        balloon.position.x=0
        balloon.velocity.multi(-1)

    elif balloon.position.x > width:
        balloon.position.x=width
        balloon.velocity.multi(-1)

    elif balloon.position.y < 0 :
        balloon.position.y=0
        balloon.velocity.multi(-1)

    elif balloon.position.y > height:
        balloon.position.y=height
        balloon.velocity.multi(-1)
    else:
        levitation = Vector(0,-0.05)
        balloon.ap_force(levitation)

    windforce = Vector(-noise.pnoise1(time)/50,noise.pnoise1(time)/50)
    balloon.ap_force(windforce)




    balloon.cal_acce()

    balloon.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
