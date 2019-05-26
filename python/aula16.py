

#           GRID



from tkinter import *

janela = Tk()

lb1 = Label(janela, text = "espaço", width = "15", height = "2", bg = "blue")
horizontal = Label(janela, text ="horizontal", bg = "yellow")
vertical = Label(janela, text ="vertical")

lb1.grid(row=0, column =1)
horizontal.grid(row=1, column =0, sticky=S)
vertical.grid(row=1, column =2, sticky=W)

janela.geometry("400x500+200+200")
janela.mainloop() 