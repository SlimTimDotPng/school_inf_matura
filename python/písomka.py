
from math import sqrt


cislo = float(input("Zadaj reálne cislo z intervalu <-1000,1000>: "))

if cislo > 1000 or cislo < -1000:
    print("Číslo" , cislo , "ktoré si zadal, nepatrí do intervalu <-1000,1000>")
    

elif cislo == 0:
    print("Číslo 0 nie je ani kladné, ani záporné, ani párne, ani nepárne, ani prvočíslo")
    

elif cislo > 0:
    odmocnina = sqrt(cislo)
    print(f"Číslo  {odmocnina:4.2f} je druhou odmocninou čísla" , cislo ,)
    
elif cislo < 0:
    mocnina = cislo * cislo
    print(f"Číslo {mocnina:10.2f}  je druhou mocninou čísla" , cislo)
    
    
