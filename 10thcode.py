a = input("What is Your Name?? : ")
print("\nHi", a, "I hope you are doing good")
b = input("\nShall we start our program?? (yes/no) : ")

if b.lower() == "yes":
    print("Let's Rock then")

    s = int(input("\nEnter Your Age " + a + ":"))
    print(" What is Your Age :", s)

    if s > 19:
        print("You can go to college now")
        ss = input("\nAre you happy now?? (Yes/No): ")
        if ss.lower() == "yes":
            print("Good Boy")
        else:
            print("\nBad Habit")
            print("GO AND STUDY, YOU STUPID")

    elif s == 18:  
        print("I guess you just passed your 12th, you can go to\nCollege from next year.")

    else:
        print("You cannot go to college now")

else:
    print("Thank you for checking my program.\nHave a Good Day", a, ":)")

print("Thank you for checking my program.\nHave a Good Day", a, ":)")
