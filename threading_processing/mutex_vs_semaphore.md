### These are mechanism of locking and signalling in multi-threaded applications and the difference between these two constructs.

**Mutex**:- Mutual Exclusion.

- A mutex is used to guard shared data such as linked list, array or any primitive type.
- A mutext only allows a single thread to access a resource or critical section.
- Once a thread acquires a mutex, all other threads attempting to acquire the same mutex are blocked until the first thread releases the mutex.

**Semaphore**:- It is used for limiting access to a collection of resources.

- Think of semaphore as having a limited number of permits to give out. If a semaphore has given out all the permits it has, then any new thread that comes along requesting a permit will be blocked till an earlier thread with a permit returns it to the semaphore.
- A typical example would be a pool of database connections that can be handed out to requesting threads.A semaphore with a single permit is called a **binary semaphore**.
- Semaphores can also be used for signaling among threads. This is an important distinction as it allows threads to cooperatively work towards completing a task.
- A semaphore can be acted upon by different threads. This is true even if the semaphore has a permit of one.

**When can a semaphore masquerede as a mutex?**

- A semaphore can potentially act as a mutex if the permits it can give out is set to 1.
- The most important difference between the two is that in case of a mutex the same thread must call acquire and subsequent release on the mutex whereas in case of a binary semaphore, different threads can call acquire and release on the semaphore.
- This leads us to the concept of ownership. A mutex is owned by the thread acquiring it till the point the owning-thread releases it, whereas for a semaphore there's no notion of **ownership**.

**Semaphore for signalling**

- Semaphores can be used for signaling amongst threads.
- For example, in case of the classical **producer/consumer** problem the producer thread can signal the consumer thread by incrementing the semaphore count to indicate to the consumer thread to consume the freshly produced item.
