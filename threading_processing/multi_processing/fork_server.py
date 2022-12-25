"""
forkserver:- start method, a brand new single threaded process, called server is started.
- Whenever, a new process needs to be created, the parent process connects to the server and requests that it forks a new process.
- Since the server process is single threaded, it can safely invoke os.fork() to create a new process.
"""

from multiprocessing import Process
import multiprocessing


class Test:
    value = 777


def process_task():
    print(Test.value)


if __name__ == "__main__":
    multiprocessing.set_start_method("forkserver")

    # change the value of Test.value before creating
    # a new process
    Test.value = 999
    process = Process(target=process_task, name="process-1")
    process.start()
    process.join()
