import turtle

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'X':
        newstr = '--FXF++FXF++FXF--'   # Rule 1
    elif ch ==  'F':
        newstr = 'FF'
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    inst = createLSystem(6, "FXF--FF--FF")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 60, 5)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()

