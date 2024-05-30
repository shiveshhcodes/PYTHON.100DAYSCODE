# Today we are gonna learn on classes and objects on OOPs of python programming language!!

class Cars:
    Owner = "Raja Jijaji"
    Name = "BMW"
    Engine = "V8"
    Colour = "Black"
    Type = "SUV"
    Model_name = "X7"
    Year = 2021
    
    def carinfo(self):
        print(f"{self.Owner} wants {self.Name} in {self.Year} and {self.Engine} Engine in his car")
    
shivesh = Cars()
# ayush = Cars()
# tejas = Cars()

shivesh.Owner = "Shivesh"
shivesh.Name = "Merceds G63"
shivesh.Engine = "V12"
shivesh.Year = 2025

shivesh.carinfo()
# ayush.Owner = "Ayush"
# ayush.Name = "Audi"
# ayush.Engine = "V12"
# ayush.Year = 2027

# tejas.Owner = "Tejas"
# tejas.Name = "Aston Martin"
# tejas.Engine = "V8"
# tejas.Year = 2030


# ayush.carinfo()
# tejas.carinfo()

# class human:
#     name = "Shivesh"
#     age = 21
#     gender = "Male"
#     height = 5.8
#     weight = 70
    
#     def info(self):
#      print(f"Hi Everyone!! My name is {self.name} , my age is {self.age} and my gender is {self.gender}")

# Sanjay = human()
# Lata = human()
# Shakshi = human()

# Sanjay.name = "Sanjay"
# Sanjay.age = "56"
# Sanjay.gender = "Male"

# Lata.name = "Lata"
# Lata.age = "50"
# Lata.gender = "Female"

# Shakshi.name = "Shakshi"
# Shakshi.age = "36"
# Shakshi.gender = "Female"

# Sanjay.info()
# Lata.info()
# Shakshi.info()


class Capitals:
    Name = "Mumbai"
    State = "Maharastra"
    Country = "India"
    
    def info(self):
      print(f"{self.Name} is located in {self.State} in {self.Country}")
      
delhi = Capitals()
Noida = Capitals()

delhi.Name = "delhi"
delhi.State = "delhi"

Noida.Name = "noida"
Noida.State = "UP"
Noida.Country = "Sri Lanka"

delhi.info()
Noida.info()