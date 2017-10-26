from buttonz import *
from graphics import *
from pic import *
from random import *
def main():
    win = GraphWin("dice roller")
    win.setCoords(0,0,10,10)
    win.setBackground("green2")
    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    rollButton = Button(win, Point(5, 4.5), 1, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Point(5, 1), 1, "Quit")

    pt = win.getMouse()
    while not quitButton.clicked(pt, Point(5,1), 1):
        if rollButton.clicked(pt, Point(5, 4.5), 1):
            value1 = randrange(1, 7)
            die1.setValue(value1)
            value2 = randrange(1, 7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

main()


