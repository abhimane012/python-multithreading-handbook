"""
This script demonstrates a basic example of multiple threads accessing shared data
without synchronization, which can lead to a race condition.

What the code does:

1. A `Ticket` class is created with a fixed number of available tickets.
2. The method `book_ticket()`:
   - Prints the current number of available tickets.
   - Checks if enough tickets are available.
   - If yes, assigns tickets to the current thread and reduces the count.
   - Otherwise, prints that tickets are not available.

3. Two threads are created:
   - Each thread tries to book 1 ticket.
   - Threads are given names ("Abhishek" and "Bhargava") for identification.

4. Both threads run at the same time:
   - Since there is no synchronization (no lock),
     both threads may read the same ticket count before updating it.
   - This can lead to incorrect results (race condition).

Key Idea:
- Multiple threads accessing and modifying shared data (`available_tickets`)
  without protection can cause unpredictable behavior.
- This example shows why synchronization (like locks) is important.
"""

from threading import Thread, current_thread

class Ticket:
    def __init__(self, tickets: int):
        self.available_tickets = tickets
    
    def book_ticket(self, ticket_count: int):
        print(f"Available Ticket Count -> {self.available_tickets}")

        if self.available_tickets >= ticket_count:
            curr_thread = current_thread()
            print(f"{ticket_count} ticket(s) allocated to {curr_thread.name}")
            self.available_tickets -= ticket_count
        else:
            print("Sorry! Tickets are not available")


ticket = Ticket(2)

t1 = Thread(target=ticket.book_ticket, args=(2,), name="Abhishek")
t2 = Thread(target=ticket.book_ticket, args=(2,), name="Bhargava")

t1.start()
t2.start()