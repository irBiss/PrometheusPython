import sys 


class Sphere():
    
    
    def __init__(self, r=1.0, x=0.0, y=0.0, z=0.0):
        self.radius = r
        self.x_center = x
        self.y_center = y
        self.z_center = z
    def get_volume(self):
	    import math
            self.v=4.0/3.0* math.pi*(self.radius**3)
	    return self.v
    def get_square(self):
	import math
	self.s=4*self.radius**2*math.pi
        return self.s
    def get_radius(self):
        return self.radius
    def get_center(self):
        return (self.x_center, self.y_center, self.z_center)
    def set_center(self, x, y, z):
        self.x_center = x
        self.y_center = y
        self.z_center = z
    def set_radius(self, r):
        self.radius = r
    def is_point_inside(self, a, b, c):
        if ((self.x_center-a)**2+(self.y_center-b)**2+(self.z_center-c)**2) <= self.radius**2:
           return True 
        return False
	  
s0 = Sphere(1.0) # test sphere creation with radius and default center
print s0.get_center() # (0.0, 0.0, 0.0)
print s0.get_volume() # 0.523598775598
print s0.get_square()
print s0.is_point_inside(0, -1.5, 0) # False
s0.set_radius(1.6) 
print s0.is_point_inside(0, -1.5, 0) # True
print s0.get_radius() # 1.6