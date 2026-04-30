"""
This script shows how to create and run a thread in Python.

Steps:
1. Define a class with a method that prints a message multiple times.
2. Create an object of the class.
3. Create a thread and pass the class method as the target function.
4. Start the thread to run the method in parallel.
"""

from threading import Thread

class Hello:
    def display(self, n: int):
        for i in range(n):
            print("Hello from class")


hello = Hello()

t1 = Thread(target=hello.display, args=(10,))

t1.start()