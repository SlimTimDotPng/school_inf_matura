n = int(input("zadaj počet riadkov a stĺpcov násobilky: "))
print("     ",end=" ")

for i in range(1, n+1):
    print(f'{i:5}', end=" ")
print()
print()
for r in range(1, n+1):
    print(f'{r:5}', end=" ")
    for s in range(1,n+1):
        print(f'{r*s:5}', end=" ")
    print()
    
