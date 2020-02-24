# === Úloha 3===
# Vytvorte program, ktorý bude simulovať semafor. Pri stlačení tlačidla preblikne na ďalší povel v poradí. Na vykresľovanie semafora vytvorte funkciu s vhodným počtom parametrov.
from tkinter import Canvas

canvas = Canvas(width=300, height=500)
canvas.pack()

teraz_povel = 0

def kresli(povel):
    global canvas
    canvas.delete('all')

    if povel == 0:
        canvas.create_oval(20,20,60,60,fill='red')
    elif povel == 1:
        canvas.create_oval(20,20,60,60,fill='red')
        canvas.create_oval(20,60,60,100,fill='orange')
    elif povel == 2:
        canvas.create_oval(20,100,60,140,fill='green')
    elif povel == 3:
        canvas.create_oval(20,60,60,100,fill='orange')

def klik(event):
    global teraz_povel
    teraz_povel += 1

    if teraz_povel == 4:
        teraz_povel = 0

    kresli(teraz_povel)

canvas.bind("<Button-1>",klik)

kresli(teraz_povel)
canvas.mainloop() 



