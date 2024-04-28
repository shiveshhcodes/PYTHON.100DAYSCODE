# here we will learn about lists.

marks = [0,12,23,34,45,56,67]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])

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

lst = [i*i for i in range(10) if i%2==1]
print(lst)

lst = [i+i for i in range(5) if i%2==0]

