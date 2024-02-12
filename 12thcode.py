# today we are going to use Loops , 
# loops are of two types , for loops and while loops

name = 'SITA'
for s in name:
 print(s)

name = 'RAM'
for i in name:
    print(i)

name = 'HANUMAN'
for i in name:
    print(i , end=",")

colors = ["BLACK" , "GREEN" , "BLUE" , "ORANGE" , "VIOLET"]
for S in colors:
    print(S)
    for i in S:
      print(i)

colors = ["RED", "GREEN", "BLUE", "ORANGE"]
for color in colors:
    print(color)
    for character in color:
        print(character)

for x in range(0,120):
    print(x+1)

x = int(input("Enter a random value: "))
print("You entered", x)

y = int(input("Again enter the random value: "))
print("You entered", y)

print("Now the range between", x , "and" , y , "will be printed")

z = input("Do You want me to show the range between these : (Yes/No Idea/No) ")

if z.lower() == "yes":
    print("\n\nHere is the result")
    for s in range(x, y+1):
        print(s) 
    print("\nhope you will have good day")
elif z.lower() == "No Idea":
      print("\n\nHere is the result ----- ")
      print("give a shot , here is the result :")
      for s in range(x,y+1):
        print(s)
else:
    print("\nTHANK YOU", "\nBOSS :)")

