## Thread Synchronization Techniques (Detailed)

When multiple threads access shared data, problems like race conditions can occur.  
To avoid this, we use synchronization techniques to control how threads access critical sections.

---

## 1. Locks (Mutex)

### What it is:
- A lock allows **only one thread at a time** to access a critical section.

### How it works:
- A thread must **acquire the lock** before entering the critical section.
- After finishing, it **releases the lock**.
- Other threads must wait until the lock is released.

### In simple terms:
- Like a **room with a key** → only one person can enter at a time.

### When to use:
- When only one thread should modify shared data.

### Problem it solves:
- Prevents race conditions by ensuring exclusive access.

---

## 2. RLock (Reentrant Lock)

### What it is:
- A special type of lock that allows the **same thread to acquire it multiple times**.

### Why needed:
- In some cases, a thread may enter a locked section and call another function
  that also tries to acquire the same lock.

### How it works:
- The same thread can lock it again without getting blocked.
- It must release the lock the same number of times it acquired it.

### In simple terms:
- Like a **person holding a key who can re-enter the same room multiple times**.

### When to use:
- When your code has **nested locking** or recursive calls.

### Problem it solves:
- Avoids deadlocks caused by the same thread trying to re-acquire a lock.

---

## 3. Semaphores

### What it is:
- A semaphore allows **a limited number of threads** to access a resource at the same time.

### How it works:
- It maintains a counter.
- Each thread decreases the counter when entering.
- When the counter reaches 0 → no more threads can enter.
- Threads must wait until others leave (counter increases).

### In simple terms:
- Like a **parking lot with limited spaces**.
  - If spaces are available → cars can enter
  - If full → cars must wait

### Types:
- **Binary Semaphore** → works like a lock (only 1 thread)
- **Counting Semaphore** → allows multiple threads

### When to use:
- When a resource can be safely used by **multiple threads, but with a limit**
  (e.g., database connections, worker pools)

### Problem it solves:
- Controls load and prevents resource exhaustion.

---

## Final Comparison

| Technique   | Threads Allowed | Special Feature                     | Use Case                          |
|------------|----------------|------------------------------------|----------------------------------|
| Lock       | 1              | Simple mutual exclusion            | Protect shared variable          |
| RLock      | 1              | Same thread can lock multiple times| Nested or recursive locking      |
| Semaphore  | Limited (n)    | Allows controlled parallel access  | Resource pools (DB, connections) |

---

## Key Takeaway

- **Lock** → Only one thread at a time  
- **RLock** → Same thread can re-enter safely  
- **Semaphore** → Limited number of threads allowed  

All of these help ensure **safe and predictable multi-threaded programs**.