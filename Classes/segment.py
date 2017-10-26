from point import *
from Line import *
class Segment:
    """ Segment class for a line segment object, defined by two points. """

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def length(self):
        """ Using delegation we use the distance method from the Point class to establish a length method to determine
        the length of a segment from within the segment class. """

        return self.point_a.distance(self.point_b)

    def line(self):
        """ Transforms a segment into a line. """

        slope = (self.point_b.y - self.point_a.y) / (self.point_b.x - self.point_a.x)
        y_intercept = self.point_a.y - slope * self.point_a.x
        return Line(slope, y_intercept)

    def midpoint(self):
        """ Calculates the midpoint on a line segment. """

        return Point((self.point_b.x + self.point_a.x) / 2, (self.point_b.y + self.point_a.y) / 2)

    def bisect(self):
        """ Creates a line bisecting the original segment at the midpoint. """

        return self.line().perpendicular(self.midpoint())
