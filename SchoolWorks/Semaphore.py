import threading
import time
import random

# This example simulates multiple devices accessing a single bank account using a semaphore.
bank = threading.Semaphore(1)  # Only one device can access the bank account at a time
lock = threading.Lock()

def access_bank(device):
    print(f"{device} is waiting to access the bank account.")
    
    # Try to acquire the semaphore
    bank.acquire() #to access the semaphore (bathroom stall), use acquire()
    print(f"{device} is accessing the bank account.")
    
    # Simulate time spent accessing the bank account
    time.sleep(random.randint(1, 3))  # Simulate variable access time
    
    print(f"{device} is leaving the bank account.")
    
    # Release the semaphore so others can enter
    bank.release()

# Simulate 3 devices accessing one bank account
devices = ["ATM", "Web-Based", "Phone-App"]
threads = []

for device in devices:
    t = threading.Thread(target=access_bank, args=(device,)) # to create a thread for each device
    with lock: # to ensure thread-safe access to the threads list
        threads.append(t) 
        t.start() 

for t in threads:
    t.join()
