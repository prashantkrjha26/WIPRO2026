import threading

def task():
    print("Thred is running")

t1= threading.Thread(target=task)
#t2= threading.Thread(target=task,args=("Thread2",))
t1.start()
#t2.start()
t1.join()
#t2.join()

print("Main thread ends")