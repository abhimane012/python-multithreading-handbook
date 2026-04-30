## Creating Threads in Python

There are 2 simple ways to create threads:

### 1. Using the `Thread` class (from `threading` module)
You directly create a thread by passing a function to the `Thread` class.

### 2. By extending the `Thread` class
You create your own class by inheriting from `threading.Thread` and override the `run()` method.