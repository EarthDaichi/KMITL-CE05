from tkinter import *

win = Tk()
win.title('Chat by Python')
win.geometry('400x360')
win.resizable(0,0)
win.config(padx=5,pady=5)
win.option_add('*font','tahoma 10')

fm1 = Frame(win)
fm1.pack(side=TOP, fill=BOTH, expand=YES)

text_msg = Text(fm1,height=15,bg='powderblue', font='tahoma 10')
text_msg.insert(1.0,'มานี: สวัสดีค่ะ')
v_scrollbar = Scrollbar(fm1,command=text_msg.yview)
v_scrollbar.pack(side=RIGHT, fill=Y)
text_msg.config(yscrollcommand=v_scrollbar.set)
text_msg.pack(side=LEFT, fill=BOTH, expand=YES)
text_msg.bind('<Key>', lambda e: 'break')

fm2 = Frame(win)
fm2.pack(side= TOP,fill=BOTH,expand=YES)

def add_radio(w):
    w.pack(side=LEFT,padx=10)
    w.config(variable=str_var, value=w.cget('text'))

str_var = StringVar(value='มานี')
add_radio(Radiobutton(fm2,text='มานี'))
add_radio(Radiobutton(fm2,text='ปิติ'))
add_radio(Radiobutton(fm2,text='วีระ'))
add_radio(Radiobutton(fm2,text='ชูใจ'))

fm3 = Frame(win)
fm3.pack(side=TOP,fill=X,expand=YES,padx=5)

ent_msg = Entry(fm3)
ent_msg.pack(side=LEFT,fill=X,expand=YES,padx=5)
bt_send = Button(fm3,text='ส่ง',command=lambda: btSend_click(), bg='lightgray',fg='blue')
bt_send.pack(side=LEFT,padx=5,ipadx=5)

def btSend_click():
    person = str_var.get()
    msg = ent_msg.get()
    text = f'\n{person}:{msg}'
    text_msg.insert(END,text)
    ent_msg.delete(0,END)

mainloop()