
while True:
    ad = input("Enter a number: ")
    try:
      a = int(ad)
      print ("your number is" , a) 
     
      if a <= 21:  # Condition for breaking the loop
            # print("Number is greater than 21. Exiting the loop.")
            break  # Exit the loop
    except ValueError:
     print("please enter a number , not alphabets")
  