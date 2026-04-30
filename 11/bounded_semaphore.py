"""
This program demonstrates a bounded semaphore and what happens
when release() is called more times than allowed.

- Only 2 threads can enter the critical section at a time.
- BoundedSemaphore prevents the value from exceeding its limit.
- An extra release() will raise a ValueError.
"""

from threading import BoundedSemaphore, Thread
import time

semaphore = BoundedSemaphore(2)

def worker(name):
    print(f"{name} is waiting to enter")

    semaphore.acquire()
    try:
        print(f"{name} entered critical section")
        time.sleep(2)
        print(f"{name} leaving critical section")
    finally:
        semaphore.release()  # correct release

threads = []
for i in range(2):
    t = Thread(target=worker, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# ❌ Intentional extra release (no matching acquire)
print("\nTrying extra release...")
try:
    semaphore.release()  # This will cause error
except ValueError as e:
    print("Error:", e)