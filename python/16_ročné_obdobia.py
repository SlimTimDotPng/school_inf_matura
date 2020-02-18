m = int(input("Zadajte číslo mesiaca: "))
print()
if m in {3, 4, 5}:                                # {} je množina prvkov,kt. nie su usporiadané
    print("jar")
else:
    if m in {6, 7, 8}:
        print("leto")
