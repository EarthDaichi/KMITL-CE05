import tkinter as tk
from tkinter import messagebox
from tkinter import IntVar

win = tk.Tk(); win.title('การใช้งาน Check Button')
win.geometry('500x300')

def ShowMessage():
    userSelected = 'ภาษาเขียนโปรแกรมที่สนใจ'
    if(chb1.var.get() == 1):
        userSelected = userSelected + ' Visual basic '
    if(chb2.var.get() == 1):
        userSelected = userSelected + ' Python '
    lbl.config(text = userSelected)

chk1 = IntVar()
chk2 = IntVar()
lbl = tk.Label(win, text = 'โปรดเลือกภาษาเขียนโปรแกรมที่สนใจ : ')
lbl.place(x=20,y=20)

chb1 = tk.Checkbutton(win,text = 'ภาษา Visual Basic', variable = chk1,
                      onvalue = 1, offvalue = 0, command = ShowMessage)
chb1.place(x=20,y=50)
chb1.var = chk1
chb2 = tk.Checkbutton(win, text = 'ภาษา python', variable = chk2,
                      onvalue = 1,offvalue = 0, command = ShowMessage)
chb2.place(x=20,y=80)
chb2.var = chk2

win.mainloop()