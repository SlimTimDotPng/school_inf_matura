
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def kruzok(suradnice):
    a = suradnice.x
    b = suradnice.y
    canvas.create_oval(a-5, b-5, a+5, b+5)

def stvorec(event):
    x = event.x
    y = event.y
    canvas.create_rectangle(x-5, y-5, x+5, y+5)


    


canvas.bind("<Button-1>", kruzok)
canvas.bind("<Button-3>", stvorec)

