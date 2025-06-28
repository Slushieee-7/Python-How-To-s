import threading

barrier = threading.Barrier(4)

class thread(threading.Thread):
    def __init__(self, thread_ID):
        print("Thread " + str(thread_ID) + " created\n")
        # Initialize the thread with a unique ID
        threading.Thread.__init__(self)
        self.thread_ID = thread_ID
    def run(self):
        print("Thread " + str(self.thread_ID) + " started\n")
        # Simulate some work before reaching the barrier
        print(str(self.thread_ID) + "\n")
        print("Parties = " + str(barrier.parties) + "\n")
        print("n_waiting = " + str(barrier.n_waiting) + "\n")
        barrier.wait()
        
        
thread1 = thread(100)
thread2 = thread(101)
thread1.start()
thread2.start()

# Wait for both threads to reach the barrier
print("Waiting for threads to reach the barrier\n")
barrier.wait()
print("threads have reached the barrier\n")

# Check the status of the barrier
print("Barrier broken = " + str(barrier.broken) + "\n")
print("In the party = " + str(barrier.parties) + "\n")
print("Threads waiting = " + str(barrier.n_waiting) + "\n")

# Now, let's break the barrier
print("Breaking the barrier\n")
barrier.abort()  # Properly break the barrier
print("Barrier aborted\n")

# Wait for the threads to finish
thread1.join()
thread2.join()

# Check the status of the barrier after breaking it
print("Checking the status of the barrier after breaking it\n")
print("Barrier broken = " + str(barrier.broken) + "\n")
print("Parties = " + str(barrier.parties) + "\n")
print("n_waiting = " + str(barrier.n_waiting) + "\n")
print("End")