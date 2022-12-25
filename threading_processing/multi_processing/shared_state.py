"""
The parent process modifies an object put on the queue but the print statements from the child process show that the change isn't visible to the child process since it has only received a copy of the object.
"""

from multiprocessing import Queue, Process, Semaphore
import multiprocessing


def child_process(q, sem1, sem2):
    var = q.get()
    print(
        "Child process received var = {0} with id {1} from queue".format(
            str(var), id(var)
        )
    )
    sem2.release()
    sem1.acquire()

    print(
        "After changes by parent process var in child process = {0}".format(str(var)),
        flush=True,
    )


if __name__ == "__main__":
    q = Queue()
    sem1 = Semaphore(0)
    sem2 = Semaphore(0)
    print("This machine has {0} CPUs".format(str(multiprocessing.cpu_count())))

    var = {"key": "value"}
    print("Parent process puts item on queue with id " + str(id(var)))

    q.put(var)

    process = Process(target=child_process, args=(q, sem1, sem2))
    process.start()

    sem2.acquire()

    # change the dictionary object
    var["key"] = "new-value"
    print("Parent process changed the enqueued item to " + str(var), flush=True)
    sem1.release()
    process.join()


"""
Also note that the ID values of the object being enqueued and dequeued are different, thus proving they are two distinct objects. If we used an integer instead e.g. var = 1 you'll see the child and parent process display the same id for the object. This is because under the hood Python returns references to existing integer objects it has already created, rather than creating new objects each time the same integer is asked for.

"""
