from tkinter import *

def clk():
    if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        lb["text"] = float(ed1.get()) + float(ed2.get())
    else:
        lb["text"] = "você é burro"
    
    

janela = Tk()

ed1 = Entry(janela)
ed1.place(x=100, y=100)
ed2 = Entry(janela)
ed2.place(x=100, y=130)

bt = Button(janela, text = "Soma", command = clk)
bt.place(x=100, y=150)

lb = Label(janela)
lb.place(x=100, y=200)

janela.geometry("400x500+200+200")
janela.mainloop()