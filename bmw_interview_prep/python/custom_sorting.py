'''
Sort a list  of string without using sort() or sorted()

Expectation:
    Implement sorting algorithm like bubble sort, selection sort etc.

    Twist: Compare strings based on ASCII

'''

from typing import List

def merge_sort(array):
    if len(array) == 1 or len(array) <= 0:
        return array
    
    mid: int = len(array)//2
    
    left_array: List[int] = merge_sort(array[:mid])
    right_array: List[int] = merge_sort(array[mid:])
    return merge(left_array, right_array)

def merge(left_array : List[int], right_array: List[int]) -> List[int]:
    sorted_array: List[int] = list()

    l_index: int = 0
    r_index: int = 0
    
    while l_index <= len(left_array) - 1 and r_index <= len(right_array) - 1:
        if left_array[l_index] <= right_array[r_index]:
            sorted_array.append(left_array[l_index])
            l_index += 1
        else:
            sorted_array.append(right_array[r_index])
            r_index += 1
    
    
    if l_index <= len(left_array) - 1:
        sorted_array.extend(left_array[l_index:])
    if r_index <= len(right_array) - 1:
        sorted_array.extend(right_array[r_index:])
    

    return sorted_array


def sort_the_array(array):
    sorted_array: List[int] = merge_sort(array)
    print("Sorted_array : ",sorted_array)


def get_ascii_dict(func):
    def inner(*args, **kwargs):
        original_result = func(*args, **kwargs)
        if isinstance(original_result, str):
            string_small_array: List[str] = list("abcdefghijklmnopqrstuvwxyz")
            string_caps_array: List[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            ascii_small_dict = { char:index+65 for index, char in enumerate(string_small_array)}
            ascii_caps_dict = {char: index + 97 for index, char in enumerate(string_caps_array)}
            transformed = []
            for data in original_result:
                if data in ascii_small_dict:
                    transformed.append(ascii_small_dict[data])
                elif data in ascii_caps_dict:
                    transformed.append(ascii_caps_dict[data])
            return transformed
        return original_result
    return inner
    
@get_ascii_dict
def sort_string(user_input):
    return user_input

if __name__ == "__main__":
    
    
    user_input = "HelloAakashRavi"
    print(sort_string(user_input))
    import pdb;pdb.set_trace()
    import sys;sys.exit()
    sort_the_array(array)