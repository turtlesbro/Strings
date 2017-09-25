import random
avg = 0
number = 0
new =0
rand = []
for i in range(100):
    rand.append(random.randrange(0, 1001))

for i in range(100):
    new = rand.pop()
    avg+=new
    number+=1
avg = avg/number
print(avg)
