import random

class Walker():
    def __init__(self):
        pass
    def decide(self):
        self.move = (random.choice(range(9)))
    def move(self,steps):
        
        for i in range(steps):
            self.decide()
            print(self.move)
walker1 = Walker()
walker1.move(12)