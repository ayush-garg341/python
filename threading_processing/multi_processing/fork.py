"""
Fork is the default method Python uses to create processes on Unix based systems.
Fork is one of the options a developer can choose to create processes.

Fork System Call -> There are two families of system calls, fork and exec that can be invoked by a process to create subprocesses on Unix based systems
    - A process can invoke this system call and get an almost clone of itself. 
    - We qualify the statement with almost because not everything is copied when a fork happens.
    - The child process gets an identical memory image so any open file descriptors are copied. However, multiple threads of a process don't get copied.
    - Any threads running in the parent process do not exist in the child process.
    - Under the hood, Python uses os.fork() to create the child process.
    - Often times we don't want to fork processes because the newly created process (called the child process) comes with identical copies of data-structures and file descriptors of the parent process, which can be problematic.

"""

# Every data structure, open file, and database connection that exists in the parent process is copied over, open and ready to use, in the child process.

from multiprocessing import Process
import multiprocessing
import os

file_desc = None


def process_task():
    # write to the file in a child process
    file_desc.write("\nline written by child process with id {0}".format(os.getpid()))
    file_desc.flush()


if __name__ == '__main__':
    # create a file descriptor in the parent process
    file_desc = open("sample.txt", "w")
    file_desc.write("\nline written by parent process with id {0}".format(os.getpid()))
    file_desc.flush()

    multiprocessing.set_start_method('fork')

    process = Process(target=process_task)
    process.start()
    process.join()
    file_desc.close()

    # read and print the contents of the file
    file_desc = open("sample.txt", "r")
    print(file_desc.read())

    os.remove("sample.txt")

