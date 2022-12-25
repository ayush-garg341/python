from threading import Thread
from threading import Lock
import time


class Counter:
    def __init__(self):
        self.count = 0
        self.lock = Lock()

    def increment(self):
        for _ in range(0, 100000):
            self.lock.acquire()
            self.count += 1
            self.lock.release()


if __name__ == "__main__":
    start = time.time()
    num_threads = 5
    counter = Counter()
    threads = [0] * num_threads

    for i in range(0, num_threads):
        threads[i] = Thread(target=counter.increment)

    for i in range(0, num_threads):
        threads[i].start()

    for i in range(0, num_threads):
        threads[i].join()

    end = time.time() - start
    if counter.count != 500000:
        print("You don't know multi-threading at all")
    else:
        print("Good job well done! in {}".format(end))

    # counter = 0
    # for _ in range(0, 500000):
    # counter += 1

    # end = time.time() - start

    # print("Good job well done! in {}".format(end))
