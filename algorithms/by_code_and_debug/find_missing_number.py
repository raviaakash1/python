'''
find missing number in an array

given an array of size n u need to find the missing number in an array

nums [1, 0, 3, 4] n = 4 here 2 is missing
'''
from typing import List

def find_missing_num(list_nums: List[int]) -> int:
    sum = 0
    for i in list_nums:
        sum += i
    return int(len(list_nums)*((len(list_nums) + 1) / 2) - sum)

from typing import List
if __name__ == "__main__":
    list_nums: List[int] = [int(i) for i in input("Enter ana array >> ").split(" ")]
    miss_num: int = find_missing_num(list_nums)
    print("missing numbers : ", miss_num)