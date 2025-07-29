from typing import List
import math
# def remove_dups(list_nums: List[int]) -> List[int]:
#     result: List[int] = [-1000]*(len(list_nums))
#     res_index: int = int(-1)
#     for num in list_nums:
#         if result[res_index] == num and res_index != -1:
#             continue
#         else:
#             res_index += 1
#             result[res_index] = num
#     slice_indx = len(result)
#     try:
#         slice_indx = result.index(-1000)
#     except:
#         pass
#     return result[:slice_indx]

# def merge_two_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
#     result: List[int] = list()
#     arr1_indx: int = int(0)
#     arr2_indx: int = int(0)
#     while arr1_indx < len(arr1) and arr2_indx < len(arr2):
#         if arr1[arr1_indx] <= arr2[arr2_indx]:
#             result.append(arr1[arr1_indx])
#             arr1_indx += 1
#         else:
#             result.append(arr2[arr2_indx])
#             arr2_indx += 1
    
#     while arr1_indx < len(arr1):
#         result.append(arr1[arr1_indx])
#         arr1_indx += 1
#     while arr2_indx < len(arr2):
#         result.append(arr2[arr2_indx])
#         arr2_indx += 1
    
#     return remove_dups(result)

def merge_two_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    result: List[int] = list()
    hash_map: int = -math.inf
    arr1_indx: int = int()
    arr2_indx: int = int()

    while arr1_indx < len(arr1) and arr2_indx < len(arr2):
        if arr1[arr1_indx] <= arr2[arr2_indx]:
            if len(result) == 0 or arr1[arr1_indx] != result[-1]:
                result.append(arr1[arr1_indx])
            arr1_indx += 1
        else:
            if len(result) or arr2[arr2_indx] != result[-1]:
                result.append(arr2[arr2_indx])
            arr2_indx += 1

    while arr1_indx < len(arr1):
        if arr1[arr1_indx] > result[-1]:
            result.append(arr1[arr1_indx])
        arr1_indx += 1
    while arr2_indx < len(arr2):
        if arr2[arr2_indx] > result[-1]:
            result.append(arr2[arr2_indx])
        arr2_indx += 1

    return result


if __name__ == "__main__":
    list_num1: List[int] = [int(i) for i in input("Enter an array >> ").split(" ")]
    list_num2: List[int] = [int(i) for i in input("Enter another array >> ").split(" ")]
    resulted_arr: List[int] = merge_two_sorted_arrays(list_num1, list_num2)
    print(resulted_arr)

