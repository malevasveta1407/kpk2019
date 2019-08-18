import tkinter


def paint(event):
    """Обработчик сабытий для холста
    :param event:событие
    :return: ничего
    """
    print(event.x, event.y)
    if event.widget != canvas:
        print('Странно, ведь paint() привязывали только к canvas...')
        return
    canvas.coords(line, 0, 0, event.x, event.y)


root = tkinter.Tk()

canvas = tkinter.Canvas(root, background='white', width=400, height=400)
canvas.bind("<Motion>", paint)
canvas.pack()

line = canvas.create_line(0, 0, 10, 10)
for i in range(10):
    canvas.create_oval(3+i*40, 3+i*40, i*40+30, i*40+30, fill='green', width=2)
root.mainloop()
print("Это строка будет достигнута только при выходе из приложения")
