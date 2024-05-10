# lets discover and learn seek() and learn() and truncate() functions in python!! (day 27)

# LETS WRITE THE CODE HERE

# f = open('45thcode.txt' , 'w')
# f.write('this is going to be my first line of code')

#  LETS RUN SEEK HERE AND SKIP THE CODE TO AFTER 7 CHARACTERS!!!

# f = open('45thcode.txt' , 'r')
# f.seek(7)

# result = f.read()
# print(result)


# # LETS DISCOVER WHAT IS TELL() FUNCTION IN PYTHON!!

# f = open('45thcode.txt' , 'r')
# f.seek(15)

# print(f.tell()) 

# result = f.read()
# print(result)


# LETS DISCOVER WHAT IS TRUNCATE () FUNCTION IN PYTHON!!

f = open('45thcode.txt' , 'a')
f.write('be my first line of code')
f.truncate(7)
# result = f.read()
# print(result)
