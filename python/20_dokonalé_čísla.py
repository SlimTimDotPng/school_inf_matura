n = int(input("Zadaj celé číslo: "))
for i in range(1, n+1):
    sucet = 0
    for j in range(1, i):
        if i%j==0:
            sucet += j
    if sucet == i:
        print(i)

