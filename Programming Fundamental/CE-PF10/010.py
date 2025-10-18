import tkinter as tk

def Click():
    lbl.config(text = 'ปุ่มได้ถูกกดแล้ว')

win = tk.Tk()
win.title('การตรวจสอบปุ่มที่ถูกกด (ปุ่มถูกคลิก)')
win.geometry('800x500')

cmd = tk.Button(win, text = 'คลิกที่นี่', command = Click)
cmd.place(x=30,y=50)

lbl = tk.Label(win, text = 'Hello GUI World!!!', fg = 'red')
lbl.place(x=30,y=80)

win.mainloop()