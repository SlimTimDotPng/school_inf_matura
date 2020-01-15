import random
import tkinter
import math

vyska, sirka = 600, 600

canvas = tkinter.Canvas(width = sirka, height = vyska, bg = 'white')
canvas.pack()

def stvorec_stred(sx,sy,a):

    canvas.create_rectangle(sx-a, sy-a, sx+a, sy+a, fill = '', outline = 'red')
    u = a * math.sqrt(2)
    return u

#HL.P.
print(stvorec_stred(200,300,65))
