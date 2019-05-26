from tkinter import *

janela = Tk()

l1 = Label(janela, width = 15, height=6, bg="red")
l2 = Label(janela, width = 15, height=6, bg="blue")
l3 = Label(janela, width = 15, height=6, bg="black")
l4 = Label(janela, width = 15, height=6, bg="yellow")
l5 = Label(janela, width = 6, height=1, bg="green")
l6 = Label(janela, width = 3, height=6, bg="pink")

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=0, column=1)
l4.grid(row=1, column=1)
l5.grid(row=2, column=0, columnspan=2, sticky=W+E)
l6.grid(row=0, column=2, rowspan=2, sticky= N+S)

janela.geometry("400x500+200+200")
janela.mainloop() 