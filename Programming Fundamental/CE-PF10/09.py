import tkinter as tk

frm = tk.Tk()
frm.config(bg = '#ccffff')
frm.geometry('960x240')
frm.title('My First GUI')

msg1 = tk.Label(frm, text = 'HI My name is Pongsakorn Sinsuwan' , bg = '#ccffff' , font = 'STKaiti 20 bold')
msg1.place(x=30,y=20)
msg2 = tk.Label(frm, text = 'I\'m 1st years student in Computer Engineering of KMITL.PCC', bg = '#ccffff' , font = 'STKaiti 20 bold')
msg2.place(x=30,y=60)
msg3 = tk.Label(frm, text = 'I\'m 42nd members of Computer Engineering',bg ='#ccffff' , font = 'STKaiti 20 bold')
msg3.place(x=30,y=100)

frm.mainloop()