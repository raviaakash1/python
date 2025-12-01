import math
import os
import random
import re
import sys

# 1 2 3 4 5

def miniMaxSum(arr):
    minimum = math.inf
    maximum = -math.inf
    start = 0
    end = 0
    sliding_window = 4
    sum = 0
    while end < len(arr):
        sum += arr[end]
        if end-start+1 < sliding_window:
            end += 1
        elif end-start+1 == sliding_window:
            minimum = min(minimum, sum)
            maximum = max(maximum, sum)
            sum -= arr[start]
            start += 1
            end += 1
    print(minimum, " ", maximum)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
