def countAll(text):
    d = {}
    text.lower()
    for letter in text:
        d[letter] = text.count(letter)
    return d
d = countAll('Banana boats')
g =[]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in d:
    g = d
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-20, -20, 500, 500)
t.speed(0)
t.fd(500)
print(d)
for letter in alphabet:
    if d[letter] == 'null':
        d[letter] = 0
t.backward(500)
for i in range(26):
    t.fd(15)
    t.left(90)
    t.fd(10)
    t.backward(10)
    t.right(90)
t.backward(390)
t.left(90)
t.fd(500)
t.backward(500)
t.speed(1)
print(g)

for letter in alphabet:
    if d[letter] > 0:
        print(d[letter])
    else:
        d=d
#if countAll():
t.fd(30300)
