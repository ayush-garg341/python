"""
When we fork, the entire Python process is duplicated in memory including the Python interpreter, code, libraries, current stack, etc. 
This creates a new copy of the python interpreter. The implication is that forking creates two python interpreters each with its own GIL. 
A single GIL is no more a blocker and we can have true multi-processing on a multi-core system.
In contrast, threads in one process share the same GIL, meaning only one thread runs at a given moment, giving only the illusion of parallelism.

Problems with fork:-
    - The main process created a Lock object and acquires it just before forking a child process. The child process receives a copy of all the global data-structures of the parent process. It attempts to acquire the lock but when the lock object was copied it was already in the locked state so the child ends up waiting on a lock object that was inherited in the locked state and will never be unlocked because there's no other thread in the process that will unlock it. The child process will hang. If you run the executable code, the execution will time out. This problem can manifest itself and be very hard to debug when you import a third-party module/library that uses threads behind the scenes. The moment when the fork happens, synchronization primitives can be copied in a state that causes the child process to hang.
    - Forking and multithreading don't mix well. Imagine a situation where a process has some threads waiting in systems calls or for IO and a different thread attempts a fork.
    - Some libraries assume proper initialization for each process but this isn't true when a process is a result of a fork.
    - Portability can be an issue because of differences amongst platforms. For instance, how open file descriptors get inherited by a child process or what system calls can be executed after a fork vary across platforms.
    - The fork method can't be used on a Windows platform.
    - Forking is prone to security holes. For instance, if a random number generator were seeded in the main process and then forked, the child would receive the same pseudo-random number generator (PRNG) state and produce the same sequence of random numbers. Security protocols such as SSL make use of random numbers and can get compromised. The random.seed() is passed in a seed value and a sequence of numbers is generated thereafter. The same seed generates the same sequence of random numbers.
"""


from threading import Lock
from multiprocessing import Process
import time
import multiprocessing

lock = Lock()


def process_task():
    lock.acquire()
    print("I am child process")
    lock.release()


if __name__ == '__main__':
    multiprocessing.set_start_method('fork')
    process = Process(target=process_task)

    # acquire the lock just before starting a new process
    lock.acquire()

    process.start()

    # release the lock after starting the child process
    lock.release()

    # wait for child process to be done
    print("Parent process waiting for child process to finish")
    process.join()
    print("done")



