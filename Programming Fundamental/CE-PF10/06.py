import tkinter as tk

frm = tk.Tk()
frm.config(bg = '#ccffff')
frm.geometry('360x240')
frm.title('My First GUI')

msg1 = tk.Label(frm, text = 'a Text in GUI')
msg1.place(x=30,y=20)
msg2 = tk.Label(frm, text = 'a Second Text in GUI', font ='consolas')
msg2.place(x=30,y=50)
msg3 = tk.Label(frm, text = 'a Third Text in GUI', font = 'consolas 18')
msg3.place(x=30,y=80)
msg4 = tk.Label(frm, text = 'a Fourth Text in GUI', font = 'consolas 18 bold')
msg4.place(x=30,y=110)

frm.mainloop()