import time
import numpy

time.sleep(1)
big_array = numpy.empty(1_000_000)
time.sleep(1)
big_array[:] = 42.0
time.sleep(1)
