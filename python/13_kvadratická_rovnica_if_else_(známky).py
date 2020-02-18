max_pocet = int(input("Zadaj ma pocet bodov z testu: "))
ziskany_pocet = int(input("Zadaj získaný počet bodov z testu: "))
p = ziskany_pocet /  max_pocet * 100
if p >= 89:
    print("Známka 1")
elif 75 <= p < 89:
    print("Známka 2")
elif 50 <= p < 75:
    print("Známka 3")
elif 35 <= p < 50:
    print("Známka 4")
else:
    print("Známka 5")
