# Race condition
from threading import Thread
import random
import time


rand_int = 0


def updater():
    global rand_int
    while True:
        rand_int = random.randint(1, 100)


def printer():
    global rand_int
    while True:
        if rand_int % 5 == 0:
            if rand_int % 5 != 0:
                print(rand_int)


if __name__ == "__main__":
    Thread(target=updater, daemon=True).start()
    Thread(target=printer, daemon=True).start()

    # Let the simulation run for 5 seconds
    time.sleep(5)
