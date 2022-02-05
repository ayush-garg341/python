from threading import Thread, Event
import time

def printer_thread():
    global primeHolder

    while not exitProg:
        # wait for a prime number to become available
        prime_available.wait()

        # print the prime number
        print(primeHolder)
        primeHolder = None

        # reset the event to false
        prime_available.clear()

        # let the finder thread know that printing is done
        prime_printed.set()


def is_prime(num):
    if num == 2 or num == 3:
        return True

    div = 2

    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True


def finder_thread():
    global primeHolder

    i = 1

    while not exitProg:

        while not is_prime(i):
            i += 1
            # Add a timer to slow down the thread
            # so that we can see the output
            time.sleep(.01)

        primeHolder = i

        # let the printer thread know we have
        # a prime available for printing
        prime_available.set()

        # wait for printer thread to print the prime
        prime_printed.wait()

        # reset the flag
        prime_printed.clear()

        i += 1


if __name__=="__main__":
    prime_available = Event()
    prime_printed = Event()
    primeHolder = None
    exitProg = False

    printerThread = Thread(target=printer_thread)
    printerThread.start()

    finderThread = Thread(target=finder_thread)
    finderThread.start()

    # Let the threads run for 3 seconds
    time.sleep(3)

    exitProg = True
    prime_available.set()
    prime_printed.set()

    printerThread.join()
    finderThread.join()

