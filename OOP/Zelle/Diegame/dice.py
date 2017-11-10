# dice.py

from random import randrange

class Dice:
    def __init__(self):
        self.dice = [0]*5
        self.rollAll()

    def roll(self, which):
        for pos in which:
            self.dice[pos] = randrange(1,7)

    def rollAll(self):
        self.roll(range(2))

    def values(self):
        return self.dice[:]

    def score(self, rolln):
        # Create the counts list
        counts = [0] * 3
        list = []
        target = 0
        for value in range(2) :
            k = self.dice
            list.append(k)
        if rolln == 1:
            if list[0] + list[1] == 2:
                score = -2
                print("ph")
            elif list[0] + list[1] == 12:
                score = -1
                print("jh")
            elif list[0] + list[1] == 3:
                score = -2
                print("yh")
            elif list[0] + list[1] == 7:
                score = 2
                print("th")
            elif list[0] + list[1] == 11:
                score = 2
                print("hh")
            else:
                rolln = rolln+1
                target = list[0] + list[1]
                score = 1
                print("hg")

        else:
            if list[0] + list[1] == target:
                score = 2
                print("hr")
            elif list[0] + list[1] == 7:
                score = 1
                print("h\h")
            else:
                score = 2
                print("sack")
        return score, target
