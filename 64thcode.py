# class Shape:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y
    
#   def area(self):
#       return self.x * self.y

# class Circle(Shape):
#     def __init__(self, radius):
#       # self.radius = radius
#       super().__init__(radius, radius)

#     def area(self):
#         return 3.14 *  super().area()
      
# # rec = Shape(3, 5)
# # print(rec.area())

# c = Circle(5)
# print(c.area())


class rec:
 def __init__(self , length , width):
   self.length = length
   self.width = width
   
 def area(self):
  return self.length * self.width
  
class circle(rec):
  def __init__(self, r):
    super().__init__(r , r)
    
  def area(self):
    return 3.14 * super().area()
  
  
c = circle(19.2)
print(c.area())
r = rec(10 ,12 )
print(r.area())