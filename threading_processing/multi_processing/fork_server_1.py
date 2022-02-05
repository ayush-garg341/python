from multiprocessing import Process
import multiprocessing
import time


def process_task():
    # block the new process
    time.sleep(1000 * 1000)


if __name__ == '__main__':
    multiprocessing.set_start_method('forkserver')

    process = Process(target=process_task)
    process.start()
    print("New process created")
    # block the main process too
    process.join()


"""
ps -aef | grep python

If you run the suggested command, you should see four python processes (not counting the grep). One is the parent process, second the child process, third the forkserver process and fourth a semaphore tracker process.

Semaphore tracker:- The semaphore tracker process gets created with both spawn and forkserver as start methods. There is a limit on the number of semaphores that can exist on a Unix based system.
- Semaphores when created by a process are linked to that process and may remain linked even if the process exits in an abnormal way e.g. it is killed.
- The semaphore tracker process is tasked with making sure there are no leaking semaphores i.e. it unlinks semaphores which were linked to processes that have already exited.
"""
