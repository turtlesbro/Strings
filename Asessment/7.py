text =  open("her-name-is-alice", "r")
text = text.read()

d = {}
g = []
word = ''
for aline in text:
    letter = aline
    if letter!= ' ':
            word = word + letter
    else:
        d[word] = text.count(word)
        word = ''

print(d)

