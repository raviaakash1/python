'''

nums = [-2 1 -3 4 -1 2 1 -5 4]

max = 6 [4 -1 2 1]

 Kadane's Algorithm


'''

from typing import List

def max_subarray_sum(nums: List[int]) -> int:
    max_current = max_global = nums[0]
    
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        max_global = max(max_global, max_current)
    
    return max_global

# Example usage
nums = [int(i) for i in input("Enter an array of numbers >> ").split()]
print(f"Maximum subarray sum is {max_subarray_sum(nums)}")