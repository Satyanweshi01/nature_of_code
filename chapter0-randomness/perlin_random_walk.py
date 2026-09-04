import random
import pygame
import math

class PerlinNoise():
    def __init__(self):
        self.storage = {}

    def __fade(self)->int:
        self.t = self.num -  self.left_num
        return 6*((self.t)**5) - 15*((self.t)**4) + 10*((self.t)**3)

    def __grad(self):

        self.left_num = math.floor(self.num)
        self.right_num = math.floor(self.num)+1
        
        if self.left_num not in self.storage:
            self.storage[self.left_num] = random.choice([1,-1])
        if self.right_num not in self.storage:
            self.storage[self.right_num] = random.choice([1,-1])
        

    def __dist(self):
        self.left_dist = self.num - self.left_num
        self.right_dist = self.num - self.right_num

    def __cont(self):
        self.left_cont = (self.left_dist*self.storage[self.left_num])
        self.right_cont = (self.right_dist*self.storage[self.right_num])

    def interpolation(self,num):
        self.num = num 
        self.__grad()
        self.__dist()
        self.__cont()
        self.fade_value = self.__fade()
        return self.left_cont + (self.right_cont-self.left_cont) * self.fade_value


noise = PerlinNoise()


pygame.init()


width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Perlin Random walker")

clock = pygame.time.Clock()
FPS = 60


class Walker():
    def __init__(self,screen):
        self.size = 5
        self.x = 540
        self.y = 360
        self.color = (255,255,255)
        self.step_size = 2
        self.screen = screen
        self.random_color()
    def random_color(self):
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    def draw(self):
        #self.random_color()
        self.rect = pygame.Rect(self.x,self.y,self.size,self.size)
        pygame.draw.rect(self.screen,self.color,self.rect)
    def decide(self):
        return random.random() # gives 0.0 - 1.0 float
    def ran_step(self):
        self.step_size+= 0.05
        return noise.interpolation(self.step_size)

    def move(self):
            self.step_size =self.ran_step()
            current_decision = self.decide()
            sub_decision = random.choice(range(4))
            #print(sub_decision)
            #print(current_decision)
            if current_decision<0.8: #this walker biased to walk upward 80% of times
                if sub_decision == 0:
                    self.y -= self.step_size
                elif sub_decision == 1:
                    self.x -=  self.step_size
                    self.y += self.step_size
                elif sub_decision == 2:
                    self.x += self.step_size
                    self.y -= self.step_size
                elif sub_decision == 3:
                    self.x -= self.step_size
                    self.y -= self.step_size
            else:
                if sub_decision == 0:
                    self.y += self.step_size
                elif sub_decision == 1:
                    self.x += self.step_size
                elif sub_decision == 2:
                    self.x -= self.step_size
                elif sub_decision == 3:
                    self.x += self.step_size
                    self.y += self.step_size

            self.draw()

            
        

walker1 = Walker(screen=screen)
walker2 = Walker(screen=screen)
walker3 = Walker(screen=screen) 

screen.fill("BLACK")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    walker1.move()
    walker2.move()
    walker3.move()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
