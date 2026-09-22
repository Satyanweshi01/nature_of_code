import pygame
import random
import math
class ObjectCA(CellSystem2d):
    def __init__(self):
        pass

class Body(Cell):
    def __init__(self,screen,x,y,size):
        
        self.screen = screen
        self.color = (0,0,0)
        self.size = size

    def draw(self):
        self.rect = pygame.Rect(self.position.x,self.position.y,self.size,self.size)
        pygame.draw.rect(self.screen,self.color,self.rect)

    def draw2(self):
        self.rect = pygame.Rect(self.position.x,self.position.y,self.size,self.size)
        angle = self.angle()
        rotated = pygame.transform.rotate(self.image, -math.degrees(angle))
        rotated_rect = rotated.get_rect(center=self.rect.center)
        self.screen.blit(rotated, rotated_rect)

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("2D automata")

clock = pygame.time.Clock()
FPS = 60

running = True
radius = 200
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")



    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()