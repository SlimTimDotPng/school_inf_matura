

def prevod(koruny):
    return round(koruny/25.5, 2)
   


#hp.p.

suma_czk = float(input("Zadaj koľko máš CZK: "))

print("Po prevode na eurá je to:", prevod(suma_czk))
