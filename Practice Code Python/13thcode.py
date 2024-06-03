# i = 139
# while(i<200):
#     print(i)
#     i = i+3

# j = input("Hi, What is Your Name :- ")
# print("Hello Mr./Mrs.", j)

# i = int(input("Guess the Maximum Number of my range: "))

# while i < 38:
#     print("No,", i, "isn't my maximum range")
#     i = int(input("Try again. Guess the Maximum Number of my range: "))

# print("Done with the loop thing")

# if i >= 38:
#     print(i, "is greater than or equal to 38, that is in my range")

# i = 991
# while(i>=90):
#     print(i)
#     i = i-1

# i = 2506
# while(i<=3000):
#     print(i)
#     i=i+19.98

# while True:
#     Number=int(input("Enter a positive Number : "))
#     print(Number)
#     if not Number > 0:
#         break

# fruits = ['apple', 'banana', 'cherry'] 
# for index , fruit in enumerate(fruits , start=1):
#     print(f"rank {index} fruit is {fruit}.")
    
# colors = ['red', 'green', 'blue']
# for index, color in enumerate(colors, start=1):
#     print(f"{index}. {color}")

# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]
# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old.")


names = ['sanjay' , 'lata' , 'shakshi' , 'shivi']
age = [59 , 52 , 29 , 27]

for names,age in zip(names,age):
    print(f"{names} is {age} years old")

# nested_list = [[1, 2], [3, 4], [5, 6]]
# flattened_list = []
# for inner_list in nested_list:
#     for element in inner_list:
#         flattened_list.append(element)
# print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]

tools = ['Claude', 'Pieces', 'Mac Gestures', 'A cup of coffee', 'Bug free code', 'Bose Headphones']

tweet = "Not gonna lie, these make my life as a dev so much easier 💻🙌 #PythonDev"

for tool in tools:
    tweet += f"\n\n🔧 {tool}: Makes coding better."

print(tweet)