"""

need to find first negative value in each window of size k

arr[] : 12 -1 -7 8 -15 30 16 18
o/p: -1 -1 -7 -15 -15 0

o/p size : arr_size - windows_size + 1

"""

def find_negative_numbers(list_nums, subarray_size):

    start = 0
    end = 0
    list_negative_nums = []
    result = []
    while end < len(list_nums):
        if list_nums[end] < 0:
            list_negative_nums.append(list_nums[end])

        if end - start + 1 < subarray_size:
            end += 1
        elif end - start + 1 == subarray_size:
            if len(list_negative_nums) == 0:
                result.append(0)
            else:
                if list_nums[start] != list_negative_nums[0]:
                    result.append(list_negative_nums[0])
                else:
                    result.append(list_negative_nums[0])
                    list_negative_nums = list_negative_nums[1:]
            start += 1
            end += 1
    return result



if __name__ == "__main__":
    list_nums = input("Enter an array : ")
    list_nums = [int(i) for i in list_nums.split()]
    subarray_size = int(input())
    print(find_negative_numbers(list_nums, subarray_size))