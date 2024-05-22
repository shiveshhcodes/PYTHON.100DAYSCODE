class person:
  def __init__(self , name , age):
    self.name = name
    self.age = int(age)
    
  def show(self):
    print(f"Hi My name is {self.name} age is {self.age}")
  
shivesh = person("shivesh" , 21)
shivesh.show()

print(shivesh.__dict__)
print(help(person))
    