import math
odvesna1=input("Zadaj dĺžku prvej prepony v pravouhlom trojuholníku a stlač ENTER: ")
odvesna2=input("Zadaj dĺžku druhej prepony v pravouhlom trojuholníku a stlač ENTER: ")
a = float(odvesna1) # funkcia float zmení string v zátvorke na desatinné číslo
b = float(odvesna2) # hovoríme tomu pretypovanie

type(a)
x=a**2+b**2
print(x)
c=math.sqrt(x)
c=round(c,2)
print()
print("prepona je:" + str(c)+"!")
input()
