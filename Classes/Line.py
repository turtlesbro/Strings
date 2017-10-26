from point import *
class Line:
    """ Line class for an object, line, defined by its slope and y-intercept. """

    def __init__(self, slope, y_intercept):
        """ A line is defined by a slope and a y-intercept. """

        self.slope = slope
        self.y_intercept = y_intercept

    def perpendicular(self, point):
        """ Computes resulting slope and y intersect of the perpendicular. """

        slope = - 1 / self.slope
        y_intercept = point.y - slope * point.x
        return Line(slope, y_intercept)

    def intersect(self, other_line):
        """ Finds the intersection of two non-vertical lines.
        see wikipedia: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_the_equations_of_the_lines
        Given the equations of two lines, the x and y coordinates of the point of intersection of two non-vertical lines
        can easily be found using the following substitutions and rearrangements:
        Suppose that two lines have the equations y = a * x + c and y = b * x + d where a and b are the slopes of the
        lines and where c and d are the y-intercepts of the lines.
        At the point where the two lines intersect (if they do), both y coordinates will be the same, hence the following equality:
        a * x + c = b * x + d .
        We can rearrange this expression in order to extract the value of x, a * x − b * x = d − c, and so,
        x = (d − c) / (a − b).
        To find the y coordinate, all we need to do is substitute the value of x into either one of the two line equations, for example, into the first:
        y = a * ((d − c) / (a − b)) + c.
        Hence, the point of intersection is P ( (d − c) / (a − b) , a * ((d − c) / (a − b)) + c.
        Note if a = b then the two lines are parallel. If c ≠ d as well, the lines are different and there is no
        intersection, otherwise the two lines are identical."""

        x = (other_line.y_intercept - self.y_intercept) / (self.slope - other_line.slope)
        y = self.slope * x + self.y_intercept
        return Point(x, y)
