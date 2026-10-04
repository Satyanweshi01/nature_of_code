import random
import math
# one of the coolest thing I have coded in my entire life
class DNA():
    def __init__(self,length):
        self.wordPool = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z', ' ']
        self.genes = ""
        self.fitness = 0
        self.length = length
        for i in range(length):
            self.genes+= random.choice(self.wordPool)
        self.genelist = [i for i in self.genes]


    def crossover(parentA,parentB)->DNA:
        child = DNA(parentA.length)

        midpoint = random.randrange(0,child.length)

        for i in range(child.length):
            if i<midpoint:
                child.genelist[i] = parentA.genelist[i]
            else:
                child.genelist[i] = parentB.genelist[i]

        child.genes = "".join(child.genelist)
        #coin flipping method
        # r1_num = random.random()
        # if r1_num > 0.5:
        #     child.genes = parentA.genes
        # else:
        #     child.genes = parentB.genes

        return child
    def mutate(self,mutationRate):
        for i in range(self.length):
            if random.random() < mutationRate:
                self.genelist[i] = random.choice(self.wordPool)
            self.genes = "".join(self.genelist)





class GA():
    def __init__(self,target,populationSize,mulationRate):
        self.target = target
        self.population = []
        self.populationSize = populationSize
        self.mulationRate = mulationRate
        for i in range(self.populationSize): # creation of creatures # initialization
            d = DNA(len(target))
            print(d.genes)
            self.population.append(d)
        self.numguess = 0

    def fitness_cal(self):
        for i in self.population: # this picks a element
            correct_char = 0
            for j in range(i.length): # this gets the genetic code/DNA
                if i.genes[j] == self.target[j]:
                    correct_char+=1
            i.fitness = correct_char/len(self.target) # fitness calculation 

    #since here we are using probablistic method, so there are multiple ways to implement this
    #one is this

    def selection(self):
        childpopulation = []
        for i in range(self.populationSize):
            # matingPool = []
            # for phrase in population:
            #     n = math.floor(phrase.fitness * 100)

            #     for i in range(n):
            #         matingPool.append(phrase)
            # parentA = random.choice(matingPool)
            # parentB = random.choice(matingPool)

            # another one is this (accept reject method)
            def randomParent():
                while True:
                    parent = random.choice(self.population)
                    r2_num = random.random()
                    if parent.fitness > r2_num:
                        return parent
            parentA = randomParent()
            parentB = randomParent()

            child = DNA.crossover(parentA,parentB)
            child.mutate(self.mulationRate)
            self.numguess += 1
            print(child.genes)
            if (child.genes == self.target):
                return True

            childpopulation.append(child)
        self.population = childpopulation




target = input("Enter the string to guess: ")
population = []
populationSize = 100
mulationRate = 0.01

ga = GA(target,populationSize,mulationRate)
evolution = True
i = 0
while evolution:
    i+=1
    print(f"generation {i}")
    ga.fitness_cal()
    flag = ga.selection()
    if flag:
        evolution = False
print(f"Number of reproduction needed: {ga.numguess}")

    