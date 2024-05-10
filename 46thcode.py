# today we are gonna learn of lemda function in python!!

def apply (fx , value):
    return 2112 + fx(value)
def cube (value):
    return value*value*value

# result = apply(lambda x : x*x*x , 5)

# print(result)
# import math as m
# square  = lambda x: x*x
# cube  = lambda x: x*x*x
# square_root  = lambda x: m.sqrt(x)
# cube_root  = lambda x: m.cbrt(x)

# x = 8128
# print(square(x))
# print(cube(x))
# print(f"(square_root{x:.2f}")
# print(f"{cube_root(x):.2f}")

# boss = lambda x ,y : x + x*x + y + y*y - x*y
# def boss(x,y):
#     return x + x*x + y + y*y - x*y
# print(boss(10,15))

result = apply (cube , 11)
print(result)
