# LABEL IN TKINTER

from tkinter import *
# ent = input("enter your word = ")
# ent1 = input("enter your number = ")
win = Tk()
win.config(bg="blue")
# var=StringVar()
# var1=IntVar()
lb=Label(win , 
        text="python",
        font=("robotic" , 30 , "bold" ),
        bg="red",
        # textvariable=var, 
        # intvariable=var1, 
        cursor="plus",
        relief="sunken",
        #  justify=LEFT
        underline=2,
        )

lb.place(x=40,y=40)
# var.set(f"{ent}")
# var1.set(ent1)
win.mainloop()