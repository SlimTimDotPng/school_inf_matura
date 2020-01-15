"""

faktoriál čísla n

"""

n = int(input("Zadaj číslo: "))
f = 1   #f = faktorial 
for i in range(1, n+1):
    f = f * i
print("Faktoriál čísla", n, "je:", f)
