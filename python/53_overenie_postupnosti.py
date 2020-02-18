import random

n = 4
z = []
#x = 0 ??????
def skuska(zoznam):
    x = False
    for j in range(0,len(zoznam)-1):
        if z[j] < z[j+1]:
            x = True
    return x



for i in range(1,n):
    z = z + [(random.randint(1,5))]

print(z)



skuska(z)
if x == True:
    print("postupnosť je rastúca")

             
