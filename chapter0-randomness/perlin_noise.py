#smooth randomness
import matplotlib.pyplot as plt
import math
import random

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

xpoints = [ i / 100 for i in range(1000) ]
num = PerlinNoise()

ypoints = [num.interpolation(j) for j in xpoints]
#print(xpoints)

#print(num.storage)
plt.plot(xpoints, ypoints)
plt.show()