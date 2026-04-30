## Thread Communication using Event (Python)

### What is an Event?

- An **Event** is used for communication between threads.
- It helps one thread **signal** another thread to continue execution.
- It internally maintains a **flag**:
  - Default value → `False`

---

### How It Works

- One thread **waits** for the event (flag = False)
- Another thread **sets** the event (flag = True)
- When the flag becomes True → waiting thread **wakes up and continues**

---

### In Simple Terms

- One thread says: *"I will wait until you give me a signal"*  
- Another thread says: *"Okay, now you can continue"*  

---

### Important Note

- Typically used for **simple communication**
- Works best for **one thread signaling another thread**
- Not ideal for complex multi-thread coordination

---

## Steps to Use Event

### Step 1: Create Event Object

```python
from threading import Event
event = Event()
```


---

### Step 2: Create Threads

- Create two threads:
  - One will **wait**
  - One will **send signal**

---

### Step 3: Make One Thread Wait

```python
event.wait()
```


- This thread will pause until the flag becomes `True`

---

### Step 4: Send Signal from Other Thread

```python
event.set()
```

- This sets flag to `True`
- All waiting threads are awakened

---

## Event Methods

### 1. `set()`

- Sets internal flag to `True`
- Wakes up all waiting threads

---

### 2. `clear()` (correct method name, not reset)

- Resets flag to `False`
- Threads calling `wait()` will block again

---

### 3. `is_set()`

- Returns `True` if flag is set

```python
if event.is_set():
# do something
```


---

### 4. `wait(timeout=-1)`

- Makes thread wait until flag becomes `True`

```
event.wait(timeout)
```


- `timeout` (optional):
  - Maximum time to wait
  - If time expires → thread continues anyway

---

## Important Points

- Default state → **False (no signal)**
- `set()` → signal given → threads continue
- `clear()` → reset → threads will wait again

---

## Simple Flow

- Thread A → waits  
- Thread B → sets event  
- Thread A → resumes  

---

## Key Takeaway

- Event is used for **simple signaling between threads**
- Useful when one thread must **wait for another to complete something**