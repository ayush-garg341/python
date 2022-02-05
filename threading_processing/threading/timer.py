"""
The Timer object allows execution of a callable object after a certain amount of time has elapsed.
The timer task will be executed even if the main thread exits.
"""

from threading import Timer
from threading import current_thread
import time


def say_hi(name):
    print("{0} says Hi {1}!".format(current_thread().getName(), name))


timer = Timer(1, say_hi, args=["reader"])
timer.start()

# try commenting below line and then start execution
time.sleep(2)

print("{0} exiting".format(current_thread().getName()))

