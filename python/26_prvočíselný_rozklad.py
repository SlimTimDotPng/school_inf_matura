c = int(input("Zadaj prirodzené číslo: "))
p = 2

while c > 0:
    if c % p == 0:
        c = c // p #alebo c //= p
        if c<=1:
            print(p)
            
        else:
            print(p, end = "*")
            
    else:
        p = p + 1
