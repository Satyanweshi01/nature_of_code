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
    balloon.ap_forces = []
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                vecx =(mouse_pos[0]-balloon.position.x)
                vecy = (mouse_pos[1]-balloon.position.y)
                windforce = Vector(-vecx/100,-vecy/100)
                balloon.ap_force(windforce)

        if event.type == pygame.QUIT:

            running = False
    screen.fill("Black")

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






    balloon.cal_acce()
    print(balloon.acceleration.mag)
    balloon.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
