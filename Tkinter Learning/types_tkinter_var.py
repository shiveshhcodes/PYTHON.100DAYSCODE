from tkinter import *
win=Tk()

var = StringVar(win,value="python",name="2")
var = IntVar(win,value="12.33")
# var.set()

print(var.get())


win.mainloop()