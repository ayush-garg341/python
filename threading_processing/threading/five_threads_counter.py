from threading import Thread
import sys


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        for _ in range(100000):
            self.count += 1


if __name__ == "__main__":
    sys.setswitchinterval(0.005)

    num_threads = 5
    threads = [0] * num_threads
    counter = Counter()

    for i in range(0, num_threads):
        threads[i] = Thread(target=counter.increment)

    for i in range(0, num_threads):
        threads[i].start()

    for i in range(0, num_threads):
        threads[i].join()

    if counter.count != 500000:
        print(" count = {0}".format(counter.count), flush=True)
    else:
        print(" count = 50,000 - Try re-running the program.")
