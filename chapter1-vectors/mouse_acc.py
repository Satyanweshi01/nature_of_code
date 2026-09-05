import random
import pygame
import math

pygame.init()


width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Mouse Acceleration Car")

clock = pygame.time.Clock()
FPS = 60

class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.mag = math.sqrt(self.x*self.x + self.y*self.y)
    def add(self,vec:Vector):
        self.x+=vec.x
        self.y+=vec.y
    def sub(self,vec):
        self.x-=vec.x
        self.y-=vec.y
    def limit(self,maxi):
        if self.mag >maxi:
            self.mag = maxi

class Car():
    def __init__(self,screen):
        self.position = Vector(540,360)
        self.velocity = Vector(0,0)
        self.acceleration = Vector(0,0)
        self.screen = screen
        self.color = (255,255,255)
        self.size = 20
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(10)
        self.position.add(self.velocity)
        self.rect = pygame.Rect(self.position.x,self.position.y,self.size,self.size)
        pygame.draw.rect(self.screen,self.color,self.rect)
def text(string,screen, text_color, x, y):
    font = pygame.font.SysFont("Arial", 30)
    img = font.render(string, True, text_color)
    screen.blit(img,(x,y))
        
car = Car(screen)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    screen.fill("BLACK")


    text(f"Velocity = {str(car.velocity.x)}",screen,(255,255,255),100,100)
    text(f"Acceration = {str(car.acceleration.x)}",screen,(255,255,255),800,100)

    car.acceleration = Vector((mouse_x-car.position.x)/10000,(mouse_y-car.position.y)/10000)
    car.update()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()