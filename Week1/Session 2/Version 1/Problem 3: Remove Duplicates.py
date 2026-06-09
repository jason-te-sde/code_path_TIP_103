"""
Write a function remove_dupes() that accepts a sorted array items, and removes the duplicates in-place such that each element appears only once. Return the length of the modified array. You may not create another array; your implementation must modify the original input array items.

def remove_dupes(items):
    pass
Example Usage

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
remove_dupes(items)

items = ["extract of malt", "haycorns", "honey", "thistle"]
remove_dupes(items)
Example Output:

4
4
"""

def remove_dupes(items):
    if not items:
        return 0
    
    slow = 0
    for fast in range(1, len(items)):
        if items[fast] != items[slow]:
            slow += 1
            items[slow] = items[fast]
    
    return slow + 1

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))
            
