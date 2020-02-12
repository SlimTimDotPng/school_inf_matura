import random

#generovanie zoznamu
n = 3
z = [[0]*n for i in range(n)]
for r in range(n):
    for s in range(n):
        z[r][s]= random.randint(2,20)
        print(z[r][s], end="  ")   #vypísanie

    print()

         




