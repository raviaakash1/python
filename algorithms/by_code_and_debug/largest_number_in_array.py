from typing import List

def merge_sort(num_list: List[int]):
    if len(num_list) <= 1:
        return num_list
    mid = len(num_list)//2
    left_arr = merge_sort(num_list[: mid])
    right_arr = merge_sort(num_list[mid:])
    return merge(left_arr, right_arr)

def merge(left_arr: List[int], right_arr: List[int]) -> List[int]:
    result: List[int] = list()
    left_arr_index: int = int(0)
    right_arr_index: int = int(0)
    while left_arr_index < len(left_arr) and right_arr_index < len(right_arr):
        if left_arr[left_arr_index] > right_arr[right_arr_index]:
            result.append(left_arr[left_arr_index])
            left_arr_index+=1
        else:
            result.append(right_arr[right_arr_index])
            right_arr_index+=1

    while left_arr_index < len(left_arr):
        result.append(left_arr[left_arr_index])
        left_arr_index += 1
    while right_arr_index < len(right_arr):
        result.append(right_arr[right_arr_index])
        right_arr_index += 1
    return result

def get_kth_largest_num(num_list: List[int], kth_largest) -> int:
    resultant_array = merge_sort(num_list)
    return resultant_array[kth_largest - 1]

if __name__ == "__main__":
    num_list : List[int] = [int(i) for i in input("Enter list of numbers >> ").split(" ")]
    kth_largest_num: int = int(input("Enter the kth largest number > "))
    print(f"Largest number in the array {get_kth_largest_num(num_list, kth_largest_num)}")
    