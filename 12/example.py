"""
This program demonstrates how to use threading.excepthook
to handle exceptions raised inside threads.

- Two threads are created:
  1. display() → raises an error intentionally
  2. hello() → runs normally

- A custom exception hook (custom_hook) is defined and assigned
  to threading.excepthook.

- When an uncaught exception occurs in a thread, the custom hook
  is called and prints details about the error.
"""

import threading
import time


def custom_hook(args):
    """Custom handler for uncaught thread exceptions."""
    print(f"Exception in thread {threading.current_thread().name}")
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])


def display():
    """Function that raises an error (string + int concatenation)."""
    for _ in range(5):
        time.sleep(3)
        print(f"Hello" + 100)  # Error due to concatenation


def hello():
    """Function that prints messages normally."""
    for _ in range(5):
        time.sleep(2)
        print("Hi....")


t1 = threading.Thread(target=display)
t2 = threading.Thread(target=hello)

threading.excepthook = custom_hook

t1.start()
t2.start()