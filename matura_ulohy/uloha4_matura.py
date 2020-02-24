# === Úloha 4===
# Napíšte program, ktorý vygeneruje a vypíše postupnosť 50 celých čísel z intervalu
# <-7000, 7000>, potom vypíše všetky záporné čísla z postupnosti na obrazovku a do textového súboru d:\maturita\zaporne.txt.
from random import randint
subor = open('zaporne.txt','w')

n = 50

postupnost = [randint(-7000,7000)for i in range(n)]

print('všetky')
for c in postupnost:
    print(c,end=' ')

print()

print("Zaporne z nich:")
for c in postupnost:
    if c < 0:
        print(c,end=' ')

        subor.write(f'{c}\n')