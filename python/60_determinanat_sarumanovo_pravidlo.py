
a = int(input("zadaj a:"))
b = int(input("zadaj b:"))
c = int(input("zadaj c:"))
d = int(input("zadaj d:"))
e = int(input("zadaj e:"))
f = int(input("zadaj f:"))
g = int(input("zadaj g:"))
h = int(input("zadaj h:"))
i = int(input("zadaj i:"))
print()
z = [
    [a,b,c],
    [d,e,f],
    [g,h,i]
    ]

for r in range(len(z)):
    for s in range(len(z)):
        print(z[r][s], end=" ")
    print()

print()

D = a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h
print("determinan týchto čísiel je:",D)


