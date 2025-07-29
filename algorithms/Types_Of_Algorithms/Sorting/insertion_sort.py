from typing import List
from take_input import get_input

'''
In this sort we keep on checking wether the subarray is sorted or not
if subarray is not sorted then the element is placed in the correct order

Example : [3, 5, 6, 4, 8, 9, 10, 7, 1]

    in first interation there is only array of size 1 [3] --> sorted
    in the second iteration [3, 5] --> sorted
    in the 3rd iteration [3, 5, 6] --> sorted
    in the 4th iteration [3, 5, 6, 4] --> 4 is not sorted
        here we will store the value 4 in a variable and start checking the correct place such that j-1 < value < j+1
        so in the inner loop after first iteration [3, 5, 6, 6]
        subsequentially we will kee iteration once the value is checked with 4 and above mentioned condition is met
        and we replace the value like this 
            before : [3, 5, 5, 6]
            after : [3, 4, 5, 6]
'''


def insertion_sort(user_input) -> List :
    for i in range(1, len(user_input)):
        key = user_input[i]
        j = i - 1
        while j >= 0 and user_input[j] > key:
            user_input[j+1] = user_input[j]
            j -= 1
        user_input[j+1] = key
    return user_input
            
if __name__ == "__main__":
    user_input: List = get_input()
    sorted_list = insertion_sort(user_input)
    print(sorted_list)
