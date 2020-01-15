import random
n = 100

z = []
for i in range(0,n):
    z.append(random.randint(1,10000))
    print(z[i],end = ", ")

print()

celkový_pocet_vymien = 0
test = True
i = 1

while test:
    pocet_vymien_pri_prechadzani = 0
    for j in range(0, n-i):
        if z[j] > z[j+1]:
           z[j], z[j+1] = z[j+1], z[j]
           pocet_vymien_pri_prechadzani += 1
    celkový_pocet_vymien += pocet_vymien_pri_prechadzani
    if pocet_vymien_pri_prechadzani == 0:
        test = False
    i += 1

print()
print("usporiadané:")
for i in range(0,n):
    print(z[i], end = ", ")
print()
print("celkový počet výmien:", celkový_pocet_vymien)
   
