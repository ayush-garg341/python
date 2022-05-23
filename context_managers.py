import os
from contextlib import contextmanager

# f = open("sample.txt", 'w')
# f.write("Adding some more text to it")
# f.close()


# use of context manager "with", no need to write close, that get handled itself and hence efficiently managing resources.
# Even if there is an error in writing or opening to it.
with open("sample.txt", "w") as f:
    f.write("Adding some text to it")


class Open_file:
    def __init__(self, file_name, mode) -> None:
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        print("Inside enter")
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exec_type, exec_val, traceback):
        print("exit called")
        self.file.close()


# Testing if exit is called when returning from with in the context decorator
def random_fn():
    print("inside fn")
    with Open_file("sample_2.txt", "w") as f:  # init and enter method called
        print("Opening a file")
        f.write("I am Ayush working as backend developer (SDE-2) at innovaccer.")
        return 6


# # exit method called

random_fn()
print(f.closed)

# Using contextlib
print("---------------- Using contextLib ------------------ ")


@contextmanager
def open_file(file_name, mode):
    try:
        f = open(file_name, mode)  # class equivalent of init and enter method
        yield f  # yieldling out file object, so that we can work with it later
    finally:
        f.close()  # exec method


with open_file("sample_3.txt", "w") as f:
    f.write("Hey! you people are awesome")

print(f.closed)

# open in python is already a context manager.


# example 2

# cwd = os.getcwd()
# os.chdir("oops")
# print(os.listdir())
# os.chdir(cwd)

# cwd = os.getcwd()
# os.chdir("solid_principles")
# print(os.listdir())
# os.chdir(cwd)


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)  # we need not to do this again and again


with change_dir("oops"):
    print(os.listdir())

with change_dir("solid_principles"):
    print(os.listdir())


"""
    Context manager is useful in many scenarios:
        1. Opening and closing database connection
        2. Acquiring and releasing locks on resources

    When using decorator contextmanager, after that we can use the function with, "with"
"""
