file = open("student", "r")

for aline in file:
    items = aline.split()
    if len(items[1:]) > 6:
        print(items[0])



