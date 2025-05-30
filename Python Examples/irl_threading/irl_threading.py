import threading
import time
import random

# Create a semaphore with 3 slots (like 3 bathroom stalls)
bathroom = threading.Semaphore(3)
lock = threading.Lock()

def use_bathroom(person):
    print(f"{person} is waiting to use the bathroom.")
    
    # Try to acquire the semaphore
    bathroom.acquire() #to access the semaphore (bathroom stall), use acquire()
    print(f"{person} has entered the bathroom.")
    
    # Simulate time spent in the bathroom
    time.sleep(random.randint(1, 3))
    
    print(f"{person} is leaving the bathroom.")
    
    # Release the semaphore so others can enter
    bathroom.release()

# Simulate 6 people trying to use the bathroom
people = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]
threads = []

for person in people:
    t = threading.Thread(target=use_bathroom, args=(person,))
    with lock:
        threads.append(t)
        t.start()

for t in threads:
    t.join()
