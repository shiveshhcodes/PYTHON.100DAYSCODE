# lets discover and learn about local and global variables in python

# this is a global variable
x = 25
print("the first global value of x is" , x)
# now , lets discover what is local variable
def local():
  global x
  x = 10
  y = 22
  print("then the local value of x is" , x)
  print("then the local value of y is" , y)

# print(f"hence ,  global value of x is {x}")
local()
# x = 21
print(f"NOW , the global value of x is now" , x)