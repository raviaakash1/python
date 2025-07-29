'''



given a list of size n there are n/2 +ve numbers and n/2 -ve numbers

u need to create a new list where elements are arranged in such order +ve -ve +ve -ve ...

nums = [5 10 -3 -1 -10 6]

o/p : [ 5 -3 10 -1 6 -10 ]


'''

from typing import List

'''
def rearrange_list(list_nums: List[int]) -> List[int]:
    list_positive: List[int] = list()
    list_negative: List[int] = list()
    result: List[int] = list()

    for i in range(len(list_nums)):
        if list_nums[i] > 0 :
            list_positive.append(i)
        else:
            list_negative.append(i)
    
    i_pos: int = 0
    i_neg: int = 0

    for i in range(len(list_nums)):
        if i % 2 == 0:
            result.append(list_nums[list_positive[i_pos]])
            i_pos += 1
        else:
            result.append(list_nums[list_negative[i_neg]])
            i_neg += 1
    return result
'''
# optimal
def rearrange_list(list_nums: List[int]) -> List[int]:
    result: List[int] = [0] * len(list_nums)

    p_index: int = 0
    n_index: int = 1

    for i in list_nums:
        if i < 0:
            result[n_index] = i
            n_index +=2
        else:
            result[p_index] = i
            p_index += 2
    return result

if __name__ == "__main__":
    list_nums: List[int] = [int(i) for i in input("Enter an array >> ").split(" ")]
    result: List[int] = rearrange_list(list_nums)
    print(result)