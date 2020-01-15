import math 
a = float(input("Zadaj koeficient a kvadratickej rovnice: "))
b = float(input("Zadaj koeficient b kvadratickej rovnice: "))
c = float(input("Zadaj koeficient c kvadratickej rovnice: "))
D = b**2 - 4*a*c

if D < 0:
    print("Kvadratická rovnica nemá riešienie v R")

else:
    if D == 0: # = je priradzovací príkaz, == je "sa rovná"
        print("Kvadratická rovnoca má jedno riešenie")
        x = -b/(2*a)
        print(f"Riešenie je: {x:6.3f}")
    else:
        if D > 0:
            print("Kvadratická rovnica má dve riešenia v R")
            x1 = (-b + math.sqrt(D))/2*a
            x2 = (-b - math.sqrt(D))/2*a
            print(f"Prvé riešenie je: {x1:6.3f}")
            print(f"Druhé riešenie je: {x2:6.2f}")
