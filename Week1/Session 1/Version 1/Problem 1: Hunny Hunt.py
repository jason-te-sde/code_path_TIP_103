"""
Write a function linear_search() to help Winnie the Pooh locate his lost items. The function accepts a list items and a target value as parameters. The function should return the first index of target in items, and -1 if target is not in items. Do not use any built-in functions.

def linear_search(items, target):
	pass
Example Usage:

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
linear_search(items, target)

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
linear_search(items, target)
Example Output:

3
-1
"""


def linear_search(items, target):

    for i in range(len(items)):
        if items[i] == target:
            return i
    
    return -1

if __name__ == "__main__":
    items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
    target = 'hunny'
    print(linear_search(items, target))

    items = ['bed', 'blue jacket', 'red shirt', 'hunny']
    target = 'red balloon'
    print(linear_search(items, target))

    # Additional edge cases
    items = ['hunny', 'bed', 'blue jacket']
    target = 'hunny'
    print(f"Target at start: {linear_search(items, target)}")  # Should be 0

    items = ['bed', 'blue jacket', 'hunny']
    target = 'hunny'
    print(f"Target at end: {linear_search(items, target)}")  # Should be 2

    items = []
    target = 'hunny'
    print(f"Empty list: {linear_search(items, target)}")  # Should be -1

    items = ['hunny']
    target = 'hunny'
    print(f"Single element match: {linear_search(items, target)}")  # Should be 0

    items = ['bed']
    target = 'hunny'
    print(f"Single element no match: {linear_search(items, target)}")  # Should be -1

    items = ['hunny', 'bed', 'hunny', 'blue jacket']
    target = 'hunny'
    print(f"Duplicates - return first: {linear_search(items, target)}")  # Should be 0
