def parnost(cislo):
    if cislo%2 == 0:
        return True
    else:
        return False

#hl.p.

cislo = int(input("Zadaj číslo: "))
if parnost(cislo):
    print(cislo,"je párne")
else:
    print(cislo,"nie je párne")
