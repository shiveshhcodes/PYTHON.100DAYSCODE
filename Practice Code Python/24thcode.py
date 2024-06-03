# name = input("Hi, What's Your Name? \n")
print("Hi", name , "We hope you are doing well. We have some good stuff for you.")
asking = input("Are you excited to start? Yes/No: ")

while True:
    if asking.lower() == "yes":  
        a = int(input("Enter a random value: "))
        b = int(input("Enter a random value again: "))

        def add(a, b):
            """This function adds two numbers."""
            addition = a + b
            return "The sum of the values you entered is " + str(addition)

        def sub(a, b):
            """This function subtracts the second number from the first."""
            subtraction = a - b
            return "The difference between the values is " + str(subtraction)

        def mean(a, b):
            """This function calculates the mean of two numbers."""
            mean_value = (a + b) / 2
            return "The mean of the values is " + str(mean_value)

        def square(a, b):
            """This function calculates the square of the sum of two numbers."""
            combined = a + b
            square_value = combined ** 2
            return "The square of values you entered is " + str(square_value)

        def cube(a, b):
            """This function calculates the cube of the sum of two numbers."""
            combined01 = a + b
            cube_value = combined01 ** 3
            return "The cube of values you entered is " + str(cube_value)

        print("Let's do some cool stuff.")
        aa = input("Ready? Yes/No: ")

        if aa.lower() == "yes":
            print(add(a, b))  
            print(sub(a, b))
            print(mean(a, b))
            print(square(a, b))
            print(cube(a, b))

            ask = input("\nWould you like to know the process? Yes/No: ")
            if ask.lower() == "yes":
                print("Addition operation:")
                print(add.__doc__) 
            else:
                print("Okay, thank you for using our program.")
                
        break
                
    elif asking.lower() == "no": 
        print("Thank you for using our program")
        break

    else:
        print("Invalid input", name, "Please enter yes or no")
        asking = input("Are you excited to start? Yes/No: ")
# # # # Hi , today we are gonna learn doc strings in python!! 
# # # # using this string is fun , so let's try this again!!
# # # just like we used f string in ouur previous code

# # name = input("Hi , What's Your Name?? ")
# # print ("Hi" , name , "We hope you doing well good, well i have some good stuff for you")
# # asking = input("Are you excited to start?? Yes/No: ")
# # if asking.lower ==("Yes"):
# #  a = int(input("enter a random value: "))
# #  b = int(input("enter a random value again: "))

# #  
    
# #  def sub(a,b):
# #     Subtraction = (a-b)
# #     print("The sum of the values you entered is " , Subtraction) 

# #  def mean(a,b):
# #     Gmean = (a*b/2)
# #     print("The sum of the values you entered is " , Gmean)
    
# #  def square(a,b):
# #     Square= (a,b**2)
# #     print("The sum of the values you entered is " , Square)
    
# #  def cube(a,b):
# #     Cube= (a,b**3)
# #     print("The sum of the values you entered is " , Cube)

# #     '''
# #  1. the first step is to get the values of a and b.
   
# #  2. after getting values of a and b , we will use the addition command in our
# #    code and then printing the output

# #  3. we can do more things , like subtraction , multiplication , division , Gmean 
# #    or many more
# #  '''

# #  print("Let's do this some cool stuff")
# #  aa = input("Ready??")
# #  if aa.lower == "(yes)":
# #   print = "addition of two numbers is " , add(a,b)
# #   print = "subtraction of two numbers is " , sub(a,b)
# #   print = "mean of two numbers is " , mean(a,b)
# #   print = "square of two numbers is " , square(a,b)
# #   print = "cube of two numbers is " , cube(a,b)

# #   ask = input("\nShould you want to know the process?? , Yes/No: ")
# #   if ask.lower() == "yes" :
# #     print(add.__doc__)
# #   else :
# #     print("Okay , we have no problem, thank you for using our program")
# # else : 
# #     print("Okay" , name , "See you later , sayonaraaaaaaaaaaaaa")





# name = input("Hi, What's Your Name? \n")
# print("Hi", name , "We hope you are doing well. We have some good stuff for you.")
# asking = input("Are you excited to start? Yes/No: ")

# while True:
#     if asking.lower() == "yes":  
#         a = int(input("Enter a random value: "))
#         b = int(input("Enter a random value again: "))

#         def add(a, b):
#             addition = a + b
#             return "The sum of the values you entered is " + str(addition)

#         def sub(a, b):
#             subtraction = a - b
#             return "The difference between the values is " + str(subtraction)

#         def mean(a, b):
#             mean_value = (a * b) / 2
#             return "The mean of the values is " + str(mean_value)

#         def square(a, b):
#             combined = a+b
#             square_value=combined **2
#             return "The square of values you entered is " + str(square_value)

#         def cube(a, b):
#             combined01 = a+b
#             cube_value = combined01 **3
#             return "The cube of values you entered is " + str(cube_value)

#         print("Let's do some cool stuff.")
#         aa = input("Ready? Yes/No: ")

#         if aa.lower() == "yes":
#             print(add(a, b))  
#             print(sub(a, b))
#             print(mean(a, b))
#             print(square(a, b))
#             print(cube(a, b))

#             ask = input("\nWould you like to know the process? Yes/No: ")
#             if ask.lower() == "yes":
#                 print("Addition operation:")
#                 print(add.__doc__) 
#             else:
#                 print("Okay, thank you for using our program.")
                
#     break
                
#     elif asking.lower() == "no": 
#      print("Thank you for using our program")

#     else:
#      print("Invalid input", name, "Please enter yes or no")

