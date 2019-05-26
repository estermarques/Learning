
#           PLACE

from tkinter import *

def click():
    lb["text"] = ed.get()

janela = Tk()

ed = Entry(janela)
ed.place(x = 100, y = 100)

bt = Button(janela, width=20, text="clica", command = click)
bt.place(x=100, y=150)

lb = Label(janela, text="label")
lb.place(x=100, y=200)

janela.geometry("300x300+300+300")
janela.mainloop()