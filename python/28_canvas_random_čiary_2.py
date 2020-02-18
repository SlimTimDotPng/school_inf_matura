import tkinter
import random
canvas = tkinter.Canvas(width = 1200, height = 1200 )
canvas.pack()
g = 0

for i in range (1, 16):
    canvas.create_line(i*10,100-g, i*10,500-g)
    canvas.update()
    canvas.after(100)
    g-=10
    
