# today we are gonna learn how to use
# else in while loop , before we knew that it is only used in for loop but
# today we are gonna learn , how to do it for while loop

# i = 0
# while i<139:
#  print(i)
#  i = i + (4) 
#  if i==128:
#   break
 
# else:
#     print("this loop is ended here")
    
# for i in range(1 ,91):
#     result = i * 9
#     print(f"9 X {i} = {result}")

# else:
#     print("none")

while True:
    try:
        value_taken=int(input("ENTER A RANDOM VALUE : "))
        n22 = int(input("till what value you want results?? "))
        print("\n okay!! there we go")
        print("\n ouput 👇🏻")

        for i in range(1 , n22+1):  
            boss = value_taken * i
            print(value_taken , "X", i , "is equals to", boss) 
            
        print("Loop completed without interruption")
        break
    except ValueError:
        print("Oops!! this is not an Integer!!")



    

# i = 1
# while i<5:
#     print(i)
#     i = i+i
# else:
#     print("the loop is broken")
    
# for i in range(15):
#  if i == 0:
#     s = i * (i)
#     print("the new values of" , i  , "using", '''i X (i+1)''' , "is" , s )
#  else:
#     s = i * (i+1)
#     print("the new values of" , i + 1 , "using", '''i X (i+1)''' , "is" , s )
    
 
# for i in range(15): 
#    s = i * (i + 1)  
#    print("The value for", i , "using i * (i + 1)  is", s) 
# else : 
#     print("thank you")

# while True:
#     try:
#         value_taken = int(input("Enter a random value: "))

#         n22 = int(input("Till what value do you want results?: "))

#         break
#     except ValueError:

#         print("Invalid input! Please enter an integer value.")


# for i in range(1, n22 + 1):
#     result = value_taken * i
#     print(value_taken, "X", i, "is equal to", result)
    
# print("Loop completed without interruption")
