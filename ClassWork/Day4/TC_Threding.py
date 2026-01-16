import threading

def task():
    print("Thred is running")

t= threading.Thread(target=task)
t.start()
t.join()

print("Main thread ends")