import random
cislo = random.randint(1,100)
#print(cislo)
zc = int(input("Hádaj číslo, ktoré si myslím: "))
print(zc)
pocet = 1
while cislo != zc and pocet < 10 :
        
        if zc < cislo:
            print("Myslím si väčšie číslo.")
            pocet += 1
            zc = int(input("Znova hádaj číslo, ktoré si myslím: "))
        else:
            print("Myslím si menšie číslo.")
            pocet += 1
            zc = int(input("Znova hádaj číslo, ktoré si myslím: "))



if cislo == zc:
    print(f"Myslel som si číslo {cislo} a TY si ho uhádol na {pocet}. pokus")

else:
    print(f"Myslel som si číslo {cislo} a neuhádol si ho.")
            


