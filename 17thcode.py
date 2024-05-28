# here we will learn about lists.

marks = [0,12,23,34,45,56,67,78,89,121,156]
marks.append(2121)
marks.remove(0)
marks.insert(0 , 9)
marks.sort()
marks.reverse()
# marks.len(marks)
print(marks)
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])

# print(marks[-3])
# print(marks[len(marks)-3])
# print(marks[7-3])
# print(marks[4])

# a = int(input("ENTER ANY NUMBER YOU THINK IT WILL BE IN MARKS LISTS "))
# if a in marks:
#  print("yes , it is in the list")
# else:
#  print("no")

# print (marks[1:-1])
# print (marks[1:4:2])

marks = [i*i for i in marks if i%5==0]
print(marks)

# lst = [i+i for i in range(5) if i%2==0]


