"""
Pipes:- Pipes can be best thought of as a two way connection between two processes.
Whatever is written to one end of the pipe can be retrieved from the other end of the pipe. If two threads or processes attempt to write to the same end of the pipe at the same time, the data can potentially become corrupt.

The Pipe constructor takes in a boolean value. If passed in False, the pipe acts as a one-way communication where one end can only send messages and the other can only receive messages.

recv_conn, send_conn = Pipe(duplex=False)

The first argument recv_conn returned by the constructor can receive messages and the second argument send_conn can send messages. By default or if the constructor is passed-in True, the connection created is bidirectional.

"""

# The child process writes ten strings to the pipe which the parent prints on the console after retrieving them from the queue.

from multiprocessing import Process, Pipe
import time

def child_process(conn):
    for i in range(0, 10):
        conn.send("hello " + str(i + 1))
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=child_process, args=(child_conn,))
    p.start()
    time.sleep(3)

    for _ in range(0, 10):
        msg = parent_conn.recv()
        print(msg)

    parent_conn.close()
    p.join()


"""
get() -> blocking call in case of queue
recv() -> blocking call in case of pipe

However both these classes offer non-blocking versions of respective methods.
"""
