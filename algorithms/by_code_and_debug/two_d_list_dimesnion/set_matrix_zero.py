'''
set matrix

wherever u find 0 in the matrix make the row and column to which it belong to 0

[
    [7, 9 ,2, 3],
    [20, 8, 0, 10],
    [29, 0 , -10, 5],
    [4, 14, 6, 7]
]

o/p

[
    [7, 0, 0 ,3],
    [0, 0 ,0 ,0],
    [0, 0 ,0 ,0],
    [4, 0, 0, 7]
]
'''


def set_matrix_zeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    zero_rows = set()
    zero_cols = set()

    # First pass: identify zero locations
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Second pass: set rows and columns to zero
    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0

    return matrix

# wrong solution wont work when multiple zeros are there in  a column
# def set_matrix_zeros(matrix):
#     col_to_not_check = list()
#     row = len(matrix)
#     col = len(matrix[0])

#     for i in range(row):
#         for j in range(col):
#             if j not in col_to_not_check:
#                 if matrix[i][j] == 0:
#                     for c in range(col):
#                         matrix[i][c] = 0
#                     for r in range(row):
#                         matrix[r][j] = 0
#                     col_to_not_check.append(j)
#                     break
                    
#     return matrix

if __name__ == "__main__":
    # row = int(input("Enter number of rows for the matrix >> "))
    # col = int(input("Enter number of columns for the matrix >> "))
    # new_matrix = [[0 for _ in range(row)] for _ in range(col)]
    # for i in range(row):
    #     row_data = [int(i) for i in input(f"Enter row {i} >> ").split(" ")]
    #     for j in range(col):
    #         new_matrix[i][j] = row_data[j]
    new_matrix = [
            [1, 2, 0],
            [4, 5, 6],
            [7, 8, 0]

    ]
    row = len(new_matrix)
    col = len(new_matrix[0])
    result = set_matrix_zeros(new_matrix)
    for i in range(row):
        for j in range(col):
            print(result[i][j], end=" ")
        print()
    print()
