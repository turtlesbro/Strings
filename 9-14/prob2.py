file = open("student", "r")
s = ''
a = 0
for aline in file:
    items = aline.split()
    statement = (items[0])
    for i in range(len(items)-1):
        s = items[i+1:i+2]
        s = str(s)
        s = s.replace('[','')
        s = s.replace(']','')
        s = s.replace("'",'')
        s = int(s)
        a = a+s
    a = a/(len(items)-1)

    print(statement)
    print(a, '%')
    a = 0
