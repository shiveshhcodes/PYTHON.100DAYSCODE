# # here we are gonna learn of finally keyword in .py

# MY CODE -- 

# try: 
#     l = [1,5,7,8,9,121]
#     n = int(input("enter a index number: "))
#     print("the index value of" , n , "is" ,  l[n])
# except:
#     print("Sorry the value of" , n , "index number does not exist!!")
# finally:
#     print("\ni do not care if an error occur or not , but i am gonna")
#     print("get printed it anyways!! lol")


# HARRY BHAIYA PRACTICE CODE -- 

def func1():
  try:
    l = [1, 5, 6, 7 , 10 , 12 , 34 , 110]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)
