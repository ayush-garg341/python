"""
Similar to the threading module, synchronization primitives exist for the multiprocessing module to coordinate among multiple processes.

Lock is a non-recursive object and shares the same DNA as the threading.Lock class. In the section on using Queues and Pipes we introduced a snippet with a bug, that could potentially hang depending on the order in which the two processes consumed objects placed on the queue. We can change that example snippet to be process-safe.
"""

# The key is to make the emptiness check and the get call atomic, i.e. when a process executes the two calls, no other process should be able to make the same calls.

from multiprocessing import Process, Queue, current_process, Lock
import multiprocessing, sys
import time
import random


def child_process(q, lock):
    count = 0
    keep_going = True

    while keep_going:
        lock.acquire()
        if not q.empty():
            print(q.get())
            count += 1
        else:
            keep_going = False

        lock.release()
        # Added this sleep so that not all items get processed by
        # a single process
        time.sleep(0.001)

    print(
        "child process {0} processed {1} items from the queue".format(
            current_process().name, count
        ),
        flush=True,
    )


if __name__ == "__main__":
    multiprocessing.set_start_method("forkserver")
    print("This machine has {0} CPUs".format(str(multiprocessing.cpu_count())))
    lock = Lock()
    q = Queue()

    random.seed()
    for _ in range(100):
        q.put(random.randrange(10))

    p1 = Process(target=child_process, args=(q, lock))
    p2 = Process(target=child_process, args=(q, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
