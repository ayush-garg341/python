# If a synchronization primitive doesn't allow reacquisition of itself by a thread that has already acquired it, then such a thread would block as soon as it attempts to reacquire the primitive a second time.

from threading import *


if __name__ == "__main__":
    ordinary_lock = Lock()

    ordinary_lock.acquire()
    ordinary_lock.acquire()

    print("{0} exiting".format(current_thread().getName()))

    ordinary_lock.release()
    ordinary_lock.release()
