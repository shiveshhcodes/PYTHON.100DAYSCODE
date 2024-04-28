l=[12,23,34,45,56,67,78,89,90,110]
d=[1212,1122]
l.append(21)
l.sort()
# l.sort(reverse=True)
print(l.count(23))
print(l.index(34))
l.insert(3,122)
l.extend(d)
print(l)