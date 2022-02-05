# No Race condition since using lock
from threading import Thread, Lock
import random
import time


rand_int = 0
lock = Lock()

def updater():
    global rand_int
    global lock
    while True:
        with lock:
            rand_int = random.randint(1, 100)


def printer():
    global rand_int
    global lock
    while True:
        with lock:
            if rand_int%5 == 0:
                if rand_int%5!=0:
                    print(rand_int)



if __name__=="__main__":
    Thread(target=updater, daemon=True).start()
    Thread(target=printer, daemon=True).start()

    # Let the simulation run for 5 seconds
    time.sleep(5)
