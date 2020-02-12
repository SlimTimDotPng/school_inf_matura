subor1 = open("timotej24.txt","r")

poc_sam = 0
while True: 
    r = subor1.readline()
    
    poc_sam += r.count("a")
    poc_sam += r.count("e")
    poc_sam += r.count("i")
    poc_sam += r.count("o")
    poc_sam += r.count("u")
    poc_sam += r.count("y")
    
    if len(r) == 0:
        break

print("Pošet samohlások je:", poc_sam)
