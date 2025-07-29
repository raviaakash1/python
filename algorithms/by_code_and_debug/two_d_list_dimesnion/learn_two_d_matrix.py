'''

what is 2D matrix

How to iterate it

Store values in 2D matrix

Basic problem on 2D Matrix

'''

'''
a list containing rows and columns

5  20  3
7 -10  9
1 -52  6

this is a 3 * 3 matrix
              |
        rows columns

number of elements = num of rows * number of columns
'''

'''
how to represent

nums = [
    [5, 20, 3],     0th index
    [7, -10, 9],    1st index
    [1, -52, 6]     2nd index
]

length of nums = 3
row= len(nums)
columns = len(nums[any_index]) len(nums[0])


iteration

for i in range(len(nums)):
    for j in range(len(nums[i])):
        print(nums[i][j])


print upper triangle
print lower triangle
print diagonal


5 10 8
7 6  3
2 1  9

   |
   |

5 10 8
* 6  3
* *  9

for upper triangle j>=i


row = len(nums)
col = len(nums[0])

for i in range(row):
    for j in range(col):
        if j>=i:
            print(nums[i][j], end = " ")
        else:
            print("*", end = " ")

for lower triangle i>=j

for diagonal i==j

for anti-diagonal

* * 8
* 6 *
2 * *

'''

# nums = [

#     [5, 10, 8],
#     [7, 6, 3],
#     [2, 1, 9],
# ]


# row = len(nums)
# col = len(nums[0])

# for i in range(row):
#     for j in range(col):
#         if i+j == row - 1:
#             print(nums[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print()


'''
Transpose of a matrix
interchanging of rows and columns

5 8 9       5 0 3
0 7 6       8 7 1
3 1 2       9 6 2


5 9 1       5 2
2 3 7       9 3
            1 7
'''

nums = [
    [5, 8, 9],
    [10, 7, 6],
    [3, 1, 2]
]

nums2 = [
    [5, 9, 1],
    [2, 3, 1]
]

def transpose(matrix):
    row = len(matrix)
    col = len(matrix[0])

    new_matrix = [[0 for _ in range(row)] for _ in range(col)]


    for i in range(0, row):
        for j in range(0, col):
            new_matrix[j][i] = matrix[i][j]
            

    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end=" ")
        print()
    print()
    for i in range(col):
        for j in range(row):
            print(new_matrix[i][j], end=" ")
        print()
    print()
transpose(nums)
transpose(nums2)