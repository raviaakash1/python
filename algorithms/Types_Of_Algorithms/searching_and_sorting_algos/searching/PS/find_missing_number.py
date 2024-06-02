'''
Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from the first N integers.

Note: There are no duplicates in the list.

Input: arr[] = {1, 2, 4, 6, 3, 7, 8} , N = 8
Output: 5
Explanation: Here the size of the array is 8, so the range will be [1, 8]. The missing number between 1 to 8 is 5
'''


def add_all_numbers(arr):
    total = 0
    for data in arr:
        total += data
    return total


def total_added(arr, n):
    return (n*(n+1))/2

def find_missing_number(arr, n):
    total_arr_number = add_all_numbers(arr)
    find_arr_total = total_added(arr, n+1)

    return find_arr_total - total_arr_number

# solve using hashing
def hash_solution(arr, n):
    temp = [0] * (n+1)
    for i in range(n):
        temp[arr[i]-1] = 1

    for i in range(n + 1):
        if temp[i] == 0:
            return i + 1


# drive code
if __name__ == "__main__":
    arr = [1, 2, 4, 6, 3, 7, 8]
    print(int(find_missing_number(arr, len(arr))))
    print(hash_solution(arr, len(arr)))