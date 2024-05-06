# # lets discover dictionaries in python todayyyyyyy

# info = {'name':'shivesh' , 'age':'21' , 'location':'chhatarpur'}
# print(info)
# # print(info['namee'])
# print(info.get('namee'))
# print(info.values())
# print(info.keys())
# print(info.items())

# for key, value in info.items():
#  print(f"the value of key {key} is {value}")


employeesinfo = {
    25: "Shivesh",
    12: "Shivangi" ,
    7: "Shakshi" , 
    1: "Lata" ,
    10: "Sanjay"
}

print(employeesinfo)
print(employeesinfo.keys())
print(employeesinfo.values())

for key , value in employeesinfo.items():
    print(f"The Employee ID is {key} and name is {value}")
    
print("\nTHANK YOU EVERYONE")