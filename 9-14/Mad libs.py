file = open("Mad", "r")
data = file.read()
string = str(data)
stringedit = string.lower()
def filereplace(numb, pos):
    numb = str(numb)
    numb9 = str(input(pos))
    return  stringedit.replace(numb, numb9)


stringedit = filereplace(9, 'Name or nickname:')
stringedit = filereplace(11, 'Noun:')
stringedit = filereplace(12, 'Exclamation:')
stringedit = filereplace(13, 'Past tense verb:')
stringedit = filereplace(14, 'Noun:')
stringedit = filereplace(15, 'Past tense verb:')
stringedit = filereplace(16, 'Noun:')
stringedit = filereplace(17, 'Adjective:')
stringedit = filereplace(18, 'Noun:')
print(stringedit)
