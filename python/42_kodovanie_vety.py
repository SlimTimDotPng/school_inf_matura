import random

#šifrátor
 
veta = input("Napíš vetu a ja ti ju zakódujem: ")

veta = veta.upper()
l = len(veta)


sifra = ""
for i in range(0,l):
    z = random.randint(65,91)
    sifra = sifra + veta[i] + chr(z)
  

print(sifra)


#dešifrátor

p = len(sifra)

decode = ""
for r in range(0,p,2):
    decode =  decode + sifra[r]

print(decode)
    
