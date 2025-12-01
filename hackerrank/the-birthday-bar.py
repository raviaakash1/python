

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    start = 0 
    end = 0
    sum = 0
    res = 0
    while end < len(s):
        sum += s[end]
        if end-start+1 < m:
            end+=1
        elif end - start + 1 == m:
            if sum == d:
                res += 1
            sum -= s[start]
            start+=1
            end+=1
    return res


if __name__ == '__main__':
    

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(str(result) + '\n')

    
