from threading import Thread, Semaphore
import time


def print_prime():
    global prime_holder
    while not exit_prog:
        # wait for a prime number to become available
        sem_find.acquire()

        # print the prime number
        print(prime_holder)
        prime_holder = None

        # let the finder thread find the next prime
        sem_print.release()


def is_prime(num):
    if num == 2 or num == 3:
        return True
    div = 2
    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True


def find_prime():
    global prime_holder
    i = 1
    while not exit_prog:
        while not is_prime(i):
            i += 1
            # Add a timer to slow down the thread
            # so that we can see the output
            time.sleep(0.01)

        prime_holder = i

        # let the printer thread know we have
        # a prime available for printing
        sem_find.release()

        # wait for printer thread to complete
        # printing the prime number
        sem_print.acquire()
        i += 1


if __name__ == "__main__":
    prime_holder = None
    exit_prog = False
    sem_find = Semaphore(0)
    sem_print = Semaphore(0)
    print_thread = Thread(target=print_prime)
    find_thread = Thread(target=find_prime)

    print_thread.start()
    find_thread.start()

    time.sleep(3)
    exit_prog = True
    print_thread.join()
    find_thread.join()
