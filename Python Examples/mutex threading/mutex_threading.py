import threading
import time
from queue import Queue

# This code implements a producer-consumer problem using threading and semaphores.
class Buffer:
    def __init__(self, capacity):
        self.queue = Queue(maxsize=capacity)
        self.capacity = capacity
        self.empty = threading.Semaphore(capacity)  # Initially, all slots are empty
        self.full = threading.Semaphore(0)          # Initially, no slots are full
        self.mutex = threading.Semaphore(1)         # Mutual exclusion

    def produce(self, item):
        self.empty.acquire()  # Wait for an empty slot
        self.mutex.acquire()  # Enter critical section

        # Add item to the buffer
        self.queue.put(item)
        print(f"Made product no. {item}")

        self.mutex.release()  # Exit critical section
        self.full.release()   # Signal that a new item is available

    def consume(self):
        self.full.acquire()   # Wait for a full slot
        self.mutex.acquire()  # Enter critical section

        # Remove item from the buffer
        item = self.queue.get()
        print(f"Consumer {item}")
        print(f"Consumed product no. {item}")

        self.mutex.release()  # Exit critical section
        self.empty.release()  # Signal that an empty slot is available

        return item

class Producer(threading.Thread):
    def __init__(self, buffer): #buffer implementation
        super().__init__()
        self.buffer = buffer

    def run(self):
        for i in range(10):
            self.buffer.produce(i)
            time.sleep(0.5)  # Simulate time to produce an item

class Consumer(threading.Thread):
    def __init__(self, buffer):
        super().__init__()
        self.buffer = buffer
 
    def run(self):
        for _ in range(10):
            self.buffer.consume()
            time.sleep(0.8)  # Simulate time to consume an item

if __name__ == "__main__":
    buffer = Buffer(5)

    producer = Producer(buffer)
    consumer = Consumer(buffer)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

