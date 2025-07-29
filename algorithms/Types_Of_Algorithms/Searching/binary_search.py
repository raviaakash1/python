import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Sorting')))

from take_input import get_input
from typing import List

def binary_search(arr: List[int], to_find: int)->int:
    right: int = len(arr) - 1
    left: int = 0
    while right >= left:
        mid: int = (right + left) // 2
        if arr[mid] == to_find:
            return mid
        elif arr[mid] < to_find:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# recursive approach
def binary_search_recrs(arr: List[int], to_find: int, left: int, right: int):
    if right >= left:
        mid: int = (right + left) // 2
        if arr[mid] == to_find:
            return mid
        elif arr[mid] > to_find:
            return binary_search_recrs(arr, to_find, left, mid - 1)
        else:
            return binary_search_recrs(arr, to_find, mid+1, right)
    return -1


if __name__ == "__main__":
    arr: List = get_input()
    to_find: int = get_input()[0]
    # iterative solution
    f_index: int = binary_search(arr, to_find)
    # recursive solution
    rf_index: int = binary_search_recrs(arr, to_find, 0, len(arr)-1)
    print(f"found at index {f_index}" if f_index != -1 else f"{to_find} not in {arr}")
    print(f"found at index {rf_index}" if rf_index != -1 else f"{to_find} not in {arr}")

# iterative solution will be prefered since although time complexity is the same
# space complexity will vary since recursive solution will add to func call stack
