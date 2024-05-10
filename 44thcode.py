f = open('44.1thcode.txt' , 'r')
# lines = ['11th line of code\n' , '22nd line of code\n' , '33rd line of code\n']
# lines = ['11th line of code\n' , '22nd line of code\n' , '33rd line of code\n']
# f.writelines(lines)

while True:
    helloo = f.readline()
    if not helloo:
        break
    print(helloo)
    

# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)


# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.write('1st line of code')
# f.write('\n2nd line of code')

# result = f.read()
# print(result)
# f.close()