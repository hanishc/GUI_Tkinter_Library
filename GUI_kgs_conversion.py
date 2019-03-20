from tkinter import *

window = Tk()

def kgs_to_params():
    grams=float(kg_value.get())*1000
    pounds=float(kg_value.get())*2.20462
    ounces=float(kg_value.get())*35.274
    t2.delete("1.0",END)
    t2.insert(END,grams)
    t3.delete("1.0",END)
    t3.insert(END,pounds)
    t4.delete("1.0",END)
    t4.insert(END,ounces)

button1 = Button(window,text="Convert",command=kgs_to_params)
button1.grid(row=0,column=2)

l1=Label(window,text="Kg")
l1.grid(row=0,column=0)

kg_value = StringVar()
t1=Entry(window,textvariable=kg_value)
t1.grid(row=0,column=1)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=0)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=1)

t4=Text(window,height=1,width=20)
t4.grid(row=1,column=2)
window.mainloop()
