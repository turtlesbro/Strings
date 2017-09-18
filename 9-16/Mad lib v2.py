file = open("MAd2", "r")
data = file.read()
string = str(data)
stringedit = string.split()
def filereplace(numb, pos):
    numb = str(numb)
    numb9 = str(input(pos))
    return numb9

replacewords = {}


numb1 = filereplace(9, 'Name or nickname:')
replacewords['9'] = numb1
numb2 = filereplace(11, 'Noun:')
replacewords['11'] = numb2
numb3 = filereplace(12, 'Exclamation:')
replacewords['12'] = numb3
numb4 = filereplace(13, 'Past tense verb:')
replacewords['13'] = numb4
numb5 = filereplace(14, 'Noun:')
replacewords['14'] = numb5
numb6 = filereplace(15, 'Past tense verb:')
replacewords['15'] = numb6
numb17 = filereplace(16, 'Noun:')
replacewords['16'] = numb17
numb7 = filereplace(17, 'Adjective:')
replacewords['17'] = numb7
numb18 = filereplace(18, 'Noun:')
replacewords['18'] = numb18
newsent = []
for i in range(len(stringedit)):
    if stringedit[i-1] in replacewords:
        newsent.append(replacewords[stringedit[i-1]])
    else:
        newsent.append(stringedit[i-1])
print(" ".join(newsent))
