# What is the main thread?

- When Python starts, the interpreter asks the operating system to create a default thread called the main thread.
- Every process has at least one thread —> the main thread.
- In Python, the main thread is created by the Python Virtual Machine (PVM) when the program begins.
- Top-level code (code run at program start) executes on the main thread.
- You can create additional threads, but the main thread stays until the process exits.
- Threads are Python objects of the threading.Thread class.
