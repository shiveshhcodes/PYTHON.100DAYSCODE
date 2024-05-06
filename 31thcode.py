# today we are gonna learn , exception handling.

# lets begin
    # table = int(a) * i 
    # print(f"The Multiplication table of {int(a)} X {i} is" , table)
# try:  
#  a = int(input("Enter a value to get Table of it - "))
#  print(f"The Multiplication Table of {a} is :")
 
#  for i in range (1,11):
#    result = int(a) * i
#    print(f"{int(a)} X {i} = " , result)
# except ValueError:
#     print("please enter a number , not alphabets")
# print("Thanks")

try:
  c = int(input("enter a integer value: " ))
  d = [1,2,5,4,3,22,232,333,2322,4444]
  print("the index value stored at", c , "position is" ,d[c])
except ValueError:
    print("value entered is not a integer number ")
except IndexError:
    print("Index Error")