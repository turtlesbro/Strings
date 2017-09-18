#Zak9-14
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-500, -500, 500, 500)
file = open("mystery.txt", "r")
for aline in file:
    items = aline.split()
    if items[0] == "UP":
        t.up()
    elif items[0] == "DOWN":
        t.down()
    else:
        t.goto(int(items[0]), int(items[1]))

