import math

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


