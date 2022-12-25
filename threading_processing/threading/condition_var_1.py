"""
cond_var = Condition()
wait() - invoked to make a thread sleep and give up resources and lock as well. When waiting thread is notified it becomes active and try to acquire the lock again, but if lock is not given up by main thread, then it can not make progess and hence can not return from the wait() call.
notify() - invoked by a thread when a condition becomes true and the invoking threads want to inform the waiting thread or threads to proceed.

NOTE:- A condition variable is always associated with a lock. The associated lock must be acquired before a thread can invoke wait() or notify() on the condition variable.

lock = Lock()
cond_var = Condition(lock) # pass custom lock to condition variable
cond_var.acquire()
cond_var.wait()

cond_var = Condition()
cond_var.acquire()
cond_var.wait()

"""
from threading import Condition

cond_var = Condition()
found_prime = False
prime_holder = None
exit_prog = False


def printer_thread_func():
    global prime_holder
    global found_prime

    while not exit_prog:

        # check for predicate
        cond_var.acquire()
        if not found_prime and not exit_prog:
            cond_var.wait()
        cond_var.release()

        if not exit_prog:
            print(prime_holder)
            prime_holder = None
            # acquire lock before modifying shared variable
            cond_var.acquire()
            found_prime = False
            # remember to wake up the other thread
            cond_var.notify()
            cond_var.release()


"""
Idiomatic use of wait():-

acquire lock
while(condition_to_test is not satisfied):
    wait

# condition is now true, perform necessary tasks

release lock

Idiomatic use of notify():-

acquire lock
set condition_to_test to true/satisfied
notify
release lock

"""
