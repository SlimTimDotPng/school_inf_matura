import math 
subor1 = open('kvadrat.txt','w')

a = input('zadaj koeficient a:')
b = input('zadaj koeficient b:')
c = input('zadaj koeficient c:')
print()

r = a+'*x*x+('+ b + ')*x+('+c+')'
print(r)

subor1.write(r + '\n')

a = float(a)
b = float(b)
c = float(c)

D = b**2 - 4*a*c

if D < 0:
    print("Kvadratická rovnica nemá riešienie v R")
else:
    if D == 0:
        print("Kvadratická rovnoca má jedno riešenie")
        x = -b/(2*a)
        print(f"Riešenie je: {x:6.3f}")
    else:
        if D > 0:
            print("Kvadratická rovnica má dve riešenia v R")
            x1 = (-b + math.sqrt(D))/2*a
            x2 = (-b - math.sqrt(D))/2*a
            print()
            print(f"Prvé riešenie je: {x1:6.3f}")
            print(f"Druhé riešenie je: {x2:6.3f}")
            
print()

if D == 0:
        
        x = -b/(2*a)
        subor1.write(f"Riešenie je: {x:6.3f}" + '\n')
else:
    if D > 0:
        x1 = (-b + math.sqrt(D))/2*a
        x2 = (-b - math.sqrt(D))/2*a
            
        subor1.write(f"Prvé riešenie je: {x1:6.3f}" + '\n')
        subor1.write(f"Druhé riešenie je: {x2:6.3f}" + '\n')
    else:
        subor1.write("Kvadratická rovnica nemá riešienie v R")
subor1.close()

