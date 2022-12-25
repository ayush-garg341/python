"""
Python allows us to share objects between processes using shared memory.
Value:-  We can use the Value class to create a ctype object in shared memory.
By default the function Value() returns a wrapper over the requested object, thus making the reads and writes to the underlying ctype object process-safe.

"""

from multiprocessing import Process, Semaphore, Value
import multiprocessing


def child_process(sem1, sem2, var):
    print(
        "Child process received var = {0} with id {1} from queue".format(
            str(var.value), id(var)
        ),
        flush=True,
    )
    sem2.release()
    sem1.acquire()

    print("After changes by parent process var = {0}".format(var.value), flush=True)


if __name__ == "__main__":
    # multiprocessing.set_start_method('spawn')
    sem1 = Semaphore(0)
    sem2 = Semaphore(0)
    print("This machine has {0} CPUs".format(str(multiprocessing.cpu_count())))

    var = Value("I", 1)
    print("Parent process puts item on queue with id " + str(id(var)))

    process = Process(target=child_process, args=(sem1, sem2, var))
    process.start()

    sem2.acquire()

    # change the var
    var.value += 2
    print("Parent process changed the enqueued item to " + str(var.value), flush=True)
    sem1.release()
    process.join()


"""
Pay attention to the ID of the var variable printed in the child and parent process. Both are the same, emphasizing that the object is shared between the two processes. However, if you uncomment the start method line 14 to change it to "spawn" and rerun the program, the IDs will be different but the output will be the same.
"""
