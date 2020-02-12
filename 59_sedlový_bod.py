z = []
N = 4

for i in range(N):
    z.append([0]*N)

z[0] = [1,0,4,8]
z[1] = [7,4,9,7]
z[2] = [3,2,1,4]
z[3] = [20,5,10,7]

for i in range(N):
    for j in range(N):
        print(z[i][j], end=" ")
    print()


for r in range(N):
    smin = z[r].index(min(z[r]))
    print(smin)
    test = True
    
    for riadok in range(N):
        if z[riadok][smin] > z[r][smin]:
            test = False
            break
    if test:
        print("Sedlový bod je:",z[r][smin], "pozicia:",r ,smin)
