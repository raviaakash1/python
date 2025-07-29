"""

given a list of numbers your task is to find 2 such number by addition of which u can get the target number

nums [5 9 1 2 4 15 6 3]  target : 13
 
Output: [1 4]

Restrictions:
- only use element once
- always one solution atleast exists

"""

from typing import List, Dict

def find_two_nums(list_nums : List[int], target: int) -> List[int]:
    hash_map = dict()
    for i in range(len(list_nums)):
        remaining: int = target - list_nums[i]
        if remaining in hash_map:
            return [hash_map[remaining], i]
        else:
            hash_map[list_nums[i]] = i

# def find_two_nums(list_nums : List[int], target: int) -> List[int]:
#     diff_list: List[int] = [0]*len(list_nums)
#     for i in range(len(list_nums)):
#         diff_list[i] = target - list_nums[i]

#     hash_map: Dict[int, int] = dict()
#     for i in range(len(list_nums)):
#          hash_map[list_nums[i]] = i
         
#     for i in range(len(diff_list)):
#         if diff_list[i] in hash_map:
#             return [i, hash_map[diff_list[i]]]

if __name__ == "__main__":
    list_nums: List[int] = [int(i) for i in input('Enter an array >> ').split(" ")]
    target: int = int(input('Enter a target number >> '))
    two_nums: List[int] = find_two_nums(list_nums, target)
    print(two_nums)