Thread communciation using Condition

Need of condition object
    - to communicate with multiple threads
    - Event object - communication between two threads

Producer - Consumer Problem

Step 1
 - Create condition object
 - Syntax -
    from threading import Condition
    condition = Condition()

Methods

1. acquire()
    - This method is used to acquire the lock

2. release()
    - this method is used to relese the lock

3. wait()
    - this method is used to block the thread
    - thread will wait unitll it gets signal from t1 thread

4. notify()
    - wakeup one thread

5. notify_all()
    - wakeup multiple thread


These methods must only be called when the calling thread has acquired the lock