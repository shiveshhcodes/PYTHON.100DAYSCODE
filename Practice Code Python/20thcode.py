# today we will learn on classes on tuple
# letsssss do this.

# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")       #add item 
# temp.pop(3)                 #remove item
# temp[0] = "Finland"         #change item
# countries = tuple(temp)
# print(countries)

Studentsname = ("shivesh" , "raj" , "akshay" , "kapil" , "prince")
temp = list(Studentsname)
temp.append("akhit , rahgir")
temp.pop(3)
temp[4] = "ashwin"
Studentsname = tuple(temp)
print(Studentsname.index("raj"))
print(Studentsname)

# from typing import Tuple

# def get_person_info() -> Tuple[str, int, float]:
#     name = "John Doe"
#     age = 30
#     height = 1.75
#     return name, age, height

# person_info = get_person_info()

# from typing import Tuple

# def get_person_info():
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     height = float(input("Enter your height in meters: "))
#     return name, age, height

# person_info = get_person_info()
# print(person_info)  # Output will depend on user input

# name, age, height = person_info
# print(f"Name: {name}, Age: {age}, Height: {height}")
