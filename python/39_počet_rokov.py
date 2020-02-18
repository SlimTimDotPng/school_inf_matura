#na retazci je ulozeny datum narodenia v pozicii(deň,mesiac,rok_meno_priezvisko)
#meno_priezvisko_ma_v_roku_x_y_rokov
a = '18102000 Timotej Sobota'
b = len(a)
rez1 = a[9:]
rez2 = a[4:8]
roky = 2019 - int(rez2)
print(rez1,'má v roku 2019',roky,'rokov')
