"""
A process is a program in execution and operating systems provide different ways of creating new processes. 
Furthermore, each operating system has its own nuances when spawning new processes, which gets reflected in Python's APIs.
The multiprocessing module offers the method set_start_method() to let the developer choose the way new processes are created.
- fork
- spawn
- fork-server
"""

from multiprocessing import Process
from multiprocessing import current_process
import os


def process_task(x, y, z, key1, key2):
    print("{0} has pid: {1} with parent pid: {2}".format(current_process().name, os.getpid(), os.getppid()))
    print("Received arguemnts {0} {1} {2} {3} {4}\n".format(x, y, z, key1, key2))

if __name__ == "__main__":
    process = [0] * 3

    for i in range(0, 3):
        process[i] = Process(target=process_task, name="process-{0}".format(i), args=(1, 2, 3),
                  kwargs={
                      'key1': 'arg1',
                      'key2': 'arg2'})
        process[i].start()

    for i in range(0, 3):
        process[i].join()

    print("{0} has pid: {1} ".format(current_process().name, os.getpid()))




"""
In the above examples, we don't specify set_start_method() and let Python choose the default.
"""
