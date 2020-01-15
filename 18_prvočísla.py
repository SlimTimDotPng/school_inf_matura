"""

uživatel zadá čislo, program zistí či je prvočíslo

"""
import math
"""
n = int(input("Zadaj číslo: "))
pocet_delitelov = 0
for i in range(2,(round(n/2)+1)):
    if n % i  == 0:
        pocet_delitelov += 1 # a += b (pripočítaj a ku b) *= , /= , -=

if pocet_delitelov == 0:
    print(f"Číslo {n} je prvočíslo")
else:
    print(f"Číslo {n} nie je prvočíslo")


#vylepšená verzia 1

n = int(input("Zadaj číslo: "))
pocet_delitelov = 0
for i in range(2,(round(math.sqrt(n))+1)):
    if n % i  == 0:
        pocet_delitelov += 1 

if pocet_delitelov == 0:
    print(f"Číslo {n} je prvočíslo")
else:
    print(f"Číslo {n} nie je prvočíslo")
"""
#vylepšená verzia 2

n = int(input("Zadaj číslo: "))
pocet_delitelov = 0
for i in range(2,(round(math.sqrt(n))+1)):
    if n % i  == 0:
        pocet_delitelov += 1
    if pocet_delitelov == 1:
        break

if pocet_delitelov == 0:
    print(f"Číslo {n} je prvočíslo")
else:
    print(f"Číslo {n} nie je prvočíslo")
