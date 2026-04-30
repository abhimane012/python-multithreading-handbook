## Race Condition

- A **race condition** is a common bug in concurrent programming.
- It happens when multiple threads try to access and modify the same data at the same time.

---

## Example

1. `var = value`
2. Thread t1 (adder) → adds something to `var`
3. Thread t2 (subtractor) → subtracts something from `var`

---

## What happens internally?

When a thread updates a variable, it usually performs these steps:

- Read the current value of the variable
- Calculate the new value
- Write the new value back

---

## Problem

- If two or more threads do these steps at the same time:
  - They may read the same old value
  - Their updates can overwrite each other
- This leads to **incorrect or unpredictable results**

---

## Key Points

- Race condition occurs due to **concurrent access to shared resources**
- Results become **unreliable**
- Common in **multi-threading and multi-processing**