"""

vypočítajte súčet čísel z intervalu <1,N>

"""

n = int(input("zadajte prirodzené číslo: "))
sucet = 0 
for i in range(1,n+1):
    sucet = sucet + i
print("Súčet od 1 po ", n, "je", sucet)


