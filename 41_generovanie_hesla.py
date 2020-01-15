import random

heslo = ""
for i in range(0,8):
    cislo = random.randint(97,122)
    znak = chr(cislo)
    
    heslo += znak

print(heslo)

