subor1 = open("timotej24.txt","r")
while True: # while prejde aspon raz, vo vnutri podmienka na ukoncenie cyklu
    r = subor1.readline()
    if len(r) == 0:
        break
    r = r.strip() #odstrani všetky medzery na začiatku a konci reťazca
    slova = r.split(" ")

    for slovo in slova:
        if len(slovo) > 0:
            if slovo[-1] in {",",".",":",";","!","?"}:
            #slovo[-1] == "," or slovo[-1] == ".":
                slovo = slovo.replace(slovo[-1], "")
            print(slovo)
