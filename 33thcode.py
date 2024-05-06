# here we are gonna learn how to raise error in our code
# we can generate personal error , to stop the code at point to not continue
# it for further process

a = int(input("Enter a value between 69 and 100 : - "))
if (a<69 or a>100):
    raise ValueError("Entered value is not between required number")
# here raise is used to generate an error.
else: 
    print("You entered", a , "is that true??")
    
    
# rajaji= input("enter a random value: - ")

# if rajaji.lower()==("quit"):
#     print("program is quitted")
# else:
#     print("entered value does not matches the case")
#     raise Exception ("ERROR 404")

# user_input=input("enter word quit - ")

# if user_input.lower()==("quit"):
#     print("Thank you for using our program")
# else: 
#     raise ("PLEASE MAKE SURE TO TYPE QUIT , NOTHING ELSE")

