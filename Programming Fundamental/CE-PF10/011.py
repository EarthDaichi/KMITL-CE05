import tkinter as tk

win = tk.Tk()
win.title('การสร้างกล่องรับข้อความจากผู้ใช้งาน')
win.geometry('500x300')

lbl = tk.Label(win,text = 'ชื่อ-นามสกุล')
lbl.place(x = 20,y=20)

txt = tk.Entry(win)
txt.place(x = 90,y =20)

win.mainloop()