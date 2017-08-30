file = open("guido_vonRossum_speech.txt", "r")

def remove_letter(theLetter, theString):
    new = theString.replace(theLetter, "")
    print(new)
    return new

data = file.read()

remove_letter("a", data)
