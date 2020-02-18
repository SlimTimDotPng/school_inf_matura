import random


n = 5
z = [[0]*n for i in range(n)]



for r in range(n):
    for s in range(n):
        z[r][s]= random.randint(0,1)
        print(z[r][s], end="  ")   

    print()

_x = int(input("Zadaj súradnicu x:"))
_y = int(input("Zadaj súradnicu y:"))

if z[_x][_y] == 1:
    z[_x][_y] = 0
else:
    z[_x][_y] = 1


for r in range(n):
    for s in range(n):
        print(z[r][s], end="  ")
    print()
