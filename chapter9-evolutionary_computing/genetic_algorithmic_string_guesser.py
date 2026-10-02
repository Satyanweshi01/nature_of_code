import random
class DNA():
    def __init__(self,length):
        self.wordPool = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z', ' ']
        self.genes = ""
        for i in range(length):
            self.genes+= random.choice(self.wordPool)
    # def print(self):
        # print(self.genes)


target = "my life my choice"
population = []

for i in range(10):
    d = DNA(len(target))
    population.append(d)
for i in population:
    print(i.genes)