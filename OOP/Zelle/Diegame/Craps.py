# guipoker.py
# 1st roll a 2,3,or12 is a Don't pass (12 is no points for No Pass) and 7 or 11 is Pass
#after, try to get the same # as first roll. If it is before 7 Pass, else don't Pass
from graphics import *
from Crapapp import PokerApp
from button import Button
from cdieview import ColorDieView

class GraphicsInterface:

    def __init__(self):
        self.win = GraphWin("Craps", 600, 400)
        self.win.setBackground("green3")
        banner = Text(Point(300,30), "Are you a lucky roller?")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)
        self.msg = Text(Point(300,380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.createDice(Point(475,100), 75)
        self.buttons = []
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(200, 280), 150, 40, "Pass")
        self.buttons.append(b)
        b = Button(self.win, Point(400, 280), 150, 40, "Don't Pass")
        self.buttons.append(b)
        b = Button(self.win, Point(570,375), 40, 30, "Quit")
        self.buttons.append(b)
        self.money = Text(Point(300,325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)


    def createDice(self, center, size):
        center.move(-3*size,0)
        self.dice = []
        for i in range(2):
            view = ColorDieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size,0)


    def setMoney(self, amt):
        self.money.setText("${0}".format(amt))

    def showResult(self, score):
        if score == 3:
            text = "You win $20"
        elif score == 2:
            text = "You lost."
        elif score == 0:
            text = ""
        else:
            text = "Tie"
        self.msg.setText(text)

    def setDice(self, values):
        for i in range(2):
            self.dice[i].setValue(values[i])

    def wantToPlay(self):
        ans = self.choose(["Roll Dice", "Quit"])
        self.msg.setText("")
        return ans == "Roll Dice"

    def close(self):
        self.win.close()

    def chooseDice(self):
        # choices is a list of the indexes of the selected dice
        choices = []                   # No dice chosen yet
        while True:
            # wait for user to click a valid button
            b = self.choose([ "Roll Dice", "Pass", "Don't Pass", "Quit"])
            choices.append["Quit"]
            if  gameisstarting:
                choices.append["Pass"]
                choices.append["Don't Pass"]
            elif gameinprogress:
                choices.append["Roll"]
            return choices     #   dice are actually selected

    def choose(self, choices):
        buttons = self.buttons

        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()  # function exit here.

    def commence(self):
        Wait = True
        while Wait == True:
            if self.choose("Pass"):
                Wait = False
                Pass = True
            elif self.choose("Don't Pass"):
                Wait = False
                Pass = False
        return Pass

inter = GraphicsInterface()
Pass = inter.commence()
app = PokerApp(inter)
app.run(Pass)
