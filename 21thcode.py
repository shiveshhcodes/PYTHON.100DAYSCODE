# import time
# t = time.strftime('%H:%M:%S')
# Hour = int(time.strftime('%H'))
# if (Hour>=0 and Hour<12):
#  print("Good Morning Shivesh")
# elif (Hour>12 and Hour<17):
#  print("Good Evening Shivesh")
# # elif (Hour>=17 and Hour<0):
# else
#  print ("Good Night Shivesh")


import time

t = time.strftime('%H:%M:%S')  
Hour = int(time.strftime('%H'))  

if 0 <= Hour < 12:  # Morning from 0 to 11s
    print("Good Morning Shivesh")
elif 12 <= Hour < 17:  # Afternoon from 12 to 16
    print("Good Afternoon Shivesh")
else:  # Evening and night from 17 to 23
    print("Good Evening Shivesh")
