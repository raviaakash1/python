from typing import List

def check_sorted(list_nums: List[int]) -> bool:
    for i in range(len(list_nums) - 1):
        if list_nums[i] > list_nums[i + 1]:
            return False
    return True

if __name__ == "__main__":
    list_nums: List[int] = [int(i) for i in input("Enter List of Numbers >> ").split()]
    is_sorted: bool = check_sorted(list_nums)
    print(f"The given array is {'sorted' if is_sorted else 'not sorted'}")