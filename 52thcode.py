# # today we are gonna learn and discover what decorators are in python!!

# def greet(fx):
#     def mfx(*args , **kwargs):
#      print("GM")
#      fx(*args , **kwargs)
#      print("GN")
#     return mfx
    

# @greet
# def add(a, b):
#    add = (a+b)
#    print("the sum of two numbers is" , add)
   
# @greet
# def diff(a, b):
#    diff = (a-b)
#    print("the difference of two numbers is" , diff)
   
# add(21,21)
# diff(21,21)


# def greet(fx):
#     def mfx(*args , **kwargs):
#         print("Good Morning")
#         fx(*args , **kwargs)
#         print("good Night")
        
#     return mfx

# @greet
# def add(a, b):
#    add = (a+b)
#    print("the sum of two numbers is" , add)
   
# @greet
# def diff(a, b):
#    diff = (a-b)
#    print("the difference of two numbers is" , diff)
   
# add(244,21)
# diff(221,21)



# def greet(fx):
#     def mfx(*args , **kwargs):
#         print("Hi sir/mam")
#         fx(*args , **kwargs)
#         print("thank you")

#     return mfx
# @greet
# def add(a, b):
#    add = (a+b)
#    print("the sum of two numbers is" , add)
   
# @greet
# def diff(a, b):
#    diff = (a-b)
#    print("the difference of two numbers is" , diff)
   
# add(244,21)
# diff(221,21)

def greet (fx):
    def mfx(*args , **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Good Night")
    return mfx

@greet
def add(a,b):
 addition = a+b
 print ("sum of two numbers you entered is" , addition)
 

a = int(input("Enter first value "))
b = int(input("Enter second value "))
result = add(a,b)
print(result)