from typing import List

def binary_search(list_nums: List[int], num_to_find: int, left: int, right: int) -> int:
    if left > right:
        return -1
    mid = (left+right) // 2
    if list_nums[mid] == num_to_find:
        return mid
    if list_nums[mid] < num_to_find:
        return binary_search(list_nums, num_to_find, mid+1, right)
    else:
        return binary_search(list_nums, num_to_find, left, mid - 1)

def find_num_in_arr(list_nums: List[int], num_to_find: int) -> int:
    return binary_search(list_nums, num_to_find, 0, len(list_nums) - 1)
    

if __name__ == "__main__":
    list_nums: List[int] = [int(i) for i in input("Enter an array of numbers >> ").split(" ")]
    num_to_find : int = int(input("Enter the number you want to find >> "))
    found: int = find_num_in_arr(list_nums, num_to_find)
    print(f"Found the number {num_to_find} at index {found} in arr {list_nums}") if found != -1 else print(f"Number {num_to_find} not found in arr {list_nums}")