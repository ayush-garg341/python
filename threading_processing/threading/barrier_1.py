"""
The barrier constructor also accepts a callable argument as an action to be performed when threads are released.
"""

from threading import Thread, Barrier, current_thread
import time
import random


def thread_task():
    time.sleep(random.randint(0, 5))
    print("\nCurrently {0} threads blocked on barrier".format(barrier.n_waiting))
    barrier.wait()


def when_all_threads_released():
    print("All threads released, reported by {0}".format(current_thread().getName()))


num_threads = 5
barrier = Barrier(num_threads, action=when_all_threads_released)
threads = [0] * num_threads

for i in range(num_threads):
    threads[i - 1] = Thread(target=thread_task)

for i in range(num_threads):
    threads[i].start()
