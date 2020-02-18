#NSD(a,b) - najväčší spoločný deliteľ

def NSD(a,b):
    zvysok = 1
    while zvysok > 0:
        zvysok = a % b
        a = b
        b = zvysok
    return a

#hl.p

c1 = int(input("Zadaj prvé číslo: "))
c2 = int(input("Zadaj druhé číslo: "))

print(f"Najváčší spoločný deliteľ čísla {c1} a čísla {c2} je {NSD(c1,c2)} ")
