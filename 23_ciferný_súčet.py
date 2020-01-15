x = int(input("Zadaj prirodzené číslo a ja ti vypočítam jeho ciferný súčet: "))
c = x
cs = 0
while c > 0:
    zv = c % 10
    c //= 10
    cs += zv
print(f"Číselný súčet čísla {x} je: {cs}")
