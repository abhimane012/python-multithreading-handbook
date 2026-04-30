"""
This script demonstrates how the `join()` method controls the execution order of threads.

What happens step by step:

1. Two functions are defined:
   - `hello()` prints "Hello" 10 times with a delay.
   - `hi()` prints "Hi" 10 times with a delay.

2. Two threads are created:
   - t1 runs the `hello()` function.
   - t2 runs the `hi()` function.

3. Execution flow:
   - t1 is started first.
   - `t1.join()` makes the main thread wait until t1 finishes.
     → So "Hello" prints completely first.

   - Then t2 is started.
   - `t2.join()` again makes the main thread wait until t2 finishes.
     → So "Hi" prints only after "Hello" is done.

4. Finally, the main thread runs its own loop and prints "Main Thread".

Key Idea:
- Because of `join()`, threads run one after another (sequentially),
  instead of running in parallel.
- This ensures a strict execution order:
  Hello → Hi → Main Thread
"""

from threading import Thread
from time import sleep

def hello():
    for _ in range(10):
        sleep(1)
        print("Hello")

def hi():
    for _ in range(10):
        sleep(1)
        print("Hi")

t1 = Thread(target=hello)
t2 = Thread(target=hi)

t1.start()
t1.join()

t2.start()
t2.join()

for _ in range(10):
    sleep(1)
    print("Main Thread")