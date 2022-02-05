"""
- Arguments to the child process are sent using pickle.
- Pickle is a module used for serializing and deserializing an object.
- The object is serialized into a stream of bytes by the sender and then reconstructed into a different incarnation of the same object from the byte stream by the receiver.
- Multiprocessing uses pickle to transport data between processes.
"""
from multiprocessing import Process
from threading import Lock
import multiprocessing

def process_task(lock):
    print("child process")


if __name__ == '__main__':
    lock = Lock()
    multiprocessing.set_start_method('spawn')
    process = Process(target=process_task,
                      args=(lock,))
    process.start()
    process.join()

