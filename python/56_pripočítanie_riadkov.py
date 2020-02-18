import random


n = 5
z = [[0]*n for i in range(n)]



for r in range(n):
    for s in range(n):
        z[r][s]= random.randint(2,20)
        print(z[r][s], end="  ")   

    print()

for s in range(n):
    z[1][s] += z[0][s]

print()
for r in range(n):
    for s in range(n):
        
        print(z[r][s], end="  ")     
    print()
