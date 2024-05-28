# here we are gonna learn and use code of set methods!! 
# so lets do thisssssss

a = {"a" , "b", "c" , "d" , "e" , "f" , "g" , "h" , "i", "j"}
b = {"e" , "f" , "g" , "h" , "i", "j" , "y"}

c = a.union(b)
d = b.intersection(a)
e = b.intersection_update(a)
f = a.symmetric_difference(b)
g = a.difference(b)
h = a.isdisjoint(b)
i = a.issuperset(b)
j = b.issubset(a)
k = a.add("p")
a.update(b)
# l = a.remove("d")
l = a.pop()
print (c)
print (d)
print (e)
print (f)
print(g)
print(h)
print(i)
print(j)
# print(a)
print(a)
print(l)

data = input ("lets check the alpha in set : ")
if data in a:
    print ("it is present in set")
else:
    print("no it is not present")