import tkinter
import random 
canvas = tkinter.Canvas(width = 1200, height = 1000 )
canvas.pack()
for s in range(1, 100):

    canvas.create_line(0, 0, random.randrange(200), 200, fill='blue')


