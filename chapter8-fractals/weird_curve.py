from cls import Vectorcls
import pygame

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("The weird curve")

clock = pygame.time.Clock()
FPS = 60
running = True
segments = []
class Kochline():
    def __init__(self,a:Vectorcls,b:Vectorcls):
        self.start = a
        self.end = b
    def draw(self):
        for line in segments:
            pygame.draw.line(screen,(255,255,255),(line.start.x,line.start.y),(line.end.x,line.end.y))
    def koch_points(self):
        a = self.start
        e = self.end
        v = Vectorcls.sub(e,a)
        line_size = Vectorcls.div(v,3)
        b = Vectorcls.add(self.start,line_size)
        d = Vectorcls.sub(self.end,line_size)
        line_size = Vectorcls.setDir(line_size,3.14/3)
        c = Vectorcls.add(b,line_size)
        return [a,b,c,d,e]
    def generate(self,segments):
        next_seg = []
        for segment in segments:
            kochPoints = segment.koch_points()
            next_seg.append(Kochline(kochPoints[0],kochPoints[1]))
            next_seg.append(Kochline(kochPoints[1],kochPoints[2]))
            next_seg.append(Kochline(kochPoints[2],kochPoints[3]))
            next_seg.append(Kochline(kochPoints[3],kochPoints[4]))
        return next_seg



koch = Kochline(Vectorcls(0,200),Vectorcls(width,200))
segments.append(Kochline(Vectorcls(0,200),Vectorcls(width,200)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            segments = koch.generate(segments)
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")
    

    koch.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()