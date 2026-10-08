import math
import random
import pygame

class DNA():
    def __init__(self,lifespan):
        self.genes = []
        self.maxspeed = 5
        self.lifespan = lifespan
        for i in range(self.lifespan):
            self.genes.append(Vectorcls.random2d())
            self.genes[i] = Vectorcls.multi(self.genes[i],random.choice([0,self.maxspeed]))
    
    def crossover(parentA,parentB):
        child = Body(parentA.screen, parentA.x, parentA.y, parentA.mass, parentA.size, parentA.target, DNA(parentA.dna.lifespan))

        midpoint = random.randrange(0,child.dna.lifespan)

        for i in range(child.dna.lifespan):
            if i<midpoint:
                child.dna.genes[i] = parentA.dna.genes[i]
            else:
                child.dna.genes[i] = parentB.dna.genes[i]

        return child
    def mutate(self,mutationRate):
        for i in range(self.lifespan):
            if random.random() < mutationRate:
                self.genes[i] = Vectorcls.random2d()


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
        return Vectorcls.div(self,self.mag())
    
    def setMag(self,mag):
        vec = self.normalize()
        return Vectorcls.multi(vec,mag)
    
    def dot(a:Vectorcls,b:Vectorcls):
        angle = math.acos(((a.position.x * b.position.x)+(a.position.y*b.position.y))/a.mag()*b.mag())
        return angle

    def angle(self):
        return math.atan2(self.y, self.x)

    def setDir(a:Vectorcls,angle): # absolute direction change, it is like assigning new direction with same magnitude
        mag = a.mag()
        x = mag*math.cos(angle)
        y = mag*math.sin(angle)
        return Vectorcls(x,y)

    def rotate(a:Vectorcls,angle):
        curr_angle = a.angle()
        new_angle = curr_angle + angle
        return Vectorcls.setDir(a,new_angle)
    
    def random2d():
        vec = Vectorcls(1,1)
        angle = random.uniform(0,2*math.pi)
        vec = Vectorcls.setDir(vec,angle)
        vec.setMag(1)
        return vec


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
    def ap_force(self,force:Vectorcls):
        if force not in self.ap_forces:
            self.ap_forces.append(force)
    def update(self):
        self.velocity = Vectorcls.add(self.acceleration,self.velocity)
        self.position = Vectorcls.add(self.velocity,self.position)

class Rockets(Mover):
    def __init__(self,x,y,mass,target,dna:DNA):
        super().__init__(x,y,mass)
        self.dna = dna
        self.movement_counter = 0 
        self.target = target
        self.fitness = 0
    def cal_fitness(self):
        dist = Vectorcls.sub(self.position,self.target.position)
        self.fitness = 1/(dist.mag()*dist.mag())
    def run(self):
        self.ap_forces = []
        self.ap_force(self.dna.genes[self.movement_counter])
        self.movement_counter += 1
        self.cal_acce()
        self.update()


class Body(Rockets):
    def __init__(self,screen,x,y,mass,size,target,dna:DNA):
        super().__init__(x,y,mass,target,dna)
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
        angle = self.velocity.angle()
        rotated = pygame.transform.rotate(self.image, -math.degrees(angle))
        rotated_rect = rotated.get_rect(center=self.rect.center)
        self.screen.blit(rotated, rotated_rect)


class GA():
    def __init__(self,target:Body,populationSize,mulationRate,lifespan,screen):
        self.target = target
        self.lifespan = lifespan
        self.screen = screen
        self.population = []
        self.avg_fitness = 0
        self.gen = 0
        self.populationSize = populationSize
        self.mulationRate = mulationRate
        for i in range(self.populationSize): # creation of creatures # initialization
            d = Body(self.screen,540,360,10,100,self.target, DNA(self.lifespan)) 
            self.population.append(d)

    def fitness_cal(self):
        for i in self.population: # this picks a element
            i.cal_fitness()

    def fitness_normalize(self):
        self.fitness_cal()
        total_fitness = 0
        total_fitness_normalized = 0
        for i in self.population:
            total_fitness+= i.fitness
        for j in self.population:
            j.fitness/=total_fitness
            total_fitness_normalized+=j.fitness
        self.avg_fitness = total_fitness/self.populationSize

    def selection(self):
        self.gen += 1
        self.fitness_normalize()
        childpopulation = []
        for i in range(self.populationSize):
            def randomParent():
                while True:
                    parent = random.choice(self.population)
                    r2_num = random.random()
                    if parent.fitness > r2_num:
                        return parent
            parentA = randomParent()
            parentB = randomParent()

            child = DNA.crossover(parentA,parentB)
            child.dna.mutate(self.mulationRate)
            childpopulation.append(child)
        self.population = childpopulation

    def live(self):
        for i in self.population:
            i.run()
            i.draw2()
        if i.movement_counter >= len(i.dna.genes):
                self.selection()
                i.movement_counter = 0

def text(string,screen, text_color, x, y):
    font = pygame.font.SysFont("Arial", 20)
    img = font.render(string, True, text_color)
    screen.blit(img,(x,y))