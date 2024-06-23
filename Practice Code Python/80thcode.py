# Intermediate level of lists.

mylist = [21 , "shivesh" , "don" , 45]
mylist.append("shibu")
mylist.insert(0, 212)
mylist.pop(2)
mylist.remove(21)
# mylist.clear()
mylist.reverse()
print(mylist)

newlist = [4] * 12
print(newlist)

combined_list = newlist + mylist
print(combined_list)


latestlist = [1,2,3,4,5,6,7,8,9]
a = latestlist[2:6]
print(a)


# b = [i*i for i in latestlist]
b = latestlist[::3]
print(b)