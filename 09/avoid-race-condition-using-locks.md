## Avoid Race Condition using Locks (Multithreading)

### Race Condition
- A **race condition** is a bug in concurrent programming.
- It happens when **two or more threads try to update the same variable at the same time**.
- This leads to **incorrect or unpredictable results**.
- It occurs due to **concurrent access to shared resources**.

---

### Thread Synchronization
- Thread synchronization is a mechanism to **control how threads access shared data**.
- It ensures that **only one thread executes the critical section at a time**.

#### Critical Section:
- The part of code where shared data is read or modified.

---

### Locks in Python

- Python provides a **Lock** class in the `threading` module.
- Locks help **prevent multiple threads from accessing shared data at the same time**.

---

### Lock States

- **Locked**
  - One thread has acquired the lock
  - Other threads must wait

- **Unlocked**
  - No thread is using the lock
  - Any thread can acquire it

---

### Steps to Use Lock

#### Step 1: Create a Lock

```python
from threading import *
my_lock = Lock()
```

#### Step 2: Acquire the Lock

my_lock.acquire()

- Makes the lock **locked**
- Other threads will wait

#### Step 3: Release the Lock
```python
my_lock.release()
```

- Makes the lock **available**
- Other threads can proceed

---

### `acquire()` Method

- Used to **lock the critical section**
- Only one thread can enter at a time

#### Syntax
```python
lock_object.acquire(blocking=True, timeout=-1)
```

- `blocking=True` → thread waits until lock is free  
- `timeout` → maximum wait time (`-1` means wait forever)

---

### Simple Understanding

- Without lock → multiple threads update data → wrong results  
- With lock → one thread at a time → correct results  

---

### Key Takeaway

- Locks are the **basic and most important way to avoid race conditions**
- Always use locks when working with **shared data in multithreading**