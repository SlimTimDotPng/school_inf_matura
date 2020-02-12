import random

n = 101
c = []
par = []
nep = []

for i in range(n):
    c += [random.randint(-100,1000)]

    


print(c)
    
for j in range(n):
    if c[j] > 0:
        if c[j] % 2 == 0:
            par.append(c[j])
        else:
            nep.append(c[j])

print('párne kladné čísla:',par )
print('počet párnych čísel je:',len(par))
print('nepárne kladné čísla:',nep )
print('počet nepárnych čísel je:',len(nep))
