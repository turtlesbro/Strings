text =  open("her-name-is-alice", "r")
text = text.read()
text = str(text)
d = {}
g = []
for i in range(3738):
    for aline in text:

        word = aline.split()
        for a in range(len(word)):
            d[word[a-1]] = text.count(word[a-1])
g.append(d)
print(g)
