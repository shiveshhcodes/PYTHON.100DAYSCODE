from tkinter import *
win=Tk()

# var = StringVar(win,value="python",name="2") #variables in string value.
# var = IntVar(win,value="12.33") #variables in integer value.
# var = BooleanVar(win,value=True) #it is specifically designed to hold boolean values (True or False)
var = DoubleVar(win,value=12.34) #it is specifically used to give float values , with integer vakue as well

print(var.get())


win.mainloop()