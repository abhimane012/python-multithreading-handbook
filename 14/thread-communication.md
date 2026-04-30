## Thread Communication in Python

### What is Thread Communication?

- In concurrent programming, multiple threads run at the same time.
- Sometimes, threads need to **coordinate with each other**.
- This coordination is called **thread communication**.

---

### Why Do Threads Need Communication?

- One thread may depend on the result of another thread
- Threads may need to:
  - Wait for a signal
  - Share data safely
  - Execute in a specific order

👉 Without communication:
- Threads may run in the wrong order
- Can lead to incorrect results or wasted work

---

### How Do Threads Communicate?

- Threads communicate using **signals or shared mechanisms**
- Python provides built-in tools for this

---

## Ways Threads Communicate

### 1. Using Event Object

- Used to **send signals between threads**
- One thread sets the event → other threads can proceed

#### Simple Idea:
- Like a **green signal**
  - Event not set → wait
  - Event set → continue

---

### 2. Using Condition Object

- Used for **more complex communication**
- Allows threads to:
  - Wait for a condition
  - Notify other threads when something changes

#### Simple Idea:
- Like a **waiting room**
  - Threads wait until a condition is met
  - One thread notifies others

---

### 3. Using Queue Module

- Used to **share data safely between threads**
- Built-in synchronization (no need for locks)

#### Simple Idea:
- Like a **line (queue)**:
  - One thread puts data
  - Another thread takes data

---

## Key Differences

| Method     | Purpose                  | Use Case                          |
|------------|--------------------------|----------------------------------|
| Event      | Simple signaling         | Start/stop threads               |
| Condition  | Complex coordination     | Wait & notify multiple threads   |
| Queue      | Data sharing             | Producer-consumer pattern        |

---

## Simple Understanding

- **Event** → "Go / Stop" signal  
- **Condition** → "Wait until something happens"  
- **Queue** → "Pass data safely"  

---

## Key Takeaway

- Thread communication is important for **coordination**
- It helps threads work **together correctly**
- Python provides simple tools to handle this safely