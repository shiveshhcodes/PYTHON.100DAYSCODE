# class Employee:
#   companyName = "Apple"
#   noOfEmployees = 0
#   def __init__(self, name):
#     self.name = name
#     self.raise_amount = 0.02
#     Employee.noOfEmployees +=1
#   def showDetails(self):
#     print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# # Employee.showDetails(emp1)
# emp1 = Employee("Shivesh")
# emp1.raise_amount = 0.3
# emp1.companyName = "Lenovo India" 
# emp1.showDetails()
# Employee.companyName = "Google"
# print(Employee.companyName)

# emp2 = Employee("Shetty")
# emp2.companyName = "Microsoft"
# emp2.showDetails()


class CSEIML_students:
  college = "IPS ACADEMY"
  def __init__(self , name , Class):
    self.Class = Class
    self.name = name
    # self.roll_number = roll_number
  
  def result(self):
   print(f"{self.name} is a student of {self.college} and his Class is {self.Class}")
   
  
class student_info(CSEIML_students):
  def infooo(self , roll):
    self.rollnumber = roll
    print(f"The Rollnumber of {self.name} is {self.rollnumber}")
   
name1 = CSEIML_students("raj" , "CSEIML")
name2 = CSEIML_students("shivesh" , "CSEIML")
name3 = student_info("shivesh" , "cseiml")

name1.result()
name2.result()
name3.infooo(233)
# name3.result()

  