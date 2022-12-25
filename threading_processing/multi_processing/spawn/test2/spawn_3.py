"""
If we pass any arguments to the process's callable target, the child process does receive them. This is in line with the documentation that says the child process inherits just enough resources from the parent process to execute the run method of the process object.
"""


from multiprocessing import Process
import multiprocessing

global_arg = "this is a global arg"


def process_task(garg, larg):
    print(garg + " - " + larg)


if __name__ == "__main__":

    multiprocessing.set_start_method("spawn")
    local_arg = "this is a global arg"

    process = Process(
        target=process_task, name="process-1", args=(global_arg, local_arg)
    )
    process.start()
    process.join()
