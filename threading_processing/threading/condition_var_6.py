"""
notify_all():- can be used when there is more than one thread waiting on a condition variable
    - It can also be used if there's a single thread waiting.
    - The sequence of events on a notify_all() when multiple threads are waiting is described below:
        - A thread comes along acquires the lock associated with the condition variable, and calls wait()
        - The thread invoking wait() gives up the lock and goes to sleep or is taken off the CPU timeslice.
        - The given up lock can be reacquired by a second thread that then too calls wait(), gives up the lock, and goes to sleep.
        - Notice that the lock is available for any other thread to acquire and either invoke a wait or a notify on the associated condition variable.
        - Another thread comes along acquires the lock and invokes notify_all() and subsequently releases the lock.
        - Note it is imperative to release the lock, otherwise the waiting threads can't reacquire the lock and return from the wait() call.
        - The waiting threads are all woken up but only one of them gets to acquire the lock. This thread returns from the wait() method and proceeds forward. The thread selected to acquire the lock is random and not in the order in which threads invoked wait()
        - Once the thread that is the first to wake up and make progress releases the lock, other threads acquire the lock one by one and proceed ahead.
"""

from threading import Condition
from threading import Thread
from threading import current_thread
import time

flag = False

cond_var = Condition()


def child_task():
    global flag
    name = current_thread().getName()

    cond_var.acquire()
    if not flag:
        # try commenting the below line and execution will start serially rather than randomly.
        cond_var.wait()
        print("\n{0} woken up \n".format(name))

    cond_var.release()

    print("\n{0} exiting\n".format(name))


thread1 = Thread(target=child_task, name="thread1")
thread2 = Thread(target=child_task, name="thread2")
thread3 = Thread(target=child_task, name="thread3")

thread1.start()
thread2.start()
thread3.start()

cond_var.acquire()
cond_var.notify_all()
cond_var.release()

thread1.join()
thread2.join()
thread3.join()

print("main thread exits")


"""
If you execute the above code multiple times, you'll recognize that the order in which threads are woken up is random.

notify(n):- Another variant of the notify method is the notify(n) which wakes up n threads. If, say five threads are waiting on a condition variable and we pass invoke notify(3), then only three of the five threads will randomly get notified.


Comment release() statement in above code has below effect :-
    - thread1 enters into fn and acquire the lock on condition var. 
    - thread1 continue execution and execute wait() command and goes to sleep while releasing all the holded resources and goes into wait queue.
    - Now main thread acquire the lock since thread1 is in wait queue and it knows that it can acquire the lock in order to notify thread1- Main thread notifies thread1 and thread1 resumes execution and exit. But did not release the lock yet.
    - Other threads 2 and 3 can not acquire the lock since thread1 has not released the lock and hence they keep waiting for lock to be released and hence program hangs.
    - CPU can randomly select any thread out of 3 threads, to start first and acquire the lock on it.
    - There might be wait queue (invoked on wait()) and other is lock status which determines whether the lock has been released or not if there is no thread in wait queue.
"""
