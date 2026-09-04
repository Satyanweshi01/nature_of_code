import pygame
import random

pygame.init()
width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Circle painter")

clock = pygame.time.Clock()
FPS = 60


class Painter():
    def __init__(self,screen):
        self.screen = screen
        self.radius = 10
    def decide(self,mu,sig):
        return random.gauss(mu,sig)
    def paint(self,sig):
        r = self.decide(190,sig*10)
        g = self.decide(190,sig*10)
        b = self.decide(190,sig*10)
        self.color = (min(255,r),min(255,g),min(255,b))
        self.position = (self.decide(500,sig*100),360)
        pygame.draw.circle(self.screen,self.color,self.position,self.radius)

class Slider():
    def __init__(self,x,y,screen):
        self.x = x #for slider pos
        self.y = y
        self.screen = screen
        self.size = 20
        self.color = (255,255,255)
        self.rect = pygame.Rect(self.x,self.y,self.size*8,self.size)
        

        self.knob_x = self.x
        self.knob_y = self.y
        self.knob_size = 10 
        self.knob_color = (0,255,0)

        self.silder_dragging = False
        
    def draw(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        self.value = (self.knob_x-800)/140
        self.knob_rect = pygame.Rect(self.knob_x,self.knob_y,self.size, self.size)
        pygame.draw.rect(self.screen,self.knob_color,self.knob_rect)


slider = Slider(800,650,screen)

painter1 = Painter(screen=screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if slider.knob_rect.collidepoint(mouse_pos):
                    slider.silder_dragging = True
        if event.type == pygame.MOUSEBUTTONUP:
            slider.silder_dragging = False
        if event.type == pygame.QUIT:
            running = False

    if slider.silder_dragging:
        mousex,mousey = pygame.mouse.get_pos()
        if mousex >= slider.x and mousex <= (slider.x+slider.size*7):
            slider.knob_x = mousex
    
    slider.draw()
    painter1.paint(sig=slider.value)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
