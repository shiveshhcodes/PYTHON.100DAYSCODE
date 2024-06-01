# practiceing walrus operator - 

foods = []
while (food := input("Enter a Number Only: ").lower()) !="quit":
    while True:
       if not food.strip():
           print("please do not leave space")
           break
       elif not food.strip().isdigit():
            print("please enter a number")
            break
       foods.append(food)
       break
print(f"so here is the list of numbers you entered = {foods} ")