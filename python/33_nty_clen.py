import random
import tkinter

"""
vyska, sirka = 1000, 1000
canvas = tkinter.Canvas(width = sirka, height = vyska, bg = 'white')
canvas.pack()
def kruh_stred(sx, sy):
    canvas.create_oval(sx, sy, sx+2, sy+2)
"""
def nty_clen(n):
    return (5+n**2)/(n+2)

#hl.p
#canvas.create_line(0,400,500,400)
for i in range(1,1000):
    print(nty_clen(i))
"""
    canvas.update()
    canvas.after(10)

    kruh_stred(4*i,200-100*nty_clen(i))
"""
