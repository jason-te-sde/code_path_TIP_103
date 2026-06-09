"""
Given an array nums with n integers, write a function non_decreasing() that checks if nums could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

def non_decreasing(nums):
	pass
Example Usage:

nums = [4, 2, 3]
non_decreasing(nums)

nums = [4, 2, 1]
non_decreasing(nums)
Example Output:

True
False
"""
# def non_decreasing(nums):

#     n = len(nums)
#     left, right = 0, n - 1
    
#     while left < n - 1 and nums[left] <= nums[left + 1]:
#         left += 1
    
#     while right > 0 and nums[right] >= nums[right - 1]:
#         right -= 1
    
#     if left >= right:
#         return True
#     elif right - left > 1:
#         return False
#     else:
#         if left == 0 or nums[left - 1] <= nums[right]:
#             return True
#         if right == n - 1 or nums[right + 1] >= nums[left]:
#             return True
    
#     return False
def non_decreasing(nums):
    changed = False
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            if changed:
                return False
            changed = True
            if i >= 2 and nums[i] < nums[i - 2]:
                nums[i] = nums[i - 1]
            else:
                nums[i - 1] = nums[i]
    return True

# Test cases - covers all edge cases
test_cases = [
    ([], True),
    ([1], True),
    ([2, 1], True),
    ([1, 2, 3], True),
    ([1, 4, 2, 3], True),
    ([2, 3, 1, 4], True),
    ([1, 2, 3, 0], True),
    ([3, 4, 2, 3], False),
    ([4, 2, 1], False),
]

for nums, expected in test_cases:
    result = non_decreasing(nums)
    status = "✓" if result == expected else "✗"
    print(f"{status} {nums} → {result}")

