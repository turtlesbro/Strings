import math
class coob:

    def __init__(self, length):
        """ Create a new point at the given coordinates. """
        self.length = length
    def get_side(self):
        a = self.length
        print('Side =', a)
        return a
    def surface_area(self):
        a = (self.length**2)*6
        print('Surface area =', a)
        return a

    def volume(self):
        a = (self.length**3)
        print('Volume =', a)
        return a

