
import os


import locale
import time
import threading
import random
import json
import struct

from threading import Lock

philosophers = []
forks = []
screenLock = threading.Lock()



"""=========================================================="""

# Layout of the table (P = philosopher, f = fork):
#          P0
#       f3    f0
#     P3        P1
#       f2    f1
#          P2

# Number of philosophers at the table. 
# There'll be the same number of forks.
numPhilosophers = 4

# Lists to hold the philosophers and the forks.
# Philosophers are threads while forks are locks.
philosophers = []
forks = []



class Philosopher(threading.Thread):
    
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
        self.count = 0

    def run(self):
        # Assign left and right fork
        leftForkIndex = self.index
        rightForkIndex = (self.index - 1) % numPhilosophers
        forkPair = ForkPair(leftForkIndex, rightForkIndex)
        
       

        # Eat forever
        
        while True:
            forkPair.pickUp(self.count)
            self.count += 1
            print('philosopher ', self.index, 'pickup; ', 'count: ', self.count)
            forkPair.putDown()
            if self.count > 50:
                self.count = 0
                time.sleep(10)
          

class ForkPair:

    def __init__(self, leftForkIndex, rightForkIndex):
        # Order forks by index to prevent deadlock
        if leftForkIndex > rightForkIndex:
            leftForkIndex, rightForkIndex = rightForkIndex, leftForkIndex
        self.firstFork = forks[leftForkIndex]
        self.secondFork = forks[rightForkIndex]

    def pickUp(self, count):
        if count <= 50:
            self.firstFork.acquire()
            self.secondFork.acquire()
        
        
             
    def putDown(self):
        if self.firstFork.locked() and self.secondFork.locked():
            self.firstFork.release()
            self.secondFork.release()
            
      

if __name__ == "__main__":

    print('starting')

    # Create philosophers and forks
    for i in range(0, numPhilosophers):
        philosophers.append(Philosopher(i))
        forks.append(threading.Lock())
        

    # All philosophers start eating
    for philosopher in philosophers:
        philosopher.start()

    """   

    # Allow CTRL + C to exit the program
    try:
        while True: time.sleep(.21)
    except (KeyboardInterrupt, SystemExit):
        os._exit(0)
    """