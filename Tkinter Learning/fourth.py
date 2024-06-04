from tkinter import *
window = Tk()

window.title("Shivesh First Gui") #this is use to add title of GUI application
window.iconbitmap(r"/Users/shiveshrichhariya/project images/google_logo_icon_188457.ico") #this is use to add a logo to the GUI application
window.attributes('-alpha',0.8) # this attribute is use to give transparency to the GUI application
window.config(bg="white") # 1. as it shows , it uses to give background color 
# window['bg']="yellow" # 2. as it shows , it uses to give background color 

window.geometry("440x330+78+203") # here 300x230 is used for size of window and + x + y are used for loaction from left of window.
# window.geometry("300x230-78-203") # here 300x230 is used for size of window and - x - y are used for loaction from right of window.
 
window.minsize(100,100) #use to maximize
window.maxsize(500,500) #use to minimize

# window.resizable(False,False) #use to fix the size and do not allow to resize it again and again

lab = Label(window, text="shiveshcodes", font=("Robotic" , 20 , "bold"), bg="green")
# lab.pack()
# lab.grid(row=25 , column=26 , padx=25 , pady=34)
lab.grid(row=25 , column=26 , padx=25 , pady=34)
# lab.pack(padx=10 , pady=10) #padding of text
# lab.pack(ipadx=3 , ipady=2 , side="left") #padding of internal box of text

# lab1 = Label(window, text="Github", font=("Robotic" , 20 , "bold"), bg="green")

# lab1.pack(padx=10 , pady=10) #padding of text
# lab1.pack(ipadx=2 , ipady=2 ,side="left") #padding of internal box of text

window.mainloop()

