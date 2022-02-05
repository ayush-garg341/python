"""
A reentrant lock is defined as a lock which can be reacquired by the same thread. A RLock object carries the notion of ownership. If a thread acquires a RLock object, it can chose to reacquire it as many times as possible.
Note that it is imperative to release the lock as many times as it is locked, otherwise the lock remains in locked state and any other threads attempting to acquire the lock get blocked.

As explained, each reentrant lock is owned by some thread when in the locked state. Only the owner thread is allowed to exercise a release() on the lock. If a thread different than the owner invokes release() a RuntimeError is thrown.
"""

from threading import RLock, Thread

def child_task():
    rlock.acquire()
    print("child task executing")
    rlock.release()


rlock = RLock()

rlock.acquire()
rlock.acquire()

rlock.release()

# UNCOMMENT THE FOLLOWING LINE TO MAKE THE
# PROGRAM EXIT NORMALLY.
rlock.release()

thread = Thread(target=child_task)
thread.start()
thread.join()

