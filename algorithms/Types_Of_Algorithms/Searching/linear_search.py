import sys
import os

from take_input import get_input
# from  ..Sorting.take_input import get_input
from typing import List

def linear_search(arr, to_find) -> int:
    for index, num in enumerate(arr):
        if num == to_find:
            return index
        
    return -1

if __name__ == "__main__":
    arr = get_input()
    to_find = get_input()[0]

    f_index = linear_search(arr, to_find)
    print(f"found at index {f_index}" if f_index != -1 else f"{to_find} not in {arr}")