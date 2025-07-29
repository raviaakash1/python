from typing import List
'''
Selection Sort:
    In this sorting mechanism we take a middle index and compare it with rest of the 
    elements present in the array, if we find an element which is smaller than the 
    element present in the middle index then we store that index info in the middle index
    we do this until the loop is exhausted.

    Once loop is exhausted we swap the elements present in middle_index(lowest elemt  for that iteration)
    with the initial index or outer loop index
     0  1  2  3
    [5, 4, 2, 1]
     ^  ^
     |  |
     i  j
     middle_index

     here we compare j with middle index and then increment it by 1 and check it with the rest of the
     elements
     
     and once the inner loop is exhauseted then we swap elements present at index i with middle_index 
     element.
'''

def selection_sort(user_input: List) -> List:
    list_size: int = len(user_input)

    for i in range(0, list_size):
        min_index: int = i
        for j in range(i+1, list_size):
            if user_input[j] < user_input[min_index]:
                min_index = j
        user_input[i], user_input[min_index] = user_input[min_index], user_input[i]

    return user_input

if __name__ == "__main__":
    user_input : List= input("Enter a list of numbers to be sorted : ").split(" ")
    if len(user_input) < 1:
        print(user_input)
    else:
        user_input = [float(i) if i.find(".") != -1 else int(i) for i in user_input]

    sorted_list: List = selection_sort(user_input)
    print("Sorted List : ", sorted_list)