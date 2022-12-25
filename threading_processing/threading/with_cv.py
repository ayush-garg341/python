from threading import Thread, Condition, Semaphore


def thread1_task(cv, sem):
    with cv:
        sem.acquire()


def thread2_task(cv, sem):
    with cv:
        sem.release()

    print("Released by thread_1 thread")


cv = Condition()
sem = Semaphore(0)

Thread(target=thread2_task, args=(cv, sem)).start()
Thread(target=thread1_task, args=(cv, sem)).start()


"""
If worker_1 is executed first then worker_2 will wait to acquire the condition variable however worker_1 will never release the condition variable since it is waiting for worker_2 to release the semaphore first.
"""
