#!/bin/python3

import math
import os
import random
import re
import sys

'''
Declare a 2-dimensional array, , with  empty arrays, all zero-indexed.
Declare an integer, , and initialize it to 0.
You need to process two types of queries:

Query: 

Compute .
Append the integer  to .
Query: 

Compute .
Set .
Store the new value of  in an answers array.
Notes:
-  is the bitwise XOR operation, which corresponds to the ^ operator in most languages. Learn more about it on Wikipedia.
-  is the modulo operator.
- Finally,  is the number of elements in .

Function Description

Complete the  function with the following parameters:
- : the number of empty arrays to initialize in 
- : 2-D array of integers

Returns

: the results of each type 2 query in the order they are presented
Input Format

The first line contains two space-separated integers, , the size of  to create, and , the number of queries, respectively.
Each of the  subsequent lines contains a query string, .

Constraints

It is guaranteed that query type  will never query an empty array or index.
Sample Input

STDIN    Function
-----    --------
2 5      size of arr[] n = 2, size of queries[] q = 5
1 0 5    queries = [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]
1 1 7
1 0 3
2 1 0
2 1 1
Sample Output

7
3

Explanation

Initial Values:


 = [ ]
 = [ ]

Query 0: Append  to .

 = [5]
 = [ ]

Query 1: Append  to .
 = [5]
 = [7]

Query 2: Append  to .

 = [5, 3]
 = [7]

Query 3: Assign the value at index  of  to . Store  in your answer array. 
 = [5, 3]
 = [7]

Query 4: Assign the value at index  of  to . Store  in your answer array. 
 = [5, 3]
 = [7]

Return your answer array [7, 3]. The code stub prints its elements on separate lines.
'''

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
