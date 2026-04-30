"""
This program demonstrates the use of threading.Event
for communication between threads.

- The 'start' thread simulates a long-running task (30 seconds).
- After finishing, it signals completion using event.set().

- The 'stop' thread waits for the event using event.wait().
- Once the event is set, it proceeds and prints a message.

- Event is used here to synchronize threads (one waits until another finishes).
"""

from threading import Thread, Event
import time

event = Event()


def start():
    """Simulates starting a program and signals completion."""
    print("Program is started")
    time.sleep(30)
    event.set()


def stop():
    """Waits for the event signal before proceeding."""
    event.wait()
    if event.is_set():
        print("Program is destroying...")


t1 = Thread(target=start)
t2 = Thread(target=stop)

t1.start()
t2.start()