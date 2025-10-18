import tkinter as tk

win = tk.Tk()
win.title('Cylinder Calculator')
win.geometry('500x300')

txt1 = tk.Label(win, text = 'ระบุรัศมีของทรงกระบอก    (cm) : ')
txt1.place(x=20,y=30)
txt2 = tk.Label(win, text = 'ระบุความสูงของทรงกระบอก (cm) : ')
txt2.place(x=20,y=60)

box1 = tk.Entry(win)
box1.place(x=200,y=30)
box2 = tk.Entry(win)
box2.place(x=200,y=60)

def Cyl():
    r = float(box1.get())
    h = float(box2.get())
    result = 3.14*r*r*h
    txt3 = tk.Label(win, text = 'ปริมาตรของทรงกระบอกคือ %.2f (cm)^2' %result)
    txt3.place(x=20,y=120)

cmd = tk.Button(win, text = 'ตกลง' , command= Cyl)
cmd.place(x=20,y=90)

win.mainloop()