import tkinter as tk

win = tk.Tk()
win.title('Distance Calculator')
win.geometry('500x300')

txt1 = tk.Label(win, text = 'ระบุความเร็วต้น  (m/s)     : ');        txt1.place(x=20,y=30)
txt2 = tk.Label(win, text = 'ระบุความเร่ง      (m/s^2) : ');        txt2.place(x=20,y=60)
txt3 = tk.Label(win, text = 'ระบุระยะเวลา      (s)          : ');  txt3.place(x=20,y=90)

box1 = tk.Entry(win); box1.place(x=150,y=30)
box2 = tk.Entry(win); box2.place(x=150,y=60)
box3 = tk.Entry(win); box3.place(x=150,y=90)

def Distance():
    u = float(box1.get())
    a = float(box2.get())
    t = float(box3.get())
    result = (u*t)+(0.5*a*(t*t))
    txt4 = tk.Label(win, text = 'ระยะทางคือ %.2f (m)' %result)
    txt4.place(x=20,y=150)

cmd = tk.Button(win, text = 'ตกลง' , command= Distance); cmd.place(x=20,y=120)

win.mainloop()