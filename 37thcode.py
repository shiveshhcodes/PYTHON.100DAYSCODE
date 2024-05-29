# lets discover some modules in python!!

# while True: 
#  a = int(input("enter a value to get its Square Root value: "))
#  index = 0
#  for i in range (a):
#   i -=1
#   from math import sqrt , pi
#   result = (sqrt(a)) * pi * i
#  print("the square root of" , a , "X 3.14 is - " , result)
#  break

while True:
    from math import sqrt, pi
    a = int(input("Enter a positive integer value: "))
    for i in range(a-1 , -1 , -2) :
        result = (sqrt(a)) * pi * i
        print(f"The square root of {a} multiplied by 3.14 and {i} is {result:.2f}")
    break

# while True:
#     from math import sqrt as s, pi as s1
#     a = int(input("Enter a positive integer value: "))
#     for i in range(a - 1, -1, -1):
#         result = (s(a)) * s1 * i
#         print(f"The square root of {a} multiplied by 3.14 and {i} is {result:.2f}")


# import math
# print(dir(math))

import math as m 
result = m.sqrt(6969)
print(f"{result:.2f}")
