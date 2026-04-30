"""
This script demonstrates how to use a Lock to avoid race conditions in multithreading.

What the code does:

1. A shared lock object is created.
2. A function `task()` is defined:
   - It takes a message and a lock as input.
   - It first acquires the lock before executing.
   - Then it prints the message 10 times with a delay.
   - Finally, it releases the lock.

3. Two threads are created:
   - t1 prints "Hello"
   - t2 prints "Hii"

4. Both threads use the same lock:
   - When one thread acquires the lock, the other must wait.
   - This ensures that only one thread runs the critical section at a time.

Key Idea:
- Because of the lock, the output will not mix.
- One thread will complete its printing first, then the other will run.
- This avoids race conditions and ensures ordered execution.
"""

from threading import Thread, Lock
from time import sleep

def task(msg: str, lock: Lock):
    lock.acquire()
    try:
        for _ in range(10):
            print(msg)
            sleep(1)
    finally:
        lock.release()

shared_lock = Lock()

t1 = Thread(target=task, args=("Hello", shared_lock))
t2 = Thread(target=task, args=("Hii", shared_lock))

t1.start()
t2.start()