# for i in range(16):
#   if(i == 10):
#     print("Skip the iteration")
#     continue
#   print("5 X", i, "=", 5 * i)
  
# i = 0
# while True:
#   print(i)
#   i = i + 1
#   if(i%100 == 0):
#     break

# for d in range(10):
#     print(d)

# print("THIS LOOP IS ENDED HERE")

# i=22
# while True:
#     print(i)
#     i = i + 3
#     if(i % 100 == 15):
#         break

# while True:
#     age = input("Enter your age: ")
#     if age.isdigit():
#         age = int(age)
#         if age >= 0:
#             print(f"Your age is {age}.")
#             break
#         else:
#             print("Age cannot be negative.")
#     else:
#         print("Invalid input. Please enter a number.")

# import time

# countdown = 100
# while countdown > 0:
#     print(f"{countdown}")
#     countdown -= 2
#     time.sleep(0.1)  # Delay of 1 second
# print("Time's up!")


# for i in range(1 , 21):
#     print(f" 19 times {i} is { 19 * i}")

import time

countdown = 1000000000
while countdown > 0:
    print(f"Remaining time is : {countdown} seconds")
    countdown -= 10000
    time.sleep(0.0000001)
    # time.strptime("%H:%M:%S")
    
print("time's UP")