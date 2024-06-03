from tkinter import *
window = Tk()

window.title("Shivesh First Gui") #this is use to add title of GUI application
window.iconbitmap(r"/Users/shiveshrichhariya/project images/google_logo_icon_188457.ico") #this is use to add a logo to the GUI application
window.attributes('-alpha',0.8) # this attribute is use to give transparency to the GUI application
window.config(bg="green") # 1. as it shows , it uses to give background color 
# window['bg']="yellow" # 2. as it shows , it uses to give background color 

window.mainloop()