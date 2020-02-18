import random


n = 5
z = [[0]*n for i in range(n)]



for r in range(n):
    for s in range(n):
        z[r][s]= random.randint(2,20)
        print(z[r][s], end="  ")   

    print()

print()

for d in range(n):
    print(z[d][d])




