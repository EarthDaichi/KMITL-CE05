import tkinter as tk

win = tk.Tk()
win.title('การสร้างกล่องรับข้อความจากผู้ใช้งาน')
win.geometry('500x300')

txt1 = tk.Label(win, text = 'โปรดป้อนความกว้าง (m) : ')
txt1.place(x=20,y=20)
txt2 = tk.Label(win, text = 'โปรดป้อนความยาว (m) : ')
txt2.place(x=20,y=50)

box1 = tk.Entry(win)
box1.place(x=150,y=20)
box2 = tk.Entry(win)
box2.place(x=150,y=50)

def Cal():
    value1 = float(box1.get())
    value2 = float(box2.get())
    ans = value1*value2
    txt3 = tk.Label(win,text = 'พื้นที่สี่เหลี่ยม = %.2f' %ans, font = 'AngsanaNew 24')
    txt3.place(x=20,y=110)

cmd = tk.Button(win, text = 'ตกลง', command = Cal)
cmd.place(x = 20,y =80)

win.mainloop()