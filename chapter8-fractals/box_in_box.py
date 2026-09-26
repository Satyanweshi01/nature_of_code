import pygame
import random

class Box():
    def __init__(self,x,y,size,screen):
        self.x = x
        self.y = y
        self.size = size
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.screen = screen
    def draw(self):
        self.rect = pygame.Rect(self.x,self.y,self.size,self.size)
        pygame.draw.rect(self.screen,self.color,self.rect)

class BoxGenerator():
    def __init__(self, max_size, screen):
        self.max_size = max_size
        self.screen = screen

    def box_draw(self):
        size = self.max_size
        factor = self.max_size/8
        x =0
        y =0

        while size >= 2:
            box = Box(x,y,size, self.screen)
            box.draw()
            size /= 2
            x += factor
            y += factor



pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Blinding lights")

clock = pygame.time.Clock()
FPS = 60
running = True

box_generator = BoxGenerator(1000,screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")

    box_generator.box_draw()


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()