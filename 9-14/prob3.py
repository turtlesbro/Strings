file = open("student", "r")
s = ''
minscore = 999
maxscore = 0
for aline in file:
    items = aline.split()
#    s = ''.join(items)
    statement = (items[0])
    for i in range(len(items)-1):

        s = items[i+1:i+2]
        s = str(s)
        s = s.replace('[','')
        s = s.replace(']','')
        s = s.replace("'",'')
        s = int(s)
        if s > maxscore:
            maxscore = s
        if s < minscore:
            minscore = s

    print(statement, 'min:', minscore, 'max:', maxscore)
    minscore = 999
    maxscore = 0

