## Need for RLock (Reentrant Lock)

### Problem with Normal Lock

- A normal `Lock` allows only **one acquire at a time**
- If the **same thread tries to acquire the lock again**, it gets **blocked**
- This leads to a **deadlock**

---

### Example Situation

- A function acquires a lock
- Inside that function, it calls another function
- The second function also tries to acquire the same lock

👉 With normal `Lock`:
- The same thread waits for itself → **deadlock**

---

### Why RLock is Needed

- **RLock allows the same thread to acquire the lock multiple times**
- It prevents self-deadlock
- Useful when working with:
  - Nested function calls
  - Recursive functions
  - Complex code where the same lock is reused

---

### How RLock Solves the Problem

- It keeps track of:
  - **Which thread owns the lock**
  - **How many times it has been acquired**

- The lock is released only when:
  - `release()` is called the same number of times as `acquire()`

---

### Simple Understanding

- **Lock** → one entry only → may cause deadlock  
- **RLock** → same thread can re-enter safely  

---

### Key Takeaway

- Use **RLock** when:
  - The same thread may need to lock multiple times
- Use **Lock** for simple, single-level locking