"""
Child process won't be able to inherit a file descriptor from the parent process and won't be able to write to it. Since using spawn rather than fork. And span does not inherit anything from parent other than modules.

Running the below code will result in an error because the value of the variable file_desc isn't copied over to the child process.
"""
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

    # changed the start method to spawn
    multiprocessing.set_start_method('spawn')

    process = Process(target=process_task)
    process.start()
    process.join()
    file_desc.close()

    # read and print the contents of the file
    file_desc = open("sample.txt", "r")
    print(file_desc.read())

    os.remove("sample.txt")

