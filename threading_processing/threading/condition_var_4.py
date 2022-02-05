"""
0.    cond_var.acquire()
1.    found_prime = <new_value> # can be True or False
2.    cond_var.notify()
3.    cond_var.release()


Changing the above code to like below one:- 

0.    cond_var.acquire()
1.    cond_var.notify()
2.    found_prime = <new_value> # can be True or False
3.    cond_var.release()

Indeed the program would continue to work correctly, since the found_prime variable is being mutated within the acquire() and release() statements and we guaranteed to hold the lock until release() is invoked. A waiting thread is only able to inspect the value of the found_prime variable once the lock is released, assuming ofcourse that the waiting thread also acquires the condition varible before testing for found_prime.
"""

from threading import Thread
from threading import current_thread
from threading import Condition
import time


def printer_thread():
    global prime_holder
    global found_prime

    while not exit_prog:

        cond_var.acquire()
        while not found_prime and not exit_prog:
            cond_var.wait()

        if not exit_prog:
            print("{0} prints {1}".format(current_thread().getName(), prime_holder))

            prime_holder = None

            found_prime = False
            cond_var.notifyAll()
        cond_var.release()

    print("printer {0} exiting".format(current_thread().getName()))


def is_prime(num):
    if num == 2 or num == 3:
        return True

    div = 2

    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1

    return True


def finder_thread():
    global prime_holder
    global found_prime

    i = 1

    while not exit_prog:

        while not is_prime(i):
            i += 1
            # Add a timer to slow down the thread
            # so that we can see the output
            time.sleep(.01)

        prime_holder = i

        cond_var.acquire()
        found_prime = True
        cond_var.notifyAll()
        cond_var.release()

        cond_var.acquire()
        while found_prime and not exit_prog:
            cond_var.wait()
        cond_var.release()

        i += 1

    print("finder exiting")


if __name__ == "__main__":
    cond_var = Condition()
    found_prime = False
    prime_holder = None
    exit_prog = False


    exit_prog = False
    printerThread = Thread(target=printer_thread)
    printerThread.start()

    printerThread2 = Thread(target=printer_thread)
    printerThread2.start()

    printerThread3 = Thread(target=printer_thread)
    printerThread3.start()

    finderThread = Thread(target=finder_thread)
    finderThread.start()

    # Let the threads run for 3 seconds
    time.sleep(3)

    exit_prog = True

    # Let the threads exit
    cond_var.acquire()
    cond_var.notifyAll()
    cond_var.release()

    printerThread.join()
    printerThread2.join()
    printerThread3.join()
    finderThread.join()




"""
Last but not the least, understand that in case of the printer program we can't use the notify() call even though one may incorrectly reason that we are attempting to wake up only the finder thread. The issue is that both the printer and finder threads are waiting on the same condition variable and a notify() call may wake up the printer thread and will go back to waiting since the finder thread hasn't found a new prime causing a deadlock.
"""
