## Thread Identifiers in Python

- Each thread has a unique identifier (ID) within a Python process.
- It is assigned by the Python interpreter.
- It is a read-only positive integer.
- The ID is assigned after the thread starts.
- This ID is stored in the `ident` attribute.

### Native Thread ID

- Each thread also has an ID given by the operating system.
- It is available using the `native_id` attribute.
- It is assigned after the thread starts.
- In most cases, `ident` and `native_id` are the same.

---

## Process ID (PID)

- PID is the identifier of a process (your program).
- You can get it using the `os` module.

---

### Example

```python
from threading import Thread, current_thread
import os

def show_ids():
    t = current_thread()
    print(f"Thread name: {t.name}")
    print(f"Thread ident: {t.ident}")
    print(f"Thread native_id: {t.native_id}")
    print(f"Process ID (PID): {os.getpid()}")

t1 = Thread(target=show_ids)

t1.start()
```