# Daemon is a computer program that runs as a background process rather than being under the direct control of an interactive user
# The difference between a regular thread and a daemon thread is that a Python program will not exit until all regular/user threads terminate. However, a program may exit if the daemon thread is still not finished.


from threading import Thread
from threading import current_thread
import time

# In the below snippet the main thread creates a non-daemonic thread and exits. However, the program continues to run.


def regular_thread_task():
    while True:
        print("{0} executing".format(current_thread().getName()))
        time.sleep(1)


regularThread = Thread(target=regular_thread_task, name="regularThread", daemon=False)
regularThread.start()  # start the regular thread

time.sleep(3)

print("Main thread exiting but Python program doesn't")


# In contrast, the runnable snippet below will exit even though the daemon thread is still executing.


def daemon_thread_task():
    while True:
        print("{0} executing".format(current_thread().getName()))
        time.sleep(1)


regularThread = Thread(target=daemon_thread_task, name="daemonThread", daemon=True)
regularThread.start()  # start the daemon thread

time.sleep(3)

print("Main thread exiting and Python program too")


if __name__ == "__main__":
    regular_thread_task()


# Resources such as open files and database connections may not shut-down properly and daemon threads are not a good choice for such tasks. One final caveat to remember is that if you don't specify the daemon parameter in the constructor then the daemonic property is inherited from the current thread.
