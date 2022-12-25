from multiprocessing import Process
import multiprocessing
import edu


def process_task():
    print("I am child process")


if __name__ == "__main__":

    # Change the method to 'spawn' and verify
    # that the modules are reimported in the child
    # process
    multiprocessing.set_start_method("spawn")
    process = Process(target=process_task)
    process.start()
    process.join()
    print("I am parent process")
