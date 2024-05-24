class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print(f"Sound made by the {self.name} is bhow bhow!!")

class Dog(Animal):
    def __init__(self, name, breed):
        # super().__init__(name , species= Dog)
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
    def make_sound(self):
        print(f"{self.name} Bark! and his breed is {self.breed}")

d = Dog("Dog", "Pommerian")
d.make_sound()

a = Animal("Roger", "Dog")
a.make_sound()