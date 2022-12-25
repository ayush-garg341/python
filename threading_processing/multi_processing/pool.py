"""
The Pool object consists of a group of processes that can receive tasks for execution.
The concept is very similar to a thread pool. Creating and tearing down threads is expensive so most programming language frameworks provide a notion of a pool of threads. Once a thread is done executing a task, it is returned back to the pool rather than being terminated. The process pool concept is similar where the processes are kept alive till there are tasks to be executed.

"""

from multiprocessing import Pool
import os
import time


def init(main_id):
    print(
        "pool process with id {0} received a task from main process with id {1}".format(
            os.getpid(), main_id
        )
    )


def square(x):
    return x * x


def on_success(result):
    print("result is " + str(result))


def on_error(err):
    print("error is " + str(err))


if __name__ == "__main__":
    main_process_id = os.getpid()

    pool = Pool(
        processes=1, initializer=init, initargs=(main_process_id,), maxtasksperchild=1
    )

    result = pool.apply_async(
        square, (9,), callback=on_success, error_callback=on_error
    )

    # prevent main from exiting before the pool process completes
    time.sleep(6)
