from graphics import *
import math

class Button:

    def __init__(self, win, center, radius, label):

        x,y = center.getX(), center.getY()

#        self.xmax, self.xmin = x+w, x-w
#        self.ymax, self.ymin = y+h, y-h

#        p1 = Point(self.xmin, self.ymin)
#        p2 = Point(self.xmax, self.ymax)

        self.rect = Circle(center, radius)
        self.rect.setFill('lightgray')
        self.rect.draw(win)

        self.label = Text(center, label)
        self.label.draw(win)

        self.deactivate()

    def clicked(self, center, p, radius):
        x_diff_square = (p.getX() - center.getX()) ** 2
        y_diff_square = (p.getY() - center.getY()) ** 2
        distance = math.sqrt(x_diff_square + y_diff_square)

        return (self.active and
                distance < radius)

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

def main():
    win = GraphWin("dice roller")
    win.setCoords(0,0,100,100)
    win.setBackground("green2")
    Buttons = Button(win, Point(50, 50), 50, "don't do it")
    Buttons.activate()

    quitButton = Button(win, Point(5, 1), 20, "Quit")

    pt = win.getMouse()
    while not quitButton.clicked(pt, Point(5, 1), 20):
        if Buttons.clicked(pt, Point(50, 50), 50):
            print("ayyye")
            quitButton.activate()
        pt = win.getMouse()
#main()
