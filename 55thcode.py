# class Student:
#     def __init__(self):
#         self._name = "Shiveshhh"

#     def _funName(self):      # protected method
#         return "shiveshhcodes"

# class Subject(Student):       #inherited class
#     pass

# obj = Student()
# obj1 = Subject()
# print(dir(obj))

# # calling by object of Student class
# print(obj._name)      
# print(obj._funName())     
# # calling by object of Subject class
# print(obj1._name)    
# print(obj1._funName())

# class objects:
#     def __init__(self , objectname):
#         self.__object = objectname
    
#     def show(self):
#      print(f"the cartoon has {self.object} in it" )
    

# box = box._object("box")
# box.show()

class objects:
    def __init__(self , name):
        self.__name = name
     
    def result(self):
      print(f"the output of box is gonna be {self.__name}")
      return 
  
class scales(objects):
    def result2(self):
      print(f"gellp {self._objects__name}")
  
  
card = objects("card")
card.result()
pen = scales("pen")
pen.result2()
  