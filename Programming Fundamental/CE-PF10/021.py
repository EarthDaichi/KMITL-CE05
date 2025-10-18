from tkinter import *
win = Tk()
win.title('Calculator by Python')
win.geometry('215x295')
win.resizable(0,0)
win.config(padx=5,pady=5)
win.option_add('*font','times 14')
win.option_add('*Button.width',3)
win.option_add('*Button.background', 'lightgray')
str_var = StringVar()
display = Entry(textvariable=str_var,width=22,justify=RIGHT,
                state=DISABLED, disabledforeground='blue', disabledbackground='wheat')
display.grid(row=0,column=0,columnspan=4,padx=2,pady=5,ipady=2)
def add_button(button,r,c,t):
    button.config(text=t,command=lambda: button_click(button))
    button.grid(row=r,column=c,padx=5,pady=5)
text =[[],['C', '(',')', '%'], [7,8,9,'/'], [4,5,6,'*'],[1,2,3,'-'],[0,'.','=','+']]
for (row,tx) in enumerate(text):
    for (col,t) in enumerate(tx):
        add_button(Button(),row,col,t)
def button_click(button):
    if str_var.get() == 'Error':
        str_var.set('')
    t = button.cget('text')
    if t == 'C':
        str_var.set('')
    elif t == '=':
        try:
            result = eval(str_var.get())
            if result % 1 ==0:
                result = int(result)
            
            str_var.set(result)
        except:
            str_var.set('Error')
    
    else:
        str_var.set(str_var.get() + str(t))
mainloop()