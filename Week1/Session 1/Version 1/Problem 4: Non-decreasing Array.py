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
def non_decreasing(nums):

    n = len(nums)
    left, right = 0, n - 1
    
    while left < n - 1 and nums[left] <= nums[left + 1]:
        left += 1
    
    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1
    
    if left >= right:
        return True
    elif right - left > 1:
        return False
    else:
        if left == 0 or nums[left - 1] <= nums[right]:
            return True
        if right == n - 1 or nums[right + 1] >= nums[left]:
            return True
    
    return False

# Test cases - covers all edge cases
test_cases = [
    ([], True),                    # Empty array
    ([1], True),                   # Single element
    ([1, 2, 3], True),             # Already sorted
    ([2, 1, 2], True),             # Conflict at start
    ([1, 3, 2], True),             # Conflict at end
    ([3, 4, 2, 3], False),         # Unfixable conflict
    ([4, 2, 1], False),            # Multiple conflicts
]

for nums, expected in test_cases:
    result = non_decreasing(nums)
    status = "✓" if result == expected else "✗"
    print(f"{status} {nums} → {result}")

