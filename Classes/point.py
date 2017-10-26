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
    def __repr__(self):
        """ Similar to overwrite of existing method for str type conversion. This allows the overwrite to be read and
         executed inside of a tuple. """

        return self.__str__()

    def distance(self, other_point):
        """ Calculate the distance between a point, self, and another point. """

        x_diff_square = (self.x - other_point.x) ** 2
        y_diff_square = (self.y - other_point.y) ** 2
        distance = math.sqrt(x_diff_square + y_diff_square)
        return distance
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
    def move(self, x, y):
         oldx = self.getX()
         oldy = self.getY()
         newx = oldx + x
         newy = oldy + y
         self = Point(newx, newy)
         return self
    def midpoint(self, target):
         xdiff = (target.getX() - self.getX())/2
         ydiff = (target.getY() - self.getY())/2
         midpoint = Point(xdiff, ydiff)
