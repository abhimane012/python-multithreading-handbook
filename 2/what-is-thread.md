## Real Life Example of Threads

Imagine a scenario:

- **100 Students** -> 1 batch -> 1 hour (1 hall)
- **100 Students** -> 4 batches -> 4 hours

To optimize time, **3 teachers** are hired. Each teacher:
- Teaches for **1 hour**.
- Uses **4 halls** simultaneously.
- Conducts **parallel teaching**.

In this analogy:
- Each **teacher** represents a **thread**.
- Each **hall** represents a **memory space**.

By using threads, tasks are executed concurrently, reducing the overall time required.

---

## What is a Thread?

A thread is an **operating system object** that executes instructions or a program. It is a **separate flow of execution** within a program.

### Key Characteristics:
- A thread represents a **task** or **sub-program**.
- Threads run **independently**, but share the same memory space.

### Example:

Imagine you are baking cookies and boiling water at the same time:
- Baking cookies is one **thread**.
- Boiling water is another **thread**.
- Both tasks are independent but share the same kitchen (memory space).

Threads allow you to perform multiple tasks simultaneously, improving efficiency and performance.
