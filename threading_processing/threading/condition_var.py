"""
Synchronization mechanisms need more than just mutual exclusion; a general need is to be able to wait for another thread to do something. Condition variables provide mutual exclusion and the ability for threads to wait for a predicate to become true.

Locks aren't enough when threads want to coordinate among themselves.
"""

from threading import Thread
import time

def print_prime():
    global found_prime
    global prime_holder
    while not exit_prog:
        while not found_prime and not exit_prog:
            # time.sleep(0.1)
            pass

        if not exit_prog:
            print(prime_holder)
            found_prime = False
            prime_holder = None



def is_prime(num):
    if num==2 or num==3:
        return True
    div = 2
    while div <= num/2:
        if num % div == 0:
            return False
        div += 1
    return True


def prime_finder():
    global found_prime
    global prime_holder

    i = 1
    while not exit_prog:
        while not is_prime(i):
            i += 1
        prime_holder = i
        found_prime = True

        while found_prime and not exit_prog:
            # time.sleep(0.1)
            pass

        i += 1


if __name__=="__main__":

    found_prime = False
    prime_holder = None
    exit_prog = False

    printer_thread = Thread(target=print_prime)
    printer_thread.start()

    finder_thread = Thread(target=prime_finder)
    finder_thread.start()

    # Let the threads run for 5 seconds
    time.sleep(3)

    # Let the threads exit
    exit_prog = True

    printer_thread.join()
    finder_thread.join()


"""
One shortcoming of the above code is we have the printer thread constantly polling in a while loop for the found_prime variable to become true. This is called busy waiting and is highly discouraged as it unnecessarily wastes CPU cycles. Ideally, the printer thread should go to sleep so that it doesn't consume any system resources and be woken up when the condition it needs to act upon becomes true. This can be achieved through condition variables.
"""
