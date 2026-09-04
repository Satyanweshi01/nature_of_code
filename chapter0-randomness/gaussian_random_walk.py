import random
import pygame

pygame.init()


width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Gaussian Random walker")

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
        return random.choice(range(9))
    def move(self):
            self.step_size = random.gauss(5,10)
            current_decision = self.decide()
            #print(current_decision)
            if current_decision == 0:
                self.y += self.step_size
                self.draw()
            elif current_decision == 1:
                self.y -= self.step_size
            elif current_decision == 2:
                self.x += self.step_size
            elif current_decision == 3:
                self.x -= self.step_size
            elif current_decision == 4:
                self.x -=  self.step_size
                self.y += self.step_size
            elif current_decision == 5:
                self.x += self.step_size
                self.y += self.step_size
            elif current_decision == 6:
                self.x -= self.step_size
                self.y -= self.step_size
            elif current_decision == 7:
                self.x += self.step_size
                self.y -= self.step_size
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
