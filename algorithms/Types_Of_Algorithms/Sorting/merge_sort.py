from typing import List
from take_input import get_input


def merge_sort(user_input) -> List:
    
    if len(user_input) <= 1:
        return user_input
    mid = len(user_input) // 2
    left_arr = user_input[:mid]
    right_arr = user_input[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    
    return merge(left, right)

def merge(left, right) -> List:
    iLeft: int = 0
    iRight: int = 0
    result: List = list()
    while iLeft < len(left) and iRight < len(right):
        if left[iLeft] <= right[iRight]:
            result.append(left[iLeft])
            iLeft += 1
        else:
            result.append(right[iRight])
            iRight += 1
    
    while iLeft < len(left):
        result.append(left[iLeft])
        iLeft += 1
    while iRight < len(right):
        result.append(right[iRight])
        iRight += 1
    return result


if __name__ == "__main__":
    user_input = get_input()
    sorted_list = merge_sort(user_input)
    print("sorted_list: ",sorted_list)