# today we are gonna learn on inheritance in python

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id 

  def showDetails(self):
    print(f"The name of Employer: {self.id} is {self.name}")

class Programmer(Employee):
  def showLanguage(self):
    print("The default langauge is Python")


e1 = Employee("SanAI", 2000)
e1.showDetails()
e2 = Programmer("Shivesh", 4100)
e2.showDetails()
e2.showLanguage()

class Employee:
  def __init__(self , name , ID , gender):
    self.name = name
    self.ID = ID
    self.gender = gender
    
  def info(self):
    print(f"{self.name} is a employee of our company , there ID is {self.ID} and there gender is {self.gender}")

# # class HR(Employee):
# #   def details(self):
# #     print("Hi , i am HR of your company")

# # shivesh = HR("Shivesh" , "21" , "Male")
# # SanAI = Employee("SanAI" , "19" , "Female")
# # shivesh.details()
# # SanAI.info()


# class Brosis:
#   def __init__(self , role , name , age):
#     self.name = name
#     self.age = age
#     self.role = role
    
#   def ShowDetails(self):
#      print(f"{self.name} is {self.role} and there age is {self.age}")
     
# class Family(Brosis):
#   def details(self):
#     print(f"{self.name} age is {self.age}")
     
# shivesh = Family("brother" , "shivesh" , "21")
# Shakshi = Brosis("sister" , "shakshi" , "29")

# Shakshi.ShowDetails()
# shivesh.details()

#  INHERITENCE

class voters:
  def __init__(self , name , age):
    self.name = name
    self.age = age
    
  def details(self):
    """
    Prints the details of a person.
    
    This method prints the name, VoterID, and age of a person.
    """

    print(f"{self.name} has VoterID and his age is {self.age}")
    
class moree(voters):
  def detail(self):
   print("happy happy happyyyy")
   
    
    
  # def moredetails(self):
  #   print(f"INDIA IS A SECURAL COUNTRY {self.name} you got {self.age} recently")
    
shivesh = voters("shivesh" , "21")
shakshi = voters("shakshi" , "29")
shakshi = moree("shakshi" , "29")

shivesh.details()
shakshi.details()
shakshi.detail()
print(voters.details.__doc__)