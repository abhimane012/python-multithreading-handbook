"""
This script demonstrates how to avoid race conditions in multithreading
by using a Lock for synchronization.

What the code does:

1. A `Ticket` class is created with:
   - A fixed number of available tickets
   - A lock object to control access to shared data

2. The method `book_ticket()`:
   - Acquires the lock before accessing shared data
   - Prints available tickets
   - Checks if enough tickets are available
   - If yes, allocates tickets and updates the count
   - Otherwise, shows a "not available" message
   - Releases the lock after completing the operation

3. Two threads are created:
   - Each thread tries to book 2 tickets
   - Threads are named ("Abhishek" and "Bhargava")

4. Execution behavior:
   - Only one thread can enter `book_ticket()` at a time
   - The second thread must wait until the first thread releases the lock

Key Idea:
- The lock ensures that only one thread accesses and modifies
  `available_tickets` at a time.
- This prevents race conditions and ensures correct results.

Important Note:
- Always release the lock after acquiring it.
- A better practice is to use `with lock:` (context manager)
  to automatically handle acquire and release.
"""

from threading import Thread, current_thread, Lock

class Ticket:
    def __init__(self, tickets: int, lock: Lock):
        self.available_tickets = tickets
        self.lock = lock
    
    def book_ticket(self, ticket_count: int):
        with self.lock:  # safer way (auto acquire & release)
            print(f"Available Ticket Count -> {self.available_tickets}")

            if self.available_tickets >= ticket_count:
                curr_thread = current_thread()
                print(f"{ticket_count} ticket(s) allocated to {curr_thread.name}")
                self.available_tickets -= ticket_count
            else:
                print("Sorry! Tickets are not available")


ticket = Ticket(2, Lock())

t1 = Thread(target=ticket.book_ticket, args=(2,), name="Abhishek")
t2 = Thread(target=ticket.book_ticket, args=(2,), name="Bhargava")

t1.start()
t2.start()