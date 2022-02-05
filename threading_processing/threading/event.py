"""
An event object is one of the simplest primitives available for synchronization. Internally, it has a boolean flag that can be set or unset using the methods set() and clear(). Additionally, a thread can check if the flag is set to true by invoking the is_set() method.

The event object exposes a wait() method that threads can invoke to wait for the internal boolean flag to become true. If the flag is already true, the thread returns immediately. If there are multiple threads waiting on the event object and an active thread sets the flag then all the waiting threads are unblocked.

A thread never gets blocked on wait() of an event object if the internal flag is set to true no matter how many times the thread invokes the wait() method.

A thread never gets blocked on wait() of an event object if the internal flag is set to true no matter how many times the thread invokes the wait() method.
"""

from threading import Thread
from threading import Event
import time


def task1():
    event.wait()
    event.wait()
    event.wait()
    print("thread invoked wait thrice")


def task2():
    time.sleep(1)
    event.set()


event = Event()

thread1 = Thread(target=task1)
thread1.start()

thread2 = Thread(target=task2)
thread2.start()

thread1.join()
thread2.join()

