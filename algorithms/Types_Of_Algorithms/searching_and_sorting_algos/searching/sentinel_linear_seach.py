'''
As name suggests it is a type of linear search where the number of comparisions are reduced as compared to the traditional linear search.

In traditional linear search, only N comparisions are made, and in sentinel linear search the sentinel value is used to avoid any out of bound comparisions
but there is no additional comparisions being made specifically for the index of the element being searched.

In this search, the last element of the array is replaced with the element to be searched and then the linear search is performed on the array without 
checking whether the current index is inside the index range of the array or not because the element to be searched will definitely be found inside the array even 
if it was not present in the original array since the last element got replaced with it. So, the index to be checked will never be out of the bounds of the array. 
The number of comparisons in the worst case there will be (N + 2).

Sentinel linear search is a variation of the standard linear search algorithm used to find a target value in an array or list.
The basic idea behind this algorithm is to add a sentinel value at the end of the array which is equal to the target value we are looking for. 
This helps to avoid checking the array boundary condition during each iteration of the loop, as the sentinel value acts as a stopper for the loop.

Although in worst-case time complexity both algorithms are O(n). Only the number of comparisons are less in sentinel linear search than linear search
'''


def sentinel_search(arr, to_find):
    last = arr[len(arr) - 1]
    arr[len(arr) - 1] = to_find
    i = 0
    while arr[i] != to_find:
        i+=1
    arr[len(arr) - 1] = last
    if i < len(arr) - 1 or last == to_find:
        return "Found"
    return "Not Found"


# driver function
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,67,7,8,9,90,0]
    to_find = 67
    print(sentinel_search(arr, to_find))