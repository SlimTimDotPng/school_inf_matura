#normálny postup
n = int(input("zadaj n: "))
for r in range(1, n+1):
    for j in range(1, n-r+1):
        print(" ",end=" ")
    for s in range(1,r+1):
        print("*",end=" ")
    print()        
print()

#skrátený
for r in range(1, n+1):
    print("a "*(n-r),"* "*r)
print()

#obrátený
for r in reversed(range(1, n+1)):
    for j in (range(1, n-r+1)):
        print(" ",end=" ")
    for s in range(1,r+1):
        print("*",end=" ")
    print()        
print()

#skrátený obrátený
for r in reversed(range(1, n+1)):
    print("a "*(n-r), "* "*r)
print()
