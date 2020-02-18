# === Úloha 2===----
# Napíšte program, ktorý  nájde v súbore vzor.txt najdlhšie slovo, vypíše ho a vypíše aj číslo riadka, na ktorom sa nachádza.

f = open("pes.txt", "r")
riadky = f.readlines() # pole, ["Ahoj sd kys\n", "Kys\n", "\n"]

najvacsie_slovo = ""
riadok_naj_slova = 0

# pre kazdy index riadka
for i_riadka in range(0, len(riadky)):
  # rozdel na slova, ale slovo moze mat este to \n za sebou
  orezany_riadok = riadky[i_riadka].strip() # zbavi ho medzier
  slova = orezany_riadok.split(" ")
  # split: rko rozdeľ podľa medzier
  # split:  "Ahoj sd kys" -> ["Ahoj", "sd", "kys"]
  for slovo in slova:

    if len(slovo) > len(najvacsie_slovo):
      najvacsie_slovo = slovo # nastavime, novy rekord
      riadok_naj_slova = i_riadka + 1

print(f"naj slovo = {najvacsie_slovo}")
print(f"je v riadku = {riadok_naj_slova}")