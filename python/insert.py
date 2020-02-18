import random

n = 20

z = [random.randint(1,5)]
for i in range(0,n):
    z = z + [z[i] + random.randint(1,5) ]

print(z)

print()
cislo = int(input("zadaj číslo:"))
"""
i = 0

while i < len(z):
    if z[i]>cislo:
        break
    i+=1
    
z.insert(i,cislo)


for t in range(0,n+1):
    print(z[t], end = ", ")
"""

dh = 0
hh = n
stred = (dh + hh) // 2

while dh != stred and hh != stred:
    if cislo > z[stred]:
        dh = stred
        stred = (dh + hh) // 2
    else:
        hh = stred
        stred = (dh + hh) // 2

if stred == 0:
    z.insert(0,cislo)
else:
    if dh == stred:
        z.insert(stred + 1, cislo)
    if hh == stred:
        z.insert(stred - 1, cislo)
    
print()
print(z)
