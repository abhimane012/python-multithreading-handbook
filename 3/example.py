"""
This script demonstrates how to get information about the main thread in Python.

Steps:
1. Import the threading module.
2. Get the currently running thread (main thread).
3. Print the thread object.
4. Print the name of the thread.
5. Print the unique identifier (ID) of the thread.
"""

import threading

main_thread = threading.current_thread()

print(main_thread)        # Shows thread object details
print(main_thread.name)   # Shows thread name (usually "MainThread")
print(main_thread.ident)  # Shows unique thread ID