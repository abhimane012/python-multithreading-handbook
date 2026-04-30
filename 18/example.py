"""
This program demonstrates a daemon thread.

- The background thread runs continuously.
- It is marked as a daemon thread, so it stops automatically
  when the main thread finishes.
"""

from threading import Thread
import time


def run_background_service():
    """Simulates a background service running in an infinite loop."""
    while True:
        print("Background service running...")
        time.sleep(1)


# Create daemon thread (runs in background)
background_thread = Thread(
    target=run_background_service,
    daemon=True
)

background_thread.start()

# Main thread work
print("Main thread is running...")
time.sleep(5)

print("Main thread finished")