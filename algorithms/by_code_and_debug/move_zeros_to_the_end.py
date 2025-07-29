from typing import List

# def move_zeros_to_end(list_nums):
#     indx_j = int(1)
#     for i in range(len(list_nums)):
#         if list_nums[i] == 0:
#             indx_j = i + 1
#             while indx_j < len(list_nums) and list_nums[indx_j] == 0:
#                 indx_j += 1
#             if indx_j < len(list_nums):
#                 list_nums[i], list_nums[indx_j] = list_nums[indx_j], list_nums[i] 


def move_zeros_to_end(list_nums: List[int]) -> None:
    pos = 0  # Position to place next non-zero
    for i in range(len(list_nums)):
        if list_nums[i] != 0:
            list_nums[pos], list_nums[i] = list_nums[i], list_nums[pos]
            pos += 1

    
if __name__ == "__main__":
    list_nums: List[int] = [int(i) for i in input("Enter an array >> ").split(" ")]
    move_zeros_to_end(list_nums)
    print(list_nums)