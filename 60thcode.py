# # class Employee:
# #   def __init__(self, name, salary):
# #     self.name = name 
# #     self.salary = salary
    
# #   @classmethod
# #   def fromStr(cls, string):
# #     name , salary = string.split('-')
# #     return cls(name , int(salary))
# #     # return cls(string.split("-")[0], int(string.split("-")[1]))
    
# # e1 = Employee("Harry", 12000)
# # print(e1.name)
# # print(e1.salary)

# # string = "John-12000"
# # e2 = Employee.fromStr(string)
# # print(e2.name)
# # print(e2.salary)

# # # class Person:
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.age = age

# # #     @classmethod
# # #     def from_string(cls, string):
# # #         name, age = string.split(',')
# # #         return cls(name, int(age))

# # # person = Person.from_string("John Doe, 30")
# # # print(person.name, person.age)

# class family:
#   def __init__(self , name , number):
#     self.name = name
#     self.number = number
    
#   @classmethod
#   def frmstrng (cls , string):
#     # return cls(string.split("-")[0] , int(string.split("-")[1]))
#     name , number = string.split('-')
#     return cls(name , int(number))
    
    
# father = family("sam" , 30)
# print(father.name , father.number)

# class employees:
#   def __init__(self , name , age):
#     self.age = age
#     self.name = name
    
#   @classmethod
#   def from_string(cls , string):
#     name , age = string.split(',')
#     return cls(name , int(age))
  
  
# e1 = employees("e1" , 21)
# print(e1.name , e1.age)

class employees:
  company = "apple"
  def __init__(self , name , age):
    self.name = name
    self.age = age
    
  def show(self):
    print(f"{self.name} is a employee of {self.company} and there age is {self.age}")
    
  # @classmethod
  # def frmstrng (cls , string):
  #   name , age = string.split('-')
  #   return cls(name , int(age))
  
  @classmethod
  def frmstrng (cls , string):
    name , age = string.split('-')
    # return cls(string.split('-')[0] , string.split('-'[1])) 
    return cls (name , int(age))
  
  @classmethod
  def new_company(cls , NC):
   cls.company = NC
   
e1 = employees("sanjay" , 21)
e1.show()
e1 = employees("sanjay" , 21)
employees.new_company("Tesla")
e1.show()
print(employees.company)

    
  
    
  