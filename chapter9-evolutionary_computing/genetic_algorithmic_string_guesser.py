import random
import math

class DNA():
    def __init__(self,length):
        self.wordPool = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z', ' ']
        self.genes = ""
        self.fitness = 0
        for i in range(length):
            self.genes+= random.choice(self.wordPool)



target = "my life my choice" # class input
population = []

for i in range(10): # creation of creatures # class input
    d = DNA(len(target))
    population.append(d)

for i in population: # this picks a element
    correct_char = 0
    for j in range(len(i.genes)): # this gets the genetic code/DNA
        if i.genes[j] == target[j]:
            correct_char+=1
    i.fitness = correct_char/len(target) # fitness calculation 

# for i in population: # printing the creatures
#     print(i.genes,i.fitness)

matingPool = []
for phrase in population:
    n = math.floor(phrase.fitness * 100)

    for i in range(n):
        matingPool.append(phrase)
parentA = random.choice(matingPool)
parentB = random.choice(matingPool)
for i in matingPool:
    print(i.genes,i.fitness)