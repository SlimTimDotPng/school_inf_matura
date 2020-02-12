subor1 = open('c:\\users\\maturita\\uloha2.txt','w')#vznikne nový priečinok
udaj = input("zadaj meno:")

subor1.write(udaj + "\n")
udaj = input("zadaj priezvisko:")
subor1.write(udaj + "\n")
udaj = input("zadaj vek:")
subor1.write(udaj + "\n")
udaj = input("zadaj adresu:")
subor1.write(udaj + "\n")
subor1.close()
