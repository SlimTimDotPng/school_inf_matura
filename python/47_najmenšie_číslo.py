import random

#min
"""
n = 10

z = []
for i in range(0,n):
    z = z + [random.randint(1,1000)]
for i in range(10):
    print(z[i], end=" ")

p_min = 0
for i in range(1,n):
    if z[i] < z[p_min]:
        p_min = i
print()
print("Najmenšie číslo je: ",z[p_min])
"""

#max
n = 10

z = []
for i in range(0,n):
    z = z + [random.randint(1,1000)]
for i in range(10):
    print(z[i], end=" ")

p_max = 0
for i in range(1,n):
    if z[i] > z[p_max]:
        p_max = i
print()
print("Najväčšie číslo je: ",z[p_max])
