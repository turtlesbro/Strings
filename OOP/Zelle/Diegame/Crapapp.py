# pokerapp.py

from dice import Dice

class PokerApp:

    def __init__(self, interface):
        self.dice = Dice()
        self.money = 100
        self.interface = interface

    def run(self, Pass):
        while self.money >= 10 and self.interface.wantToPlay():
            self.playRound(Pass)
        self.interface.close()

    def playRound(self, Pass):
        self.money = self.money - 10
        roundgoing = True
        roll = 1
        while roundgoing == True:
            self.interface.setMoney(self.money)
            self.doRolls()
            score, target = self.dice.score(roll)
            Win = 0
            if Pass == True:
                if score == 2:
                    self.money = self.money + 20
                    roundgoing = False
                    Win = 3
                elif score == -2 or score == -1:
                    roundgoing = False
                    Win = 2
                else:
                    roundgoing = True
                    roll = roll+1
            else:
                if score == 2:
                    roundgoing = False
                    Win = 2
                elif score == -1:
                    self.money = self.money + 10
                    roundgoing = False
                    Win = 1
                elif score == -2:
                    self.money = self.money + 20
                    roundgoing = False
                    Win = 3
                else:
                    roundgoing = True
                    roll = roll+1
            self.interface.showResult(Win)
        self.interface.setMoney(self.money)

    def doRolls(self):
        self.dice.rollAll()
        self.interface.setDice(self.dice.values())

