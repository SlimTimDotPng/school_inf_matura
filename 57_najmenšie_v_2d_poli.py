import random


n = 5
z = [[0]*n for i in range(n)]



for r in range(n):
    for s in range(n):
        z[r][s]= random.randint(2,20)
        print(z[r][s], end="  ")   

    print()




p_min = 0
z_min = 0
for zoznam in range(n):
    for prvok in range(n):
        if z[z_min][p_min] > z[zoznam][prvok]:
            p_min = prvok
            z_min = zoznam
print() 
print("Najmenšie číslo je: ",z[z_min][p_min],"na pozícii",z_min ,",", p_min)
