import tkinter
canvas = tkinter.Canvas(width = 1200, height = 1000 )
canvas.pack()
canvas.create_line(110, 10, 10, 200, fill='blue')
canvas.create_line(10, 200, 210, 200, fill='blue')
canvas.create_line(210, 200, 110, 10, fill='blue')

canvas.create_line(160, 10, 60, 200, fill='red')
canvas.create_line(60, 200, 260, 200, fill='red')
canvas.create_line(260, 200, 160, 10, fill='red')



canvas.create_rectangle(300, 200, 500, 300,width= 8,outline='red' ,fill='blue')


canvas.create_rectangle(200, 400, 500, 700)

canvas.create_oval(500, 600, 600, 700,fill='grey')

canvas.create_oval(700, 400, 800, 600,fill='green')
