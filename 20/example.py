"""
This program demonstrates the use of threading.Barrier.

- A Barrier makes threads wait until a fixed number of them
  reach a common point.
- Once all threads arrive, they are released together.
"""

from threading import Thread, Barrier
import time


# Barrier for 3 threads (synchronization point)
sync_point = Barrier(3)


def worker_task(thread_name):
    """Simulates work before and after a synchronization point."""
    print(f"{thread_name}: working before barrier")
    time.sleep(2)

    print(f"{thread_name}: waiting at barrier")
    sync_point.wait()  # all threads must reach here

    print(f"{thread_name}: passed barrier and continuing work")


def run_demo():
    """Creates and runs multiple threads demonstrating barrier usage."""
    threads = []

    for i in range(3):
        thread = Thread(target=worker_task, args=(f"Thread-{i}",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    run_demo()