import threading
import os
from os import system

import locale
import time
import threading
import random
import json
import struct

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
        print('philosopher', index)

    def run(self):
        # Assign left and right fork
        leftForkIndex = self.index
        rightForkIndex = (self.index - 1) % numPhilosophers
        forkPair = ForkPair(leftForkIndex, rightForkIndex)
        
        # This prints out the threads name on the left of our "progress bar"
        with screenLock:
            print ('philosopher', self.index, ' is eating')

        # Eat forever
        # Make this section into a monitor; the threads (philosophers) will have to request their fork pairs instead 
        # of just taking them when they're available.
        count = 0
        #while count < 100:
        while True:
            #print('philosopher', self.index, ' is eating forever')
            forkPair.pickUp(self)
            #print('philosopher ', self.index, 'pickup; ', 'count: ', count)
            count += 1
            forkPair.putDown()
            #print('philosopher ', self.index, 'put down;', 'count: ', count )
              

class ForkPair:
    

    def __init__(self, leftForkIndex, rightForkIndex):
        # Order forks by index to prevent deadlock
        if leftForkIndex > rightForkIndex:
            leftForkIndex, rightForkIndex = rightForkIndex, leftForkIndex
        self.firstFork = forks[leftForkIndex]
        self.secondFork = forks[rightForkIndex]
        self.count = 0

    def pickUp(self, Philosopher):
        self.count += 1
        print('picked up by ', Philosopher.index, 'count: ', self.count)
        # Acquire by starting with the lower index
        # limit the eating behavior
        self.firstFork.acquire()
        self.secondFork.acquire()
        if count > 101:
            self.firstFork.release()
            self.secondFork.release()
        
    def putDown(self):
        # The order does not matter here
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