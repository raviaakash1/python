"""
Given an array of integers and a number , find the maximum sum of a subarray of size .
Example:

Input: nums = [2, 1, 5, 1, 3, 2], k = 3  
Output: 9  # [5, 1, 3]

"""
import math
def max_subarray_size_k(list_nums, k):

    start = 0
    end = 0
    maximum = -math.inf
    
    sum = 0
    while end < len(list_nums):
        sum += list_nums[end]
        if (end - start + 1) < k:
            end += 1
        elif end - start + 1 == k:
            maximum = max(maximum, sum)
            sum -= list_nums[start]
            start += 1
            end += 1
    return maximum



if __name__ == "__main__":
    list_size = input("Enter an array : ")
    list_nums = [int(i) for i in list_size.split()]
    subarray_size = int(input())
    print(max_subarray_size_k(list_nums, subarray_size))
