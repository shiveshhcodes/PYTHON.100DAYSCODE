# # CODE WITH HARRY EXCERSISE!!!!!!

user_input=input("enter a value between 20 and 100: - ")

if user_input.lower()==("quit"):
    print("Thank you for using our program")
else: 
    try:
        a = int(user_input)
        if a<20 or a>100:
         raise ValueError ("Entered value is not in range")
        else:
            print("You entered" , a , "is that true?")
    except ValueError as ve:
        print("Error" , ve)
    finally:
     ("Thank you for using our programmmmmmmme!!!!")
        
# today we are gonna learn some short hand if-else statements!!!!

