## RLock (Reentrant Lock) in Python

### What is RLock?

- **RLock (Reentrant Lock)** is a special type of lock in Python.
- It allows the **same thread to acquire the lock multiple times**.
- It is a **modified version of a normal Lock**.

---

### Why do we need RLock?

- With a normal **Lock**:
  - If a thread tries to acquire the same lock again → it gets **blocked (deadlock)**

- With **RLock**:
  - The same thread can acquire the lock multiple times safely
  - It will not get blocked

---

### In Simple Terms

- **Lock** → one entry only  
- **RLock** → same thread can re-enter multiple times  

---

### How RLock Works

- RLock internally keeps track of:
  1. **Which thread currently holds the lock**
  2. **How many times the lock has been acquired (count)**

- Each time the same thread calls `acquire()`:
  - The **count increases**

- Each time `release()` is called:
  - The **count decreases**

- The lock is fully released only when:
  - **count becomes 0**
  - Then other threads can acquire the lock

---

### Steps to Use RLock

#### Step 1: Create RLock

```python
from threading import RLock
my_lock = RLock()
```


---

#### Step 2: Acquire Lock

```python
my_lock.acquire()
```

- Same thread can call this multiple times
- RLock tracks the thread and increases count

---

#### Step 3: Release Lock

```python
my_lock.release()
```

- Must be called the **same number of times** as `acquire()`
- Lock is released only when count becomes 0

---

### Important Points

- RLock knows:
  - **Which thread is holding the lock**
  - **How many times it has been acquired**
- Other threads must still **wait** until the lock is fully released
- Improper release (less or more calls) can cause issues

---

### When to Use RLock?

- When your code has:
  - **Nested function calls**
  - **Recursive functions**
  - Same thread needs to acquire the lock multiple times

---

### Key Difference: Lock vs RLock

| Feature        | Lock            | RLock                     |
|----------------|------------------|----------------------------|
| Multiple acquire (same thread) | ❌ Not allowed | ✅ Allowed |
| Tracks owner thread | ❌ No | ✅ Yes |
| Tracks acquire count | ❌ No | ✅ Yes |
| Risk of self-deadlock | High | Low |

---

### Key Takeaway

- Use **Lock** for simple cases  
- Use **RLock** when the same thread needs to acquire the lock multiple times  
- RLock internally tracks **thread ownership + count**, making it safer for complex scenarios