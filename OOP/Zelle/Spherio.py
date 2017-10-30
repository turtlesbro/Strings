#Write a class to represent the geometric solid sphere. Your class should implement the following methods:
#__init__(self, radius) Creates a sphere having the given radius.
#get_radius(self) Returns the radius of the sphere.
#surface_area(self) Returns the surface area of the sphere.
#volume(self) Returns the volume of the sphere.

#Write a class to represent a cube. The constructor should accept the length of a side as a parameter. Your class should implement methods to obtain the side length, calculate surface area and volume, similar to the sphere class.

#Using the single responsibility principle, conceive of a system of objects in which both the sphere and the cube could exist and how you might implement the objects in your system.
import math

class SPhere:

    def __init__(self, radius):
        """ Create a new point at the given coordinates. """
        self.radius = radius
    def get_radius(self):
        a = self.radius
        print('Radius', a)
        return a

    def surface_area(self):
        a =  (self.radius**2)*4*math.pi
        print('Surface area =', a)
        return a

    def volume(self):
        a = (self.radius**3)*math.pi*(4/3)
        print('Volume =', a)
        return a

