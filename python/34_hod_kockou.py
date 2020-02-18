import random
import tkinter
canvas = tkinter.Canvas( width = 1000, height = 1000 )
canvas.pack()


def sucet():
    h = random.randint(1,6)
    b = random.randint(1,6)
    
    s = b + h
    return s 


#hl.p.
a8 = 0
a7 = 0
a11 = 0


for i in range(1,1001):
    if sucet() == 7:
        a7 += 1
        
    if sucet() == 11:
        a11 += 1

    if sucet() == 8:
        a8 += 1
        
print(f'Súčet 8 padol {a8} krát')
print(f'Súčet 11 padol {a11} krát')
print(f'Súčet 7 padol {a7} krát')

canvas.create_line(0, 400, 200, 400)   
canvas.create_line(50, 400, 50, 400-a8)
canvas.create_line(100, 400, 100, 400-a11)
canvas.create_line(150, 400, 150, 400-a7)

canvas.create_text(50, 420, text = 8, font = 'Arial 20 bold')
canvas.create_text(100, 420, text = 11, font = 'Arial 20 bold')
canvas.create_text(150, 420, text = 7 , font = 'Arial 20 bold')
