## Exceptions in Multithreading (Python)

### Basic Question

- What happens if an exception occurs in one thread?
- Does it affect other threads?

---

### Key Idea

- An exception in one thread **does NOT stop other threads**
- Each thread handles its own exceptions independently

---

## How Exceptions Work in Threads

When an exception occurs inside a thread:

- Python internally calls:
```python
threading.excepthook()
```

- It receives a single argument:
- A **named tuple** containing details about the exception

---

### This Named Tuple Contains:

1. **Exception Type (Class)**
 - Example: `ValueError`, `ZeroDivisionError`

2. **Exception Instance (Value)**
 - The actual error message

3. **Traceback Object**
 - Shows where the error occurred

4. **Thread Object**
 - The thread in which the exception happened

---

## Exception Flow

### For Main Thread

- Exceptions are handled by:
```python
sys.excepthook
```

---

### For Child Threads (Created Threads)

- Flow of exception handling:


thread → threading.excepthook() → sys.excepthook


- First handled by `threading.excepthook()`
- If not handled, passed to `sys.excepthook`

---

## Important Points

- Exception in one thread:
  - ❌ Does NOT crash the entire program (by default)
  - ❌ Does NOT stop other threads
  - ✅ Only affects that specific thread

- If you want custom handling:
  - Override `threading.excepthook()`

---

## Simple Understanding

- Each thread = independent worker  
- If one fails → others continue working  

---

## Key Takeaway

- Exceptions in threads are **isolated**
- Python provides hooks (`threading.excepthook`) to handle them
- Always handle exceptions properly in threads to avoid silent failures