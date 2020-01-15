import random
"""
z = ["pa"]*20 #* viacnásobne zopakuje obsah premenej do novej štruktúry
print(z)
for i in range(0,20):
    z[i] = random.randint(1,1000)
for i in range(20):
    print(z[i], end=" ")

"""
#2.spôsob
"""
z = []
for i in range(0,20):
    z = z + [random.randint(1,1000)]
for i in range(20):
    print(z[i], end=" ")
"""
#3. spôsob
"""
z = []
for i in range(0,20):
    z.append(random.randint(1,1000))
for i in range(20):
    print(z[i], end=" ")
"""

z = []
for i in range(0,20):
    z = z + [random.randint(1,1000)]
"""
for i in reversed(range(20)):
    print(z[i], end=" ")
print()
print()
"""
for i in range(20):
    print(z[i], end=" ")

