a = input("Tell Me Your Name?? : ")
print("\nHi", a, "I hope you are doing fantastic")
b = input("\nDo You agree to all our T&C's? (yes/no) : ")

if b.lower() == "yes":
    print("Let's do it then")

    s = int(input("\nWhat's your Age??" + a + ":"))
    print("Your Age is :", s )

    if s > 18:
        print("You can go to college now , You are adult ")
        ss = input("\nAre you happy now?? (Yes/No): ")
        if ss.lower() == "yes":
            print("Good Boy")
        else:
            print("\nBad Habit")
            print("GO AND STUDY, YOU STUPID")

    elif s == 17:  
        print("I guess you just passed your 12th, you can go to\nApply for college next year buddy.")

    else:
        print("You cannot go to college now")

else:
    print("Thank you for checking my program.\nHave a Good Day", a, ":)")

print("Thank you for checking my program.\nHave a Good Day", a, ":)")
