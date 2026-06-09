"""
Given an integer array nums, write a function sort_by_parity() that moves all the even integers to the beginning of the array, followed by all the odd integers.

Return any array that satisfies this condition.

def sort_by_parity(nums):
    pass
Example Usage

nums = [3, 1, 2, 4]
sort_by_parity(nums)

nums = [0]
sort_by_parity(nums)
Example Output:

[2, 4, 3, 1]
[0]
"""
def sort_by_parity(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        while left < right and nums[left] % 2 == 0:
            left += 1
        while left < right and nums[right] % 2 == 1:
            right -= 1
        
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    
    return nums 


nums = [3, 1, 2, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))
