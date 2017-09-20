def countAl(text):
    countAll(text, 'a')
    countAll(text, 'b')
    countAll(text, 'c')
    countAll(text, 'd')
    countAll(text, 'e')
    countAll(text, 'f')
    countAll(text, 'g')
    countAll(text, 'h')
    countAll(text, 'i')
    countAll(text, 'j')
    countAll(text, 'k')
    countAll(text, 'l')
    countAll(text, 'm')
    countAll(text, 'n')
    countAll(text, 'o')
    countAll(text, 'p')
    countAll(text, 'q')
    countAll(text, 'r')
    countAll(text, 's')
    countAll(text, 't')
    countAll(text, 'u')
    countAll(text, 'v')
    countAll(text, 'w')
    countAll(text, 'x')
    countAll(text, 'y')
    countAll(text, 'z')

def countAll(text, letter):
    for letter in text:
        if text.count(letter) > 0:
            d[letter] = text.count(letter)




d = {}
countAl("banana")
print(d)
