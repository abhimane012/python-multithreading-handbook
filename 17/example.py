"""
This program demonstrates the Producer–Consumer pattern using Queue.

- Producer generates random numbers and adds them to the queue.
- Consumer retrieves and processes items from the queue.
- Queue handles thread-safe communication automatically.
"""

from threading import Thread
from queue import Queue
from time import sleep
from random import randint


def produce_items(shared_queue: Queue):
    """Continuously produces random numbers and puts them into the queue."""
    print("Producer started...")

    while True:
        item = randint(1, 100)
        sleep(0.5)

        print(f"Produced: {item}")
        shared_queue.put(item)


def consume_items(shared_queue: Queue):
    """Continuously consumes items from the queue when available."""
    print("Consumer started...")

    while True:
        item = shared_queue.get()  # blocks until item is available
        print(f"Consumed: {item}")
        sleep(1)


# Queue with max size 1 (bounded buffer)
shared_queue = Queue(maxsize=1)

# Create threads
producer_thread = Thread(target=produce_items, args=(shared_queue,))
consumer_thread = Thread(target=consume_items, args=(shared_queue,))

# Start threads
producer_thread.start()
consumer_thread.start()