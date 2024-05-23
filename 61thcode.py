class person:
  def __init__(self , naam , age):
    self.naam = naam
    self.age = int(age)
    
  def show(self):
    print(f"Hi My naam is {self.naam} age is {self.age}")
  
shivesh = person("shivesh" , 21)
shivesh.show()

print(shivesh.__dict__)
print(help(person))
    