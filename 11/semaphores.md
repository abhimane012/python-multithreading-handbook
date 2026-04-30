## Semaphores in Python

### What is a Semaphore?

- In **Lock** and **RLock**, only **one thread** can access the critical section at a time.
- But sometimes, we want **multiple threads (limited number)** to run at the same time.

👉 This is where **Semaphore** is used.

---

### Why Use Semaphore?

- A **Semaphore** is used to **limit access to shared resources**
- It allows **a fixed number of threads** to enter the critical section at once

### In Simple Terms

- Think of a **parking lot with limited slots**:
  - If slots are available → cars (threads) can enter
  - If full → cars must wait

---

### How Semaphore Works

- It maintains a **counter (limit)**
- Each `acquire()`:
  - Decreases the counter
- Each `release()`:
  - Increases the counter

- When counter = 0:
  - No more threads can enter
  - Other threads must wait

---

## Steps to Use Semaphore

### Step 1: Create a Semaphore

```python
from threading import Semaphore
s = Semaphore(n)
```

- `n` = number of threads allowed at the same time

---

### Step 2: Acquire

```python
s.acquire()
```

- Decreases the counter
- If limit reached → thread waits

---

### Step 3: Release

```python
s.release()
```

- Increases the counter
- Allows waiting threads to proceed

---

## Important Points

- Semaphore allows **multiple threads**, not just one
- So it **does NOT fully prevent race conditions**
- It only **controls how many threads can access at once**

---

## When Can It Avoid Race Condition?

- If you use:
```python
Semaphore(1)
```

- Then it behaves like a **Lock (Mutex)**
- Only one thread is allowed → race condition avoided

---

## Internal Behavior

- Semaphore internally uses **locking mechanisms (like RLock)**
- It manages thread access safely

---

## Common Problem

- You must call `release()` **same number of times as `acquire()`**
- If not:
- Threads may get stuck
- Resource access becomes incorrect

---

## Solution: BoundedSemaphore

- Python provides **BoundedSemaphore**
- It prevents releasing more times than acquired

### Why use it?

- Avoids mistakes in `acquire()` / `release()` count
- Safer for real-world applications

---

## Key Difference

| Feature            | Lock / RLock | Semaphore        |
|--------------------|-------------|------------------|
| Threads allowed     | 1           | Limited (n)      |
| Prevent race condition | Yes      | Not always       |
| Use case           | Critical section | Resource limiting |

---

## Key Takeaway

- **Lock / RLock** → only one thread  
- **Semaphore** → limited number of threads  
- Use Semaphore when you want **controlled parallelism**, not strict exclusivity 