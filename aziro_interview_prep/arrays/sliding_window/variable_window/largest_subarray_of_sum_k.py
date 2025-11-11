

def find_largest_subarray(list_nums, target_value):
    start = 0
    end = 0
    sum = 0
    maximum = 0
    while end < len(list_nums) and start < len(list_nums):
        
        sum += list_nums[end]
        
        if sum < target_value:
            end += 1
        elif sum == target_value:
            maximum = max(maximum, end-start+1)
            print([list_nums[i] for i in range(start, end + 1)])
            end += 1
        elif sum > target_value:
            while sum > target_value:
                sum -= list_nums[start]
                start += 1
            if sum == target_value:
                maximum = max(maximum, end-start+1)
                print([list_nums[i] for i in range(start, end + 1)])
            end += 1
    return maximum


if __name__ == "__main__":
    list_nums = input()
    list_nums = [int(i) for i in list_nums.split()]
    target_value = int(input())

    print(find_largest_subarray(list_nums, target_value))