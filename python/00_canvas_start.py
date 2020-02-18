from random import *
import tkinter
canvas = tkinter.Canvas(bg = 'black', width = 1000, height = 1000 )
canvas.pack()

x = 10
y = 10

for i in range (1,26):
    x += 20
    y += 20
    canvas.create_line(x, 10, 510, y, fill = 'white', width = 2)
    canvas.update()
    canvas.after(100)


x = 510
y = 10

for s in range (1,26):
    y += 20
    x -= 20
    canvas.create_line(510, y, x, 510, fill = 'white', width = 2)
    canvas.update()
    canvas.after(100)


x = 510
y = 10

for s in range (1,26):
    y += 20
    x -= 20
    canvas.create_line(x, 10, 10, y, fill = 'white', width = 2)
    canvas.update()
    canvas.after(100)

x = 510
y = 510

for s in range (1,26):
    y -= 20
    x -= 20
    canvas.create_line(x, 510, 10, y, fill = 'white', width = 2)
    canvas.update()
    canvas.after(100)



