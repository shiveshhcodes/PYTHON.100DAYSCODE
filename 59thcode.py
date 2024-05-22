# class Employee:
#   company = "Apple"
#   def show(self):
#     print(f"The name is {self.name} and company is {self.company}")

#   @classmethod
#   def changeCompany(cls, newCompany):
#     cls.company = newCompany


# e1 = Employee()
# e1.name = "Harry"
# e1.show()
# e1.changeCompany("Tesla")
# e1.show()
# e1.changeCompany("google")
# e1.show()
# e1.name = "don"
# e1.show()
# print(Employee.company)

class Parents:
 parent = "Mom"
 
 def show(self):
   print(f"Kid name is {self.name} and his parent are {self.parent}")
   
 @classmethod
 def change_parent_name(cls , new_parent):
  cls.parent = new_parent
  
  
S1 = Parents()
S1.name = "shivesh"
# S1.parent = "Mom"
S1.show()

Parents.change_parent_name("dad")
S1.show()
print (Parents.parent)