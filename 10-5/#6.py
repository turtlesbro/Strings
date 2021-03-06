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
         xdiff = (target.getX() - self.getX())/2
         ydiff = (target.getY() - self.getY())/2
         midpoint = Point(xdiff, ydiff)
         return midpoint
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
         t = m
         return t

    def move(self, x, y):
         oldx = self.getX()
         oldy = self.getY()
         newx = oldx + x
         newy = oldy + y
         self = Point(newx, newy)
         return self
    def circlefail(self, point2, point3):
         selfx = self.getX()
         selfy = self.getY()
         p2x = point2.getX()
         p2y = point2.getY()
         p3x = point3.getX()
         p3y = point3.getY()
         x1 = selfx
         y1 = selfy
         x2 = p2x
         y2 = p2y
         y3 = p3y
         x3 = p3x

         h = .1
         t = -100.0
         r = -100.0
         x = x1
         y = y2
         answer = False
         while answer == False:
                 eq = (x-h)**2+(y-t)**2
                 ans = r**2
                 if eq == ans and x == x1:
                     x = x2
                     y = y2
                 elif eq == ans and x == x2:
                     x = x3
                     y = y3
                 elif eq == ans and x == x3:
                     answer = True
                 elif eq != ans and x==x3 or x==x2:
                     x = x1
                     y = y1
                     if h<100:
                         h = h +.1
                     elif t<100:
                         t+= .1
                         h = 0
                     else:
                         r+=.1
                         t = 0
                         h = .1
                 elif eq!= ans:
                     if h<100:
                        h = h +.1
                     elif t<100:
                         t+= .1
                         h = -100
                     else:
                         r+=.1
                         t = -100
                         h = -100
         print((x-h)**2+(y-t)**2, '=', r**2)
         return "(x-h)**2+(y-t)**2, '=', r**2"
    def distanceformula(self, p2):
        y1 = self.getY()
        x1 = self.getX()
        y2 = p2.getY()
        x2 = p2.getX()
        d = math.sqrt((x2-x1)**2+(y2-y1)**2)
        return d

    def circle(self, p2, p3):
        line1 = self.linequation(p2)
        line2 = self.linequation(p3)
        line3 = p3.linequation(p2)
        midpoint1 = self.dist(p2)
        midpoint2 = self.dist(p3)
        midpoint3 = p3.dist(p2)
        invline1 = 1/line1
        invline2 = 1/line2
        invline3 = 1/line3
        yint1 = midpoint1.getY() - invline1* midpoint1.getX()
        yint2 = midpoint2.getY() - invline2* midpoint2.getX()
        yint3 = midpoint3.getY() - invline3* midpoint3.getX()
        x = -10
        ans1 = invline1*x+yint1
        ans2 = invline2*x+yint2
        ans3 = invline3*x+yint3
        if ans1 == ans2 or ans2 == ans3 or ans1 == ans3:
            y = ans1
            l = Point(x, y)
            print('midpoint:', l, 'radius:', self.distanceFromOrigin)
        else:
             x = x+.1
    def v2circle(self, p2, p3):
        a = self.distanceformula(p2)
        b = self.distanceformula(p3)
        c = p3.distanceformula(p2)
        prod = a*b*c
        line1 = self.dist(p2)


        height = p3.distanceformula(line1)
        bottom = a*height*2
        radius = prod/bottom
        return radius

p = Point(math.sqrt(2), math.sqrt(2))
q = Point(0, 2)
j = Point(math.sqrt(3), math.sqrt(1))
p = p.v2circle(j, q)
print(p)
#Product~of~the~triangle~side~lengths/The~area~of~the~triangle~multiplied~by~4
