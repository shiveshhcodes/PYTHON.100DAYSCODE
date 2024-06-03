#lets do some multithreading stuff!! hehehe

import time
import threading

def func(seconds):
  print(f"sleeping for {seconds} now!!")
  time.sleep(seconds)
     
# this is normal code here!!
# func(4)
# func(2)
# func(3)

# now do threading thing here!

time1 = time.perf_counter()
t1 = threading.Thread(target=func , args=[4])
t2 = threading.Thread(target=func , args=[2])
t3 = threading.Thread(target=func , args=[1])


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()
print(time2 - time1)