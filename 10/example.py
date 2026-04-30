"""
This script demonstrates how to use RLock (Reentrant Lock) with multiple threads
and multiple functions.

What this code shows:

1. An RLock is created:
   - It allows the same thread to acquire the lock multiple times.
   - It ensures only one thread executes the critical section at a time.

2. There are two functions:
   - `outer_task()` acquires the lock and calls `inner_task()`
   - `inner_task()` also tries to acquire the same lock

3. Since RLock is used:
   - The same thread can acquire the lock again inside `inner_task()`
   - No deadlock occurs

4. Two threads are created:
   - Both threads run `outer_task()`
   - One thread completes fully before the other starts (due to locking)

Key Idea:
- RLock allows **nested locking** (lock inside lock)
- It tracks:
  - Which thread owns the lock
  - How many times it has been acquired

Important Note:
- Each `acquire()` must have a matching `release()`
"""

from threading import Thread, RLock, current_thread
import time

lock = RLock()

def inner_task():
    thread_name = current_thread().name

    print(f"{thread_name} trying to acquire lock in inner_task")
    lock.acquire()
    print(f"{thread_name} acquired lock in inner_task")

    time.sleep(1)

    print(f"{thread_name} releasing lock in inner_task")
    lock.release()


def outer_task():
    thread_name = current_thread().name

    print(f"{thread_name} trying to acquire lock in outer_task")
    lock.acquire()
    print(f"{thread_name} acquired lock in outer_task")

    time.sleep(1)

    # Calling another function that also uses the same lock
    inner_task()

    print(f"{thread_name} releasing lock in outer_task")
    lock.release()


t1 = Thread(target=outer_task, name="Thread-1")
t2 = Thread(target=outer_task, name="Thread-2")

t1.start()
t2.start()
