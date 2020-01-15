def hodnota(slovo):
    x = 0
    for i in slovo:
        x = x + ord(i)
    return x

veta = input("zadaj vetu: ")
z = 0
for r in veta:
    if r != (" "):
      z = z+ ord(r)
       

print(z)




        
