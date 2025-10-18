import tkinter as tk

frm = tk.Tk()
frm.config(bg = '#ccffff')
frm.geometry('360x240')
frm.title('My First GUI')
msg = tk.Label(frm, text = ' a Text in GUI')
msg.place(x=30,y=20)

frm.mainloop()