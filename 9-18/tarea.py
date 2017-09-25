def countAll(text, d):
    text.lower()
    for letter in text:
        d[letter] = text.count(letter)
    return d


def main():
    d = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        d[letter] = 0
    d = countAll('Banana boats are low key snipez on the potato', d)
    import turtle
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(-20, -20, 500, 500)
    t.speed(0)
    t.fd(500)
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
    t.right(90)
    t.pensize(5)
    t.penup()
    t.right(90)
    t.fd(10)

    t.left(90)
    t.fd(7)
    for letter in alphabet:
        t.write(letter)
        t.fd(15)
    t.backward(397)
    t.left(90)
    t.fd(10)
    t.right(90)
    t.pendown()
    t.fd(3)
    for letter in alphabet:
        t.left(90)
        t.fd(d[letter]*20)
        t.right(90)
        t.fd(9)
        t.right(90)
        t.fd(d[letter]*20)
        t.left(90)
        t.fd(6)
    t.speed(1)

    t.fd(30300)
main()
