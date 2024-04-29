# today we will learn on classes on tuple
# letsssss do this.

# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")       #add item 
# temp.pop(3)                 #remove item
# temp[2] = "Finland"         #change item
# countries = tuple(temp)
# print(countries)

Studentsname = ("shivesh" , "raj" , "akshay" , "kapil" , "prince")
temp = list(Studentsname)
temp.append("ankita")
temp.pop(3)
temp[4] = "ashwin"
Studentsname = tuple(temp)
print(Studentsname)
print(Studentsname.index("raj"))
