
subor1 = open('C:\\Users\\maturita\\basen.txt','r')
subor2 = open('c:\\users\\maturita\\kopia.txt','w')

slovo = input('zadaj svoje slovo:')

while True:
    r = subor1.readline()

    if len(r) == 0:
        break
    s = r.strip()
    if len(s) == 0:
        subor2.write(slovo + '\n' )

    else:
        subor2.write(r)

subor1.close()
subor2.close()
