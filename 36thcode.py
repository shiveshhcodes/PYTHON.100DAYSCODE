# names = {"shivesh" , "nimki" , "isha" , "lakshya" , "shukla" , "prince"}

# while len(names)>1:
#  remove = names.pop()
#  print("removed item = " , remove , "\nremaining item = " , names )
 

# Function to get the last remaining name in a set
# def get_last_remaining_name(names_set):
#     while len(names_set) > 1:  # Loop until one item is left
#         removed_item = names_set.pop()  # Randomly remove an item
#         print("Removed item =", removed_item, "\nRemaining items =", names_set)  # Show removed and remaining items

#     return names_set.pop()  # Return the final remaining item

# # Create a set from user input
# user_input = input("Enter comma-separated names to create a set: ")
# # Split the input into a list, then create a set
# names = set(user_input.split(','))  # Create a set from the input string

# # Get the last remaining name
# last_name = get_last_remaining_name(names)

# # Display the final remaining item
# print("The final remaining item is:", last_name)


# today we are gonna learn Enumerate function.
marks = [1,12,13,122,344,55,66]

# index = 0
# for mark in marks:
#   print(mark)
#   if (index == 2):
#    print("HE IS THE TOPPER")
#   index +=1
a=int(input("enter a value : "))
for index , mark in enumerate (marks):
    print(mark)
    if (index == a):
        print("he's the topper!!")