from tkinter import *

#Creating an empty window.
window = Tk()

def kms_to_miles():
#    print("on")
    miles=float(c1_value.get())*1.6
    t1.insert(END,miles)

b1 = Button(window,text="Execute",command=kms_to_miles)

# grid is a Button widget method.
# pack method is also present but grid has more control on rows and columns.
b1.grid(row=0,column=0)

c1_value=StringVar()
c1 = Entry(window,textvariable=c1_value)
c1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

#end of code.
window.mainloop()
