import pygame
import random

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Line maze")

clock = pygame.time.Clock()
FPS = 60
running = True

class Line():
    def __init__(self,start:tuple,end:tuple,screen):
        self.start = start
        self.end = end
        self.color = (255,255,255)
        self.screen = screen
    def draw(self):
        pygame.draw.line(self.screen,self.color,self.start,self.end)

class Linegenerator():
    def __init__(self,screen):
        self.x1 = width / 4
        self.y1 = height / 2
        self.x2 = 3 * width / 4
        self.y2 = height / 2
        self.dx = self.x2 - self.x1
        self.dy = self.y2 - self.y1
        self.screen= screen
        main_line = Line((self.x1 ,self.y1),(self.x2,self.y2),self.screen)
        main_line.draw()

    def branching(self):
        if self.dx == 0 and self.dy > 4:
            return Line((self.x1 - self.dy / 3,self.y1),(self.x1 + self.dy / 3,self.y1),screen), Line((self.x1 - self.dy / 3,self.y2),(self.x1 + self.dy / 3,self.y2),screen)
        elif self.dy == 0 and self.dx > 4:
            return Line((self.x1, self.y1 - self.dx / 3),(self.x1, self.y1 + self.dx / 3),screen), Line((self.x2, self.y1 - self.dx / 3),(self.x2, self.y1 + self.dx / 3),screen)
    def draw_branch(self):
        line1, line2 = self.branching()
        line1.draw()
        line2.draw()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")


    line_gen = Linegenerator(screen=screen)
    line_gen.draw_branch()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()