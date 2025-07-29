'''

Find longest consecutive subsequnce


nums = [1 99 101 98 2 5 3 100]

you have to find the longest subsequence is the given array

here in this example its 4  [98 99 100 101]

'''

from typing import List

# method 1
# sort the elements and find the longest sunsequnce
'''
def merge_sort(list_nums: List[int]) -> List[int]:

    if len(list_nums) <= 1:
        return list_nums
    mid = len(list_nums) // 2
    left_arr = merge_sort(list_nums[:mid])
    right_arr = merge_sort(list_nums[mid:])

    return merge(left_arr, right_arr)

def merge(left_arr: List[int], right_arr: List[int]) -> List[int]:

    result: List[int] = list()

    l_index = 0
    r_index = 0
    while l_index < len(left_arr) and r_index < len(right_arr):
        if left_arr[l_index] <= right_arr[r_index]:
            result.append(left_arr[l_index])
            l_index += 1
        else:
            result.append(right_arr[r_index])
            r_index += 1
    
    while l_index < len(left_arr):
        result.append(left_arr[l_index])
        l_index += 1
    while r_index < len(right_arr):
        result.append(right_arr[r_index])
        r_index += 1
    
    return result

def get_longest_subsequence(list_nums: List[int]) -> int:
    sorted_arr: List[int] = merge_sort(list_nums)
    print(sorted_arr)
    longest_subsequence: int = 1
    p_number : int = sorted_arr[0]
    sequence: int = 1
    for i in range(1,len(sorted_arr)):
        if sorted_arr[i] - p_number == 1:
            sequence += 1
            longest_subsequence = max(sequence, longest_subsequence)
            p_number = sorted_arr[i]
        else:
            sequence = 1
            p_number = sorted_arr[i]
    return longest_subsequence

'''
# optimal

def get_longest_subsequence(list_nums: List[int]) -> int:
    my_set: set = set()

    for i in range(len(list_nums)):
        my_set.add(list_nums[i])
    
    longest: int = 0

    for num in my_set:
        if num-1 not in my_set:
            count = 1
            x = num
            while x+1 in my_set:
                count+=1
                x+=1
            longest = max(longest, count)
    return longest


if __name__ == "__main__":
    list_nums: List[int] = [int(i) for i in input("Enter an array >> ").split(" ")]
    longest_subsequence : int = get_longest_subsequence(list_nums)
    print(longest_subsequence)