# === Úloha 1===
# Napíšte program, ktorý vypočíta súčin, celočíselný podiel a zvyšok pri delení dvoch náhodne vygenerovaných prirodzených čísel bez použitia operácií *, div a mod.

from random import randint

a = randint(0,100)
b = randint(0,100)
sucin = 0

for i in range(a):
    sucin += b

zvysok = a 
podiel = 0
while zvysok >= b:
    zvysok -= b
    podiel += 1

print(f'{a}*{b}={sucin}')
print(f'{a}/{b}={podiel} zvyšok {zvysok}')