t = True
#vowel stripper
file = open("Guidotextedit", "r")

def remove_letter(theLetter, theString):
    new = theString.replace(theLetter, "")
    return new

data = file.read()
string = str(data)
new = remove_letter("e", string)
new = remove_letter("a", new)
new = remove_letter("y", new)
new = remove_letter("o", new)
new = remove_letter("u", new)
new = remove_letter("i", new)



while t == True:

    x = new.find('.')
    print(new[0:x+1])
    y = string.find('.')
    Answer = str(input('Type what you think this says(type the period too): '))
    if Answer.lower() == string[0:y+1].lower():
        print('Good job')
    else:
      print('Nope, the correct answer was:', string[0:y+1])

      t = False
    new = new[x+2:]
    string = string[y+2:]
