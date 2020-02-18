# === Úloha 2===----
# Napíšte program, ktorý  nájde v súbore vzor.txt najdlhšie slovo, vypíše ho a vypíše aj číslo riadka, na ktorom sa nachádza.

f = open("pes.txt", "r")
riadky = f.readlines() # pole, ["Ahoj sd kys\n", "Kys\n", "\n"]

# kebyze chcem index
# for i in range(0, len(riadky)):
#   print(riadky[i])


najvacsia_dlzka = 0
index_najvacsieho_slova = 0

# pre kazdy index riadka
for i_riadka in range(0, len(riadky)):
  # rozdel na slova, ale slovo moze mat este to \n za sebou
  orezany_riadok = riadky[i_riadka].strip() # zbavi ho medzier
  slova = orezany_riadok.split(" ")
  # split: rko rozdeľ podľa medzier
  # split:  "Ahoj sd kys" -> ["Ahoj", "sd", "kys"]
  for slovo in slova:
    # ked to slovo v tom riadku je dlhsie ako dlzka navjacsia
    # tak to je vlastne teraz nova najvacisa dlzka (rekord novy)
    # (ak najdeme dlhsie slovo, nastav novu rekordnu dlzku a
    # tiez nastav index toho najdeneho slova)
    if len(slovo) > najvacsia_dlzka:
      najvacsia_dlzka = len(slovo)
      index_najvacsieho_slova = i_riadka

print()