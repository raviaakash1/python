"""
Given an unsorted array of integers nums and a target value target, return all unique pairs of numbers that sum to the target.
Each pair should be returned in sorted order, and the result should not contain duplicates.


Input: nums = [1, 3, 2, 2, 4, 0], target = 4  
Output: [[0, 4], [1, 3], [2, 2]]

since unique pairs hence no duplicates allowed
"""

def merge_sort(list_nums):
    if len(list_nums) == 1:
        return list_nums
    mid = len(list_nums) // 2
    left_subarray = merge_sort(list_nums[:mid])
    right_subarray = merge_sort(list_nums[mid:])
    return merge(left_subarray, right_subarray)

def merge(left_subarray, right_subarray):
    merged_array = list()

    l_index = 0; r_index = 0

    while l_index < len(left_subarray) and r_index < len(right_subarray):
        if left_subarray[l_index] <= right_subarray[r_index]:
            merged_array.append(left_subarray[l_index])
            l_index += 1
        else:
            merged_array.append(right_subarray[r_index])
            r_index += 1
    while l_index < len(left_subarray):
        merged_array.append(left_subarray[l_index])
        l_index += 1
    while r_index < len(right_subarray):
        merged_array.append(right_subarray[r_index])
        r_index += 1

    return merged_array

def return_all_unique_pairs(list_nums, target_sum):
    
    sorted_array = merge_sort(list_nums)
    
    start_index = 0
    end_index = len(sorted_array) - 1
    result = list()
    while start_index < end_index:
        if sorted_array[start_index] == sorted_array[end_index]:
            import pdb;pdb.set_trace()
            end_index -= 1
            continue
        if sorted_array[start_index] + sorted_array[end_index]  == target_sum:
            result.append([start_index, end_index])
            start_index += 1
        elif sorted_array[start_index] + sorted_array[end_index] < target_sum:
            start_index += 1
        elif sorted_array[start_index] + sorted_array[end_index] > target_sum:
            end_index -= 1
    return result


"""
def two_sum_all_pairs(nums, target):
    nums.sort()
    res = []
    left, right = 0, len(nums) - 1

    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            res.append([nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return res
"""

if __name__ == "__main__":
    list_len = int(input())
    list_nums = [int(input()) for _ in range(list_len)]
    target_sum = int(input())

    print(return_all_unique_pairs(list_nums, target_sum))