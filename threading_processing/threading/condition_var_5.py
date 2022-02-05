"""
wait(n):- floating point parameter n
    - This is the number of seconds a calling thread would wait to be notified by another thread.
    - The wait method times out after n seconds and the thread is woken up even if no notification is received.

"""

from threading import Condition
from threading import Thread
import time

flag = False

cond_var = Condition()


def child_task():
    cond_var.acquire()

    if (flag == False):
        cond_var.wait(1)

    if (flag == False):
        print("child thread times out waiting for a notification")

    # don't forget to release the lock    
    cond_var.release()


thread = Thread(target=child_task)
thread.start()

time.sleep(3)
thread.join()

