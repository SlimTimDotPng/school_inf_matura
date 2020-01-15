#PODPROGRAMY (v pythone sa nazývajú funkcie)
import random
import tkinter


vyska, sirka = 600, 800
canvas = tkinter.Canvas(width = sirka, height = vyska)
canvas.pack()

def kruh():
    r = random.randint(20, 40)
    x = random.randint(40, sirka - 40)
    y = random.randint(40, vyska - 40)
    farba = random.choice(('red','green','blue'))
    canvas.create_oval(x, y, x+r, y+r, fill = farba)

#HL. Program

for i in range (1,300):
    kruh()
    
