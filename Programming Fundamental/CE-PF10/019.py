import tkinter as tk
from tkinter import messagebox
from tkinter import IntVar

win = tk.Tk();win.title('การใช้งาน Check Button')
win.geometry('500x300')
lbl = tk.Label(win, text ='กรุณาระบุสัญชาติ : ')
lbl.place(x=20,y=20)

def ShowMessage():
    if(national.get() ==1 ):national1 = ' ไทย'
    elif(national.get() ==2 ):national1 = ' จีน'
    elif(national.get() ==3 ):national1 = ' ญี่ปุ่น'
    elif(national.get() ==4 ):national1 = ' อเมริกา'
    userSelected = 'สัญชาติของคุณคือ' + str(national1)
    lbl.config(text = userSelected)
national = IntVar()

opt1 = tk.Radiobutton(win, text = 'ไทย',variable = national, value = 1,command = ShowMessage)
opt1.place(x=20,y=40)
opt2 = tk.Radiobutton(win, text = 'จีน',variable = national, value = 2,command = ShowMessage)
opt2.place(x=20,y=60)
opt3 = tk.Radiobutton(win, text = 'ญี่ปุ่น',variable = national, value = 3,command = ShowMessage)
opt3.place(x=20,y=80)
opt4 = tk.Radiobutton(win, text = 'อเมริกา',variable = national, value = 4,command = ShowMessage)
opt4.place(x=20,y=100)

win.mainloop()