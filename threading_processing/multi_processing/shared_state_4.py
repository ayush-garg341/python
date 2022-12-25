"""
Note that these shared state objects can only be inherited by the child process. Trying to pass them via a Queue or a Pipe will result in an error
"""


from multiprocessing import Process, Value, Queue
import multiprocessing


def child_process(var, q):
    print(
        "Child process received var = {0} with id {1} from queue".format(
            str(var.value), id(var)
        ),
        flush=True,
    )


if __name__ == "__main__":
    q = Queue()
    print("This machine has {0} CPUs".format(str(multiprocessing.cpu_count())))

    var = Value("I", 1, lock=False)

    # generates error
    q.put(var)

    print("Parent process puts item on queue with id " + str(id(var)))

    process = Process(target=child_process, args=(var, q))
    process.start()
    process.join()
