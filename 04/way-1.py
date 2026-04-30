"""
This example shows how to create and run a thread using the Thread class.

High-Level Steps:
1. Import required classes from the threading module.
2. Define a function (display) that contains the task for the thread.
3. Create a Thread object and pass the function and its arguments.
4. Start the thread using start() → this runs the function in a separate thread.
5. Continue executing the main thread in parallel.

Result:
- Child thread prints its details and message.
- Main thread prints "Main Thread" at the same time.
"""

from threading import Thread, current_thread

def display(n: int, msg: str):
    print(f"Current thread details -> {current_thread()}")
    for i in range(n):
        print(msg)


t1 = Thread(target=display, args=(10, "Hello Thread - 1"))

t1.start()

for i in range(10):
    print("Main Thread")