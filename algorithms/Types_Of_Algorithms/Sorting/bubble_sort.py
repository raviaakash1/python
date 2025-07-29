from typing import List
from take_input import get_input

'''
Bubble Sort
    also in this sorting method we check the adjacent elements
    here we try to push the largest element to the right most index ( at the very end )

    nums = [5, 4, 6, 7]
            ^
            |
            check with the next index i.e. 4 if current pointer is greater than the next index swap
            [4, 5, 6, 7]
                ^
                |
            comp 5 with 6
            [4, 5, 6, 7]
                   ^
                   |
            comp 6 with 7
            [4, 5, 6, 7]
                      ^
                      |

            [5, 6, 1, 4, 3]
             i        j
'''

def bubble_sort(user_input) -> List:
    left: int = 0
    right : int = len(user_input) - 2
    
    for i in range(right, -1, -1):
        for j in range(0, i+1):
            if user_input[j] > user_input[j+1]:
                user_input[j], user_input[j+1] = user_input[j+1], user_input[j]
    return user_input    


if __name__ == "__main__":
    user_input : List = get_input()
    sorted_list: List = bubble_sort(user_input)
    print("Sorted List : ", sorted_list)