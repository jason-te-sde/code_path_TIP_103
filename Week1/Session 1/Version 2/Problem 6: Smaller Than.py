"""
Write a function smaller_than_current that accepts a list of integers nums and, for each element in the list nums[i], determines the number of other elements in the array that are smaller than it. More formally, for each nums[i] count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer as a list.

def smaller_than_current(nums):
	pass
Example Usage:

nums = [8, 1, 2, 2, 3]
smaller_than_current(nums)

nums = [6, 5, 4, 8]
smaller_than_current(nums)

nums = [7, 7, 7, 7]
smaller_than_current(nums)
Example Output:

[4, 0, 1, 1, 3]
[2, 1, 0, 3]
[0, 0, 0, 0]

"""

def smaller_than_current(nums):
    sorted_nums = sorted(nums)
    num_to_count = {}
    
    for i, num in enumerate(sorted_nums):
        if num not in num_to_count:
            num_to_count[num] = i
    
    return [num_to_count[num] for num in nums]

nums = [8, 1, 2, 2, 3]
print(smaller_than_current(nums))

nums = [6, 5, 4, 8]
print(smaller_than_current(nums))

nums = [7, 7, 7, 7]
print(smaller_than_current(nums))