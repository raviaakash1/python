'''

given list of 0's and 1's in an array find where maximum consecutive ones are present

nums = [1 1 0 1 0 1 1 1 1 0 1 1]
                  |
at this index max consecutive 1's are present

'''

from typing import List, Dict

"""
def find_consecutive_ones(nums: List[int]) -> int:
    max_len = cur_len = 0
    max_start = cur_start = -1

    for i, val in enumerate(nums):
        if val == 1:
            if cur_len == 0:
                cur_start = i
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
                max_start = cur_start
        else:
            cur_len = 0  # Reset on zero

    return max_start
"""

def find_consecutive_ones(list_nums: List[int]) -> int:
    ones_info: Dict[str, int]= {
        "len_ones" : 0,
        "found_index": -1
    }
    index: int = -1
    length_one: int = 0
    flag: bool = False
    for i in range(len(list_nums)):
        if list_nums[i] == 1 and flag:
            length_one += 1
        if list_nums[i] == 1 and not flag:
            flag = True
            length_one += 1
            index = i
        elif list_nums[i] == 0:
            flag = False
            if index != -1 and length_one != 0:
                if ones_info["len_ones"] < length_one:
                    ones_info["len_ones"] = length_one
                    ones_info["found_index"] = index
            index = -1
            length_one = 0
        
    if index != -1 and length_one != 0:
        if ones_info["len_ones"] < length_one:
            ones_info["len_ones"] = length_one
            ones_info["found_index"] = index        
    return ones_info["len_ones"]

if __name__ == "__main__":
    list_nums: List[int] = [int(i) for i in input("Enter an array of 1's and 0's >> ").split(" ")]
    found_index = find_consecutive_ones(list_nums)
    print(f"Consecutive 1's found at index {found_index} in {list_nums}")