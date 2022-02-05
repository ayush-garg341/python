### Spawn Intro

- Next option available to create a process is the spawn method.

- **exec system call:-**

  - When you issue an ls or a find command in your terminal, the shell first forks itself and then invokes one of the variants of the exec family of system calls.
  - An exec call transforms the calling process into another.
  - The program in the calling process is replaced with another program and is run from the entry point.
  - Realize the distinction between a program and a process as it matters in this context.
  - The program is just a set of instructions and data that is used to initialize a process.
  - Using exec, the running process loads a program (instructions and data) and replaces its own program with the loaded one and starts execution.
  - Both fork and exec can be called independently and need not be called in succession.
  - For instance, a process that is ending can simply call exec and start another program rather than forking itself.
  - Similarly, a process listening on a socket may want to fork itself to let the child process deal with a received request while it goes back to listening.
  - But the usual way to create a new process in the Unix world is to first fork in the parent process and then exec in the child process.
  - The child process's PID doesn't change and the parent process can wait for the child process to finish before resuming execution.
  - **Remember**, forking produces two processes, whereas exec loads an executable in the existing process's address space.

- **spawn call:-**
  - Spawn is essentially a combination of fork followed by an exec (one of its variants) system call.
  - The module state isn’t inherited by a child process, rather it starts from scratch.
  - A new python interpreter process is created and the child doesn't inherit any resources from the parent process other than those required to execute the specified callable target.
  - Note that spawning a process is slower than forking a process. When a child process is spawned anything imported at the module level in the **main** module of the parent process gets reimported in the child.
