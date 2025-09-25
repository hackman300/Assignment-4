# Problem 1: Duplicate Tracker
def has_duplicates(product_ids):
    data = set()
    for id in product_ids:
        if id in data:
            return True
        data.add(id)
    return False
test_1 = [1,2,2,3,4]
test_2 = ["a", "b", "c", "c"]
print(has_duplicates(test_1))
print(has_duplicates(test_2))
print("\n")
'''
A set is best because it is efficient in finding duplicates in a list of elements. The operations that are 
performed are a for loop to iterate through the entire list, the an if statement to see if there are any duplicates.
'''


# Problem 2: Order Manager
from collections import deque

class TaskQueue:
    def __init__(self):
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: {task}")

    def remove_oldest_task(self):
        if self.tasks:
            task = self.tasks.popleft()
            print(f"Removed oldest task: {task}")
            return task
        print("Nothing to queue.")
        return None

queue = TaskQueue()
queue.add_task("Test 1")
queue.add_task("Test 2")
queue.remove_oldest_task()
queue.remove_oldest_task()
queue.remove_oldest_task()
print("\n")
'''
A deque is best for first in first out operations like adding to the 
end and removing from the front. For software like restaurant managers 
that need to manage reservations, this is where queues come into play.
'''


# Problem 3: Unique Value Counter
class UniqueTracker:
    def __init__(self):
        self.unique_values = set()

    def add(self, value):
        self.unique_values.add(value)
        print(f"Added value: {value}, Unique values: {self.unique_values}")

    def unique_count(self):
        count = len(self.unique_values)
        print(f"Current unique count: {count}")
        return count

tracker = UniqueTracker()
tracker.add(1)
tracker.add(2)
tracker.add(1)
tracker.add(3)
tracker.unique_count()
'''
A set automatically handles uniqueness, making sure duplicates are 
ignored without extra checks. The len() operation is in a function called unique_count(), 
which is used to handle data where we only care about distinct counts.
'''
