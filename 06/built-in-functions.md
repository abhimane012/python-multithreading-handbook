## Built-in Functions for Threading in Python

### 1. `is_alive()`
- Checks if a thread is currently running.
- Returns `True` or `False`.

### 2. `main_thread()`
- Returns the main thread object.

### 3. `active_count()`
- Returns the number of currently running threads.

### 4. `enumerate()`
- Returns a list of all active thread objects.

### 5. `get_native_id()`
- Returns the native (OS-level) ID of the **current thread**.
- Available since Python 3.8+

---

## Example

```python
import threading
import time

def task():
    print("Thread is running")
    time.sleep(1)

t1 = threading.Thread(target=task)

print("Before start:", t1.is_alive())  # False

t1.start()

print("After start:", t1.is_alive())   # True

print("Main thread:", threading.main_thread().name)

print("Active threads:", threading.active_count())

print("All threads:", threading.enumerate())

print("Current thread native id:", threading.get_native_id())

t1.join()

print("After completion:", t1.is_alive())  # False
```