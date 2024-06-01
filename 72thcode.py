import time 

# def usingWhile():
#   i = 0
#   while i<50000:
#     i = i +1
#     print(i) 

# # def usingFor():
# #   for i in range(500):
# #     print(i)

# # init = time.time()
# # usingFor()
# # t1 = time.time() - init
# init = time.time()
# usingWhile()
# t2 = time.time() - init
# # print(t1)
# print(t2)

# def usingI():
#     for i in range(5):
#       print(i)
# start = time.time()



# usingI()
# time.sleep(1.5)
# print("the total time + 1.5 second delay is = " , time.time() - start)
  
  
# # print(4)
# # time.sleep(3.5)
# # print("This is printed after 3.5 seconds")
 
# # t = time.localtime()
# # formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

# # print(formatted_time) 

# import time

end_time = time.time() + 11 # Calculate the end time, 20 seconds from now

while time.time() < end_time:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
    time.sleep(1)  # Wait for 1 second before printing the time again


