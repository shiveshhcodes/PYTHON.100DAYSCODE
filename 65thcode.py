# class Vector:
#   def __init__(self, i, j, k):
#     self.i = i
#     self.j = j
#     self.k = k

#   def __str__(self):
#     return f"{self.i}i + {self.j}j + {self.k}k"

#   def __add__(self, x):
#     return Vector(self.i + x.i,  self.j+x.j, self.k+x.k) 
# v1 = Vector(2, 5, 6)
# print(v1)

# v2 = Vector(1, 2, 9)
# print(v2)

# print(v1 + v2)
# print(type(v1 + v2))


class Vector:
  def __init__(self , i , j , k):
    self.i = i
    self.j = j
    self.k = k
    
  def addition(self):
    # return f"{self.i}i + {self.j}j + {self.k}k"
    print(f"{self.i}i + {self.j}j + {self.k}k")
    
  def __add__(self , x):
    return Vector(self.i + x.i , self.j + x.j , self.k + x.k)
  
    # def __add__(self, x):
    # return Vector(self.i + x.i,  self.j+x.j, self.k+x.k)
    

v1 = Vector(2,7,1)
v1.addition()
v2 = Vector(21,21,1)
v2.addition()

print(v1 + v2)
# print(v1+v2)  
  