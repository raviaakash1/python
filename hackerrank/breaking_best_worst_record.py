import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min_list = []
    max_list = []
    
    min_score, max_score = scores[0], scores[0]
    min_list.append(min_score)
    max_list.append(max_score)
    min_count, max_count = 0, 0
    for i in range(1, len(scores)):
        max_score = max(max_score, scores[i])
        min_score = min(min_score, scores[i])
        if max_score not in max_list:
            max_list.append(max_score)
            max_count += 1
        if min_score not in min_list:
            min_list.append(min_score)
            min_count += 1
    return [max_count, min_count]
        
        
        
        
if __name__ == '__main__':
    

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
    