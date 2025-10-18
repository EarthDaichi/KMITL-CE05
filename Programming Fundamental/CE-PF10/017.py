import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title('Distance Calculator 2')
win.geometry('500x300')

U = tk.Label(win, text = 'ระบุความเร็วต้น  (m/s)     : ');        U.place(x=20,y=30)
A = tk.Label(win, text = 'ระบุความเร่ง      (m/s^2) : ');        A.place(x=20,y=60)
T = tk.Label(win, text = 'ระบุระยะเวลา      (s)          : ');  T.place(x=20,y=90)

box_U = tk.Entry(win); box_U.place(x=150,y=30)
box_A = tk.Entry(win); box_A.place(x=150,y=60)
box_T = tk.Entry(win); box_T.place(x=150,y=90)

def Distance():
    u = float(box_U.get())
    a = float(box_A.get())
    t = float(box_T.get())
    result = (u*t)+(0.5*a*(t*t))
    messagebox.showinfo('การคำนวณหาระยะทาง', 'ระยะทาง = %.2f' %result)

cmd = tk.Button(win, text = 'ตกลง' , command= Distance); cmd.place(x=20,y=120)

win.mainloop()