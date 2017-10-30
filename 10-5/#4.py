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
    def xreflewct(self):
         newx = self.getX()

         newx = 0 - newx
         y = self.getY()
         flip = Point(newx, y )
         return flip
    def linequation(self, p2):
         y1 = self.getY()
         x1 = self.getX()
         y2 = p2.getY()
         x2 = p2.getX()
         rise = y1 - y2
         run = x1 - x2
         #run/run-x1
         b = y1 - x1*y1
         m = rise/run
         t = (m, b)
         return t

p = Point(3, 4)
q = Point(5, 12)
linequation = p.linequation(q)
print(linequation)
