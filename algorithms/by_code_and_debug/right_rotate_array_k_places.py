from typing import List

# def rotate_array_by_k_places(list_nums: List[int], kth_place):
#     result: List[int] = [0]*len(list_nums)
#     for i in range(len(list_nums)):
#         if i+kth_place >= len(list_nums):
#             result[(kth_place + i) - len(list_nums) ] = list_nums[i]
#         else:
#             result[i+kth_place] = list_nums[i]
#     return result

# def roatate_array_by_k_places(list_nums: List[int], kth_place):
#     n = len(list_nums)
#     kth_place = n % kth_place
#     list_nums[:] = list_nums[n-kth_place:] + list_nums[:n-kth_place]
#     return list_nums
'''
other ways
def rotate_array_by_k_places(list_nums: List[int], kth_place: int) -> List[int]:
    n = len(list_nums)
    result = [0] * n
    for i in range(n):
        target_index = i + kth_place
        if target_index >= n:
            target_index -= n  # simulate wrap-around
        result[target_index] = list_nums[i]
    return result

def rotate_array_by_k_places(list_nums: List[int], kth_place: int) -> List[int]:
    n = len(list_nums)
    result = [0] * n
    for i in range(n):
        result[(i + kth_place) % n] = list_nums[i]
    return result

def rotate_array_by_k_places(list_nums: List[int], kth_place: int) -> List[int]:
    n = len(list_nums)
    result = [0] * n
    for i in range(n):
        result[(i + kth_place) % n] = list_nums[i]
    return result

'''

# optimal solution

def reverse_num(list_nums, left, right):
    while left < right:
        list_nums[left], list_nums[right] = list_nums[right], list_nums[left]
        left += 1
        right -= 1

def rotate_array_by_k_places(list_nums, kth_place):
    list_len = len(list_nums)
    kth_place = list_len % kth_place
    reverse_num(list_nums, list_len-kth_place, list_len-1)
    reverse_num(list_nums, 0, list_len-kth_place-1)
    reverse_num(list_nums, 0,list_len-1)

if __name__ == "__main__":
    list_nums: List[int] = [int(i) for i in input("Enter an array >> ").split(" ")]
    dispalcement: int = int(input("Enter number of places to rotate array >> "))
    rotate_array_by_k_places(list_nums, dispalcement)
    print(list_nums)