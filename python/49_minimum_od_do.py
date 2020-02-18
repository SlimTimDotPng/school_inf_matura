#zle
"""
def minimum(a,c): 
    poz_min = 0
    
    for i in range(a,len(c)):
        if c[i] < c[poz_min]:
            poz_min = i
    return poz_min

z= [90,420,85,41,74,76,94,71,7,69]

for j in range(len(z)):
    z[j], z[minimum(j,z)] = z[minimum(j,z)], z[j]

print(z,end=" ")
"""

def minimum(a,c): 
    poz_min = 0
    
    for i in range(a,len(c)):
        if c[i] < c[poz_min]:
            poz_min = i
    return poz_min

z= [90,420,85,41,74,76,94,71,7,69]

for j in range(len(z)):
    poz_min = j
    for k in range(j,len(z)):
        if z[k] < z[poz_min]:
            poz_min = k
    z[j], z[poz_min] = z[poz_min], z[j]


    
print(z,end=" ")
