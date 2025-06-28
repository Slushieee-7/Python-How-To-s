import threading
import time
import random

i = int(input("Enter how many limited players: "))
if i >20:
    print("The maximum number of players is 20. Setting to 20.")
    i = 20
    
names = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", 
         "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", 
         "Player 11", "Player 12", "Player 13", "Player 14", "Player 15", 
         "Player 16", "Player 17", "Player 18", "Player 19", "Player 20"]
threads = []
# This example simulates multiple players playing a game using a semaphore.
limit = threading.Semaphore(i)  # Only i players can play at the same time

def waiting_area(name):
    print(f"{name} is at the waiting area.")
    
    # Try to acquire the semaphore
    limit.acquire()  # Use the semaphore to control access
    print(f"{name} is now playing.")
    
    # Simulate time spent playing the game
    time.sleep(random.randint(1, 3))  # Simulate variable access time
    
    print(f"{name} is now leaving the game.")
    
    # Release the semaphore so others can enter
    limit.release()

for name in names:
    t = threading.Thread(target=waiting_area, args=(name,))  # Create a thread for each player
    threads.append(t) 
    t.start() 

for t in threads:
    t.join()
