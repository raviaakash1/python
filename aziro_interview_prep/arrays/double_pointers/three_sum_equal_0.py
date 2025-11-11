"""
Given an integer array nums, return all unique triplets [a, b, c] such that a + b + c == 0.
The solution set must not contain duplicate triplets.


Input: nums = [-1, 0, 1, 2, -1, -4]  
Output: [[-1, -1, 2], [-1, 0, 1]]
"""
def merge_sort(list_nums):
    if len(list_nums) == 1:
        return list_nums
    mid = len(list_nums) // 2
    left_array = merge_sort(list_nums[:mid])
    right_array = merge_sort(list_nums[mid:])
    return merge(left_array, right_array)

def merge(left_array, right_array):
    merged_array = list()
    
    l_index = 0
    r_index = 0

    while l_index < len(left_array)  and r_index < len(right_array):
        if left_array[l_index] <= right_array[r_index]:
            merged_array.append(left_array[l_index])
            l_index += 1
        else:
            merged_array.append(right_array[r_index])
            r_index += 1
    
    while l_index < len(left_array):
        merged_array.append(left_array[l_index])
        l_index += 1
    while r_index < len(right_array):
        merged_array.append(right_array[r_index])
        r_index += 1
    
    return merged_array

def three_sum_problem(list_nums):
    sorted_array = merge_sort(list_nums)

    res = []
    for i in range(len(sorted_array) - 2):
        if i > 0 and sorted_array[i] == sorted_array[i - 1]:
            continue  # skip duplicate i
        left, right = i + 1, len(sorted_array) - 1
        while left < right:
            total = sorted_array[i] + sorted_array[left] + sorted_array[right]
            if total == 0:
                res.append([sorted_array[i], sorted_array[left], sorted_array[right]])
                left += 1
                right -= 1
                while left < right and sorted_array[left] == sorted_array[left - 1]:
                    left += 1
                while left < right and sorted_array[right] == sorted_array[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return res

            


if __name__ == "__main__":
    list_len = int(input())
    list_nums = [int(input()) for _ in range(list_len)]
    print(three_sum_problem(list_nums))