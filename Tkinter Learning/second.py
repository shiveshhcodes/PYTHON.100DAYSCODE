from tkinter import *
window = Tk()

window.title("Shivesh First Gui") #this is use to add title of GUI application
window.iconbitmap(r"/Users/shiveshrichhariya/project images/google_logo_icon_188457.ico") #this is use to add a logo to the GUI application
window.attributes('-alpha',0.8) # this attribute is use to give transparency to the GUI application
window.config(bg="green") # 1. as it shows , it uses to give background color 
# window['bg']="yellow" # 2. as it shows , it uses to give background color 

window.geometry("300x230+78+203") # here 300x230 is used for size of window and + x + y are used for loaction from left of window.
# window.geometry("300x230-78-203") # here 300x230 is used for size of window and - x - y are used for loaction from right of window.

# window.minsize(100,100) #use to maximize
# window.maxsize(500,500) #use to minimize

window.resizable(False,False) #use to fix the size and do not allow to resize it again and again


window.mainloop()

