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
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))#(255,255,255)
        self.screen = screen
    def draw(self):
        pygame.draw.line(self.screen,self.color,self.start,self.end)

class Linegenerator():
    def __init__(self,screen,depth,x1,y1,x2,y2,linelist):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.dx = self.x2 - self.x1
        self.dy = self.y2 - self.y1
        self.screen= screen
        self.depth=depth
        self.linelist = linelist
        self.branch_gen()


    def branching(self):
        if self.dx == 0 and self.dy > 4:
            return Linegenerator(self.screen,self.depth-1,self.x1 - self.dy / 3,self.y1,self.x1 + self.dy / 3,self.y1,self.linelist), Linegenerator(self.screen,self.depth-1,self.x1 - self.dy / 3,self.y2,self.x1 + self.dy / 3,self.y2,self.linelist)
        elif self.dy == 0 and self.dx > 4:
            return Linegenerator(self.screen,self.depth-1,self.x1, self.y1 - self.dx / 3,self.x1, self.y1 + self.dx / 3,self.linelist), Linegenerator(self.screen,self.depth-1,self.x2, self.y1 - self.dx / 3,self.x2, self.y1 + self.dx / 3,self.linelist)
    def branch_gen(self):
        if self.depth <= 0:
            return 
        main_line = Line((self.x1 ,self.y1),(self.x2,self.y2),self.screen)
        line1,line2 = self.branching()
        self.linelist.append(main_line)
        line1.branch_gen()
        line2.branch_gen()


linelist = []
line_gen = Linegenerator(screen,10,width / 4,height / 2,3 * width / 4,height / 2,linelist)


while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            line_gen.branch_gen()
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")

    #line_gen.branch_gen()
    for line in line_gen.linelist:
        line.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()