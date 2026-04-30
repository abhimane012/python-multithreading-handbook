## What are Daemon Threads in Python?

### Types of Threads

In Python, threads are of two types:

- **Non-daemon threads (user/supporting threads)**
- **Daemon threads (background/support threads)**

---

## Real-World Example (Code Editor App)

A code editor runs multiple threads at the same time:

- Thread 1 → Main Thread  
- Thread 2 → Interactive Shell  
- Thread 3 → Editor UI  
- Thread 4 → Python Interpreter  
- Thread 5 → Text Highlighting  
- Thread 6 → Memory Management  

### Classification:

- **Non-daemon threads**
  - Thread 1 to Thread 4
- **Daemon threads**
  - Thread 5 and Thread 6

---

## Non-Daemon Threads

- These are **important application threads**
- The program **does NOT stop until all non-daemon threads finish**

### Simple Meaning:
- As long as these threads are running → program stays alive

---

## Daemon Threads

- These are **background helper threads**
- They continuously run in the background
- They support non-daemon threads

### Behavior:
- When all **non-daemon threads finish**
  → daemon threads are **automatically stopped**
  → program exits

---

## Simple Understanding

- Non-daemon → "main work threads"
- Daemon → "background support threads"

---

## Use of Daemon Threads

Daemon threads are commonly used for:

- Monitoring tasks
- Background services
- Auto-save / cleanup operations
- Logging systems
- Memory management

---

## Key Characteristics

### 1. Daemon threads run in background
- They do not block program exit

### 2. They stop automatically
- When no non-daemon threads are running

---

## Important Questions

### ❓ What decides daemon nature?

- A thread’s daemon status is decided **before starting the thread**
- It is set using a flag (`daemon=True` or `daemon=False`)

---

### ❓ Can we change daemon nature?

- ❌ No, you cannot change it after the thread has started
- You must set it **before calling `start()`**

---

### ❓ Default nature of main thread

- The **main thread is always non-daemon**
- It controls the lifecycle of the program

---

## Simple Flow

- Non-daemon threads → run main program  
- Daemon threads → support in background  
- Program ends → when non-daemon threads finish  

---

## Key Takeaway

- **Non-daemon threads** keep the program alive  
- **Daemon threads** are background helpers  
- When main work is done → daemon threads are stopped automatically  