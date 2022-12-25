"""
Programs often use resources other than CPU time, including access to local disks, network sockets, and databases etc. The usage pattern is usually a try-except-finally block. Any cleanup actions are performed in the finally block.

The with statement wraps the execution of a block of statements in a context defined by a context manager object.

Context Manager Protocol:- A context manager object abides by the context management protocol, which states that an object defines the following two methods. 
    - Python calls these two methods at appropriate times in the resource management cycle.
        - __enter__()
        - __exit__()

with context-expression [as target]:
    statement#1
    statement#2
        .
        .
        .
    statement#n

- __enter__() should return an object that is assigned to the variable after 'as' in the above template. By default the returned object is None, and is optional. A common pattern is to return self and keep the functionality required within the same class.

- __exit__() is called on the original Context Manager object, not the object returned by __enter__()

- If an error is raised in __init__() or __enter__() then the code block is never executed and __exit__() is not called

- Once the code block is entered, __exit__ is always called, even if an exception is raised in the code block.

# example without with
file = None
try:
    file = open("test.txt")
except Exception as e:
    print(e)

finally:
    if file is not None:
        file.close()

# example of with
with open("test.txt") as file:    
    data = file.read()
"""


class ExampleClass(object):
    def __init__(self, val):
        print("init")
        self.val = val

    def display(self):
        print(self.val)

    def __enter__(self):
        print("enter invoked")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit invoked")


if __name__ == "__main__":
    with ExampleClass("hello world") as example:
        example.display()
