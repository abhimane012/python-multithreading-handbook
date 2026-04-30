"""
This program demonstrates the use of a semaphore to control access
to a critical section using multiple threads.

- A semaphore with value 3 allows only 3 threads to run the critical
  section at the same time.
- Additional threads must wait until one of the running threads exits.
- The 'with semaphore' statement automatically handles acquire() and release().
"""

from threading import Semaphore, Thread
import time

# allow max 3 threads at a time
semaphore = Semaphore(3)

def worker(name):
    """Thread function that tries to enter a limited-access section."""
    print(f"{name} is waiting to enter")

    with semaphore:  # automatically calls acquire() and release()
        print(f"{name} entered critical section")
        time.sleep(10)
        print(f"{name} leaving critical section")

threads = []
for i in range(6):
    t = Thread(target=worker, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()