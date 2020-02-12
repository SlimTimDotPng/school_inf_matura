import random

n = 23
ziaci = []
low = []
mid = []
high = []
bigbrain = []
cislo = 0

for i in range(n):
    ziaci += [random.randint(78,147)]

print(ziaci)
print()

for j in range(n):
    if ziaci[j] < 90:
        low.append(ziaci[j])
    if 90 < ziaci[j] and ziaci[j] < 110:
        mid.append(ziaci[j])
    if 110 < ziaci[j] and ziaci[j] < 130:
        high.append(ziaci[j])
    else:
        bigbrain.append(ziaci[j])


for r in range(n):
    cislo += ziaci[r]


    
print('priemerné IQ v triede s ',n,' žiakmi je: ',cislo/n)
print()

print(low)
print('počet žiakov s IQ pod 90:',len(low))
print()
print(mid)
print('počet žiakov s IQ medzi 90 a 110:',len(mid))
print()
print(high)
print('počet žiakov s IQ medzi 110 a 130:',len(high))
print()
print(bigbrain)
print('počet žiakov s IQ nad 130:',len(bigbrain))
