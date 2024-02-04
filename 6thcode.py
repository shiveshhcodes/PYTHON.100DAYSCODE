a = input("what is your name Sir/Mam: ")
print("Ok, your name is", a, "hahaha , i caught you")
print("\nSachbol yahi hai na tera naam")

b = input("Yes/No : ")
if b.lower() == "no" :
 print("Thank you for letting us know,", a, "We deeply regret for this mistake")
else :
 print("\nNow let's gather more information about you")

 c = input("Tell me what is your date of birth: ")
 print("Your date of birth is", c)
 d = input("Type any number between 01-10: ")
 print("The multiplication (x) of the number you thought and your date of birth is", int(d) * int(c))
 print("I hope you liked my this day 06 of the program. Have a good day", a, "And Happy Birthday \nIf it's", c, "today")
