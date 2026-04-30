## Thread Communication using Queue (Python)

### What is a Queue?

- A **Queue** is used to safely share data between threads.
- It follows **FIFO (First In First Out)**:
  - First item added → first item removed

---

### Why Use Queue?

- In multithreading, sharing data directly can cause **race conditions**
- Queue provides a **safe way to pass data between threads**

---

## Producer-Consumer Problem

- A common use case of Queue

### Roles:

- **Producer Thread**
  - Adds data to the queue

- **Consumer Thread**
  - Removes data from the queue

---

### In Simple Terms

- Producer → puts items in a box  
- Consumer → takes items from the box  

---

## Creating a Queue

- Use the `queue` module

```python
import queue
my_queue = queue.Queue(maxsize)
```

- `maxsize` (optional):
  - Maximum number of items allowed
  - If full → producer waits

---

## Queue Methods

### 1. `put(item, block=True)`

- Adds an item to the queue

```python
my_queue.put(item)
```

- If queue is full:
  - Thread waits (if `block=True`)

---

### 2. `get()`

- Removes and returns an item from the queue

```python
item = my_queue.get()
```

- If queue is empty:
  - Thread waits until item is available

---

## How It Works

1. Producer adds data using `put()`
2. Consumer removes data using `get()`
3. Queue handles synchronization internally

---

## Benefits

### ✅ Thread Safe
- No race conditions
- Safe for multiple threads

### ✅ Built-in Synchronization
- No need to manually use locks
- Queue internally manages locking

### ✅ Easy to Use
- Simple API (`put()` and `get()`)

---

## Simple Flow

- Producer → `put()` → Queue → `get()` → Consumer

---

## Key Takeaway

- Queue is the **best way to share data between threads**
- It solves the **producer-consumer problem safely**
- No need to manually handle locks