

import math
import os
import random
import re
import sys



#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def remove_duplicates_2d(lst):
    seen = set()
    result = []
    for sublist in lst:
        t = tuple(sublist)
        if t not in seen:
            seen.add(t)
            result.append(sublist)
    return result

def mergeHighDefinitionIntervals(intervals):
    # corner conditions
    # list empty
    if len(intervals) == 0:
        return []
    # only one element
    if len(intervals) == 1 and len(intervals[0]) != 0:
        return intervals
    intervals = sorted(remove_duplicates_2d(intervals))
    
    result = [intervals[0]]
    # rest usecase
    for index, interval in enumerate(intervals[1:]):
        if interval[0] > result[-1][1]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    
    return result
    
if __name__ == '__main__':
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
