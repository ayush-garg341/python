"""
Two ways process can communicate between themselves:-
    - Queues
    - Pipes

Queues:- The multiprocessing module offers three types of queues which are all FIFO structures based on the queue module's Queue (queue.Queue) implementation in the standard library.
    - Simple Queue
    - Queue
    - Joinable Queue ( a subclass of Queue)

The queues in the multiprocessing module can be shared among multiple processes. Remember the following:-
    - We can enqueue any element in the queue that is picklable.
    - Queues are thread and process safe.
    - If multiple processes enqueue objects at the same time in a queue, the receiver may receive them out of order. However, all the object enqueued by a single process are always received in order.
    - The official documentation cautions that when an item is placed in an empty queue, there is a "infinitesimal" delay before the empty() method returns false.

"""

# The main process acts as a producer and fills up a queue with ten messages. The child processes each access the queue and consumes messages from it.

from multiprocessing import Queue, current_process, Process
import multiprocessing, sys
import random


def child_process(q):
    count = 0
    while not q.empty():
        print(q.get())
        count += 1

    print(
        "child process {0} processed {1} items from the queue".format(
            current_process().name, count
        ),
        flush=True,
    )


if __name__ == "__main__":
    multiprocessing.set_start_method("forkserver")
    q = Queue()

    print("This machine has {0} CPUs".format(str(multiprocessing.cpu_count())))

    random.seed()
    for _ in range(100):
        q.put(random.randrange(10))

    p1 = Process(target=child_process, args=(q,))
    p2 = Process(target=child_process, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


"""
If you execute the above code multiple times, it is likely that one of the runs will hang and an execution timeout will occur.
    - Thread T1 checks if the queue is empty and finds it non-empty and proceeds to next line.
    - Thread T2 which is running on a different processor makes the same empty check at the same time or before T1 gets a chance to execute the get() call and finds the queue non-empty.
    - Both T1 and T2 attempt a get()
    - As mentioned queue is thread and processor safe so only one process gets an item from the queue.
    - get() is a blocking call and the other thread gets blocked and the program hangs.

This is a classic synchronization problem encountered both with threads of a single process and with multiple processes trying to access a shared data structure.
"""
