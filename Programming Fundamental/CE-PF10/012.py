import tkinter as tk

win = tk.Tk()
win.title('การสร้างกล่องรับข้อความจากผู้ใช้งาน')
win.geometry('500x300')

lbl = tk.Label(win,text = 'ชื่อ-นามสกุล')
lbl.place(x = 20,y=20)

txt = tk.Entry(win)
txt.place(x = 90,y =20)

def ShowMessage():
    name = txt.get()
    lbl2 = tk.Label(win, text = 'สวัสดี คุณ' + name, font = 'AngsanaNew 24')
    lbl2.place(x=20,y=50)

cmd = tk.Button(win,text = 'ตกลง', command = ShowMessage)
cmd.place(x=20,y=50)

win.mainloop()