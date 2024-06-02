'''
Find 3 largest element in an array
'''


def find_three_largest_elements(arr):
    data_seq = []
    max = -1
    second_max = -1
    third_max = -1
    for data in arr:
        if data > max:
            if max > second_max:
                if second_max > third_max:
                    third_max = second_max
                second_max = max
            max = data
        if data < max:
            if data > second_max:
                third_max = second_max
                second_max = data
            else:
                if data > third_max:
                    third_max = data
    return max, second_max, third_max

        




# driver code
if __name__ == "__main__":
    arr = [12, 13, 1, 10, 34, 11, 34]
    print(find_three_largest_elements(arr))