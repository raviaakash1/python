'''
Linear Search is defined as a sequential search algorithm that starts at one end and goes through each element of a list until the desired element is found, 
otherwise the search continues till the end of the data set.

How Does Linear Search Algorithm Work?

In Linear Search Algorithm, 

    Every element is considered as a potential match for the key and checked for the same.
    If any element is found equal to the key, the search is successful and the index of that element is returned.
    If no element is found equal to the key, the search yields “No match found”.

Advantages of Linear Search:

    Linear search can be used irrespective of whether the array is sorted or not. It can be used on arrays of any data type.
    Does not require any additional memory.
    It is a well-suited algorithm for small datasets.

Drawbacks of Linear Search:

    Linear search has a time complexity of O(N), which in turn makes it slow for large datasets.
    Not suitable for large arrays.

When to use Linear Search?

When we are dealing with a small dataset.
When you are searching for a dataset stored in contiguous memory.

'''

def linear_search(arr, to_find):

    # we can use enumerate to get the index
    # for index, elem in enumerate(arr):
    #     if to_find == elem:
    #         return index
    # return "Not present in the array"

    # we can also iterate through index 
    # for i in range(len(arr)):
    #     if arr[i] == to_find:
    #         return i
    # return "Not present in array"

    # since in python we store data in a list we can find if element in present in list using index 
    # drawback if element not present in the list this will raise ValueError
    return arr.index(to_find)



# driver code
if __name__ == "__main__":
    arr = [1,346,12,3456,123,94]
    to_find = 346
    print(linear_search(arr, to_find))

'''
Time Complexity:

    Best Case: In the best case, the key might be present at the first index. So the best case complexity is O(1)
    Worst Case: In the worst case, the key might be present at the last index i.e., opposite to the end from which the search has started in the list. 
    So the worst-case complexity is O(N) where N is the size of the list.
    Average Case: O(N)
'''