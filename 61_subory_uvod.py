subor1 = open("timotej24.txt", "r")
while True:
    r = subor1.readline()
    d = len(r)
    if d == 0:
        break
    print(r)
    print("dlžka riadka:", d)
