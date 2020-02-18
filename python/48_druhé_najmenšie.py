import random

n = 10

z = []
for i in range(0,n):
    z = z + [random.randint(1,1000)]
for i in range(10):
    print(z[i], end=" ")

p_min = 0
