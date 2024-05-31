# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = False
# print(happy)

# print(happy := True)

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#       break
#   foods.append(food)
# foods = list()
# while (food := input("What food do you like?: ")) != "quit":
#     foods.append(food)

# numbers = [5,4,3,2,1]
# while (num := numbers > 0):
#     numbers.pop(num)




      
num = []
while (food := input("Enter any Number: ").lower()) != "quit":
    while not food.strip().isdigit():  # Check if the input is not a valid number
        print("Please enter a number.")
        food = input("Enter any Number: ").lower()
    num.append(food)
print(num)
