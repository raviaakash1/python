'''
Conditions for when to apply Binary Search in a Data Structure:

To apply Binary Search algorithm:

    The data structure must be sorted.
    Access to any element of the data structure takes constant time.
    
Advantages of Binary Search:

    Binary search is faster than linear search, especially for large arrays.
    More efficient than other searching algorithms with a similar time complexity, such as interpolation search or exponential search.
    Binary search is well-suited for searching large datasets that are stored in external memory, such as on a hard drive or in the cloud.

Drawbacks of Binary Search:

    The array should be sorted.
    Binary search requires that the data structure being searched be stored in contiguous memory locations. 
    Binary search requires that the elements of the array be comparable, meaning that they must be able to be ordered.
'''

# normal impl
def binary_search(arr, to_find, l, r):
    while l <= r:
        m = l + (r - l) // 2
        if to_find == arr[m]:   
            return "Found"
        if  arr[m] < to_find:
            l = m + 1
        else:
            r = m - 1

    return "Not Found"


# recursive impl
def binary_search_recvrsive(arr, to_find, left, right):
    
    if right < left:
        return "Not Found"
    mid = left + (right - left) // 2
    
    if to_find == arr[mid]:
        return "Found"
    if to_find < arr[mid]:
        return binary_search_recvrsive(arr, to_find, left, mid-1)
    else:
        return binary_search_recvrsive(arr, to_find, mid+1, right)



if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    to_find = 3
    l = 0
    r = len(arr) - 1
    print(binary_search(arr, to_find, l, r))
    print(binary_search_recvrsive(arr, to_find, l, r))


'''
    Time Complexity: 
        Best Case: O(1)
        Average Case: O(log N)
        Worst Case: O(log N)
    Auxiliary Space: O(1), If the recursive call stack is considered then the auxiliary space will be O(logN).
'''