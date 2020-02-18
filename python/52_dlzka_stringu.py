#program vygeneruje postupnosť reťazcov náhodnej dížky z intervalu(1-20)
#vytvorte funkuciu, kt. bude mať ako parameter daný zoznam.
#výstup bude nový zoznam, bude obsahovať dížky stringov pôvedneho zoznamu
import random
n = 10
z = []

def dlzky(zoznam):
    z2 = []
    for i in range(n):
        
        x = len(zoznam[i])
        z2.append(x)
    return z2
        
    

slovo = ""
for i in range(n):
    for j in range(random.randint(1,20)):
        cislo = random.randint(97,122)
        znak = chr(cislo)
        slovo += znak

    z = z + [slovo]    
    slovo = ""


print(z)
print()

dlzky_slov = dlzky(z)

print(dlzky_slov)



p_max = 0
for i in range(1,n):
    if dlzky_slov[i] > dlzky_slov[p_max]:
        p_max = i 

print()
print(p_max)
print()
print(z[p_max])
    
    
