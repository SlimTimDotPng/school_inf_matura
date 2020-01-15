import tkinter
canvas = tkinter.Canvas(width=1000,height=1000)
canvas.pack()

def kruh(x,y,r):
    canvas.create_oval(x-r,y-r,x+r,y+r)

def terc(stred):
    sx = stred.x
    sy = stred.y
    r= 10
    for i in range(1,11):
        r+=10
        kruh(sx,sy,r)

canvas.bind('<Button-1>',terc)
        
        
