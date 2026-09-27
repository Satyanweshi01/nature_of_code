from cls import Vectorcls
import pygame

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("The Tree fractal")

segments = []
class TreeGenerator():
    def __init__(self,a:Vectorcls,b:Vectorcls,angle,length_red_multiplier):
        self.start = a
        self.end = b
        self.angle = angle
        self.length_red_multiplier = length_red_multiplier
    def draw(self):
        for line in segments:
            pygame.draw.line(screen,(255,255,255),(line.start.x,line.start.y),(line.end.x,line.end.y))
    def childlength(self):
        parent_length = Vectorcls.sub(self.end,self.start)
        parent_mag = parent_length.mag()
        return parent_length*self.length_red_multiplier

    def generate(self):
        parent_angle = Vectorcls.sub(self.end,self.start).normalize()
        Vectorcls.rotate()

clock = pygame.time.Clock()
FPS = 60
running = True

tree_gen = TreeGenerator(Vectorcls(width/2,600),Vectorcls(width/2,400),60,0.8)
segments.append(TreeGenerator(Vectorcls(width/2,600),Vectorcls(width/2,400),60,0.8))

    
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            segments = koch.generate(segments)
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")
    tree_gen.draw()


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()