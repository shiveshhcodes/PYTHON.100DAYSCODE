# today we are gonna learn MAP , FILTER AND REDUCE IN PYTHON!!

# MAP
# def square (a):
#     return a*a

l = [1,2,3,4,5,6,7,8,9,10]

# newl=[]
# for item in l:
#  newl.append(square(item))
# print(newl)

# newl = list(map(square , l))
# print(newl)


# FILTER

# def maximum(a):
#     return a>4

# newll = list(filter(maximum , l))
# # newll = list(filter(lambda a: a>6 , l))
# print(newll)


# REDUCE 

# from functools import reduce

# numbers = [1,2,3,4]

# multiplication = reduce(lambda x,y: x/y , numbers)
# print("{:.5f}".format(multiplication))
 
 
from functools import reduce

num = [1,2,3.4,5.6,7.8,9.65]
multiply = reduce(lambda x,y: x*y*y , num)
print("{:.3f}".format(multiply))