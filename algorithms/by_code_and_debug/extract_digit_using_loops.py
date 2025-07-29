from math import *
from typing import List
def get_number_of_digits(data: int) -> int:
    result: int = int(0)
    while data:
        result += 1
        data = data//10
    return result

def get_num_of_digits_log(data: int) -> int:
    return int(log10(data)) + 1

def get_digits(data: int) -> int:
    result: List = list()
    while data:
        result.append(data%10)
        data = data//10
    result.reverse()
    return result



if __name__ == "__main__":
    data: int = int(input("Enter a digit >> "))
    num_digits: int = get_number_of_digits(data)
    n_d: int = get_num_of_digits_log(data)
    digits: List = get_digits(data)
    print(num_digits)
    print(digits)
    print(n_d)