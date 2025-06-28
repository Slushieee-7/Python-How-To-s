import threading
import time
import random

NUM_PLAYERS = 6

game_running = threading.Event()
barrier = threading.Barrier(NUM_PLAYERS)
players = []

class Player(threading.Thread):
    def __init__(self, player_id):
        super().__init__()
        self.player_id = player_id
        self.active = True

    def run(self):
        print(f"Player {self.player_id} is joining the game... \n")
        try:
            barrier.wait()
            if self.active:
                print(f"Player {self.player_id} has joined! Game started!")
                # Simulate Player 1 leaving after 2 seconds
                if self.player_id == 1:
                    time.sleep(2)
                    print(f"Player {self.player_id} is leaving the game after 2 seconds!")
                    self.active = False
                    game_running.clear()
                    barrier.abort()  # Immediately break the barrier for all
        except threading.BrokenBarrierError:
            print(f"Player {self.player_id} could not join, barrier broken.")

# Start player threads
for i in range(NUM_PLAYERS):
    p = Player(i+1)
    players.append(p)
    p.start()

# Wait for all players to reach the barrier
try:
    barrier.wait()
    print("All players have joined. Game is starting!")
    game_running.set()
except threading.BrokenBarrierError:
    print("Game cannot start, not enough players.")

# No need for a monitoring loop; game stops immediately when a player leaves

# Wait for all threads to finish
for p in players:
    p.join()

print("Game ended.")
