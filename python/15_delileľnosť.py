"""

Všetky párny, deliteľné 14 a nesudeliteľné 11


for i in range(2, 1001,2):
    if i%14==0 and i%11!=0: # != znamená nerovná sa 
        print(i)


for i in range(14, 101,14):
    if i%11!=0: # != znamená nerovná sa 
        print(i)


for i in range(22, 101,11):
    if i%2==0 and i%13!=0: 
        print(i)

"""

for i in range(0,101,2):
    if i%11 == 0 or i%13 == 0: 
        print(i)
