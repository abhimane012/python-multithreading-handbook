## Need of Threading

### Scenario 1

Imagine a calculator that performs the following operations: addition, subtraction, multiplication, and division. Each operation takes **0.01 seconds** to complete.

- For **100 calls**, the total time required would be:
    ```
    0.01 sec * 100 = 1 second
    ```

Using **multi-threading**, we can divide the workload among multiple threads:

- **Thread 1**: Handles 25 calls
- **Thread 2**: Handles 25 calls
- **Thread 3**: Handles 25 calls
- **Thread 4**: Handles 25 calls

By processing these calls in parallel, the total time reduces to approximately:
```
0.25 seconds
```

---

### Scenario 2

In a payment application, multiple users (User1, User2, ..., UserN) interact with a payment server. The server processes transactions and communicates with a database.

#### Without Threads:
If the server does not use threads, each transaction must complete before the next one begins. This causes delays for other users.

```
User1 -> Payment Server -> Database
    +--------+      +----------------------+      +----------+
    | User1  | ---> | Payment Server (Sync)| ---> | Database |
    +--------+      +----------------------+      +----------+
        (blocks until complete)

    +--------+      +----------------------+      +----------+
    | User2  | ---> | Payment Server (Sync)| ---> | Database |
    +--------+      +----------------------+      +----------+
        (waits for User1 to finish)

    +--------+      +----------------------+      +----------+
    | User3  | ---> | Payment Server (Sync)| ---> | Database |
    +--------+      +----------------------+      +----------+
        (processed after previous completes)
```

#### With Threads:
Using threads, the server can handle multiple transactions simultaneously. While one transaction is being processed, the server can start processing others.

```
+--------+      +----------------------+      +----------+
| User1  | ---> | Payment Server (T1)  | ---> | Database |
+--------+      +----------------------+      +----------+

+--------+      +----------------------+      +----------+
| User2  | ---> | Payment Server (T2)  | ---> | Database |
+--------+      +----------------------+      +----------+

+--------+      +----------------------+      +----------+
| User3  | ---> | Payment Server (T3)  | ---> | Database |
+--------+      +----------------------+      +----------+
```

#### Example:
- **Without Threads**:
    - User1's transaction takes 5 seconds.
    - User2 must wait for 5 seconds before their transaction starts.
    - Total time for 2 users: **10 seconds**.

- **With Threads**:
    - User1 and User2's transactions are processed simultaneously.
    - Total time for 2 users: **5 seconds**.

Threads improve efficiency and reduce waiting time for users.
