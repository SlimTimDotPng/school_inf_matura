x = float(input("Zadaj prirodzené číslo, ktoré chceš odmocniť: "))
od = 1
do = x
a = 0
t = 0
while abs(x-a**2) > 0.001:
    t += 1
    a = (od + do) / 2
    if a**2 == x:
        break
    if a**2 > x:
        do = a
    else:
        od = a

print(f"Program vypracoval {t} výpočtov")        
print(f"druha odmocnina z {x} je {round(a, 3)}")


