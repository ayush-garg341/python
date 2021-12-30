### Mutex vs Monitor

- Monitors are advanced concurrency constructs and specific to languages frameworks.
- It is exposed as a concurrency construct by some programming language frameworks, including Python.
- Concisely, a monitor is a mutex and then some. The additional composition of monitors consists of **condition variables**.
- Monitors are generally language-level constructs whereas mutex and semaphore are lower-level or OS-provided constructs.
- To understand monitor let's see what problem they solve.

  - Usually, in multi-threaded applications, a thread needs to wait for some program predicate to be true before it can proceed forward.
  - Think about a producer/consumer application. If the producer hasn't produced anything the consumer can't consume anything.
  - So the consumer must wait on a predicate that lets the consumer know that something has indeed been produced.
  - So the crude way of accomplishing this:
    ```
    void busy_wait_function() {
          // acquire mutex
          while (predicate is false) {
            // release mutex
            // acquire mutex
          }
          // do something useful
          // release mutex
      }
    ```
  - This works but is an example of **"spin waiting"** which wastes a lot of CPU cycles.

#### Condition Variables

- Mutex provides mutual exclusion. However, at times mutual exclusion is not enough.
- We want to test for a predicate with a mutually exclusive lock so that no other thread can change the predicate when we test for it, but if we find the predicate to be false, we'd want to wait on a condition variable till the predicate's value is changed.
- Each condition variable exposes two methods:-

  - wait() -> when called on the condition variable, will cause the associated mutex to be atomically released and the calling thread would be placed in a wait queue.

    - Since the mutex is now released, it gives other threads a chance to change the predicate that will eventually let the thread that was just placed in the wait queue to make progress.
    - The predicate in this example would be the **size of the buffer**.

  - signal() -> Now imagine a producer places an item in the buffer. The predicate, the size of the buffer, just changed and the producer wants to let the consumer threads know that there is an item to be consumed.

    - This producer thread would then invoke **signal()** on the condition variable.
    - The signal() method, when called on a condition variable, causes one of the threads that has been placed in the wait queue to get ready for execution.
    - **Note** that we didn't say the woken up thread starts executing. It just gets ready - and that could mean being placed in the ready queue.
    - It is only after the producer thread which calls the signal() method has released the associated mutex that the thread in the ready queue starts executing.
    - The thread in the ready queue must wait to acquire the mutex associated with the condition variable before it can start executing.

      ```
      void efficient_waiting_function() {
            mutex.acquire()
            while (predicate == false) {
              cond_var.wait()
            }
            // Do something useful
            mutex.release()
        }

        void change_predicate() {
            mutex.acquire()
            set predicate = true
            cond_var.signal()
            mutex.release()
        }
      ```

#### Monitor Explained

- A monitor is made up of mutex and one or more condition variable.
- A single monitor can have multiple condition variables but not vice versa.
- Another way to think about a monitor is to consider it as an entity having two queues or sets where threads can be placed.
- One is the **entry set** and the other is the **wait set**.
- When a thread A enters a monitor, it is placed into the entry set.
- If no other thread owns the monitor, which is equivalent of saying no thread is actively executing within the monitor section, then thread A will acquire the monitor and is said to own it too.
- Thread A will continue to execute within the monitor section till it exits the monitor or calls **wait()** on an associated condition variable and be placed into the wait set.
- While thread A owns the monitor, no other thread will be able to execute any of the critical sections protected by the monitor.
- New threads requesting ownership of the monitor get placed into the entry set.
- **Note** that only a single thread will be able to own the monitor at any given point and will have exclusive access to data structures or critical sections protected by the monitor.
- Practically, in **Python**, a **Condition object** is a monitor which implicitly has a lock or can be passed one explicitly. You can think of a monitor as a mutex with a wait set.

#### Mesa vs Hoare Monitor

- **Mesa Montitors**

  - Once the asleep thread is signaled and woken up, you may ask why does it needs to check for the condition being false again if the signaling thread must have just set the condition to true?
    ```
    while( condition == false ) {
        condVar.wait();
    }
    ```
  - It is possible that in the time gap between when thread B calls notify() and releases its mutex and the instant at which the asleep thread A wakes up and reacquires the mutex, the predicate is changed back to false by another thread different than the signaler and the awoken threads!

- **Hoare Montitors**
  - The signaling thread B yields the monitor to the woken up thread A and thread A enters the monitor while thread B sits out. This guarantees that the predicate will not have changed and instead of checking for the predicate in a while loop, an if-clause would suffice.
  - The woken-up/released thread A immediately starts execution when the signaling thread B signals that the predicate has changed.
  - No other thread gets a chance to change the predicate since no other thread gets to enter the monitor.
  - Mesa monitors are more efficient than Hoare monitors.

#### Semaphore vs Monitor

- Monitor, mutex, and semaphores can be confusing concepts initially. A monitor is made up of a mutex and a condition variable. One can think of a mutex as a subset of a monitor.
- Difference between semaphore and monitors
  - A monitor and a semaphore are interchangeable. However, monitors take care of atomically acquiring the necessary locks whereas, with semaphores, the onus of appropriately acquiring and releasing locks is on the developer, which can be error-prone.
  - Semaphores are lightweight when compared to monitors, which are bloated.
  - In Python the class Condition is the implementation of the monitor concept. Condition variables enforce correct locking by raising an exception when a thread attempts to invoke the wait() or notify() methods without acquiring the lock associated with the condition variable.
  - A semaphore can allow several threads access to a given resource or critical section. However, only a single thread can own the monitor and access associated resource at any point.
