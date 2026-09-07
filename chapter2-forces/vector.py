import math


class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.mag = math.sqrt(self.x*self.x + self.y*self.y)

    def add(self,vec:Vector):
        self.x+=vec.x
        self.y+=vec.y
    def sub(self,vec):
        self.x-=vec.x
        self.y-=vec.y
    def multi(self,scalar):
        self.x*=scalar
        self.y*=scalar
    def div(self,scalar):
        self.x/=scalar
        self.y/=scalar

    def limit(self,maxi):
        if self.mag > maxi:
            scale = maxi/self.mag
            self.x*=scale
            self.y*=scale
            self.mag = maxi
    def mag_update(self):
        self.mag = math.sqrt(self.x*self.x + self.y*self.y)
        return self.mag
    
    def normalize(self):
        if self.mag_update() == 0:
            self.div(self.mag_update())

class Mover():
    def __init__(self,x,y):
        self.position = Vector(x,y)
        self.velocity = Vector(0,0)
        self.acceleration = Vector(0,0)
        self.ap_forces = []
    def cal_acce(self):
        self.acceleration.multi(0)
        #print(self.acceleration.x,self.acceleration.y)
        for i in self.ap_forces:
            self.acceleration.add(i)    
        self.acceleration.mag_update()
        self.update()
    def ap_force(self,force:Vector):
        if force not in self.ap_forces:
            self.ap_forces.append(force)
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        

    
        
