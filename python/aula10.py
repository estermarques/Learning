
#           PACK

from tkinter import *

janela = Tk()

lb1 = Label(janela, text = "ummmm", bg = "green", font=('arial','30'),)
lb2 = Label(janela, text = "palavra", font=('Symbol','30'), bg = "red")
lb3 = Label(janela, text = "lbl3", bg = "yellow")
lb4 = Label(janela, text = "lbl4", bg = "brown")

lb1.pack(side = TOP)
lb2.pack(side = TOP, expand = 1,anchor=E)
lb3.pack(anchor = SE, expand = 1)
lb4.pack(anchor=S, expand = 1)

janela.geometry("400x500+200+200")
janela.mainloop() 