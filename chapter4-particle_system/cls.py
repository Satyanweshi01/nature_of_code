import math
import random
import pygame
import noise
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

class Particle(Body):
    def __init__(self,screen,x,y,mass,size,lifespan,time):
        super().__init__(screen,x,y,mass,size)
        self.time = time
        self.velocity = Vectorcls(random.choice([noise.pnoise1(self.time)*2,-noise.pnoise1(self.time)*2]),random.choice([noise.pnoise1(self.time)*8,-noise.pnoise1(self.time)*8]))
        self.lifespan = lifespan
    def update(self):
        super().update()
        self.lifespan -= 2
    def isalive(self):
        # if self.lifespan >= 0:
        #     return False
        # else:
        #     return True
        return self.lifespan>=0
    def draw(self):
        if self.isalive():
            super().draw()
    def run(self):
        if self.isalive():
            self.draw()
            self.update()


class Emitter(Body):
    def __init__(self,screen,x,y,mass,size):
        super().__init__(screen,x,y,mass,size)
        self.particles = []

    def addParticle(self,particle:Particle,time):
        if particle is None:
            particle = Particle(self.screen,self.x,self.y,10,10,255,time)
        if particle not in self.particles:
            self.particles.append(particle)
    def effectParticles(self,acc:Vectorcls):
        for i in self.particles:
            i.ap_forces =[]
            i.ap_force(acc)
            i.cal_acce()
    def drawParticles(self):
        for i in self.particles[::-1]:
            i.draw()


def text(string,screen, text_color, x, y):
    font = pygame.font.SysFont("Arial", 30)
    img = font.render(string, True, text_color)
    screen.blit(img,(x,y))
        