import tkinter as tk
from tkinter import messagebox

win = tk.Tk(); win.title('การสร้าง MessageBox')
win.geometry('500x300')

text1 = tk.Label(win, text = 'ชื่อ-นามสกุล')
text1.place(x=20,y=20)

box1 = tk.Entry(win);box1.place(x=100,y=20)

def ShowMessageBox():
    name = box1.get()
    messagebox.showinfo('ข้อมูลของคุณ','ชื่อ-นามสกุลของคุณคือ '+name)

cmd = tk.Button(win,text = 'ยืนยันการสร้างข้อมูล', command = ShowMessageBox)
cmd.place(x=20,y=50)

win.mainloop()