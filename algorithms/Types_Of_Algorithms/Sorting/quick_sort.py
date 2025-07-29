from typing import List
from take_input import get_input

'''
    1) Pick a pivot
        - it can be the first element
        - it can be the last element
        - it can be the middle element
        - it can be any random element

    2) put pivot at its correct position/index

    in this example we will take pivot as first element

    Algo used : Divide and conquer
'''

def partition(data, low, high) -> int:
    pivot: int = data[low]
    i: int = low
    j: int = high

    while i<j:
        while data[i] <= pivot and i <= high - 1:
            i+=1
        while data[j] > pivot and j >= low + 1:
            j-=1
        if i<j:
            data[i], data[j] = data[j], data[i]
    
    data[j], data[low] = data[low], data[j]
    return j


def quick_sort(user_input, low, high) -> List:
    if low<high:
        p_index = partition(user_input, low, high)
        quick_sort(user_input, low, p_index-1)
        quick_sort(user_input, p_index+1, high)
if __name__ == "__main__":
    user_input = get_input()
    quick_sort(user_input, 0, len(user_input) - 1)
    print(user_input)