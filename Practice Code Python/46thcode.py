# today we are gonna learn of lemda function in python!!

# def apply (fx , value):
#     return 10 + fx(value)
# def cube (value):
#     return value*value*value

# result = apply(lambda x : x*x*x , 1)

# print(result)
# import math as m


# square  = lambda x: x*x 
# cube  = lambda x : x*x*x
# square_root  = lambda x: m.sqrt(x)
# cube_root  = lambda x: m.cbrt(x)

# print(square(14))
# print(cube(9))
# print(square_root(576))
# print(cube_root(125))

# x = 8128
# print(square(x))
# print(cube(x))
# print(f"(square_root{x:.2f}")
# print(f"{cube_root(x):.2f}")

# boss = lambda x ,y : x + x*x + y + y*y - x*y
"""
    Calculate the result of the expression x + x*x + y + y*y - x*y.

    Args:
        x (int or float): The first input value.
        y (int or float): The second input value.

    Returns:
        int or float: The result of the expression.
"""
def boss_sum(x,y):
    return x + x*x + y + y*y
# print(boss_sum(10,15))

result = boss_sum(5,10)
print(result)
