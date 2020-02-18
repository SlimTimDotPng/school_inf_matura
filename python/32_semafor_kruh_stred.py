import random
import tkinter


vyska, sirka = 1000, 1000
canvas = tkinter.Canvas(width = sirka, height = vyska, bg = 'white')
canvas.pack()

def kruh_stred(sx, sy, farba):
    
    canvas.create_oval(sx, sy, sx+50, sy+50, fill = farba)
    
#HL.p.
    
canvas.create_rectangle(200 ,400 ,250, 550,fill = 'black')
while True:
    kruh_stred(200,400,'red')
    canvas.update()
    canvas.after(5555)

    kruh_stred(200,400,'black' )

    kruh_stred(200,450,'orange' )
    canvas.update()
    canvas.after(4444)

    kruh_stred(200,450,'black' )

    kruh_stred(200,500,'green' )
    canvas.update()
    canvas.after(5555)

    kruh_stred(200,500,'black' )

    kruh_stred(200,450,'orange' )
    canvas.update()
    canvas.after(4444)

    kruh_stred(200,450,'black' )
