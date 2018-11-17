class Line():
    
    #coor1,coor 2 are tuples (x,y)
    #tuples cannot be changed!
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((y2-y1)/(x2-x1))

# EXAMPLE OUTPUT of Line Class
coordinate1 = (3,2)
coordinate2 = (8,10)
l1 = Line(coordinate1,coordinate2)
print("The distance is {} ".format(l1.distance()))
print("The slope is {}".format(l1.slope()))

class Cylinder():
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
    	#volume = pir**2h
        return 3.14*self.radius**2*self.height
    
    def surface_area(self):
        #surface area = height * 2pi*radius
        return (2)*(3.14)*(self.radius)**2 +2*(3.14)*(self.radius)*(self.height)


 # EXAMPLE OUTPUT
c = Cylinder(2,3)

print("VOLUME of c is {}".format(c.volume()))
print("SURFACE Area of c is {} ".format(c.surface_area()))