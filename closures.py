import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running {} with arguments {}'.format(func.__name__, args))
        print(func(*args))

    return log_func

def add(x, y):
    return x+y

def subtract(x, y):
    return x - y

add_logger = logger(add)
sub_logger = logger(subtract)

add_logger(1, 2)
add_logger(5, 12)

sub_logger(5, 3)
sub_logger(12, 5)



def outer_fn(msg):

    msg = msg

    def inner_fn():
        print(msg)

    return inner_fn

hi_fn = outer_fn("Hi!")
hello_fn = outer_fn("Hello!")

print(hi_fn.__name__)
print(hello_fn.__name__)

hi_fn()
hello_fn()