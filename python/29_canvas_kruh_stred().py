#PODPROGRAMY (v pythone sa nazývajú funkcie)
import random
import tkinter


vyska, sirka = 600, 600
canvas = tkinter.Canvas(width = sirka, height = vyska, bg = 'white')
canvas.pack()

def kruh_stred(sx, sy):
    farba = random.choice(('red','green','blue'))
    canvas.create_oval(sx, sy, sx+20, sy+20, fill = farba)

#HL. Program
s1, s2 = 30, 30
m1, m2 = s1, s2
while s1 < sirka-30:
    fill = 'white'

    kruh_stred(s1, s2)
    s1 += 3
    s2 += 3

    canvas.update()
    canvas.after(60)

    
    canvas.create_oval(m1, m2, m1+20, m2+20, fill = 'white', outline = 'white')
    m1 += 3
    m2 += 3







print("koniec")


