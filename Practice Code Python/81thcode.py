# intermediate level of tuple 

# mytuple = (21.23 , "shivesh")
# print(type(mytuple))

# item = mytuple[1]
# print(item)

# for i in mytuple:
#  print(mytuple)
 
 
# letter = ("a" , "b" , "c" ,"d" , "e")
# print(len(letter))
# print(letter.count('b'))
# print(letter.index('d'))

# print(list(letter))
# print(tuple(letter))

import sys
numbers = (1,2,3,4,5,6,7,8,9)
letters = ("shivesh" , "don" , "is" , "going" , "to" , "be" , "successful")

print(sys.getsizeof(numbers) , "bytes")
print(sys.getsizeof(letters) , "bytes")