from contextlib import contextmanager


@contextmanager
def single():
    print("Yielding")
    yield
    print("Exiting context manager")


context = single()
with context:
    pass

"""
    Will raise RuntimeError, can't call twice context manager.
"""
# with context:
#     pass


"""
    But what if we wanted to be able to run the context manager twice? Well we’d need to use one that is “reentrant”. 
"""


from contextlib import redirect_stdout
from io import StringIO

stream = StringIO()
write_to_stream = redirect_stdout(stream)
with write_to_stream:
    print("Write something to the stream")
    with write_to_stream:
        print("Write something else to stream")

print(stream.getvalue())

"""
    Here we create a nested context manager where they both write to StringIO, which is an in-memory text stream. 
    The reason this works instead of raising a RuntimeError like before is that redirect_stdout is reentrant and allows us to call it twice
"""
