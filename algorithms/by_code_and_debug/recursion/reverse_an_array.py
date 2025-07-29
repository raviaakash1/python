from typing import List

def reverse_the_array(array: List[int], start_index = 0) -> List[int]:
    if start_index == len(array) // 2:
        return array
    array[start_index], array[len(array) - 1 -start_index] = array[len(array) - 1 -start_index], array[start_index]
    return reverse_the_array(array, start_index+1)

# reverse sub arrays

def reverse_sub_array(array: List[int], start_index: int, end_index: int, index: int = 0) -> List[int]:
    if index >= (end_index - start_index + 1) // 2:
        return array
    array[start_index + index], array[end_index - index] = array[end_index - index], array[start_index + index]
    return reverse_sub_array(array, start_index, end_index, index + 1)


if __name__ == "__main__":
    list_nums: List[int] = [int(i) for i in input("Enter a list of numbers -> ").split(" ")]
    reversed_array: List[int] = reverse_the_array(list_nums)
    # print(reversed_array)
    index_range: List[int] = [int(i) for i in input("Enter start and end index ->").split(" ")]
    rev_array: List[int] = reverse_sub_array(list_nums, index_range[0], index_range[1], index_range[1]-index_range[0] + 1)
    print(rev_array)
