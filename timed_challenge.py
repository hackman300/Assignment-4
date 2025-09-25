# Selected question from timed_challenge.txt:
# 3. Remove Duplicates (Keep Order)
def remove_duplicates_keep_order(items):
    data = set()
    result = []
    for item in items:
        if item not in data:
            data.add(item)
            result.append(item)
    return result

print(remove_duplicates_keep_order(["apple", "banana", "apple", "kiwi", "banana"]))
print(remove_duplicates_keep_order([1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9]))
print(remove_duplicates_keep_order(["a", "b", "b", "c", "c", "d" ]))
print(remove_duplicates_keep_order([]))


'''
For the "Remove Duplicates" problem, I chose to use a set to find the data of items already found in the list. 
The variable named "data" is used as a lookup table to check if an item has already been discovered. This assures that 
duplicates are skipped without duplicative comparisons. Meanwhile, the list "result" is appended only with unique data in the order they first appear. 

The time limit challenge was more about how to code a straightforward program rather than a complex one. With a 
30-minute window, coding simple implementations is the way to go when you have multiple test cases that need to be tested. 
The main functions that needed to be implemented were to iterate through a list, delete data that shows up more than once, and keep the same order.

Some of the trade-offs included not handling errors properly. Not checking if the input is correct allows for the program to break, 
possibly messing up the main system in the process. Also, using a list comprehension could have been more effective; I stuck with a 
simple for-loop for simple usage because of the time limit. Overall, this challenge was a balance of both speed and correctness.
'''
