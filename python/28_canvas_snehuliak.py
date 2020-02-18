import tkinter
import random
canvas = tkinter.Canvas(width = 1200, height = 1000 )
canvas.pack()

for s in range(1, 10):

    canvas.create_rectangle(random.randrange(1000), random.randrange(1000), random.randrange(1000), random.randrange(1000))
