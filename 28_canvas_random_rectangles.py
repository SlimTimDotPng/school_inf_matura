import tkinter
import random
canvas = tkinter.Canvas(width = 1200, height = 1000 )
canvas.pack()




for s in range(1, 1111):
    


    x = (random.randrange(500))
    y = (random.randrange(500))
    velkost = (random.randrange(500))
    farba = random.choice(('red','green','yellow','grey','blue'))
    canvas.create_rectangle(x , y, x+velkost,y+velkost,fill = farba)
    canvas.create_text(x+velkost/2,y+velkost/2, text = s , font = 'Arial 20 bold')
    canvas.update()
    canvas.after(10)
