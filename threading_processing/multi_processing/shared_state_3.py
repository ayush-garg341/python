"""
Array:- Array is very similar to how we use Value.
Note we are using semaphores only to coordinate the two processes.
"""

from multiprocessing import Process, Semaphore, Array
import multiprocessing


def child_process(sem1, sem2, arr):
    print(
        "Child process received var = {0} with id {1} from queue".format(
            str(arr[0]), id(arr)
        ),
        flush=True,
    )
    sem1.release()
    sem2.acquire()

    print(
        "After changes by parent process, child process sees var as = {0}".format(
            arr[0]
        ),
        flush=True,
    )


if __name__ == "__main__":
    sem1 = Semaphore(0)
    sem2 = Semaphore(0)
    print("This machine has {0} CPUs".format(str(multiprocessing.cpu_count())))

    arr = Array("i", range(5))
    print("Parent process puts item on queue with id " + str(id(arr)))

    process = Process(target=child_process, args=(sem1, sem2, arr))
    process.start()

    sem1.acquire()

    # change var and verify the change is reflected in the child process
    arr[0] += 100
    print("Parent process changed the enqueued item to " + str(arr[0]), flush=True)
    sem2.release()
    process.join()
