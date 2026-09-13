import math
import random
import pygame
class Vectorcls():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(vec1:Vectorcls,vec2:Vectorcls):
        vecx = vec1.x+vec2.x
        vecy = vec1.y+vec2.y
        return Vectorcls(vecx,vecy)
    def sub(vec1:Vectorcls,vec2:Vectorcls):
        vecx = vec1.x-vec2.x
        vecy = vec1.y-vec2.y
        return Vectorcls(vecx,vecy)
    def multi(vec1:Vectorcls,scalar):
        vecx = vec1.x*scalar
        vecy = vec1.y*scalar
        return Vectorcls(vecx,vecy)
    def div(vec1:Vectorcls,scalar):
        vecx = vec1.x/scalar
        vecy = vec1.y/scalar
        return Vectorcls(vecx,vecy)

    def limit(self,maxi):
        if self.mag() > maxi:
            scale = maxi/self.mag()
            self.x*=scale
            self.y*=scale

    def mag(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    def normalize(self):
        if self.mag() != 0:
            return Vectorcls.div(self,self.mag())

class Mover():
    def __init__(self,x,y,mass):
        self.x =x
        self.y =y
        self.position = Vectorcls(x,y)
        self.velocity = Vectorcls(0,0)
        self.acceleration = Vectorcls(0,0)
        self.mass = mass
        self.ap_forces = []
    def cal_acce(self):
        self.acceleration = Vectorcls.multi(self.acceleration,0)
        for i in self.ap_forces:
            i = Vectorcls.div(i,self.mass)
            self.acceleration = Vectorcls.add(self.acceleration,i)
        self.update()
    def ap_force(self,force:Vectorcls):
        if force not in self.ap_forces:
            self.ap_forces.append(force)
    def update(self):
        self.velocity = Vectorcls.add(self.acceleration,self.velocity)
        self.position = Vectorcls.add(self.velocity,self.position)
    def angle(self):
        return math.atan(self.velocity.y/self.velocity.x) if self.velocity.x > 0 else 0

        
class Body(Mover):
    def __init__(self,screen,x,y,mass,size):
        super().__init__(x,y,mass)
        self.screen = screen
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.size = size
        self.image = pygame.image.load("arrow.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))

    def draw(self):
        self.rect = pygame.Rect(self.position.x,self.position.y,self.size,self.size)
        pygame.draw.rect(self.screen,self.color,self.rect)

    def draw2(self):
        self.rect = pygame.Rect(self.position.x,self.position.y,self.size,self.size)
        angle = self.angle()
        rotated = pygame.transform.rotate(self.image, -math.degrees(angle))
        rotated_rect = rotated.get_rect(center=self.rect.center)
        self.screen.blit(rotated, rotated_rect)

def text(string,screen, text_color, x, y):
    font = pygame.font.SysFont("Arial", 30)
    img = font.render(string, True, text_color)
    screen.blit(img,(x,y))
        