"""
A barrier is a synchronization construct to wait for a certain number of threads to reach a common synchronization point in code. The involved threads each invoke the barrier object's wait() method and get blocked till all of threads have called wait().
When the last thread invokes wait() all of the waiting threads are released simultaneously.

"""

from threading import Thread, Barrier
import time
import random


def thread_task():
    time.sleep(random.randint(0, 7))
    print("\nCurrently {0} threads blocked on barrier".format(barrier.n_waiting))
    barrier.wait()


num_threads = 5
barrier = Barrier(num_threads)
threads = [0] * num_threads

for i in range(num_threads):
    threads[i - 1] = Thread(target=thread_task)

for i in range(num_threads):
    threads[i].start()
