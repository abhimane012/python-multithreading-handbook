"""
This program demonstrates thread synchronization using Condition.

- input_numbers() collects user input and signals when data is ready.
- calculate_sum() waits for data and computes the total.
- calculate_average() waits for data and computes the average.

Condition is used so that consumer threads wait until data is available.
"""

from threading import Thread, Condition

numbers = []
condition = Condition()
is_data_ready = False


def input_numbers():
    """Collect numbers from user and notify waiting threads."""
    global is_data_ready

    with condition:
        for _ in range(10):
            value = int(input("Enter a number: "))
            numbers.append(value)

        is_data_ready = True
        condition.notify_all()


def calculate_sum():
    """Wait for data and calculate total sum."""
    with condition:
        print("Sum thread waiting...")

        while not is_data_ready:
            condition.wait()

        total = sum(numbers)
        print(f"Total Sum: {total}")


def calculate_average():
    """Wait for data and calculate average."""
    with condition:
        print("Average thread waiting...")

        while not is_data_ready:
            condition.wait()

        average = sum(numbers) / len(numbers)
        print(f"Average: {average}")


# Create threads
input_thread = Thread(target=input_numbers)
sum_thread = Thread(target=calculate_sum)
avg_thread = Thread(target=calculate_average)

# Start consumer threads first (best practice)
sum_thread.start()
avg_thread.start()
input_thread.start()

# Wait for all threads to finish
input_thread.join()
sum_thread.join()
avg_thread.join()