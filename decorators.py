from functools import wraps


def decorator_fn(original_fn):
    def wrapper_fn(*args, **kwargs):
        print("wrapper fn executed this before {}".format(original_fn.__name__))
        return original_fn(*args, **kwargs)

    return wrapper_fn


"""
Without using purely decorator syntax, below is how we can simulate the decorator functionality.

def display():
    print("display fn. ran")

decorator_display = decorator_fn(display)
decorator_display() 

"""


"""
    We can achieve the decorator functionality using class decorator also. But fun. decorator are more common
"""


class decorator_class(object):
    def __init__(self, original_fn) -> None:
        self.original_fn = original_fn

    def __call__(self, *args, **kwds):
        print("call method executed this before {}".format(self.original_fn.__name__))
        return self.original_fn(*args, **kwds)


def my_logger(original_fn):
    import logging

    logging.basicConfig(
        filename="{}.log".format(original_fn.__name__), level=logging.INFO
    )

    @wraps(original_fn)
    def wrapper_fn(*args, **kwargs):
        logging.info(
            "Running {} with args: {} and kwargs: {}".format(
                original_fn.__name__, args, kwargs
            )
        )
        return original_fn(*args, **kwargs)

    return wrapper_fn


def my_timer(original_fn):
    import time

    @wraps(original_fn)
    def wrapper_fn(*args, **kwargs):
        t = time.time()
        original_fn(*args, **kwargs)
        t2 = time.time() - t
        print("{} took {} secs to run".format(original_fn.__name__, t2))
        return t2

    return wrapper_fn


# @decorator_fn
# # @decorator_class
# def display():
#     print("display fn. ran")
# display()


# @decorator_fn
# @decorator_class
@my_logger
@my_timer
def display_info(name, age):
    import time

    time.sleep(1)
    print("display_info ran with argument ({} {})".format(name, age))


display_info("AAAyush", 26)


"""
Single decorator is equivalent to

@decorator_fn_one
@display():
    pass
display = decorator_fn_one(display) ---> return a reference to wrapper fun. check using print(display.__name__) // wrapper_fn


@decorator_fn_two
@decorator_fn_one
@display():
    pass
display = decorator_fn_two(decorator_fn_one(display)) ---> wrapper fn. will be passed to decorator_fn_two


"""


"""
It's always the good idea to preserve the info of original function when using decorator stack or multiple decorator on
single function.
We can do so using functool module.
If we don't want the wrapper fn as returned value from decorator, we can use something like

@wraps(original_fn)

"""
