from tkinter import *
okn=Tk()
okn.title("Calc")

entry=Entry(okn)
entry.grid(row=0, column=0, columnspan=4)
entry.focus_set() #i can write in entry

def num(n):
    entry.insert(END,n)
    
def equ():
    try:
        eque=entry.get()
        value=eval(eque)
        entry.delete(0, END)
        entry.insert(0, value)
    except NameError: #delete a+a= / jakakaka=
        entry.delete(0, END)
        e="Write numbers!"
        entry.insert(0,e)
    
def clearr():
    entry.delete(0, END)
    
def clear():
    get=entry.get()
    gett=get[:-1]
    entry.delete(0, END)
    entry.insert(0, gett)

Button(okn, text="7", command=lambda:num(7), width=3).grid(row=1, column=0)
Button(okn, text="8", command=lambda:num(8), width=3).grid(row=1, column=1)
Button(okn, text="9", command=lambda:num(9), width=3).grid(row=1, column=2)
Button(okn, text="4", command=lambda:num(4), width=3).grid(row=2, column=0)
Button(okn, text="5", command=lambda:num(5), width=3).grid(row=2, column=1)
Button(okn, text="6", command=lambda:num(6), width=3).grid(row=2, column=2)
Button(okn, text="1", command=lambda:num(1), width=3).grid(row=3, column=0)
Button(okn, text="2", command=lambda:num(2), width=3).grid(row=3, column=1)
Button(okn, text="3", command=lambda:num(3), width=3).grid(row=3, column=2)
Button(okn, text="0", command=lambda:num(0), width=8).grid(row=4, column=0, columnspan=2)
Button(okn, text=".", command=lambda:num("."), width=3).grid(row=4, column=2)

Button(okn, text="=", command=lambda:equ(), width=2).grid(row=1, column=3, columnspan=1)
Button(okn, text="+", command=lambda:num("+"), width=2).grid(row=2, column=3)
Button(okn, text="-", command=lambda:num("-"), width=2).grid(row=3, column=3)
Button(okn, text="÷", command=lambda:num("/"), width=2).grid(row=4, column=3)

Button(okn, text="C", width=2, command=clear).grid(row=0, column=4)
Button(okn, text="AC", height=6, command=clearr).grid(row=1, column=4, rowspan=4)
okn.mainloop()
