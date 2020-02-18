n = int(input("zadaj číslo n: "))
sucet = 0
for i in reversed(range(1,n+1,2)):
    sucet = sucet + i
    print(i,end=" ")
print()
print()
print("sučet nepárnych čísel od 1 po ", n, "je: ", sucet)
      
        
