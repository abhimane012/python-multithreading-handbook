"""
This script demonstrates how to create a thread by extending the Thread class.

What it does:
1. Defines a Calculator class that inherits from Thread.
2. The thread runs the `run()` method automatically when `start()` is called.
3. Inside `run()`:
   - It generates two random numbers.
   - Performs addition and subtraction using class methods.
   - Adds the results to a shared variable `result`.
   - Repeats this process 10 times.
4. The main program starts the thread and waits for 2 seconds.
5. Finally, it prints the accumulated result.

Note:
- `start()` creates a new thread and internally calls `run()`.
- `time.sleep(2)` is used to give the thread time to finish execution.
- The `result` variable is updated inside the thread.
"""

from threading import Thread
from random import randint
import time

class Calculator(Thread):
    def __init__(self, result = 0):
        self.result = result
        super().__init__()

    def add(self, val1: int, val2: int):
        print(f"Performing addition")
        return val1 + val2

    def sub(self, val1: int, val2: int):
        print(f"Performing subtraction")
        return val1 + val2
    
    def run(self):
        for i in range(10):
            num1 = randint(1, 100)
            num2 = randint(1, 100)

            add_res = self.add(num1, num2)
            sub_res = self.sub(num1, num2)

            self.result += (add_res + sub_res)


calculator = Calculator()

calculator.start()

time.sleep(2)
print(f"Final result {calculator.result}")