# Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
from threading import Thread
from threading import current_thread

def thread_task(a, b, c, key1, key2):
    print("{0} received the arguments: {1} {2} {3} {4} {5}".format(current_thread().getName(), a, b, c, key1, key2))



mythread = Thread(
    group=None,  # reserved
    target=thread_task,  # callable object
    name="demoThread",  # name of thread
    args=(1, 2, 3),  # arguments passed to the target
    kwargs={'key1': 777,
            'key2': 111},  # dictionary of keyword arguments
    daemon=None  # set true to make the thread a daemon
)


mythread.start() # start the thread

mythread.join() # wait for the thread to complete
