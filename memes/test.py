import random

n = 20

z = [0]

for i in range(0,n):
    z = z + [z[i] + random.randint(1,5)]

for j in range(0,n):
    print(z[j], end = ", ")

print()
cislo = int(input("zadaj číslo:"))

for k in range(0,n):
    if cislo > z[k]:
        z.insert(z[k],cislo)

for l in range(0,n):
    print(z[j], end = ", ")
