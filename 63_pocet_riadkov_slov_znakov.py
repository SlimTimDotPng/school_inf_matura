subor1 = open("timotej24.txt","r")

p_r = 0
p_s = 0
p_z = 0

while True: # while prejde aspon raz, vo vnutri podmienka na ukoncenie cyklu
    r = subor1.readline()

    
    if len(r) == 0:
        break

    p_r += 1
    
    r = r.strip() #odstrani všetky medzery na začiatku a konci reťazca

    p_z += len(r)
    
    slova = r.split(" ")
    
    
    

    for slovo in slova:
        
        if len(slovo) > 0:
            if slovo[-1] in {",",".",":",";","!","?"}:
            #slovo[-1] == "," or slovo[-1] == ".":
                slovo = slovo.replace(slovo[-1], "")
            print(slovo)
            p_s += 1
    



print("Počet riadkov je:", p_r)
print("Počet slov je:", p_s)
print("Počet znakov je:", p_z)
