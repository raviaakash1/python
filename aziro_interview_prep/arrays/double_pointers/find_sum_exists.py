'''
Given a sorted array of integers nums and a target value target, return the indices of the two numbers such that they add up to the target.
Assume there is exactly one solution.
'''

def get_sum(list_nums, target_sum):
    start_index = 0
    end_index = len(list_nums) - 1
    while start_index < end_index:
        if list_nums[start_index] + list_nums[end_index] == target_sum:
            return [start_index, end_index]
        elif list_nums[start_index] + list_nums[end_index] < target_sum:
            start_index += 1
        else:
            end_index -= 1
    return -1


if __name__ == "__main__":
    list_len = int(input())
    list_nums = [int(input()) for _ in range(list_len)]
    target_sum = int(input())
    print(get_sum(list_nums, target_sum))

