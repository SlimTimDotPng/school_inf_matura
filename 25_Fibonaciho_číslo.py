a = 0
b = 1
c = 1
while c <= 1000000:
    
    print(c, end=", ")
    c = a + b
    a = b
    b = c
print("koniec")
