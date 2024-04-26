import time


def my_timer(original_fn):
    def wrapper_fn(*args, **kwargs):
        t = time.time()
        original_fn(*args, **kwargs)
        t2 = time.time() - t
        print("{} took {} secs to run".format(original_fn.__name__, t2))
        return t2

    return wrapper_fn
