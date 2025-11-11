"""
Given a an array find max for all the subararys of size k

I/P
arr[] : 1 3 -1 -3 5 3 6 7
k : 3

o/p : 3 3 5 5 6 7

Note output array size will be : arr_size - k + 1

"""
import math
def find_max_in_a_subarray(list_nums, subarray_size):
    start = 0
    end = 0
    result = list()
    list_max = list()
    maximum = -math.inf
    while end < len(list_nums):
        maximum = max(maximum, list_nums[end])
        if maximum not in list_max:
            list_max.clear()
            list_max.append(maximum)
        if maximum in list_max and list_nums[end] not in list_max:
            list_max.append(list_nums[end])
        if end-start+1 < subarray_size:
            end += 1
        elif end - start + 1 == subarray_size:
            if list_nums[start] == list_max[0]:
                result.append(maximum)
                list_max = list_max[1:]
                if len(list_max) == 0:
                    maximum = -math.inf
                else:
                    maximum = list_max[0]
                
            else:
                result.append(maximum)
            start += 1
            end += 1
    if len(result) != len(list_nums) - subarray_size + 1:
        import pdb;pdb.set_trace()
    return result



if __name__ == "__main__":

    # list_nums = input()
    # list_nums = [int(i) for i in list_nums.split()]
    list_nums = list(range(10000))
    subarray_size = 500
    # subarray_size = int(input())
    import json
    f = open(f"aziro_interview_prep\arrays\sliding_window/result.txt", "w")
    f.write(json.dumps(find_max_in_a_subarray(list_nums, subarray_size), indent = 4))