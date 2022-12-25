"""
A semaphore is nothing more than an atomic counter that gets decremented by one whenever acquire() is invoked and incremented by one whenever release() is called.

# semaphore initialized with a default count of 1
semaphore = Semaphore()

# semaphore initialized with count set to 5
sem_with_count = Semaphore(5)

acquire():- If a thread invokes acquire() on a semaphore, the semaphore counter is decremented by one. If the count is greater than 0, then the thread immediately returns from the acquire() call. If the semaphore counter is zero when a thread invokes acquire(), the thread gets blocked till another thread releases the semaphore.


release():- When a thread invokes the release() method, the internal semaphore counter is incremented by one. If the counter value is zero and another thread is already blocked on an acquire() then a release would unblock the waiting thread.

The primary use of semaphores is signaling among threads which are working to achieve a common goal.
"""

from threading import Thread
from threading import Semaphore
import time


def task1():
    sem.acquire()


def task2():
    sem.release()


# initialize with zero
sem = Semaphore(0)

# start thread 2 first which invokes release()
thread2 = Thread(target=task2)
thread2.start()

# delay starting thread 1 by three seconds
time.sleep(3)

# start thread 1
thread1 = Thread(target=task1)
thread1.start()

thread1.join()
thread2.join()
