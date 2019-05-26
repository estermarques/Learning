#aulas 5 a 7

from functools import partial
from tkinter import *

def bt_click(botao):
    print(botao["text"])


janela = Tk()

bt =Button(janela, width=10, text= "clica aqui mané")
bt["command"] = partial(bt_click, bt)
bt.place(x=21, y=20)

bt2 =Button(janela, width=10, text= "clica aqui pfvr")
bt2["command"] = partial(bt_click, bt2)
bt2.place(x=21, y=50)

janela.geometry("150x100+200+200")

janela.mainloop()