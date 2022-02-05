"""
Finder thread: as soon as it finds the prime number it will notify to printer thread.
"""

from threading import Condition

cond_var = Condition()
found_prime = False
prime_holder = None
exit_prog = False


def finder_thread():
    global prime_holder
    global found_prime

    i = 1

    while not exit_prog:

        while not is_prime(i):
            i += 1

        primeHolder = i

        cond_var.acquire()
        found_prime = True
        cond_var.notify()
        cond_var.release()

        cond_var.acquire()
        while found_prime and not exit_prog:
            cond_var.wait()
        cond_var.release()

        i += 1

