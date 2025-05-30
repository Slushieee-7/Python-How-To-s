
counter = 0

lock = threading.Lock() #creates a lock object 

def increment_counter():
    global counter
    for _ in range (100000): #repeats the next code 100,000 times 
        with lock: #acquires the lock before running the code
            counter += 1 #incrementer
            print(counter)
        #after the code finishes, the lock is automatically released
        
threads = []
for _ in range (5): #creates 5 separate threads that will also increment the counter
    t = lock.Thread(target=increment_counter) #threads that will increment 
    threads.append(t) #appends the thread (t) in a list 
    t.start() #starts the threading process
    
for t in threads: #waits for each thread to finish the execution 
    t.join()

print("Final counter value: ", counter)

import threading 