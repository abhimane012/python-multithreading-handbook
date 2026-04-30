"""
Demonstrates threading.Timer for delayed execution.

- A timer runs a function once after a fixed delay.
- Useful for notifications, reminders, or scheduled tasks.
"""

from threading import Timer
import time


def show_notification(message):
    """Prints a delayed notification message."""
    print(f"\n[NOTIFICATION] {message}")
    print(f"[TIME] {time.strftime('%H:%M:%S')}")


def run_demo():
    print(f"[MAIN] Started at {time.strftime('%H:%M:%S')}")

    # Schedule a task to run after 5 seconds
    notification_timer = Timer(
        5.0,
        show_notification,
        args=("Hello! This is a delayed message.",)
    )

    print("[MAIN] Timer scheduled (5 seconds delay)")
    notification_timer.start()

    # Simulate main thread doing work
    for step in range(3):
        print(f"[MAIN] Working... step {step + 1}")
        time.sleep(1)

    print("[MAIN] Main thread finished")


if __name__ == "__main__":
    run_demo()