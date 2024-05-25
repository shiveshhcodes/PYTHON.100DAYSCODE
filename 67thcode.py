# class Employee:
#   def __init__(self, name):
#     self.name = name
#   def show(self):
#     print(f"The name is {self.name}")

# class Dancer:
#   def __init__(self, dance):
#     self.dance = dance

#   def show(self):
#     print(f"The dance is {self.dance}")

# class DancerEmployee(Employee, Dancer):
#   def __init__(self, dance, name):
#     self.dance = dance
#     self.name = name

# o  = DancerEmployee("Kathak", "Mahak")
# print(o.name)
# print(o.dance)
# o.show() 
# print(DancerEmployee.mro())

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound madeeee by the animal")
        
class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
        
class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dogggg")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed
    def make_sound(self):
        print("Barkkkk!")
        
    def __str__(self):
      return f"{self.name} is a dog breed of {self.breed} and his fur colors is {self.species}"
        
bulldog = Dog("Pullu" , "Bulldog" , "brown")
print(bulldog)
bulldog.make_sound()



