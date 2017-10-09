import math
class Point:

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def dist(self, target):
         xdiff = target.getX() - self.getX()
         ydiff = target.getY() - self.getY()
         dist = math.sqrt(xdiff**2 + ydiff**2)

         return dist
p = Point(3, 4)
q = Point(5, 12)
mid = p.dist(q)
print(mid)
