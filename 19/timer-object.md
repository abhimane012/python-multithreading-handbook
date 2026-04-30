## Timer Object in Python (threading)

### What is a Timer Object?

- A **Timer** is a special type of thread in Python.
- It is used to **run a function after a fixed delay**.
- It comes from the `threading` module.

---

## How does a Timer work?

- A Timer does not run immediately.
- Instead, it waits for a **specified amount of time**.
- After the delay, it automatically executes the given function.

---

## Simple Understanding

- Think of it like an **alarm clock**
  - You set a time delay
  - After that time → it rings (runs the function)

---

## Key Features

- Runs only **once** after the delay
- Runs in a **separate thread**
- Does not block the main program
- Can be canceled before execution

---

## How Timer Object Works

1. You define a function (task to run later)
2. You create a Timer with:
   - delay time (seconds)
   - function to execute
3. You start the Timer
4. After the delay → function runs automatically

---

## Important Methods

### 1. `start()`
- Starts the timer countdown
- After delay → function executes

---

### 2. `cancel()`
- Stops the timer before it executes
- Works only if timer has not finished waiting

---

## Simple Flow

- Create Timer → Start → Wait → Execute Function

---

## Example Use Cases

- Delayed notifications
- Auto-save after delay
- Retry logic with delay
- Scheduled tasks (simple scheduling)

---

## Key Takeaway

- Timer = **delayed execution thread**
- It runs a function **after a fixed time**
- Useful for simple scheduling tasks in Python