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

while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        if age >= 0:
            print(f"Your age is {age}.")
            break
        else:
            print("Age cannot be negative.")
    else:
        print("Invalid input. Please enter a number.")