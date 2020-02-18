b = int(input("Zadaj celé číslo: "))
print("delitele čísla", b,"sú:")
sucet = 0
for i in range(1, b+1):
    if b%i==0:
        print(i,end=" ")
        sucet += i
print()    
print("Súčet všetkých deliteľov čísla", b,"je:",sucet)
