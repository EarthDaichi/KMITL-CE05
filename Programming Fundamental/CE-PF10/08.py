import tkinter as tk

frm = tk.Tk()
frm.config(bg = '#ccffff')
frm.geometry('360x240')
frm.title('My First GUI')

msg1 = tk.Label(frm, text = 'a Text in GUI')
msg1.place(x=30,y=20)
msg2 = tk.Label(frm, text = 'a Second Text in GUI', bg = '#ccffff' , font ='consolas')
msg2.place(x=30,y=50)
msg3 = tk.Label(frm, text = 'a Third Text in GUI', bg = '#ccffff' , font = 'consolas 18')
msg3.place(x=30,y=80)
msg4 = tk.Label(frm, text = 'a Fourth Text in GUI', bg = '#ccffff' , font = 'consolas 18 bold')
msg4.place(x=30,y=110)
msg5 = tk.Label(frm, text = 'a Fifth Text in GUI', bg = '#ccffff' , fg = '#0000ff', font = 'consolas 18 bold')
msg5.place(x=30,y=140)

frm.mainloop()