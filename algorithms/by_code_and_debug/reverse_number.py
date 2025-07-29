from typing import List

def reverse_num(list_nums, left, right):
    while left < right:
        list_nums[left], list_nums[right] = list_nums[right], list_nums[left]
        left += 1
        right -= 1
    

if __name__ == "__main__":
    list_nums: List[int] = [int(i) for i in input("Enter an array >> ").split(" ")]
    reverse_num(list_nums, 0, len(list_nums) - 1)
    