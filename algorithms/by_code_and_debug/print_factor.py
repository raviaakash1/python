from typing import List
from math import *
def get_factors(data: int) -> List[int]:
    return [num for num in range(1,data + 1) if data%num == 0]

def optimized_by_half(data: int) -> List[int]:
    result = []
    for i in range(1, data//2+1):
        if data % i == 0:
            result.append(i)
    result.append(data)
    return result

# using sqrt
def most_optimal(data: int)-> List[int]:
    result = []
    for i in range(1, int(sqrt(data)) + 1):
        if data % i == 0:
            result.append(i)
            if i != data//i:
                result.append(data//i)
    result.sort()
    return result

if __name__ == "__main__":
    data: int = int(input("Enter a digit >> "))
    factors: List[int] = get_factors(data)
    factors_opt_by_two: List[int] = optimized_by_half(data)
    
    print(factors)
    print(factors_opt_by_two)
    print(most_optimal(data))