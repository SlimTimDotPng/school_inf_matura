a = int(input("Zadaj prirodzené číslo, ktoré chceš deliť: "))
c = a
b = int(input("Zadaj prirodzené číslo ,s ktorým chceš deliť: "))
pocitadlo = 0
while a >= b:
    a -= b
    pocitadlo += 1
zv = a
print(f"Celočíselný podiel čísla {c} číslom {b} je {pocitadlo} a zvyšok je {zv}")
