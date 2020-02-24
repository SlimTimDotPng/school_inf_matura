# === Úloha 2===----
# Napíšte program, ktorý  nájde v súbore vzor.txt najdlhšie slovo, vypíše ho a vypíše aj číslo riadka, na ktorom sa nachádza.

subor = open("pes.txt", "r")

riadky = subor.readlines()

nv_slovo = ''
riadok_nv_slova = 0
#ir = index riadka
for ir in range(0, len(riadky)):
    orezanyr = riadky[ir].strip()
    slova = orezanyr.split(' ')

    for slovo in slova:
        if  len(slovo) > len(nv_slovo):
            nv_slovo = slovo
            riadok_nv_slova += 1

print(nv_slovo)
print(riadok_nv_slova)

subor.close()