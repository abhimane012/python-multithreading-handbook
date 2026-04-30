## Thread Names in Python

- Every thread has a name.
- Default naming format: `Thread-1`, `Thread-2`, ..., `Thread-n`
  - First thread → `Thread-1`
  - Second thread → `Thread-2`
- The thread name is stored in the `name` attribute of the thread object.
- The main thread is named `MainThread`.

### Example

```python
from threading import Thread, current_thread

def show_thread_name():
    print(f"Current thread: {current_thread().name}")

# Main thread
print(f"Main thread: {current_thread().name}")

# Creating new threads
t1 = Thread(target=show_thread_name)
t2 = Thread(target=show_thread_name)

t1.start()
t2.start()
```
