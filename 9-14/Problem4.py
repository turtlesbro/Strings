file = open("k;hsdfa", "r")
import turtle
numb = 0
totalx = 0
totaly = 0
t = turtle.Turtle()
t.pensize(9)
t.goto(-200, 0)
t.fd(400)
t.fd(-200)
t.right(90)
t.fd(200)
t.right(180)
t.fd(400)
for line in file:
    item = line.split()
    xcoord = item[0]
    xcoord = str(xcoord)
    xcoord = xcoord.replace('[', '')
    xcoord = xcoord.replace(']', '')
    xcoord = xcoord.replace("'", '')
    xcoord = int(xcoord)
    ycoord =item[1]
    ycoord = str(ycoord)
    ycoord = ycoord.replace('[', '')
    ycoord = ycoord.replace(']', '')
    ycoord = ycoord.replace("'", '')
    ycoord = int(ycoord)
    t.penup()
    t.goto(xcoord, ycoord)
    t.pendown()
    t.fd(1)
    totaly = totaly + ycoord
    numb+=1
    totalx = totalx +xcoord
averagey = totaly/numb
averagex = totalx/numb
#y=averagey+m(x−averagex)
print(averagex, averagey)
